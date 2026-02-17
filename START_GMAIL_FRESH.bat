@echo off
echo ============================================
echo Gmail Watcher - Fresh Start
echo ============================================
echo.
echo Deleting old token (if exists)...
if exist "AI_Employee_Vault\gmail_token.pickle" (
    del "AI_Employee_Vault\gmail_token.pickle"
    echo Token deleted.
) else (
    echo No old token found.
)
echo.
echo Starting Gmail Watcher...
echo.
echo Browser will open for authentication.
echo Login with: leezasarwar0@gmail.com
echo Click "Allow" to give permissions.
echo.
echo ============================================
echo.

cd /d "D:\LEEZA\HACKATHON 0\silver"
python AI_Employee_Vault\gmail_watcher.py

pause
