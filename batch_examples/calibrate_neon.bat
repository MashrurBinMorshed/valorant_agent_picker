@echo off
REM Valorant Instalocker - Calibrate Template
REM Creates a template for better NEON detection

cd /d "%~dp0"
python instalocker.py calibrate --agent NEON
pause
