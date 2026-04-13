import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab, Image
import threading
import keyboard
from pathlib import Path

# Configuration
NEON_NAME = "NEON"
CONFIDENCE_THRESHOLD = 0.7
MOUSE_SPEED = 0.1  # seconds to move mouse (lower = faster)
HOTKEY = "ctrl+shift+n"  # Hotkey to toggle the instalocker
ACTIVE = False

def take_screenshot():
    """Capture screenshot of entire screen"""
    screenshot = ImageGrab.grab()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def find_agent_name_position(screenshot, agent_name):
    """
    Find the position of agent name text in screenshot
    Returns (x, y) center position of the agent name if found
    """
    # Convert to grayscale for better text detection
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    
    # Use Tesseract OCR (requires pytesseract)
    try:
        import pytesseract
        pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        # Get text data
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        
        # Search for agent name
        for i, text in enumerate(data['text']):
            if agent_name.lower() in text.lower():
                x = data['left'][i] + data['width'][i] // 2
                y = data['top'][i] + data['height'][i] // 2
                return (x, y)
    except ImportError:
        print("pytesseract not installed. Using fallback color detection method...")
    
    return find_agent_by_color_detection(screenshot)

def find_agent_by_color_detection(screenshot):
    """
    Fallback method: Detect Neon by agent card appearance
    Neon has a distinctive purple/cyan color scheme
    """
    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    
    # Neon's color range (purple/magenta range in HSV)
    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([150, 255, 255])
    
    # Create mask for Neon's color
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find largest contour (most likely the agent card)
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return (cx, cy)
    
    return None

def move_mouse_to(x, y):
    """Move mouse to position with configurable speed"""
    pyautogui.moveTo(x, y, duration=MOUSE_SPEED)

def click_agent():
    """Click on agent position"""
    pyautogui.click()
    time.sleep(0.2)

def instant_lock():
    """Main instalocker function"""
    global ACTIVE
    
    if not ACTIVE:
        return
    
    print("[*] Searching for Neon agent...")
    
    while ACTIVE:
        try:
            # Take screenshot
            screenshot = take_screenshot()
            
            # Find Neon position
            position = find_agent_name_position(screenshot, NEON_NAME)
            
            if position:
                x, y = position
                print(f"[+] Found Neon at position ({x}, {y})")
                
                # Move to Neon
                move_mouse_to(x, y)
                time.sleep(0.1)
                
                # Click to lock in
                click_agent()
                print("[✓] Neon locked in!")
                ACTIVE = False
                break
            
            # Small delay to avoid 100% CPU usage
            time.sleep(0.05)
            
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(0.1)

def toggle_instalocker():
    """Toggle instalocker on/off"""
    global ACTIVE
    ACTIVE = not ACTIVE
    
    if ACTIVE:
        print(f"[▶] Instalocker ACTIVATED! Waiting for agent select screen...")
        threading.Thread(target=instant_lock, daemon=True).start()
    else:
        print("[⏸] Instalocker deactivated")

def setup_hotkey():
    """Setup global hotkey listener"""
    print(f"[*] Press {HOTKEY} to toggle instalocker")
    keyboard.add_hotkey(HOTKEY, toggle_instalocker)

def main():
    """Main entry point"""
    print("=" * 50)
    print("  VALORANT INSTALOCKER - NEON")
    print("=" * 50)
    print(f"\nHotkey: {HOTKEY}")
    print("Status: Ready")
    print("\nInstructions:")
    print("1. Start Valorant and queue for a match")
    print("2. When you're in the match, press the hotkey to activate")
    print("3. The instalocker will automatically pick Neon")
    print("\n" + "=" * 50)
    
    # Setup hotkey
    setup_hotkey()
    
    # Keep the program running
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        exit(0)

if __name__ == "__main__":
    main()
