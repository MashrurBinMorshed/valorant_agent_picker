@echo off
REM Valorant Instalocker - Debug Mode
REM Shows detailed output for troubleshooting

cd /d "%~dp0"
python instalocker.py start --debug
pause
