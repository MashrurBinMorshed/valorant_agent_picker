# ✅ SETUP COMPLETE - What You Have

Your Valorant Instalocker is now fully set up with **complete CLI support**!

## 📦 What You Got

### ✨ NEW CLI Interface (Main Feature)
- **`instalocker.py`** - Full command-line control
  - Configure everything from terminal
  - No GUI needed
  - Save configurations
  - Perfect for scripting

### 🖥️ 7 Ways to Use It
1. **CLI** - `python instalocker.py start`
2. **Batch Files** - Double-click in `batch_examples/`
3. **Menu** - `python launcher.py`
4. **Setup Guide** - `python setup.py`
5. **Help** - `python help.py`
6. **Advanced** - `python advanced_instalocker.py`
7. **Basic** - `python main.py`

---

## 🚀 QUICKEST START (2 minutes)

### Option A: Windows Users (Easiest)
```
1. Open: batch_examples/
2. Double-click: start_neon.bat
3. Go to Valorant agent select
4. Press: Ctrl+Shift+N
5. Done!
```

### Option B: CLI Users (Recommended)
```bash
python instalocker.py start
# Press Ctrl+Shift+N in agent select
```

### Option C: First Time Setup
```bash
python setup.py
# Follow prompts
# Then use instalocker
```

---

## 📚 Documentation Files

| File | Read This If |
|------|---|
| **START_HERE.md** | You just got this |
| **QUICKSTART.md** | You want 5-minute setup |
| **CLI_GUIDE.md** | You want full CLI reference |
| **CLI_CHEATSHEET.md** | You want quick command lookup |
| **OVERVIEW.md** | You want to compare all methods |
| **FILE_INDEX.md** | You want to understand all files |
| **README.md** | You want detailed setup |

---

## 💻 Common Commands

```bash
# START WITH DEFAULTS
python instalocker.py start

# WITH CUSTOM AGENT
python instalocker.py start --agent REYNA

# WITH CUSTOM HOTKEY
python instalocker.py start --hotkey "alt+r"

# SHOW YOUR CONFIG
python instalocker.py config --show

# SAVE DEFAULT AGENT
python instalocker.py config --set agent=REYNA

# CREATE BETTER TEMPLATE
python instalocker.py calibrate --agent NEON

# RUN ONCE NOW
python instalocker.py start --no-hotkey
```

---

## 🎯 Next Steps

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Test It (1 min)
```bash
python instalocker.py start --no-hotkey
```

### Step 3: Use It (Now!)
- Go to Valorant agent select
- Run: `python instalocker.py start`
- Press: Your hotkey (default: Ctrl+Shift+N)
- Enjoy!

---

## 🎮 During a Match

1. **Queue** for a match
2. **Get to agent select**
3. **Run:** `python instalocker.py start`
4. **Wait for your turn**
5. **Press hotkey** (Ctrl+Shift+N)
6. **Agent locked!**

---

## ⚡ Popular Hotkey Examples

```bash
# Super simple
python instalocker.py start --hotkey "f6"

# Alt combinations
python instalocker.py start --hotkey "alt+n"

# Ctrl+Shift (default)
python instalocker.py start --hotkey "ctrl+shift+n"

# Set as default
python instalocker.py config --set hotkey="alt+n"
```

---

## 🎨 Pick Any Agent

```bash
python instalocker.py start --agent NEON
python instalocker.py start --agent REYNA
python instalocker.py start --agent SAGE
python instalocker.py start --agent JETT
# ... any Valorant agent
```

---

## 🕹️ Windows Batch Files

For super easy access, use batch files in `batch_examples/`:

**Just double-click:**
- `start_neon.bat` - Pick Neon
- `start_reyna.bat` - Pick Reyna  
- `start_fast.bat` - Fast mode
- `run_once.bat` - Run once
- `calibrate_neon.bat` - Create template
- `show_config.bat` - View settings
- `start_debug.bat` - Debug

---

## 📋 CLI Syntax

