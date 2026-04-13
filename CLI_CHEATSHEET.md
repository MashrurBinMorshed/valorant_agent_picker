# Valorant Instalocker - CLI Cheat Sheet

Quick reference for command-line usage.

## Quick Commands

```bash
# Start with defaults (NEON, Ctrl+Shift+N)
python instalocker.py start

# Show current config
python instalocker.py config --show

# Change agent to REYNA
python instalocker.py config --set agent=REYNA

# Run once immediately
python instalocker.py start --no-hotkey

# Calibrate for NEON
python instalocker.py calibrate --agent NEON
```

---

## All START Options

```bash
python instalocker.py start [OPTIONS]

OPTIONS:
  --agent AGENT           Agent name (NEON, REYNA, SAGE, etc.)
  --hotkey HOTKEY        Activation hotkey (ctrl+shift+n, alt+n, f6, etc.)
  --mouse-speed SPEED    Mouse speed 0.01-0.2 (0.05 = default)
  --confidence CONF      Detection confidence 0.0-1.0 (0.75 = default)
  --max-time TIME        Max search seconds (15 = default)
  --debug                Show debug output
  --no-hotkey            Run once immediately without hotkey
```

---

## All CONFIG OPTIONS

```bash
python instalocker.py config [OPTIONS]

OPTIONS:
  --show                 Display all current settings
  --set KEY=VALUE        Set one or more settings
  --reset                Reset to defaults

KEYS FOR --set:
  agent                  Target agent name
  hotkey                 Activation hotkey
  mouse_speed            Mouse movement speed
  confidence             Detection confidence
  click_offset_x         X click offset
  click_offset_y         Y click offset
  max_time               Max search time
  debug                  Debug mode on/off
```

---

## START EXAMPLES

```bash
# Pick NEON (default)
python instalocker.py start

# Pick REYNA with Alt+R hotkey
python instalocker.py start --agent REYNA --hotkey "alt+r"

# Fast mouse (0.02 speed)
python instalocker.py start --mouse-speed 0.02

# Strict detection
python instalocker.py start --confidence 0.85

# 20 second timeout
python instalocker.py start --max-time 20

# Debug output
python instalocker.py start --debug

# All together
python instalocker.py start --agent SAGE --hotkey "shift+s" --mouse-speed 0.03 --confidence 0.8 --max-time 10 --debug

# Run once now
python instalocker.py start --no-hotkey

# Simple hotkey
python instalocker.py start --hotkey "f6"
```

---

## CONFIG EXAMPLES

```bash
# Show what's configured
python instalocker.py config --show

# Change to REYNA
python instalocker.py config --set agent=REYNA

# Multiple settings at once
python instalocker.py config --set agent=SAGE hotkey="alt+s" mouse_speed=0.05

# Reset everything
python instalocker.py config --reset

# Change multiple
python instalocker.py config --set agent=NEON confidence=0.8 max_time=20 mouse_speed=0.02
```

---

## CALIBRATE EXAMPLES

```bash
# Calibrate NEON (default)
python instalocker.py calibrate

# Calibrate REYNA
python instalocker.py calibrate --agent REYNA

# Calibrate SAGE
python instalocker.py calibrate --agent SAGE
```

---

## HOTKEY OPTIONS

```bash
"f6"                    # Function keys
"f7"
"ctrl+shift+n"          # Ctrl combinations
"alt+n"                 # Alt combinations
"shift+f6"              # Shift combinations
"o"                     # Single key
"n"
```

---

## COMMON WORKFLOWS

### Workflow 1: Quick Default
```bash
python instalocker.py start
```

### Workflow 2: Setup Once, Run Many
```bash
# First time: configure your preferences
python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.03

# Then: just run with no options
python instalocker.py start
```

### Workflow 3: Different Agents
```bash
# Always pick REYNA
python instalocker.py start --agent REYNA

# Or set as default
python instalocker.py config --set agent=REYNA
```

### Workflow 4: Fast Pickup
```bash
# Ultra fast
python instalocker.py start --mouse-speed 0.01 --max-time 10
```

### Workflow 5: Test Before Match
```bash
# Test without hotkey
python instalocker.py start --no-hotkey
```

### Workflow 6: Debug Problems
```bash
# See what's happening
python instalocker.py start --debug
```

---

## MOUSE SPEED PRESETS

```bash
# Super fast (might miss)
--mouse-speed 0.01

# Fast (recommended)
--mouse-speed 0.05

# Normal
--mouse-speed 0.1

# Slow (more visible)
--mouse-speed 0.2
```

---

## CONFIDENCE PRESETS

```bash
# Very lenient (more false positives)
--confidence 0.5

# Balanced (recommended)
--confidence 0.75

# Strict (might miss)
--confidence 0.9
```

---

## BATCH FILES (Windows)

```bash
# In batch_examples/ folder:
start_neon.bat         # Pick NEON
start_reyna.bat        # Pick REYNA
start_fast.bat         # Fast mode
start_debug.bat        # Debug mode
run_once.bat           # Run once
show_config.bat        # Show settings
calibrate_neon.bat     # Create template
```

Just double-click to run!

---

## EXIT

Press `Ctrl+C` anytime to stop.

---

## TROUBLESHOOTING

| Issue | Command |
|-------|---------|
| Doesn't detect agent | `python instalocker.py start --debug` |
| Mouse too slow | `python instalocker.py start --mouse-speed 0.02` |
| False detections | `python instalocker.py start --confidence 0.85` |
| Hotkey not working | Run as Administrator |
| Wrong position | `python instalocker.py calibrate` |
| Want to customize | `python instalocker.py config --set agent=XXX` |

---

## ALL AGENTS

```
NEON, REYNA, SAGE, JETT, VIPER, KILLJOY, SOVA, PHOENIX, 
CYPHER, OMEN, RAZE, BREACH, BRIMSTONE, CHAMBER, ASTRA, 
HARBOR, GEKKO, SKYE, KAY/O, FADE
```

---

Print this for quick reference! 📋

