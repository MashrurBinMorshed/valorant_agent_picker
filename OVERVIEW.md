# Valorant Instalocker - Complete Overview

All the different ways to use the instalocker.

## 📋 Versions & Modes

### 1. CLI Version (Recommended) ⭐
**File:** `instalocker.py`
**Best for:** Power users, scripting, full control

```bash
python instalocker.py start
python instalocker.py config --show
python instalocker.py calibrate --agent NEON
```

**Pros:**
- ✓ Full control via command line
- ✓ Easy to script and automate
- ✓ Configuration file support
- ✓ No GUI overhead
- ✓ Perfect for batch files

**See:** [CLI_GUIDE.md](CLI_GUIDE.md) or [CLI_CHEATSHEET.md](CLI_CHEATSHEET.md)

---

### 2. Windows Batch Files (Easiest) 🎯
**Location:** `batch_examples/` folder
**Best for:** Quick clicking, no typing

**Files:**
- `start_neon.bat` - Pick Neon
- `start_reyna.bat` - Pick Reyna
- `start_fast.bat` - Fast mode
- `start_debug.bat` - Debug/troubleshooting
- `run_once.bat` - Run once immediately
- `calibrate_neon.bat` - Create template
- `show_config.bat` - Show settings

**How to use:** Just double-click!

```
double-click → Pick agent → Profit!
```

---

### 3. Launcher Menu (Interactive)
**File:** `launcher.py`
**Best for:** Beginners, menu selection

```bash
python launcher.py
```

Menu options:
1. Advanced Instalocker
2. Basic Instalocker
3. Calibration Tool
4. Exit

---

### 4. Advanced Version (Feature-Rich)
**File:** `advanced_instalocker.py`
**Best for:** Maximum features, debugging

```bash
python advanced_instalocker.py
```

Features:
- Multi-method detection (OCR, Template, Color)
- Better accuracy
- Detailed configuration options

---

### 5. Basic Version (Lightweight)
**File:** `main.py`
**Best for:** Simple setup, minimal overhead

```bash
python main.py
```

---

## 🚀 Getting Started (Choose Your Path)

### Path 1: I Just Want to Click and Go
```
1. Go to batch_examples/
2. Double-click start_neon.bat
3. Go back to Valorant
4. Press Ctrl+Shift+N during agent select
5. Done!
```

### Path 2: I Want Full Control
```
1. Open terminal/PowerShell
2. python instalocker.py start --agent NEON
3. Press Ctrl+Shift+N during agent select
```

### Path 3: I Want to Customize Everything
```
1. Open terminal/PowerShell
2. python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.02
3. python instalocker.py start
4. Press Alt+R during agent select
```

### Path 4: I'm New and Want Guidance
```
1. python launcher.py
2. Choose option 1
3. Follow prompts
```

---

## 📁 File Structure

```
instalocker_valorant/
├── instalocker.py              ← CLI version (RECOMMENDED)
├── launcher.py                 ← Menu interface
├── advanced_instalocker.py     ← Feature-rich version
├── main.py                     ← Basic version
├── calibrate.py                ← Calibration tool
│
├── CLI_GUIDE.md                ← Full CLI documentation
├── CLI_CHEATSHEET.md           ← Quick reference
├── QUICKSTART.md               ← Quick start guide
├── README.md                   ← Setup guide
│
├── batch_examples/             ← Windows batch files
│   ├── start_neon.bat
│   ├── start_reyna.bat
│   ├── start_fast.bat
│   ├── run_once.bat
│   ├── calibrate_neon.bat
│   └── ...
│
├── requirements.txt            ← Python dependencies
├── config.ini                  ← Configuration
└── instalocker_config.json     ← CLI config (auto-created)
```

---

## 🎮 Usage Comparison

| Method | Ease | Control | Speed |
|--------|------|---------|-------|
| Batch Files | ⭐⭐⭐⭐⭐ | ⭐ | Fast |
| CLI | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Very Fast |
| Launcher | ⭐⭐⭐⭐ | ⭐⭐ | Fast |
| Advanced | ⭐⭐ | ⭐⭐⭐⭐ | Fast |
| Basic | ⭐⭐ | ⭐⭐ | Very Fast |

---

## 📚 Documentation Map

Need help? Here's where to look:

