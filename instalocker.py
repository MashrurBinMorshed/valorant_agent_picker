#!/usr/bin/env python3
"""
Valorant Instalocker - CLI Interface
Full command-line control over the instalocker
"""

import argparse
import sys
import os
from pathlib import Path
import time
import json
from typing import Optional
import threading
import pyautogui
import keyboard
import cv2
import numpy as np
from PIL import ImageGrab
import ctypes
from ctypes import wintypes

__version__ = "1.0.0"

# Default configuration
DEFAULT_CONFIG = {
    "agent": "NEON",
    "hotkey": "ctrl+shift+n",
    "confidence": 0.75,
    "mouse_speed": 0.05,
    "click_offset_x": 0,
    "click_offset_y": 20,  # Reduced from 50 for better accuracy
    "max_time": 15,
    "debug": False,
}

CONFIG_FILE = Path("instalocker_config.json")
ACTIVE = False
CURRENT_CONFIG = DEFAULT_CONFIG.copy()

def load_config() -> dict:
    """Load configuration from file or use defaults"""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                return {**DEFAULT_CONFIG, **config}
        except Exception as e:
            print(f"[!] Error loading config: {e}")
    return DEFAULT_CONFIG.copy()

def save_config(config: dict):
    """Save configuration to file"""
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"[✓] Config saved to {CONFIG_FILE}")
    except Exception as e:
        print(f"[!] Error saving config: {e}")

def take_screenshot():
    """Capture screenshot"""
    screenshot = ImageGrab.grab()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_agent_ocr(screenshot, agent_name):
    """Find agent using OCR"""
    try:
        import pytesseract
        pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        
        for i, text in enumerate(data['text']):
            if agent_name.lower() in text.lower():
                x = data['left'][i] + data['width'][i] // 2
                y = data['top'][i] + data['height'][i] // 2
                conf = data['conf'][i] / 100.0
                return (x, y, conf)
    except:
        pass
    return None

def find_agent_by_template(screenshot, agent_name):
    """Find agent using template matching"""
    template_file = Path(f"{agent_name.lower()}_template.jpg")
    if not template_file.exists():
        return None
    
    template = cv2.imread(str(template_file))
    if template is None:
        return None
    
    try:
        # Resize template to match screenshot if needed
        h, w = template.shape[:2]
        
        # Try template matching
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val > 0.65:  # Lower threshold for better detection
            x = max_loc[0] + w // 2
            y = max_loc[1] + h // 2
            return (x, y, max_val)
    except:
        pass
    
    return None

def find_agent_color(screenshot, agent_name):
    """Find agent by color - improved for agent select"""
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    
    # Neon = Purple/Cyan (more specific range)
    # Look for darker purple in agent cards area (left side of screen)
    lower_purple = np.array([120, 60, 60])
    upper_purple = np.array([160, 255, 200])
    
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    
    # Apply morphological operations to clean up
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find largest contour (should be agent card)
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        
        # Agent card should have reasonable size (not tiny UI elements)
        if area > 2000:
            M = cv2.moments(largest)
            if M["m00"] != 0:
                x = int(M["m10"] / M["m00"])
                y = int(M["m01"] / M["m00"])
                return (x, y, 0.6)
    
    return None

def find_agent_position(screenshot, agent_name, config):
    """Find agent position using multiple methods"""
    methods = [
        ("Template", find_agent_by_template),
        ("OCR", find_agent_ocr),
        ("Color", find_agent_color),
    ]
    
    for method_name, method_func in methods:
        result = method_func(screenshot, agent_name)
        if result:
            if config["debug"]:
                print(f"[D] Found {agent_name} via {method_name}: {result}")
            return result[:2]  # Return (x, y)
    
    return None

