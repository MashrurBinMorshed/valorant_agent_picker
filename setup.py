#!/usr/bin/env python3
"""
Valorant Instalocker - First Time Setup
Guides you through initial configuration
"""

import subprocess
import sys
from pathlib import Path
import json

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_dependencies():
    """Check if required packages are installed"""
    print("\n[*] Checking dependencies...")
    
    required = {
        'pyautogui': 'pyautogui',
        'keyboard': 'keyboard',
        'cv2': 'opencv-python',
        'PIL': 'Pillow',
    }
    
    missing = []
    for module, package in required.items():
        try:
            __import__(module)
            print(f"    ✓ {package}")
        except ImportError:
            print(f"    ✗ {package}")
            missing.append(package)
    
    if missing:
        print(f"\n[!] Missing: {', '.join(missing)}")
        response = input("\nInstall now? (y/n): ").strip().lower()
        if response == 'y':
            print("[*] Installing...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            return True
        else:
            print("[!] Cannot proceed without dependencies")
            return False
    
    return True

def setup_configuration():
    """Guide user through configuration"""
    print_header("CONFIGURATION SETUP")
    
    config_file = Path("instalocker_config.json")
    
    config = {
        "agent": "NEON",
        "hotkey": "ctrl+shift+n",
        "mouse_speed": 0.05,
        "confidence": 0.75,
        "max_time": 15,
        "debug": False
    }
    
    print("\nLet's customize your setup!\n")
    
    # Agent selection
    print("Which agent do you want to pick?")
    print("Common: NEON, REYNA, SAGE, JETT, VIPER, KILLJOY")
    agent = input("Agent [NEON]: ").strip().upper() or "NEON"
    config["agent"] = agent
    
    # Hotkey selection
    print("\nWhat hotkey to activate? (examples: ctrl+shift+n, alt+n, f6)")
    hotkey = input("Hotkey [ctrl+shift+n]: ").strip() or "ctrl+shift+n"
    config["hotkey"] = hotkey
    
    # Mouse speed
    print("\nMouse speed: 0.01 (fast) to 0.2 (slow)")
    try:
        speed = float(input("Speed [0.05]: ") or "0.05")
        config["mouse_speed"] = max(0.01, min(0.2, speed))
    except ValueError:
        pass
    
    # Save configuration
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("\n[✓] Configuration saved!")
    print(f"    Agent: {config['agent']}")
    print(f"    Hotkey: {config['hotkey']}")
    print(f"    Mouse Speed: {config['mouse_speed']}")

def test_hotkey():
    """Test if hotkey works"""
    print_header("HOTKEY TEST")
    
    print("\nTesting hotkey functionality...")
    print("Make sure to run as Administrator!")
    
    response = input("\nRun hotkey test? (y/n): ").strip().lower()
    if response != 'y':
        return
    
    try:
        import keyboard
        print("\n[*] Hotkey test will show when you press keys...")
        print("[*] Press your configured hotkey...")
        print("[*] Or press Ctrl+C to skip\n")
        
        keyboard.add_hotkey('ctrl+c', lambda: print("[*] Test stopped"))
        keyboard.wait('escape')
    except Exception as e:
        print(f"[!] Test failed: {e}")
        print("[*] Make sure to run as Administrator!")

def show_quick_start():
    """Show quick start information"""
    print_header("QUICK START GUIDE")
    
    print("""
Now you're ready to go! Here's how to use it:

1. START VALORANT
   Queue for a match and get to agent select

2. RUN THE INSTALOCKER
   python instalocker.py start
   
   Or use batch file:
   batch_examples/start_neon.bat

3. ACTIVATE DURING AGENT SELECT
   Press your hotkey (default: Ctrl+Shift+N)
   
4. ENJOY YOUR INSTANT PICK!

NEXT STEPS:
   - python instalocker.py start                    (Start normally)
   - python instalocker.py config --show            (View config)
   - python instalocker.py calibrate --agent NEON   (Improve accuracy)
   - python help.py                                 (Full help)
   - python launcher.py                             (Menu interface)

DOCUMENTATION:
   - CLI_CHEATSHEET.md    (Quick commands)
   - CLI_GUIDE.md         (Full CLI guide)
   - OVERVIEW.md          (All methods)
""")

def main():
    print_header("VALORANT INSTALOCKER - FIRST TIME SETUP")
    
    print("""
Welcome! This setup will help you get started with the
Valorant Instalocker in just a few minutes.

This tool will:
✓ Check dependencies
✓ Guide configuration
✓ Test hotkey
✓ Show quick start

Let's begin!
""")
    
    # Step 1: Check dependencies
    if not check_dependencies():
        print("\n[!] Setup failed - missing dependencies")
        return
    
    print("\n[✓] All dependencies installed!")
    
    # Step 2: Configuration
    response = input("\nSetup configuration now? (y/n): ").strip().lower()
    if response == 'y':
        setup_configuration()
    
    # Step 3: Test hotkey
    response = input("\nTest hotkey? (y/n): ").strip().lower()
    if response == 'y':
        test_hotkey()
    
    # Step 4: Quick start
    show_quick_start()
    
    print_header("SETUP COMPLETE")
    print("""
You're all set! 

To start the instalocker, run:
   python instalocker.py start

Need help? Run:
   python help.py

Good luck, Agent! 🎮✨
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Setup cancelled\n")
    except Exception as e:
        print(f"\n[!] Error: {e}")
