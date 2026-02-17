@echo off
cls
echo ============================================================
echo WhatsApp Watcher - FINAL START
echo ============================================================
echo.
echo BEFORE YOU START - CHECK THESE:
echo.
echo 1. Did you add ANTHROPIC_API_KEY to .env file?
echo    File location: D:\LEEZA\HACKATHON 0\silver\.env
echo    Line 35: ANTHROPIC_API_KEY=sk-ant-xxxxx
echo.
echo 2. Are you ready to scan QR code?
echo    You have 20 MINUTES after QR appears
echo    Keep your phone ready!
echo.
echo ============================================================
echo.
echo If both are ready, press any key to start...
pause >nul
echo.
echo Starting watcher...
echo.
echo REMEMBER:
echo   - QR code will appear in Chrome
echo   - Pick up phone immediately
echo   - Open WhatsApp on phone
echo   - Tap 3 dots (top right) -^> Linked Devices -^> Link a Device
echo   - Scan QR code on computer screen
echo   - Wait for "LOGIN SUCCESSFUL!" message
echo.
echo ============================================================
echo.

cd /d "%~dp0"
python "AI_Employee_Vault\whatsapp_watcher.py"

echo.
echo ============================================================
echo Watcher stopped.
echo ============================================================
pause
