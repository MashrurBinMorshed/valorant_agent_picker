# VALORANT INSTALOCKER - SETUP GUIDE

## Overview
This instalocker automatically picks **Neon** (or any agent) during agent selection in Valorant with instant mouse control.

**Now with full CLI (Command-Line Interface)!** - Complete command-line control without GUI menus.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR (Optional but Recommended)
For better text recognition, install Tesseract:
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install to default location: `C:\Program Files\Tesseract-OCR\`

### 3. Run the Instalocker (CLI Version)
```bash
# Quick start with defaults
python instalocker.py start

# With custom agent and hotkey
python instalocker.py start --agent REYNA --hotkey "alt+r"

# See all options
python instalocker.py start --help
```

### 4. Configure
Press your hotkey during agent select to activate.

---

## CLI Documentation

For complete CLI command reference, see [CLI_GUIDE.md](CLI_GUIDE.md) or [CLI_CHEATSHEET.md](CLI_CHEATSHEET.md).

### Common CLI Commands

```bash
# Start picker
python instalocker.py start

# Show config
python instalocker.py config --show

# Set default agent
python instalocker.py config --set agent=REYNA

# Run once immediately
python instalocker.py start --no-hotkey

# Create template for better detection
python instalocker.py calibrate --agent NEON
```

---

## Windows Batch Files (Easy Mode)

Use pre-made batch files in `batch_examples/` folder:
- `start_neon.bat` - Pick Neon
- `start_reyna.bat` - Pick Reyna
- `start_fast.bat` - Fast mode
- `run_once.bat` - Run once
- `calibrate_neon.bat` - Create template

Just double-click!

---

## Alternative: GUI Launcher

For menu-based interface:
```bash
python launcher.py
```

---

## How It Works

### Detection Methods (Priority Order)
1. **OCR (Tesseract)** - Recognizes "NEON" text directly
2. **Template Matching** - Compares against known Neon card image
3. **Color Detection** - Identifies Neon's purple/cyan color scheme

### Configuration Options

Edit the top of `advanced_instalocker.py`:

```python
CONFIDENCE_THRESHOLD = 0.75   # Detection confidence (0-1)
MOUSE_SPEED = 0.05            # Mouse move speed (lower = faster)
HOTKEY = "ctrl+shift+n"       # Activation hotkey
CLICK_OFFSET_Y = 50           # Vertical offset for clicking
```

---

## Usage Instructions

1. **Start Valorant** and queue for a match
2. **Enter Agent Select screen**
3. **Press your hotkey** (default: `Ctrl+Shift+N`)
4. **Instalocker will automatically**:
   - Detect Neon's position
   - Move mouse to Neon
   - Click to lock in
   - Display confirmation message

---

## Troubleshooting

### Instalocker doesn't detect Neon
- Ensure Valorant window is visible
- Try increasing timeout in the script
- Manually calibrate by capturing a template (see "Advanced" section)

### Mouse moves too slow/fast
- Adjust `MOUSE_SPEED` value (0.01 = fast, 0.2 = slow)

### Hotkey not working
- Run as Administrator
- Try different hotkey combo: `"alt+n"`, `"f6"`, etc.

### Tesseract not found
- Install from: https://github.com/UB-Mannheim/tesseract/wiki
- Or adjust path in script: `pytesseract.pytesseract_cmd = r'path\to\tesseract.exe'`

---

## Advanced

### Create Custom Neon Template
1. Open agent select with Neon visible
2. Run: `python calibrate.py`
3. This creates `neon_template.jpg` for template matching

### Different Agent Picker
Modify detection to find a different agent by:
- Changing color range in `find_neon_by_color()`
- Creating a template for the different agent
- Adjusting OCR text search

---

## Safety Notes

- **USE AT YOUR OWN RISK** - Valorant may detect automation
- Account bans possible if detected
- Not recommended for ranked matches
- Test in Practice Tool first

---

## Requirements

- Python 3.8+
- Valorant installed
- Admin privileges (for keyboard hook)
- 1600x900+ screen resolution recommended

---

## Support

If detection fails:
1. Check if Valorant window is active
2. Verify agent select screen is visible
3. Try different `CONFIDENCE_THRESHOLD` value
4. Check console output for error messages

Good luck, Agent!
