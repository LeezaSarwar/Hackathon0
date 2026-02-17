@echo off
echo ============================================================
echo GMAIL DRAFT GENERATOR
echo ============================================================
echo.
echo This tool creates AI draft replies for Gmail emails
echo WITHOUT needing Gmail API or OAuth setup!
echo.
echo Just paste the email and get an AI draft reply.
echo.
echo ============================================================
echo.
pause

cd /d "%~dp0"
python gmail_draft_generator.py

echo.
pause
