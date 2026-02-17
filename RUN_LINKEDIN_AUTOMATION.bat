@echo off
echo ========================================
echo LinkedIn Automation Starter
echo ========================================
echo.
echo Starting LinkedIn automation...
echo Browser will open automatically.
echo.
echo IMPORTANT:
echo - If not logged in, you'll have 120 seconds to login manually
echo - The automation will check for approved posts every 5 minutes
echo - Press Ctrl+C to stop the automation
echo.
echo ========================================
echo.

cd /d "D:\LEEZA\HACKATHON 0\silver"
python "AI_Employee_Vault\linkedin_automation.py"

pause