Full command format:
```
python instalocker.py COMMAND [OPTIONS]

COMMANDS:
  start      Run the instalocker
  config     Manage settings
  calibrate  Create templates

START OPTIONS:
  --agent NAME          Agent to pick
  --hotkey COMBO        Activation hotkey
  --mouse-speed VALUE   Speed (0.01-0.2)
  --confidence VALUE    Strictness (0.0-1.0)
  --max-time VALUE      Timeout in seconds
  --debug               Show details
  --no-hotkey           Run once now
```

Full reference: [CLI_GUIDE.md](CLI_GUIDE.md)

---

## 💾 Saving Your Config

```bash
# Set your preferences ONCE
python instalocker.py config --set agent=REYNA
python instalocker.py config --set hotkey="alt+r"
python instalocker.py config --set mouse_speed=0.05

# VIEW your config
python instalocker.py config --show

# Now just run with no options
python instalocker.py start
# Uses all your saved preferences!
```

---

## 🔧 Improving Detection

If the instalocker isn't detecting your agent:

```bash
# Create a template for better accuracy
python instalocker.py calibrate --agent NEON

# Then run normally
python instalocker.py start
```

---

## 🆘 If Something Goes Wrong

```bash
# See what's happening
python instalocker.py start --debug

# Check your settings
python instalocker.py config --show

# Reset to defaults
python instalocker.py config --reset

# Get help
python help.py
```

---

## 📖 Documentation Map

```
START_HERE.md (you are here)
    ↓
Read → QUICKSTART.md (5 min overview)
    ↓
Need CLI help? → CLI_CHEATSHEET.md (quick ref)
Need everything? → CLI_GUIDE.md (full docs)
Need all methods? → OVERVIEW.md (compare)
Need file details? → FILE_INDEX.md
```

---

## ✅ VERIFICATION CHECKLIST

Have you:
- [ ] Installed Python 3.8+
- [ ] Run `pip install -r requirements.txt`
- [ ] Run `python instalocker.py start` 
- [ ] Created batch shortcuts (optional)
- [ ] Tested with `--no-hotkey` flag
- [ ] Configured your agent (if not Neon)

---

## 🎯 YOUR FIRST RUN

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test it works
python instalocker.py start --no-hotkey

# 3. Normal use
python instalocker.py start

# Then in Valorant:
# - Press Ctrl+Shift+N during agent select
# - Watch it work!
```

---

## 🚀 READY TO BEGIN?

### Quick Start (Pick One)

**Option 1: Windows Batch (Easiest)**
```
→ Go to batch_examples/ folder
→ Double-click start_neon.bat
done!
```

**Option 2: CLI (Recommended)**
```bash
python instalocker.py start
```

**Option 3: First Time Setup**
```bash
python setup.py
```

---

## 📞 GETTING HELP

| Need | Do This |
|------|---------|
| Quick commands | See CLI_CHEATSHEET.md |
| Full CLI guide | Read CLI_GUIDE.md |
| All features | Check OVERVIEW.md |
| File purposes | Look at FILE_INDEX.md |
| General help | Run `python help.py` |

---

## ⚠️ FINAL REMINDERS

✅ **Run as Administrator** (for hotkey support)
✅ **Test in Practice Tool** before ranked
✅ **Keep Valorant window visible** (for detection)
✅ **Check your settings** with `config --show`
✅ **Use responsibly** (Valorant may detect automation)

---

## 🎮 YOU'RE ALL SET!

Everything is installed and ready to go.

**Next action:** Pick your favorite method above and start using it!

---

## 📞 I'M CONFUSED - WHERE DO I START?

**Answer:** Read [START_HERE.md](START_HERE.md) (you are here!)

**Then:** Pick one option from "QUICKEST START" above and do it.

**That's it!** You're ready to go.

---

## 💡 PRO TIP

Save your favorite settings:
```bash
python instalocker.py config --set agent=REYNA hotkey="alt+r"
```

Then next time just run:
```bash
python instalocker.py start
```

All your preferences are saved!

---

## 🎉 ENJOY!

You now have a **full-featured Valorant Instalocker with complete CLI support**!

Pick your method and start using it. Good luck, Agent! 🎮✨

---

**Questions?** Read any of the documentation files.

**Problems?** Run `python help.py` or `python instalocker.py start --debug`

**Ready?** Go to Valorant and start instant-locking!

