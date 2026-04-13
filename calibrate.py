"""
Calibration script to create Neon template for template matching
Run this when Neon is visible in agent select screen
"""

import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab
from pathlib import Path
import sys

def take_screenshot():
    """Capture screenshot"""
    screenshot = ImageGrab.grab()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def show_regions(image):
    """Display possible agent card regions for calibration"""
    h, w = image.shape[:2]
    
    # Common agent card positions on screen
    regions = [
        ("Center", (w//2-150, h//2-100, 300, 200)),
        ("Left", (w//4-100, h//2-100, 200, 200)),
        ("Right", (w-w//4-100, h//2-100, 200, 200)),
        ("Top-Center", (w//2-150, h//4-50, 300, 150)),
    ]
    
    print("\n" + "="*60)
    print("POSSIBLE NEON CARD REGIONS:")
    print("="*60)
    for name, (x, y, rw, rh) in regions:
        print(f"  {name:12} | Pos: ({x:4}, {y:4}) | Size: {rw}x{rh}")
    print("="*60)

def manual_template_capture():
    """Manual template selection"""
    print("\n[*] MANUAL TEMPLATE CAPTURE")
    print("="*60)
    print("Keep your mouse pointer on Neon's agent card")
    print("Press SPACE when ready to capture template")
    print("="*60)
    
    import keyboard
    keyboard.wait('space')
    
    # Get mouse position
    x, y = pyautogui.position()
    
    # Capture template around mouse (300x200 region)
    template_width = 280
    template_height = 200
    
    start_x = max(0, x - template_width // 2)
    start_y = max(0, y - template_height // 2)
    
    print(f"\n[*] Capturing from position: ({start_x}, {start_y})")
    print("    3...")
    time.sleep(1)
    print("    2...")
    time.sleep(1)
    print("    1...")
    time.sleep(1)
    
    screenshot = take_screenshot()
    h, w = screenshot.shape[:2]
    
    # Ensure we don't go out of bounds
    end_x = min(w, start_x + template_width)
    end_y = min(h, start_y + template_height)
    
    template = screenshot[start_y:end_y, start_x:end_x]
    
    # Save template
    output_path = Path("neon_template.jpg")
    cv2.imwrite(str(output_path), template)
    
    print(f"\n[✓] Template saved to: {output_path}")
    print(f"    Size: {template.shape[1]}x{template.shape[0]} pixels")
    
    return output_path

def auto_detect_by_color(image):
    """Auto-detect Neon card by color"""
    print("\n[*] AUTO-DETECTING NEON BY COLOR...")
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Neon purple/magenta range
    lower_purple = np.array([125, 40, 40])
    upper_purple = np.array([155, 255, 255])
    mask = cv2.inRange(hsv, lower_purple, upper_purple)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        print("[!] Could not auto-detect Neon. Please use manual capture.")
        return None
    
    # Find largest contour
    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    
    print(f"[+] Detected at: ({x}, {y}) | Size: {w}x{h}")
    
    # Extract template with padding
    padding = 20
    x1 = max(0, x - padding)
    y1 = max(0, y - padding)
    x2 = min(image.shape[1], x + w + padding)
    y2 = min(image.shape[0], y + h + padding)
    
    template = image[y1:y2, x1:x2]
    
    output_path = Path("neon_template.jpg")
    cv2.imwrite(str(output_path), template)
    
    print(f"[✓] Template saved to: {output_path}")
    print(f"    Size: {template.shape[1]}x{template.shape[0]} pixels")
    
    return output_path

def validate_template():
    """Validate saved template"""
    template_path = Path("neon_template.jpg")
    
    if not template_path.exists():
        print("[!] Template not found!")
        return False
    
    template = cv2.imread(str(template_path))
    if template is None:
        print("[!] Could not read template file")
        return False
    
    h, w = template.shape[:2]
    print(f"\n[✓] Template valid!")
    print(f"    File: {template_path}")
    print(f"    Size: {w}x{h} pixels")
    
    return True

def main():
    """Main calibration flow"""
    print("\n" + "="*60)
    print("       VALORANT INSTALOCKER - TEMPLATE CALIBRATION")
    print("="*60)
    
    print("\nSTEP 1: Get current screenshot")
    time.sleep(2)
    screenshot = take_screenshot()
    print("[✓] Screenshot captured")
    
    # Show regions
    show_regions(screenshot)
    
    print("\n" + "="*60)
    print("STEP 2: Choose capture method")
    print("="*60)
    print("1. Auto-detect by color (Fast)")
    print("2. Manual capture (Accurate)")
    print("3. Skip calibration")
    
    choice = input("\nSelect [1-3]: ").strip()
    
    if choice == "1":
        print("\n[*] Attempting auto-detection...")
        auto_detect_by_color(screenshot)
    
    elif choice == "2":
        manual_template_capture()
    
    elif choice == "3":
        print("[*] Skipping calibration")
        return
    
    else:
        print("[!] Invalid choice")
        return
    
    # Validate
    print("\nSTEP 3: Validating template...")
    if validate_template():
        print("\n" + "="*60)
        print("✓ CALIBRATION COMPLETE!")
        print("  Template ready for use in advanced_instalocker.py")
        print("="*60)
    else:
        print("\n[!] Template validation failed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Calibration cancelled")
    except Exception as e:
        print(f"\n[!] Error: {e}")
