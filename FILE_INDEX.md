# FILE INDEX - Valorant Instalocker

Complete guide to all files and their purposes.

## 🚀 MAIN PROGRAMS

| File | Purpose | Usage |
|------|---------|-------|
| `instalocker.py` | **CLI Interface (RECOMMENDED)** | `python instalocker.py start` |
| `launcher.py` | Menu-based interface | `python launcher.py` |
| `advanced_instalocker.py` | Feature-rich version | `python advanced_instalocker.py` |
| `main.py` | Basic lightweight version | `python main.py` |
| `calibrate.py` | Template calibration tool | `python calibrate.py` |

## 🛠️ SETUP & CONFIGURATION

| File | Purpose |
|------|---------|
| `setup.py` | **First-time setup guide** - Run this first! |
| `help.py` | Comprehensive help documentation |
| `requirements.txt` | Python package dependencies |
| `config.ini` | Configuration file template |
| `instalocker_config.json` | *Auto-created* - Saved configuration |

## 📚 DOCUMENTATION

| File | Purpose | Best For |
|------|---------|----------|
| `README.md` | Setup guide and overview | Getting started |
| `QUICKSTART.md` | 5-minute quick start | Impatient users |
| `CLI_GUIDE.md` | **Complete CLI reference** | Command-line users |
| `CLI_CHEATSHEET.md` | **Quick command reference** | Quick lookup |
| `OVERVIEW.md` | All methods comparison | Choosing approach |
| `FILE_INDEX.md` | This file | Understanding files |

## 🪟 WINDOWS BATCH FILES

Location: `batch_examples/`

| File | Purpose | Double-Click To |
|------|---------|-----------------|
| `start_neon.bat` | Pick NEON (default) | Start with Neon |
| `start_reyna.bat` | Pick REYNA | Start with Reyna |
| `start_fast.bat` | Ultra-fast mode | Run fast |
| `start_debug.bat` | Debug output | Troubleshoot |
| `run_once.bat` | Run once immediately | One-time pickup |
| `show_config.bat` | Display configuration | View settings |
| `calibrate_neon.bat` | Create template | Improve accuracy |

## 📂 DIRECTORY STRUCTURE

```
instalocker_valorant/
│
├── 🚀 MAIN PROGRAMS
├── instalocker.py              ← CLI Interface (START HERE)
├── launcher.py                 ← Menu interface
├── advanced_instalocker.py     ← Feature-rich
├── main.py                     ← Basic version
├── calibrate.py                ← Setup tool
│
├── 🛠️ SETUP
├── setup.py                    ← First-time setup
├── help.py                     ← Help documentation
├── requirements.txt            ← Dependencies
├── config.ini                  ← Config template
├── instalocker_config.json     ← Auto-created config
│
├── 📚 DOCUMENTATION
├── README.md                   ← Setup guide
├── QUICKSTART.md               ← Quick 5-min start
├── CLI_GUIDE.md                ← Full CLI guide
├── CLI_CHEATSHEET.md           ← Command reference
├── OVERVIEW.md                 ← Methods comparison
├── FILE_INDEX.md               ← This file
│
├── 🪟 BATCH FILES
└── batch_examples/
    ├── start_neon.bat
    ├── start_reyna.bat
    ├── start_fast.bat
    ├── start_debug.bat
    ├── run_once.bat
    ├── show_config.bat
    └── calibrate_neon.bat
```

## 🎯 GETTING STARTED PATHS

### Path 1: FASTEST (Just Click)
```
1. Open: batch_examples/
2. Double-click: start_neon.bat
3. Go to Valorant agent select
4. Press Ctrl+Shift+N
5. Done!
```

### Path 2: CLI (Recommended)
```
1. Run: python instalocker.py start
2. Go to Valorant agent select
3. Press Ctrl+Shift+N
4. Done!
```

### Path 3: Guided Setup
```
1. Run: python setup.py
2. Follow prompts
3. Run instalocker.py or batch file
4. Done!
```

