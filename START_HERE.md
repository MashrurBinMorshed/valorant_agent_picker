# 🎮 VALORANT INSTALOCKER - CLI VERSION

> **Complete command-line control for instant agent selection**

## ⚡ START IN 2 MINUTES

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the instalocker
python instalocker.py start

# 3. During agent select, press Ctrl+Shift+N
# Done! Neon is locked in.
```

---

## 🎯 CHOOSE YOUR METHOD

### Method 1: CLI (Recommended) ✨
```bash
python instalocker.py start
```
**Best for:** Full control, scripting, automation

### Method 2: Batch File (Easiest) 🖱️
```
Open batch_examples/ → Double-click start_neon.bat
```
**Best for:** Windows users, quick access

### Method 3: Menu (Beginner-Friendly) 📋
```bash
python launcher.py
```
**Best for:** New users, choosing options

---

## 📚 DOCUMENTATION QUICK LINKS

| Want To... | See This |
|---|---|
| Get started in 5 min | [QUICKSTART.md](QUICKSTART.md) |
| See all CLI commands | [CLI_CHEATSHEET.md](CLI_CHEATSHEET.md) |
| Full CLI guide | [CLI_GUIDE.md](CLI_GUIDE.md) |
| Compare all methods | [OVERVIEW.md](OVERVIEW.md) |
| Understand all files | [FILE_INDEX.md](FILE_INDEX.md) |
| Get help | `python help.py` |

---

## 🚀 QUICK COMMANDS

```bash
# START
python instalocker.py start

# With custom agent
python instalocker.py start --agent REYNA

# With custom hotkey
python instalocker.py start --hotkey "alt+n"

# Show configuration
python instalocker.py config --show

# Change default agent
python instalocker.py config --set agent=REYNA

# Create template for better detection
python instalocker.py calibrate --agent NEON

# Run once without hotkey
python instalocker.py start --no-hotkey

# Debug mode
python instalocker.py start --debug
```

---

## 💻 WINDOWS BATCH FILES

Go to `batch_examples/` and double-click:
- `start_neon.bat` - Start with Neon
- `start_reyna.bat` - Start with Reyna
- `start_fast.bat` - Ultra-fast mode
- `start_debug.bat` - Troubleshooting
- `run_once.bat` - Run once now
- `calibrate_neon.bat` - Create template
- `show_config.bat` - View settings

---

## ⚙️ CONFIGURATION

### Show Current Config
```bash
python instalocker.py config --show
```

### Set Values
```bash
python instalocker.py config --set agent=REYNA
python instalocker.py config --set hotkey="alt+r"
python instalocker.py config --set mouse_speed=0.05
```

### Reset to Defaults
```bash
python instalocker.py config --reset
```

---

## 🎮 USAGE

1. **Run the instalocker** - See commands above
2. **Start Valorant** - Queue for a match
3. **Reach agent select** - Wait for your turn
4. **Press hotkey** - Default: `Ctrl+Shift+N`
5. **Enjoy your pick!** - Agent is locked in

---

## 🔧 SETUP GUIDE

### First Time? Run This:
```bash
python setup.py
```
This will guide you through:
- Checking dependencies
- Configuring your settings
- Testing your hotkey
- Quick start info

---

## 🎯 COMMON USE CASES

### Use Case 1: Pick Neon (Default)
```bash
python instalocker.py start
```

### Use Case 2: Pick Different Agent
```bash
python instalocker.py start --agent REYNA
```

### Use Case 3: Save Your Preferences
```bash
python instalocker.py config --set agent=REYNA hotkey="alt+r"
python instalocker.py start  # Uses saved config
```

### Use Case 4: Fast Mode
```bash
python instalocker.py start --mouse-speed 0.02
```

### Use Case 5: Test Without Hotkey
```bash
python instalocker.py start --no-hotkey
```

### Use Case 6: Troubleshoot
```bash
python instalocker.py start --debug
```

---

## 🎨 CUSTOMIZATION

### Available Agents (Pick Any)
```
NEON, REYNA, SAGE, JETT, VIPER, KILLJOY, SOVA, PHOENIX,
CYPHER, OMEN, RAZE, BREACH, BRIMSTONE, CHAMBER, ASTRA,
HARBOR, GEKKO, SKYE, KAY/O, FADE
```

### Hotkey Examples
```bash
--hotkey "ctrl+shift+n"    # Default
--hotkey "alt+n"           # Alt + N
--hotkey "f6"              # Function key
--hotkey "o"               # Single key
```

### Mouse Speed Options
```bash
--mouse-speed 0.01         # Super fast
--mouse-speed 0.05         # Fast (default)
--mouse-speed 0.1          # Normal
--mouse-speed 0.2          # Slow
```

---

## 📋 COMPLETE CLI REFERENCE

Full command syntax:
```bash
python instalocker.py COMMAND [OPTIONS]

COMMANDS:
  start      Start the instalocker
  config     Manage configuration
  calibrate  Create agent template

