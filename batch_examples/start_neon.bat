@echo off
REM Valorant Instalocker - Pick NEON (Default)
REM Hotkey: Ctrl+Shift+N

cd /d "%~dp0"
python instalocker.py start --agent NEON --hotkey "ctrl+shift+n"
pause