### Path 4: Menu (Interactive)
```
1. Run: python launcher.py
2. Choose option 1-3
3. Follow prompts
4. Done!
```

## 📖 DOCUMENTATION MAP

| Need Help With | See File |
|---|---|
| Getting started | QUICKSTART.md |
| CLI commands | CLI_GUIDE.md or CLI_CHEATSHEET.md |
| All methods | OVERVIEW.md |
| Setup & install | README.md |
| File purposes | FILE_INDEX.md (this file) |
| All help | help.py or help.md (soon) |

## 🔧 COMMON TASKS

### Task: Install Dependencies
```bash
pip install -r requirements.txt
```

### Task: First-Time Setup
```bash
python setup.py
```

### Task: View Help
```bash
python help.py
```

### Task: Start Instalocker (CLI)
```bash
python instalocker.py start
```

### Task: Show Configuration
```bash
python instalocker.py config --show
```

### Task: Change Agent
```bash
python instalocker.py start --agent REYNA
```

### Task: Run Batch File (Windows)
```
Go to batch_examples/ and double-click
```

### Task: Create Template (Better Detection)
```bash
python instalocker.py calibrate --agent NEON
```

## 💡 WHICH FILE SHOULD I USE?

| Your Situation | Use This |
|---|---|
| First time? | `setup.py` |
| Want menu? | `launcher.py` |
| Want CLI? | `instalocker.py` |
| Windows user? | `batch_examples/*.bat` |
| Need help? | `help.py` |
| Need quick ref? | `CLI_CHEATSHEET.md` |
| Want full docs? | `CLI_GUIDE.md` |
| All methods? | `OVERVIEW.md` |

## 📋 FEATURE MATRIX

| Feature | Batch | CLI | Launcher | Advanced | Basic |
|---------|-------|-----|----------|----------|-------|
| Easy to use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Customizable | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Configuration | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| Speed | Fast | Very Fast | Fast | Fast | Very Fast |

## 🎮 QUICK REFERENCE

```bash
# SETUP (Do this once)
pip install -r requirements.txt
python setup.py

# START (Do this every time)
python instalocker.py start

# ALTERNATIVES
batch_examples/start_neon.bat      # Windows - just double-click
python launcher.py                 # Menu interface
python help.py                     # Show help
```

## ✅ FILE CHECKLIST

When you open the folder, you should have:

### Main Programs
- [ ] instalocker.py
- [ ] launcher.py
- [ ] advanced_instalocker.py
- [ ] main.py
- [ ] calibrate.py

### Setup & Config
- [ ] setup.py
- [ ] help.py
- [ ] requirements.txt
- [ ] config.ini

### Documentation
- [ ] README.md
- [ ] QUICKSTART.md
- [ ] CLI_GUIDE.md
- [ ] CLI_CHEATSHEET.md
- [ ] OVERVIEW.md
- [ ] FILE_INDEX.md

### Batch Examples
- [ ] batch_examples/start_neon.bat
- [ ] batch_examples/start_reyna.bat
- [ ] batch_examples/start_fast.bat
- [ ] batch_examples/start_debug.bat
- [ ] batch_examples/run_once.bat
- [ ] batch_examples/show_config.bat
- [ ] batch_examples/calibrate_neon.bat

## 🚀 RECOMMENDED FIRST STEPS

1. **Read**: QUICKSTART.md (5 min)
2. **Install**: `pip install -r requirements.txt` (2 min)
3. **Setup**: `python setup.py` (3 min)
4. **Test**: `python instalocker.py start --no-hotkey` (1 min)
5. **Use**: Press hotkey during agent select!

## 📞 NEED HELP?

| Question | Answer |
|----------|--------|
| How do I start? | Read QUICKSTART.md |
| How do CLI? | Read CLI_GUIDE.md |
| Where's quick ref? | See CLI_CHEATSHEET.md |
| How to choose? | See OVERVIEW.md |
| What file does what? | You're reading it! |
| General help? | Run `python help.py` |

---

**That's it!** You now understand what every file does.

Pick your starting point and get going! 🎮✨

