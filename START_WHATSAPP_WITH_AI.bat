@echo off
echo ============================================================
echo WhatsApp Watcher with AI Draft Replies
echo ============================================================
echo.

REM Check if API key is set
if "%ANTHROPIC_API_KEY%"=="" (
    echo [WARNING] ANTHROPIC_API_KEY not set!
    echo.
    echo To enable AI draft replies, set your API key:
    echo   set ANTHROPIC_API_KEY=your-api-key-here
    echo.
    echo Press any key to continue without AI drafts...
    pause >nul
    echo.
) else (
    echo [OK] API Key detected - AI drafts will be generated
    echo.
)

echo Starting WhatsApp Watcher...
echo.
echo Instructions:
echo 1. Chrome browser will open with WhatsApp Web
echo 2. Scan QR code with your phone (10 minutes timeout)
echo 3. After login, watcher will monitor messages every 30 seconds
echo 4. Press Ctrl+C to stop
echo.
echo ============================================================
echo.

cd /d "%~dp0"
python "AI_Employee_Vault\whatsapp_watcher.py"

pause
