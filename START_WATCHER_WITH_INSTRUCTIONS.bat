@echo off
echo ============================================================
echo WhatsApp Watcher - START WITH CLEAR INSTRUCTIONS
echo ============================================================
echo.

cd /d "%~dp0"

echo Step 1: Checking API key...
python -c "from dotenv import load_dotenv; import os; load_dotenv(); key = os.getenv('ANTHROPIC_API_KEY'); print('OK: API key loaded') if key and key != 'your_anthropic_api_key_here' else print('ERROR: API key not set'); exit(0 if key and key != 'your_anthropic_api_key_here' else 1)"

if errorlevel 1 (
    echo ERROR: API key not configured!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo IMPORTANT INSTRUCTIONS - READ CAREFULLY!
echo ============================================================
echo.
echo The watcher will now start and open a browser window.
echo.
echo YOU MUST DO THESE STEPS:
echo.
echo 1. A browser window will open with WhatsApp Web
echo 2. You will see a QR CODE on the screen
echo 3. DO NOT CLOSE THE BROWSER WINDOW!
echo.
echo 4. Pick up your PHONE
echo 5. Open WhatsApp app
echo 6. Tap 3 dots menu (top right)
echo 7. Tap "Linked Devices"
echo 8. Tap "Link a Device"
echo 9. Point camera at QR code on computer screen
echo 10. Wait for it to connect
echo.
echo After scanning, you will see:
echo "LOGIN SUCCESSFUL! WhatsApp Web is now connected!"
echo.
echo Then send yourself a message: "urgent need help"
echo.
echo Wait 30 seconds and check:
echo AI_Employee_Vault\Needs_Action\
echo.
echo A new file will appear with AI draft!
echo.
echo ============================================================
echo.
echo Press any key to start the watcher...
pause > nul

echo.
echo Starting WhatsApp Watcher...
echo.
echo REMEMBER:
echo - Keep browser window OPEN
echo - Keep this terminal OPEN
echo - SCAN THE QR CODE with your phone!
echo.
echo ============================================================
echo.

python AI_Employee_Vault/whatsapp_watcher.py

echo.
echo ============================================================
echo Watcher stopped.
echo ============================================================
pause
