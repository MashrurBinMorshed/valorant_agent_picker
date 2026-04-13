# Valorant Instalocker - CLI Guide

## Overview

The instalocker now has a full **command-line interface (CLI)** for complete control without GUI menus.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Commands

### 1. START - Run the Instalocker

**Basic usage:**
```bash
python instalocker.py start
```

**With options:**
```bash
# Pick a different agent
python instalocker.py start --agent REYNA

# Set custom hotkey
python instalocker.py start --hotkey "alt+n"

# Adjust mouse speed (0.01 = fast, 0.2 = slow)
python instalocker.py start --mouse-speed 0.05

# Set detection confidence (0.5 = lenient, 1.0 = strict)
python instalocker.py start --confidence 0.75

# Set max search time in seconds
python instalocker.py start --max-time 20

# Enable debug output
python instalocker.py start --debug

# Run once without hotkey (immediate pickup)
python instalocker.py start --no-hotkey
```

**Examples:**
```bash
# Quick start with defaults
python instalocker.py start

# Start picking REYNA with fast mouse
python instalocker.py start --agent REYNA --mouse-speed 0.02

# Start with custom hotkey and debug mode
python instalocker.py start --hotkey "f6" --debug

# Run once immediately
python instalocker.py start --no-hotkey

# Combine multiple options
python instalocker.py start --agent VIPER --hotkey "shift+f" --mouse-speed 0.03 --max-time 15
```

---

### 2. CONFIG - Manage Configuration

**Show current configuration:**
```bash
python instalocker.py config --show
```

**Set configuration values:**
```bash
python instalocker.py config --set agent=REYNA
python instalocker.py config --set agent=SAGE mouse_speed=0.1
python instalocker.py config --set confidence=0.8 max_time=20
```

**Reset to defaults:**
```bash
python instalocker.py config --reset
```

**Configuration options:**
- `agent` - Agent to pick (NEON, REYNA, SAGE, JETT, VIPER, KILLJOY, etc.)
- `hotkey` - Activation hotkey (ctrl+shift+n, alt+n, f6, etc.)
- `mouse_speed` - Mouse speed 0.01-0.2 (lower = faster)
- `confidence` - Detection confidence 0.0-1.0
- `click_offset_x` - Horizontal click offset
- `click_offset_y` - Vertical click offset
- `max_time` - Max search time in seconds
- `debug` - Enable debug output

**Examples:**
```bash
# See what's configured
python instalocker.py config --show

# Change default agent to REYNA
python instalocker.py config --set agent=REYNA

# Make mouse slower
python instalocker.py config --set mouse_speed=0.1

# Set multiple at once
python instalocker.py config --set agent=SAGE hotkey="alt+s" mouse_speed=0.05

# Reset everything to defaults
python instalocker.py config --reset
```

---

### 3. CALIBRATE - Create Agent Template

**Calibrate for an agent:**
```bash
python instalocker.py calibrate --agent NEON
```

**Steps:**
1. Run the command
2. Keep Valorant agent select visible
3. Position your mouse on the agent card
4. Press SPACE to capture
5. Template is saved as `neon_template.jpg`

**Example:**
```bash
# Calibrate NEON (default)
python instalocker.py calibrate

# Calibrate different agent
python instalocker.py calibrate --agent REYNA
python instalocker.py calibrate --agent SAGE
```

---

### 4. VERSION

**Show version:**
```bash
python instalocker.py --version
```

---

## Usage Workflows

### Workflow 1: Quick Start
```bash
# Just run with defaults
python instalocker.py start
```
- Agent: NEON
- Hotkey: Ctrl+Shift+N
- Waits for you to press hotkey during agent select

### Workflow 2: Custom Agent
```bash
# Pick REYNA instead
python instalocker.py start --agent REYNA --hotkey "alt+r"
```

### Workflow 3: Immediate Pickup
```bash
# Run once immediately without waiting for hotkey
python instalocker.py start --no-hotkey
```

### Workflow 4: Save Configuration
```bash
# Set your preferred config once
python instalocker.py config --set agent=REYNA mouse_speed=0.05 hotkey="alt+r"

# Now just run with defaults
python instalocker.py start
```

### Workflow 5: Debug Mode
```bash
# Run with detailed output
python instalocker.py start --debug
```

### Workflow 6: Batch Script
Create `run_instalocker.bat`:
```batch
@echo off
python instalocker.py start --agent NEON --hotkey "ctrl+shift+n"
pause
```

Then run: `run_instalocker.bat`