def find_lock_in_button(screenshot):
    """Find the LOCK IN button location"""
    # LOCK IN button is typically red/pink and in center-bottom of screen
    # Using template or color detection
    
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    
    # Red color range for LOCK IN button
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)
    
    # Look in center-bottom area only
    h, w = screenshot.shape[:2]
    mask[:h//2, :] = 0  # Ignore top half
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find largest red area (should be LOCK IN button)
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        
        if area > 500:  # LOCK IN button should be reasonably sized
            M = cv2.moments(largest)
            if M["m00"] != 0:
                x = int(M["m10"] / M["m00"])
                y = int(M["m01"] / M["m00"])
                return (x, y)
    
    # Fallback: estimate LOCK IN button position (center-bottom)
    return (w // 2, int(h * 0.65))

def click_using_windows_api(x, y, verbose=False):
    """Click using Windows API - more reliable than PyAutoGUI"""
    if verbose:
        print(f"[*] Clicking at ({int(x)}, {int(y)}) using Windows API...")
    
    try:
        # Move cursor
        ctypes.windll.user32.SetCursorPos(int(x), int(y))
        time.sleep(0.05)
        
        # Send mouse down
        ctypes.windll.user32.mouse_event(2, int(x), int(y), 0, 0)  # 2 = LEFT_DOWN
        time.sleep(0.05)
        
        # Send mouse up
        ctypes.windll.user32.mouse_event(4, int(x), int(y), 0, 0)  # 4 = LEFT_UP
        time.sleep(0.05)
        
        if verbose:
            print(f"[✓] Click sent successfully")
        return True
    except Exception as e:
        if verbose:
            print(f"[!] Windows API click failed: {e}")
        return False

def execute_instalocker(config: dict, verbose: bool = True):
    """Execute the instalocker"""
    global ACTIVE
    
    agent = config["agent"].upper()
    max_time = config["max_time"]
    
    if verbose:
        print(f"\n[▶] Searching for {agent}...")
        print(f"    Max time: {max_time}s")
        print(f"    Confidence: {config['confidence']}")
    
    start_time = time.time()
    attempts = 0
    
    while ACTIVE and (time.time() - start_time) < max_time:
        try:
            screenshot = take_screenshot()
            position = find_agent_position(screenshot, agent, config)
            
            if position:
                x, y = position
                x += config["click_offset_x"]
                y += config["click_offset_y"]
                
                if verbose:
                    elapsed = time.time() - start_time
                    print(f"\n[+] {agent} found at ({x}, {y}) - {elapsed:.2f}s")
                    print(f"[*] Moving to agent card and clicking...")
                
                # Move to position
                pyautogui.moveTo(int(x), int(y), duration=config["mouse_speed"])
                time.sleep(0.1)
                
                # Click using Windows API
                click_using_windows_api(x, y, verbose=True)
                time.sleep(0.3)
                
                if verbose:
                    print(f"[✓] {agent} card selected")
                
                # Wait for LOCK IN button to appear
                time.sleep(0.5)
                
                if verbose:
                    print(f"[*] Looking for LOCK IN button...")
                screenshot = take_screenshot()
                lock_pos = find_lock_in_button(screenshot)
                
                if lock_pos:
                    lx, ly = lock_pos
                    if verbose:
                        print(f"[+] Found LOCK IN button at ({lx}, {ly})")
                    
                    # Move to button
                    pyautogui.moveTo(int(lx), int(ly), duration=0.1)
                    time.sleep(0.1)
                    
                    if verbose:
                        print(f"[*] Clicking LOCK IN button...")
                    
                    # Click using Windows API
                    click_using_windows_api(lx, ly, verbose=True)
                    time.sleep(0.3)
                    
                    if verbose:
                        print(f"[✓] {agent} LOCKED IN!")
                else:
                    if verbose:
                        print(f"[!] LOCK IN button not found")
                
                ACTIVE = False
                return True
            
            attempts += 1
            time.sleep(0.05)
        
        except Exception as e:
            if verbose or config["debug"]:
                print(f"[!] Error: {e}")
                import traceback
                traceback.print_exc()
            time.sleep(0.1)
    
    if verbose:
        print(f"\n[✗] Timeout - {agent} not found")
    
    ACTIVE = False
    return False

def cmd_start(args):
    """Start the instalocker"""
    global ACTIVE, CURRENT_CONFIG
    
    config = CURRENT_CONFIG.copy()
    
    # Override with CLI arguments
    if args.agent:
        config["agent"] = args.agent
    if args.hotkey:
        config["hotkey"] = args.hotkey
    if args.mouse_speed is not None:
        config["mouse_speed"] = args.mouse_speed
    if args.confidence is not None:
        config["confidence"] = args.confidence
    if args.max_time is not None:
        config["max_time"] = args.max_time
    if args.debug:
        config["debug"] = True
    
    CURRENT_CONFIG = config
    
    print("\n" + "="*60)
    print("   VALORANT INSTALOCKER - CLI")
    print("="*60)
    print(f"\n[CONFIG]")
    print(f"  Agent: {config['agent']}")
    print(f"  Hotkey: {config['hotkey']}")
    print(f"  Mouse Speed: {config['mouse_speed']}")
    print(f"  Confidence: {config['confidence']}")
    print(f"  Max Time: {config['max_time']}s")
    print(f"  Debug: {config['debug']}")
    
    if not args.hotkey_disabled:
        print(f"\n[*] Press {config['hotkey']} to activate instalocker")
        print("[*] Press Ctrl+C to exit\n")
        
        def on_hotkey():
            global ACTIVE
            if not ACTIVE:
                ACTIVE = True
                threading.Thread(target=execute_instalocker, args=(config, True), daemon=True).start()
        
        keyboard.add_hotkey(config["hotkey"], on_hotkey)
        
        try:
            keyboard.wait()
        except KeyboardInterrupt:
            print("\n\n[*] Exiting...\n")
    else:
        print(f"\n[*] Running once (no hotkey)...\n")
        ACTIVE = True
        execute_instalocker(config, True)

def cmd_config(args):
    """Manage configuration"""
    if args.show:
        config = load_config()
        print("\n[CURRENT CONFIGURATION]")
        for key, value in config.items():
            print(f"  {key}: {value}")
        print()
    
    elif args.set:
        config = load_config()
        for setting in args.set:
            key, value = setting.split("=", 1)
            # Try to convert to appropriate type
            try:
                if value.lower() in ["true", "false"]:
                    value = value.lower() == "true"
                elif value.replace(".", "", 1).isdigit():
                    value = float(value) if "." in value else int(value)
            except:
                pass
            config[key] = value
            print(f"[✓] {key} = {value}")
        save_config(config)
    
    elif args.reset:
        save_config(DEFAULT_CONFIG)
        print("[✓] Config reset to defaults")
    
    else:
        config = load_config()
        print("\n[CURRENT CONFIGURATION]")
        for key, value in config.items():
            print(f"  {key}: {value}")
        print()

def cmd_calibrate(args):
    """Calibrate agent detection"""
    print("\n[CALIBRATION MODE]")
    print("Keep your mouse on the agent card")
    print("Press SPACE to capture template\n")
    
    try:
        keyboard.wait('space')
    except KeyboardInterrupt:
        print("[*] Calibration cancelled")
        return
    
    x, y = pyautogui.position()
    print(f"\n[*] Position: ({x}, {y})")
    print("    Capturing in 3...")
    time.sleep(1)
    print("    2...")
    time.sleep(1)
    print("    1...\n")
    time.sleep(1)
    
    screenshot = take_screenshot()
    
    # Capture around position
    w, h = 280, 200
    x1 = max(0, x - w//2)
    y1 = max(0, y - h//2)
    
    template = screenshot[y1:y1+h, x1:x1+w]
    
    filename = f"{args.agent.lower()}_template.jpg"
    cv2.imwrite(filename, template)
    
    print(f"[✓] Template saved to: {filename}")
    print(f"    Size: {template.shape[1]}x{template.shape[0]} pixels\n")

def cmd_version(args):
    """Show version"""
    print(f"\nValorant Instalocker v{__version__}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Valorant Instalocker - CLI Control",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
EXAMPLES:
  %(prog)s start                    # Start with current config
  %(prog)s start --agent REYNA      # Start and pick REYNA
  %(prog)s start --no-hotkey        # Run once immediately
  %(prog)s config --show            # Show current config
  %(prog)s config --set agent=REYNA mouse_speed=0.1
  %(prog)s calibrate --agent NEON   # Calibrate for NEON
  %(prog)s --version                # Show version
        """
    )
    
    parser.add_argument('--version', action='store_true', help='Show version')
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # START command
    start_parser = subparsers.add_parser('start', help='Start the instalocker')
    start_parser.add_argument('--agent', default=None, help='Agent to lock (default: NEON)')
    start_parser.add_argument('--hotkey', default=None, help='Hotkey to activate (e.g., "alt+n")')
    start_parser.add_argument('--mouse-speed', type=float, default=None, help='Mouse movement speed (0.01-0.2)')
    start_parser.add_argument('--confidence', type=float, default=None, help='Detection confidence (0.0-1.0)')
    start_parser.add_argument('--max-time', type=int, default=None, help='Max search time in seconds')
    start_parser.add_argument('--debug', action='store_true', help='Enable debug output')
    start_parser.add_argument('--no-hotkey', dest='hotkey_disabled', action='store_true', help='Run once without hotkey')
    start_parser.set_defaults(func=cmd_start)
    
    # CONFIG command
    config_parser = subparsers.add_parser('config', help='Manage configuration')
    config_parser.add_argument('--show', action='store_true', help='Show current config')
    config_parser.add_argument('--set', nargs='+', help='Set config values (e.g., agent=REYNA mouse_speed=0.1)')
    config_parser.add_argument('--reset', action='store_true', help='Reset to defaults')
    config_parser.set_defaults(func=cmd_config)
    
    # CALIBRATE command
    calibrate_parser = subparsers.add_parser('calibrate', help='Calibrate agent detection')
    calibrate_parser.add_argument('--agent', default='NEON', help='Agent to calibrate (default: NEON)')
    calibrate_parser.set_defaults(func=cmd_calibrate)
    
    args = parser.parse_args()
    
    # Load config at startup
    global CURRENT_CONFIG
    CURRENT_CONFIG = load_config()
    
    if args.version:
        cmd_version(args)
    elif args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Interrupted by user")
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)
