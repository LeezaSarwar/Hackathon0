@echo off
echo ============================================================
echo WhatsApp Watcher - Quick Test
echo ============================================================
echo.

cd /d "%~dp0"

echo Checking API key...
python -c "from dotenv import load_dotenv; import os; load_dotenv(); key = os.getenv('ANTHROPIC_API_KEY'); print('OK: API key loaded (' + str(len(key)) + ' chars)') if key and key != 'your_anthropic_api_key_here' else print('ERROR: API key not set'); exit(0 if key and key != 'your_anthropic_api_key_here' else 1)"

if errorlevel 1 (
    echo.
    echo ERROR: API key not configured!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Starting WhatsApp Watcher
echo ============================================================
echo.
echo IMPORTANT INSTRUCTIONS:
echo.
echo 1. A browser window will open with WhatsApp Web
echo 2. You'll see a QR code
echo 3. Pick up your phone and open WhatsApp
echo 4. Tap 3 dots menu -^> "Linked Devices"
echo 5. Tap "Link a Device"
echo 6. Scan the QR code on your computer screen
echo.
echo After scanning:
echo 7. Wait for "LOGIN SUCCESSFUL!" message
echo 8. Send yourself a WhatsApp message: "urgent need help"
echo 9. Wait 30 seconds
echo 10. Check AI_Employee_Vault\Needs_Action\ for new file
echo.
echo ============================================================
echo.
pause

echo Starting watcher...
echo.
python AI_Employee_Vault/whatsapp_watcher.py

pause
