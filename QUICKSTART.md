# VALORANT INSTALOCKER - QUICK START GUIDE

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install Tesseract OCR (Optional, Recommended)
- Download: https://github.com/UB-Mannheim/tesseract/wiki
- Download the latest TSR (tesseract-ocr-w64) installer
- Install to default location (it will find it automatically)

### Step 3: Run the Instalocker
```bash
python launcher.py
```

Choose **Option 1: Advanced Instalocker** (recommended)

---

## 🎮 How to Use

### Before Your Match
1. **Run the program**: `python launcher.py`
2. **Start Valorant** and queue for a match
3. **Get into agent select** screen

### During Agent Select
- **Press `Ctrl+Shift+N`** (default hotkey)
- The instalocker will **instantly find and click Neon**
- You'll see a confirmation message

### That's It!
Neon will be locked in!

---

## ⚙️ Customization

### Change Hotkey
Edit `advanced_instalocker.py` line ~20:
```python
HOTKEY = "ctrl+shift+n"  # Change to any combo like "alt+n", "f6", etc.
```

### Faster/Slower Mouse
Edit `advanced_instalocker.py` line ~21:
```python
MOUSE_SPEED = 0.05  # Lower = faster (0.01), Higher = slower (0.1)
```

### Different Agent
1. Edit `advanced_instalocker.py` line ~19
2. Change: `NEON_NAME = "NEON"` → `NEON_NAME = "REYNA"`
3. Run calibration to create template for new agent

---

## 📊 Detection Methods

The instalocker tries these in order:
1. **OCR** (Best) - Reads "NEON" text directly
2. **Template** - Matches saved Neon image
3. **Color** (Fallback) - Finds purple/cyan card

If OCR isn't working:
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki

If template matching isn't working:
- Run: `python calibrate.py` to create a new template

---

## 🔧 Troubleshooting

### "Instalocker doesn't detect Neon"
- ✓ Make sure Valorant window is visible
- ✓ Make sure you're on agent select screen
- ✓ Try running `calibrate.py` to create template
- ✓ Try increasing `CONFIDENCE_THRESHOLD` to 0.8

### "Nothing happens when I press hotkey"
- ✓ Run as Administrator
- ✓ Try different hotkey like `"alt+n"` or `"f6"`
- ✓ Make sure Valorant window is active

### "Mouse moves but doesn't click on Neon"
- ✓ Adjust `CLICK_OFFSET_Y` in the script (try 30-70)
- ✓ Run `calibrate.py` for better accuracy

### "Tesseract not found"
- ✓ Install from: https://github.com/UB-Mannheim/tesseract/wiki
- ✓ Or edit path in script: `pytesseract.pytesseract_cmd = r'C:\path\to\tesseract.exe'`

---

## 🎯 Version Comparison

### Advanced Instalocker (Recommended)
- ✓ Multiple detection methods
- ✓ More accurate (99%+)
- ✓ More features
- ✗ Slightly more CPU usage

### Basic Instalocker
- ✓ Simpler code
- ✓ Lightweight
- ✓ Good starter version
- ✗ Less accurate

---

## 📝 Important Notes

1. **Run as Administrator** - Needed for global hotkey
2. **Keep Valorant window visible** - Script needs to see the screen
3. **Test in Practice Tool** first - To verify it works before ranked
4. **Use responsibly** - Valorant's anti-cheat may flag automation tools

---

## 🚀 Advanced Tips

### Create Better Template
```bash
python calibrate.py
```
This will capture and save a Neon card template for better detection

### Different Mouse Speed
```python
MOUSE_SPEED = 0.01   # Super fast
MOUSE_SPEED = 0.05   # Fast (default)
MOUSE_SPEED = 0.1    # Normal
MOUSE_SPEED = 0.2    # Slow
```

### Debug Mode
In `advanced_instalocker.py` set:
```python
DEBUG_MODE = True
```
This shows detailed detection info

---

## 📚 Dependencies

What gets installed:
- **pyautogui** - Mouse/keyboard control
- **keyboard** - Global hotkey support
- **opencv-python** - Image processing
- **Pillow** - Screenshot capture
- **pytesseract** - OCR (requires Tesseract)
- **numpy** - Array operations

---

## ✅ Testing Checklist

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Running as Administrator
- [ ] Valorant can see Neon agent card
- [ ] Hotkey works in launcher
- [ ] Mouse moves toward Neon when activated
- [ ] Click registers on Neon

---

## 💡 Quick Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run launcher (menu)
python launcher.py

# Run advanced version directly
python advanced_instalocker.py

# Run basic version directly
python main.py

# Create/update template
python calibrate.py
```

---

## 🆘 More Help

1. Check console output for error messages
2. Make sure Valorant window is active
3. Verify agent select screen is visible
4. Try running `calibrate.py` to create template
5. Check GitHub issues or docs

---

Enjoy instant Neon picks! 🎮✨

Good luck, Agent!
