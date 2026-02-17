@echo off
echo ============================================================
echo Starting WhatsApp Watcher with Debug Mode
echo ============================================================
echo.
echo INSTRUCTIONS:
echo 1. Browser window will open
echo 2. If you see QR code, scan it with your phone
echo 3. Once logged in, send a test message with keywords:
echo    - urgent, help, pricing, payment, etc.
echo 4. Watch the terminal for live updates
echo.
echo Press Ctrl+C to stop the watcher
echo ============================================================
echo.
pause

python "AI_Employee_Vault/whatsapp_watcher.py"

pause