---

## Configuration File

Settings are saved in `instalocker_config.json`:

```json
{
  "agent": "NEON",
  "hotkey": "ctrl+shift+n",
  "confidence": 0.75,
  "mouse_speed": 0.05,
  "click_offset_x": 0,
  "click_offset_y": 50,
  "max_time": 15,
  "debug": false
}
```

**Auto-created on first run** with defaults.

Modify directly or use `config --set` command.

---

## Windows Batch File

Use `instalocker.bat` for easy Windows launching:

```bash
instalocker.bat start
instalocker.bat start --agent REYNA
instalocker.bat config --show
instalocker.bat calibrate --agent SAGE
```

No need to type `python instalocker.py` each time.

---

## Common Hotkey Options

```bash
# Simple
"f6"
"f7"
"o"

# With Ctrl
"ctrl+n"
"ctrl+shift+n"

# With Alt
"alt+n"
"alt+r"
"alt+shift+n"

# With Shift
"shift+n"
"shift+f6"
```

---

## Agents Available

Pick any Valorant agent:
```bash
python instalocker.py start --agent NEON       # Neon
python instalocker.py start --agent REYNA      # Reyna
python instalocker.py start --agent SAGE       # Sage
python instalocker.py start --agent JETT       # Jett
python instalocker.py start --agent VIPER      # Viper
python instalocker.py start --agent KILLJOY    # Killjoy
python instalocker.py start --agent SOVA       # Sova
python instalocker.py start --agent PHOENIX    # Phoenix
python instalocker.py start --agent CYPHER     # Cypher
python instalocker.py start --agent OMEN       # Omen
python instalocker.py start --agent RAZE       # Raze
python instalocker.py start --agent BREACH     # Breach
python instalocker.py start --agent BRIMSTONE  # Brimstone
python instalocker.py start --agent CHAMBER    # Chamber
python instalocker.py start --agent ASTRA      # Astra
python instalocker.py start --agent HARBOR     # Harbor
python instalocker.py start --agent GEKko      # Gekko
python instalocker.py start --agent SKYE       # Skye
python instalocker.py start --agent KAY/O      # KAY/O
python instalocker.py start --agent FADE       # Fade
```

---

## Mouse Speed Guide

```bash
# Ultra fast (risky - might miss)
python instalocker.py start --mouse-speed 0.01

# Fast (recommended)
python instalocker.py start --mouse-speed 0.05

# Normal
python instalocker.py start --mouse-speed 0.1

# Slow (more reliable but visible)
python instalocker.py start --mouse-speed 0.2
```

---

## Advanced Examples

### Example 1: Production Setup
```bash
# Set your preferred config once
python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.03

# Then just run with no arguments
python instalocker.py start
```

### Example 2: Multiple Users
```bash
# User 1 prefers SAGE
python instalocker.py config --set agent=SAGE hotkey="alt+s"
python instalocker.py start

# User 2 prefers NEON
python instalocker.py config --set agent=NEON hotkey="alt+n"
python instalocker.py start
```

### Example 3: Fast Setup Script
Create `fast_neon.bat`:
```batch
@echo off
python instalocker.py start --agent NEON --mouse-speed 0.02 --hotkey "ctrl+shift+n"
```

### Example 4: Debug Session
```bash
# See what's happening
python instalocker.py start --debug
```

Output:
```
[D] Found NEON via OCR: (640, 360, 0.95)
[+] NEON found at (640, 410) - 0.34s
[✓] NEON LOCKED IN!
```

---

## Tips & Tricks

1. **Save time**: Use config to set defaults
   ```bash
   python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.03
   ```

2. **Test before match**: Use `--no-hotkey` to run once
   ```bash
   python instalocker.py start --no-hotkey
   ```

3. **Fast clicks**: Lower mouse speed
   ```bash
   python instalocker.py start --mouse-speed 0.02
   ```

4. **More reliable**: Higher confidence
   ```bash
   python instalocker.py start --confidence 0.8
   ```

5. **Create template**: Improves detection
   ```bash
   python instalocker.py calibrate --agent NEON
   ```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Hotkey not working | Run as Administrator |
| Mouse moves wrong position | Adjust `click_offset_x` and `click_offset_y` |
| Doesn't detect agent | Run calibration, increase `max_time` |
| Mouse too slow | Decrease `mouse_speed` value |
| False detections | Increase `confidence` value |

---

## Exit

Press `Ctrl+C` to stop the instalocker anytime.

---

Enjoy your instant picks! 🎮
