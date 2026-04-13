@echo off
REM Valorant Instalocker - Run Once (No Hotkey)
REM Immediately picks Neon without waiting

cd /d "%~dp0"
python instalocker.py start --no-hotkey
pause
