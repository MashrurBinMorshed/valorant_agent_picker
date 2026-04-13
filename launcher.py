"""
Quick launcher for Valorant Instalocker
Choose which version to run
"""

import subprocess
import sys
from pathlib import Path

def check_dependencies():
    """Check if required packages are installed"""
    required = ['pyautogui', 'keyboard', 'cv2', 'PIL']
    missing = []
    
    for package in required:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("[!] Missing dependencies!")
        print(f"    Run: pip install -r requirements.txt\n")
        return False
    
    return True

def main():
    print("\n" + "="*60)
    print("   VALORANT INSTALOCKER - LAUNCHER")
    print("="*60)
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    print("\n[✓] All dependencies installed\n")
    
    print("SELECT VERSION TO RUN:")
    print("-" * 60)
    print("1. Advanced Instalocker (Recommended)")
    print("   - Multi-method detection (OCR, Template, Color)")
    print("   - Better accuracy and reliability")
    print("")
    print("2. Basic Instalocker")
    print("   - Simpler implementation")
    print("   - Lighter on resources")
    print("")
    print("3. Calibration Tool")
    print("   - Create/update Neon template")
    print("   - Improves detection accuracy")
    print("")
    print("4. Exit")
    print("-" * 60)
    
    choice = input("\nEnter choice [1-4]: ").strip()
    
    if choice == "1":
        print("\n[▶] Starting Advanced Instalocker...")
        print("    Press Ctrl+Shift+N to activate")
        print("    Press Ctrl+C to exit\n")
        subprocess.run([sys.executable, "advanced_instalocker.py"])
    
    elif choice == "2":
        print("\n[▶] Starting Basic Instalocker...")
        print("    Press Ctrl+Shift+N to activate")
        print("    Press Ctrl+C to exit\n")
        subprocess.run([sys.executable, "main.py"])
    
    elif choice == "3":
        print("\n[▶] Starting Calibration Tool...")
        subprocess.run([sys.executable, "calibrate.py"])
    
    elif choice == "4":
        print("\n[*] Exiting...\n")
        return
    
    else:
        print("[!] Invalid choice\n")
        main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Launcher closed\n")
    except Exception as e:
        print(f"\n[!] Error: {e}")
        input("Press Enter to exit...")
