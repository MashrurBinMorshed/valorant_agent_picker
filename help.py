#!/usr/bin/env python3
"""
Valorant Instalocker - Help Command
Display help information and usage examples
"""

import sys

HELP_TEXT = """
╔════════════════════════════════════════════════════════════════╗
║        VALORANT INSTALOCKER - HELP & DOCUMENTATION            ║
╚════════════════════════════════════════════════════════════════╝

GETTING STARTED
═══════════════════════════════════════════════════════════════

1. INSTALLATION
   ────────────
   pip install -r requirements.txt

2. CHOOSE YOUR METHOD
   ──────────────────

   A) EASIEST - Windows Batch Files
      Go to batch_examples/ and double-click any .bat file
      
   B) CLI - Full Control
      python instalocker.py start
      
   C) MENU - Interactive
      python launcher.py

3. USAGE
   ──────
   Press your hotkey during agent select to activate.


QUICK COMMANDS
═══════════════════════════════════════════════════════════════

START THE INSTALOCKER
   python instalocker.py start

SHOW CONFIGURATION
   python instalocker.py config --show

SET DEFAULT AGENT
   python instalocker.py config --set agent=REYNA

CREATE TEMPLATE (Better Detection)
   python instalocker.py calibrate --agent NEON

RUN ONCE (No Hotkey)
   python instalocker.py start --no-hotkey

DEBUG MODE
   python instalocker.py start --debug


COMMAND REFERENCE
═══════════════════════════════════════════════════════════════

START OPTIONS
   --agent AGENT         Pick agent (NEON, REYNA, SAGE, etc.)
   --hotkey HOTKEY      Activation key (ctrl+shift+n, alt+n, f6)
   --mouse-speed SPEED  Speed 0.01-0.2 (lower = faster)
   --confidence CONF    Strictness 0.0-1.0 (higher = stricter)
   --max-time TIME      Search timeout in seconds
   --debug              Show detailed output
   --no-hotkey          Run once immediately

CONFIG OPTIONS
   --show               Display all settings
   --set KEY=VALUE      Change settings (can set multiple)
   --reset              Restore defaults

CALIBRATE OPTIONS
   --agent AGENT        Agent to calibrate


EXAMPLES
═══════════════════════════════════════════════════════════════

EXAMPLE 1: Start Right Now
   python instalocker.py start
   
   → Picks NEON
   → Press Ctrl+Shift+N in agent select
   → Done!

EXAMPLE 2: Different Agent
   python instalocker.py start --agent REYNA
   
   → Picks REYNA
   → Press Ctrl+Shift+N in agent select

EXAMPLE 3: Custom Hotkey
   python instalocker.py start --hotkey "alt+r"
   
   → Press Alt+R to activate

EXAMPLE 4: Fast Mode
   python instalocker.py start --mouse-speed 0.02
   
   → Ultra-fast mouse movement

EXAMPLE 5: Save Configuration
   python instalocker.py config --set agent=REYNA
   python instalocker.py config --set hotkey="alt+r"
   python instalocker.py start
   
   → Next time just: python instalocker.py start

EXAMPLE 6: Full Custom Setup
   python instalocker.py start \\
     --agent SAGE \\
     --hotkey "alt+s" \\
     --mouse-speed 0.05 \\
     --confidence 0.8
   
   → Fully customized


HOTKEY OPTIONS
═══════════════════════════════════════════════════════════════

Simple Keys
   "f6"                 Function key
   "o"                  Letter key
   
With Modifiers
   "ctrl+n"             Control + N
   "alt+n"              Alt + N
   "shift+n"            Shift + N
   "ctrl+shift+n"       Ctrl + Shift + N (Default)

Combinations
   "alt+shift+n"
   "ctrl+alt+n"


AGENTS
═══════════════════════════════════════════════════════════════

All Available Agents:
   NEON, REYNA, SAGE, JETT, VIPER, KILLJOY, SOVA, PHOENIX,
   CYPHER, OMEN, RAZE, BREACH, BRIMSTONE, CHAMBER, ASTRA,
   HARBOR, GEKKO, SKYE, KAY/O, FADE


CONFIGURATION FILE
═══════════════════════════════════════════════════════════════

Auto-created: instalocker_config.json

Example contents:
   {
     "agent": "NEON",
     "hotkey": "ctrl+shift+n",
     "mouse_speed": 0.05,
     "confidence": 0.75,
     "max_time": 15,
     "debug": false
   }

Edit directly or use: python instalocker.py config --set


BATCH FILES (WINDOWS)
═══════════════════════════════════════════════════════════════

Location: batch_examples/

Files Included:
   start_neon.bat          Pick NEON (default)
   start_reyna.bat         Pick REYNA
   start_fast.bat          Ultra-fast mode
   start_debug.bat         Debug output
   run_once.bat            Run immediately
   show_config.bat         Show settings
   calibrate_neon.bat      Create template

Usage: Just double-click!


TROUBLESHOOTING
═══════════════════════════════════════════════════════════════

HOTKEY NOT WORKING
   → Run as Administrator
   → Try different hotkey combination
   → Check if Valorant window is active

AGENT NOT DETECTED
   → Create template: python instalocker.py calibrate --agent NEON
   → Increase max-time: python instalocker.py start --max-time 20
   → Use debug: python instalocker.py start --debug

MOUSE MOVEMENTS WRONG
   → Run calibration for your agent
   → Adjust offsets in config
   → Use debug mode to see positions

TESSERACT NOT FOUND
   → Install from: https://github.com/UB-Mannheim/tesseract/wiki
   → Or skip OCR (uses color detection fallback)

DETECTION TOO SENSITIVE
   → Increase confidence: python instalocker.py start --confidence 0.85
   → Reduce max-time: python instalocker.py start --max-time 10

DETECTION NOT SENSITIVE ENOUGH
   → Decrease confidence: python instalocker.py start --confidence 0.65
   → Increase max-time: python instalocker.py start --max-time 20
   → Create template: python instalocker.py calibrate --agent NEON


DOCUMENTATION FILES
═══════════════════════════════════════════════════════════════

README.md              Full setup guide
QUICKSTART.md          Quick 5-minute setup
CLI_GUIDE.md           Complete CLI documentation
CLI_CHEATSHEET.md      Quick command reference
OVERVIEW.md            All methods comparison
config.ini             Configuration template


PERFORMANCE TIPS
═══════════════════════════════════════════════════════════════

FASTER DETECTION
   python instalocker.py start --mouse-speed 0.02

MORE RELIABLE
   python instalocker.py start --confidence 0.85

BALANCED
   python instalocker.py start --mouse-speed 0.05 --confidence 0.75

DEBUG INFO
   python instalocker.py start --debug


KEYBOARD SHORTCUTS
═══════════════════════════════════════════════════════════════

During Execution:
   Ctrl+C    Stop the instalocker
   
During Calibration:
   Space     Capture template
   Ctrl+C    Cancel calibration


FREQUENTLY ASKED QUESTIONS
═══════════════════════════════════════════════════════════════

Q: Which version should I use?
A: Use CLI (instalocker.py) - simplest and most powerful.

Q: How do I pick a different agent?
A: python instalocker.py start --agent REYNA

Q: Can I save my settings?
A: Yes: python instalocker.py config --set agent=REYNA

Q: Will I get banned?
A: Valorant may flag automation. Use at your own risk.

Q: How fast is it?
A: <500ms typically from hotkey to locked in.

Q: Does it work on Linux/Mac?
A: Windows only (uses Windows-specific imports).

Q: Can I run multiple at once?
A: Yes, in different terminals with different hotkeys.

Q: How do I improve detection?
A: Run: python instalocker.py calibrate --agent NEON

Q: What if detection fails?
A: Check debug output: python instalocker.py start --debug

Q: Can I use different hotkeys for different agents?
A: Yes, run multiple instances or change hotkey as needed.


GETTING HELP
═══════════════════════════════════════════════════════════════

1. Check documentation files (see DOCUMENTATION FILES above)
2. Run with --debug tag: python instalocker.py start --debug
3. Check console output for error messages
4. Try calibration: python instalocker.py calibrate --agent NEON


VERSION INFO
═══════════════════════════════════════════════════════════════

Display version:
   python instalocker.py --version

Current version: 1.0.0


SAFETY & ETHICS
═══════════════════════════════════════════════════════════════

⚠️  WARNING
  - This tool is experimental
  - Using automation may violate Valorant's Terms of Service
  - Your account could be suspended or banned
  - Use only in practice or casual matches
  - Use at your own risk

✅  RECOMMENDED
  - Test in Practice Tool first
  - Use only for casual/unrated matches
  - Be aware of anti-cheat detection
  - Read Valorant's ToS before using


ADDITIONAL RESOURCES
═══════════════════════════════════════════════════════════════

Important Files:
   requirements.txt       Dependencies to install
   config.ini            Configuration options
   instalocker.py        Main CLI program

Folders:
   batch_examples/       Windows batch files


EXAMPLES CHEAT SHEET
═══════════════════════════════════════════════════════════════

# Start with defaults
python instalocker.py start

# Pick REYNA with Alt+R hotkey
python instalocker.py start --agent REYNA --hotkey "alt+r"

# Show current configuration
python instalocker.py config --show

# Save REYNA as default
python instalocker.py config --set agent=REYNA

# Fast mode
python instalocker.py start --mouse-speed 0.02

# Debug mode
python instalocker.py start --debug

# Run once now
python instalocker.py start --no-hotkey

# Create template
python instalocker.py calibrate --agent NEON


SYSTEM REQUIREMENTS
═══════════════════════════════════════════════════════════════

- Windows 7+ or Windows 10/11
- Python 3.8+
- Administrator privileges (for global hotkey)
- 1600x900+ screen resolution (recommended)
- Valorant installed


CREDITS
═══════════════════════════════════════════════════════════════

Built with:
  - PyAutoGUI (mouse/keyboard control)
  - OpenCV (image recognition)
  - Tesseract OCR (text detection)
  - keyboard (global hotkey)


═══════════════════════════════════════════════════════════════

For more help, check the documentation files or run:
   python instalocker.py --help

Good luck, Agent! 🎮✨

═══════════════════════════════════════════════════════════════
"""

def main():
    print(HELP_TEXT)

if __name__ == "__main__":
    main()