OPTIONS (for 'start'):
  --agent AGENT           Agent to pick
  --hotkey HOTKEY        Activation hotkey
  --mouse-speed SPEED    Mouse speed (0.01-0.2)
  --confidence CONF      Detection confidence
  --max-time TIME        Search timeout (seconds)
  --debug                Show debug output
  --no-hotkey            Run once immediately

OPTIONS (for 'config'):
  --show                 Display settings
  --set KEY=VALUE        Change settings
  --reset                Reset to defaults

OPTIONS (for 'calibrate'):
  --agent AGENT          Agent to calibrate
```

See [CLI_GUIDE.md](CLI_GUIDE.md) for complete reference.

---

## 🔍 DETECTION METHODS

The instalocker tries these in order:
1. **OCR** - Reads agent name text (most reliable)
2. **Template** - Matches saved agent image
3. **Color** - Detects agent card colors (fallback)

Improve detection:
```bash
# Create template for better accuracy
python instalocker.py calibrate --agent NEON
```

---

## 📁 FILE STRUCTURE

```
instalocker_valorant/
├── instalocker.py          ← Main CLI
├── setup.py                ← First time setup
├── help.py                 ← Help
├── requirements.txt        ← Dependencies
├── CLI_GUIDE.md            ← Full CLI docs
├── CLI_CHEATSHEET.md       ← Quick ref
├── QUICKSTART.md           ← 5-min guide
├── OVERVIEW.md             ← All methods
├── FILE_INDEX.md           ← File guide
└── batch_examples/         ← Windows scripts
```

More detailed breakdown in [FILE_INDEX.md](FILE_INDEX.md).

---

## 🚨 REQUIREMENTS

- **OS:** Windows 7+
- **Python:** 3.8+
- **Admin:** Run as Administrator (for hotkey)
- **Screen:** 1600x900+ (recommended)
- **Packages:** See requirements.txt

Install packages:
```bash
pip install -r requirements.txt
```

---

## ⚠️ SAFETY & ETHICS

**WARNING:** This tool automates game input. Be aware:
- May violate Valorant's Terms of Service
- Account could be suspended or banned
- Use only in practice or casual matches
- Valorant has anti-cheat detection
- Use at your own risk

**Recommended:**
- Test in Practice Tool first
- Use only for casual/unrated matches
- Don't use in ranked
- Read Valorant's ToS

---

## 🆘 TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Hotkey not working | Run as Administrator |
| Agent not detected | Run `python instalocker.py calibrate --agent NEON` |
| Wrong mouse position | Use `--debug` and check output |
| Too slow/fast | Adjust `--mouse-speed` |
| False detections | Increase `--confidence` |

See [README.md](README.md) for more troubleshooting.

---

## 📞 HELP & SUPPORT

```bash
# Show full help
python help.py

# View configuration
python instalocker.py config --show

# Debug output
python instalocker.py start --debug

# First time setup
python setup.py
```

---

## 📖 NEXT STEPS

1. **Install:** `pip install -r requirements.txt`
2. **Learn:** Read [QUICKSTART.md](QUICKSTART.md) (5 min)
3. **Setup:** `python setup.py` (3 min)
4. **Test:** `python instalocker.py start --no-hotkey`
5. **Use:** During agent select, press your hotkey!

---

## 🎯 QUICK START EXAMPLES

### Example 1: Right Now
```bash
python instalocker.py start
```

### Example 2: With Options
```bash
python instalocker.py start --agent REYNA --hotkey "alt+r"
```

### Example 3: Save & Run
```bash
python instalocker.py config --set agent=REYNA
python instalocker.py start
```

### Example 4: Windows Only
```
batch_examples/start_neon.bat (double-click)
```

---

## 💡 PRO TIPS

1. **Save time:** Configure once, run many times
   ```bash
   python instalocker.py config --set agent=REYNA
   ```

2. **Use batch files:** Save shortcut to taskbar

3. **Create templates:** Better detection
   ```bash
   python instalocker.py calibrate --agent NEON
   ```

4. **Debug mode:** See what's happening
   ```bash
   python instalocker.py start --debug
   ```

5. **Run multiple:** Different terminals, different hotkeys

---

## 📚 DOCUMENTATION

| File | Purpose |
|------|---------|
| [QUICKSTART.md](QUICKSTART.md) | 5-minute setup |
| [CLI_GUIDE.md](CLI_GUIDE.md) | Complete CLI guide |
| [CLI_CHEATSHEET.md](CLI_CHEATSHEET.md) | Command reference |
| [OVERVIEW.md](OVERVIEW.md) | All methods |
| [FILE_INDEX.md](FILE_INDEX.md) | File guide |
| [README.md](README.md) | Setup guide |

---

## ✨ YOU'RE READY!

```
1. pip install -r requirements.txt
2. python instalocker.py start
3. Go to agent select
4. Press Ctrl+Shift+N
5. Enjoy your instant pick!
```

---

## 🎮 GOOD LUCK, AGENT!

> **Questions?** Check the docs or run `python help.py`

> **Problems?** See troubleshooting section above

> **Want full CLI ref?** Read [CLI_GUIDE.md](CLI_GUIDE.md)

---

**Happy picking!** 🎮✨

