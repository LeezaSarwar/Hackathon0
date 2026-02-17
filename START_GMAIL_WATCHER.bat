@echo off
echo ============================================
echo Starting Gmail Watcher
echo ============================================
echo.
echo Location: D:\LEEZA\HACKATHON 0\silver
echo.
echo What will happen:
echo 1. Watcher will start
echo 2. Browser will open for Google login
echo 3. Login with your Gmail account
echo 4. Click "Allow" to give permissions
echo 5. Watcher will start monitoring emails
echo.
echo Press Ctrl+C to stop the watcher
echo ============================================
echo.

cd /d "D:\LEEZA\HACKATHON 0\silver"
python AI_Employee_Vault\gmail_watcher.py

pause
