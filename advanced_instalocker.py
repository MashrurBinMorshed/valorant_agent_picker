"""
Advanced Valorant Instalocker with template matching
More reliable detection using pre-defined Neon card template
"""

import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab, Image
import threading
import keyboard
from pathlib import Path
import os

# Configuration
NEON_NAME = "NEON"
CONFIDENCE_THRESHOLD = 0.75
MOUSE_SPEED = 0.05  # seconds to move mouse (lower = faster) 
HOTKEY = "ctrl+shift+n"  # Hotkey to toggle
CLICK_OFFSET_X = 0  # X offset from detected position
CLICK_OFFSET_Y = 50  # Y offset (usually need to click below text)
ACTIVE = False
DEBUG_MODE = False

def take_screenshot():
    """Capture screenshot of entire screen"""
    screenshot = ImageGrab.grab()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def capture_neon_template():
    """
    Capture a template image of Neon card from current screen
    This is a calibration function - run this first to create template
    """
    print("[*] Capturing Neon template... Keep Valorant frontmost!")
    time.sleep(2)
    
    screenshot = take_screenshot()
    
    # Save template
    template_path = Path("neon_template.jpg")
    cv2.imwrite(str(template_path), screenshot[400:600, 200:400])
    print(f"[+] Template saved to {template_path}")

def find_neon_template_matching(screenshot):
    """
    Find Neon using template matching
    Requires neon_template.jpg to exist
    """
    template_path = Path("neon_template.jpg")
    
    if not template_path.exists():
        print("[!] Template not found. Using color detection instead...")
        return find_neon_by_color(screenshot)
    
    template = cv2.imread(str(template_path))
    
    if template is None:
        return find_neon_by_color(screenshot)
    
    # Resize template if screenshot is different size
    h, w = template.shape[:2]
    
    # Multi-scale matching for robustness
    scales = [1.0, 0.9, 1.1]
    best_match = None
    best_val = 0
    best_pos = None
    
    for scale in scales:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale)
        
        result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val > best_val:
            best_val = max_val
            best_match = resized_template
            best_pos = max_loc
    
    if best_val > CONFIDENCE_THRESHOLD:
        # Calculate center of match
        h, w = best_match.shape[:2]
        x = best_pos[0] + w // 2 + CLICK_OFFSET_X
        y = best_pos[1] + h // 2 + CLICK_OFFSET_Y
        return (x, y, best_val)
    
    return None

def find_neon_by_color(screenshot):
    """
    Detect Neon by distinctive color/appearance
    Neon has purple/cyan color scheme
    """
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
    
    # Create masks for purple/magenta tones characteristic of Neon
    lower_purple1 = np.array([125, 40, 40])
    upper_purple1 = np.array([155, 255, 255])
    
    # Also check for cyan (alternative Neon accent color)
    lower_cyan = np.array([80, 50, 50])
    upper_cyan = np.array([100, 255, 255])
    
    mask_purple = cv2.inRange(hsv, lower_purple1, upper_purple1)
    mask_cyan = cv2.inRange(hsv, lower_cyan, upper_cyan)
    mask = cv2.bitwise_or(mask_purple, mask_cyan)
    
    # Morphological operations to clean up
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Find largest contour
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        
        # Sanity check - agent card should have reasonable size
        if area > 1000:
            M = cv2.moments(largest)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"]) + CLICK_OFFSET_Y
                return (cx, cy, area)
    
    return None

def find_neon_ocr(screenshot):
    """
    Find Neon using OCR (Tesseract)
    Slower but more reliable for text detection
    """
    try:
        import pytesseract
        
        # Configure Tesseract path (adjust if needed)
        pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        
        gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        
        # Find "NEON" text
        for i, text in enumerate(data['text']):
            if NEON_NAME.lower() in text.lower():
                x = data['left'][i] + data['width'][i] // 2 + CLICK_OFFSET_X
                y = data['top'][i] + data['height'][i] // 2 + CLICK_OFFSET_Y
                confidence = data['conf'][i] / 100.0
                
                if confidence > 0.6:
                    return (x, y, confidence)
    
    except ImportError:
        pass
    
    return None

def find_neon_position(screenshot):
    """
    Try multiple methods to find Neon in priority order
    """
    # Method 1: OCR (most reliable)
    result = find_neon_ocr(screenshot)
    if result:
        return result
    
    # Method 2: Template matching
    result = find_neon_template_matching(screenshot)
    if result:
        return result
    
    # Method 3: Color detection (fallback)
    result = find_neon_by_color(screenshot)
    if result:
        return result
    
    return None

def move_mouse_to(x, y):
    """Smooth mouse movement"""
    pyautogui.moveTo(int(x), int(y), duration=MOUSE_SPEED)

def click():
    """Click at current mouse position"""
    pyautogui.click()
    time.sleep(0.1)

def instant_lock():
    """Main instalocker loop"""
    global ACTIVE
    
    attempt_count = 0
    max_attempts = 300  # ~15 seconds at 50ms intervals
    
    print("[*] Instalocker active - searching for Neon...")
    
    while ACTIVE and attempt_count < max_attempts:
        try:
            screenshot = take_screenshot()
            result = find_neon_position(screenshot)
            
            if result:
                x, y = result[0], result[1]
                confidence = result[2] if len(result) > 2 else "N/A"
                
                print(f"[+] NEON FOUND! Position: ({x:.0f}, {y:.0f}) | Confidence: {confidence}")
                
                # Move to position
                move_mouse_to(x, y)
                time.sleep(0.05)
                
                # Click to lock
                click()
                print("[✓] NEON LOCKED IN!")
                
                ACTIVE = False
                return True
            
            attempt_count += 1
            time.sleep(0.05)
        
        except Exception as e:
            print(f"[!] Error: {e}")
            time.sleep(0.1)
    
    if attempt_count >= max_attempts:
        print("[✗] Timeout - Neon not found")
        ACTIVE = False
    
    return False

def toggle_instalocker():
    """Toggle instalocker"""
    global ACTIVE
    ACTIVE = not ACTIVE
    
    if ACTIVE:
        print(f"\n{'='*50}")
        print("[▶] INSTALOCKER ACTIVATED!")
        print(f"{'='*50}\n")
        threading.Thread(target=instant_lock, daemon=True).start()
    else:
        print(f"\n{'='*50}")
        print("[⏸] Instalocker deactivated")
        print(f"{'='*50}\n")

def setup_hotkey():
    """Setup global hotkey"""
    print(f"\n[*] Global hotkey: {HOTKEY}")
    keyboard.add_hotkey(HOTKEY, toggle_instalocker)

def main():
    """Main entry point"""
    print("\n" + "="*60)
    print("   VALORANT INSTALOCKER - ADVANCED NEON PICKER")
    print("="*60)
    print("\nFEATURES:")
    print("  ✓ Multi-method detection (OCR, Template, Color)")
    print("  ✓ Instant mouse movement")
    print("  ✓ Global hotkey support")
    print("  ✓ Confidence scoring")
    print("\nUSAGE:")
    print(f"  1. Press {HOTKEY} to activate")
    print("  2. Switch to Valorant")
    print("  3. Auto-pick will trigger during agent select")
    print("\nCONTROLS:")
    print(f"  {HOTKEY} = Toggle instalocker")
    print("  Ctrl+C    = Exit")
    print("\n" + "="*60 + "\n")
    
    setup_hotkey()
    
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n[*] Exiting...\n")
        exit(0)

if __name__ == "__main__":
    main()
