@echo off
REM Valorant Instalocker - Fast Mode (NEON)
REM Ultra-fast mouse speed + short timeout

cd /d "%~dp0"
python instalocker.py start --agent NEON --mouse-speed 0.02 --max-time 10
pause
