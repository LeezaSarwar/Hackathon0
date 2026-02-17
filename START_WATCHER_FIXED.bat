@echo off
cls
echo ============================================================
echo WhatsApp Watcher - FIXED VERSION
echo ============================================================
echo.
echo FIXES APPLIED:
echo - Popup dismissal (Get WhatsApp for Windows)
echo - Checks 10 chats instead of 5
echo - Force click to bypass overlays
echo - Multiple message selectors
echo - Better error handling
echo.
echo ============================================================
echo.
echo INSTRUCTIONS:
echo 1. Wait for login confirmation
echo 2. Send test message: "urgent help pricing"
echo 3. Wait 30 seconds for check cycle
echo 4. Watch for detailed output
echo.
echo ============================================================
pause

cd "D:\LEEZA\HACKATHON 0\silver"
python AI_Employee_Vault/whatsapp_watcher.py

pause