| Question | See |
|----------|-----|
| How do I get started? | [QUICKSTART.md](QUICKSTART.md) |
| How do I use the CLI? | [CLI_GUIDE.md](CLI_GUIDE.md) |
| Quick command reference? | [CLI_CHEATSHEET.md](CLI_CHEATSHEET.md) |
| Setup & installation? | [README.md](README.md) |
| How to create templates? | Advanced setup in CLI_GUIDE.md |
| Troubleshooting? | README.md Troubleshooting section |

---

## ⚡ Quick Reference

### CLI Quick Start
```bash
# Install
pip install -r requirements.txt

# Run with defaults
python instalocker.py start

# Run with custom agent
python instalocker.py start --agent REYNA --hotkey "alt+r"

# Show config
python instalocker.py config --show

# Change defaults
python instalocker.py config --set agent=REYNA mouse_speed=0.05

# Create template for better detection
python instalocker.py calibrate --agent NEON
```

### Batch Files
```
Open batch_examples/ → Double-click any .bat file
```

### Menu
```bash
python launcher.py
```

---

## 🔧 Configuration

### Via CLI
```bash
python instalocker.py config --set agent=REYNA
python instalocker.py config --set hotkey="alt+r"
python instalocker.py config --set mouse_speed=0.05
python instalocker.py config --show
```

### Via Config File
Edit `instalocker_config.json`:
```json
{
  "agent": "NEON",
  "hotkey": "ctrl+shift+n",
  "mouse_speed": 0.05,
  "confidence": 0.75
}
```

---

## 🎯 Common Scenarios

### Scenario 1: Just Want Neon
**Solution:** Use batch file or:
```bash
python instalocker.py start
```

### Scenario 2: Pick Different Agent
**Solution:**
```bash
python instalocker.py start --agent REYNA
```

Or:
```bash
python instalocker.py config --set agent=REYNA
python instalocker.py start
```

### Scenario 3: Fast Pickup
**Solution:**
```bash
python instalocker.py start --mouse-speed 0.02
```

### Scenario 4: Custom Hotkey
**Solution:**
```bash
python instalocker.py start --hotkey "alt+n"
```

### Scenario 5: Save Configuration
**Solution:**
```bash
python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.03
python instalocker.py start  # Uses saved config
```

### Scenario 6: Test Before Match
**Solution:**
```bash
python instalocker.py start --no-hotkey
```

### Scenario 7: Troubleshoot
**Solution:**
```bash
python instalocker.py start --debug
```

---

## 💡 Pro Tips

1. **Save your config once:**
   ```bash
   python instalocker.py config --set agent=REYNA hotkey="alt+r" mouse_speed=0.03
   ```
   Then just: `python instalocker.py start`

2. **Use batch files for quick access:**
   - Create shortcut to `batch_examples/start_neon.bat`
   - Pin to taskbar
   - Double-click anytime

3. **Create templates for better detection:**
   ```bash
   python instalocker.py calibrate --agent NEON
   ```

4. **Test without hotkey:**
   ```bash
   python instalocker.py start --no-hotkey
   ```

5. **Run multiple instances with different agents:**
   - Terminal 1: `python instalocker.py config --set agent=NEON`
   - Terminal 2: `python instalocker.py config --set agent=REYNA`
   - Run both and use different hotkeys

---

## 🆘 Troubleshooting Map

| Problem | Try This |
|---------|----------|
| Hotkey not working | Run as Administrator |
| Agent not detected | `python instalocker.py calibrate --agent NEON` |
| Mouse wrong position | `python instalocker.py start --debug` |
| Too slow | `python instalocker.py start --mouse-speed 0.02` |
| False detections | `python instalocker.py start --confidence 0.85` |
| Tesseract not found | Install from https://github.com/UB-Mannheim/tesseract/wiki |

---

## 📝 Summary

| Use Case | Recommended Method |
|----------|-------------------|
| "Just make it work" | Batch file (double-click) |
| "I want control" | CLI (`instalocker.py start`)|
| "I'm learning" | Launcher (`launcher.py`) |
| "I need support" | Advanced (`advanced_instalocker.py`) |
| "Keep it simple" | Basic (`main.py`) |

---

## 🚀 Next Steps

1. **Choose your path** above
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Pick your method:**
   - Batch file? Go to `batch_examples/` and double-click
   - CLI? Run `python instalocker.py start`
   - Menu? Run `python launcher.py`
4. **Configure to your needs**
5. **Test it out**
6. **Enjoy instant picks!**

---

Good luck, Agent! 🎮✨

