@echo off
cls
echo ============================================================
echo WhatsApp Watcher - Fresh Start
echo ============================================================
echo.
echo Changes Made:
echo   - QR scan timeout: 20 minutes (was 10 min)
echo   - After login: Continuous monitoring (NO timeout)
echo   - AI draft replies: Enabled
echo.
echo ============================================================
echo.
echo What Will Happen:
echo   1. Chrome browser will open
echo   2. WhatsApp Web will load
echo   3. QR code will appear
echo   4. YOU HAVE 20 MINUTES to scan it
echo   5. After scan: Monitoring starts (runs forever)
echo   6. When "urgent need help" arrives: Draft reply created
echo.
echo ============================================================
echo.
echo Ready to start? Press any key...
pause >nul
echo.
echo Starting WhatsApp Watcher...
echo.

cd /d "%~dp0"
python "AI_Employee_Vault\whatsapp_watcher.py"

echo.
echo ============================================================
echo Watcher stopped.
echo ============================================================
pause
