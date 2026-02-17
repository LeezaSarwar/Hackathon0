@echo off
echo ============================================================
echo WhatsApp Watcher - System Status Check
echo ============================================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)
echo.

echo Checking required packages...
python -c "import dotenv; import anthropic; import playwright; print('OK: All packages installed')"
if errorlevel 1 (
    echo ERROR: Missing packages!
    echo Run: pip install python-dotenv anthropic playwright
    pause
    exit /b 1
)
echo.

echo Checking .env file...
if not exist ".env" (
    echo ERROR: .env file not found!
    pause
    exit /b 1
)
echo OK: .env file exists
echo.

echo Checking API key configuration...
python -c "from dotenv import load_dotenv; import os; load_dotenv(); key = os.getenv('ANTHROPIC_API_KEY'); exit(0 if key and key != 'your_anthropic_api_key_here' else 1)"
if errorlevel 1 (
    echo.
    echo ============================================================
    echo WARNING: API Key Not Configured
    echo ============================================================
    echo.
    echo The ANTHROPIC_API_KEY in .env file is not set.
    echo.
    echo Files WILL be created but NO AI draft replies.
    echo.
    echo To fix:
    echo 1. Get API key from: https://console.anthropic.com/
    echo 2. Edit .env file and replace placeholder
    echo 3. Run this script again
    echo.
    echo ============================================================
    echo.
    pause
) else (
    echo OK: API key is configured
    echo.
    echo ============================================================
    echo System Ready!
    echo ============================================================
    echo.
    echo All checks passed. You can now:
    echo.
    echo 1. Run diagnostic demo:
    echo    python demo_diagnostic_logging.py
    echo.
    echo 2. Test with existing files:
    echo    python test_whatsapp_fix.py
    echo.
    echo 3. Start the watcher:
    echo    python AI_Employee_Vault/whatsapp_watcher.py
    echo.
    echo ============================================================
    echo.
)

pause
