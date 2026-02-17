@echo off
echo ============================================================
echo GMAIL DRAFT GENERATOR - IMPROVED
echo ============================================================
echo.
echo This version has TWO options:
echo 1. Type/paste short emails directly
echo 2. Read from file (BEST for long emails)
echo.
echo For long emails like the Google Cloud one:
echo - Copy email to a text file (email.txt)
echo - Choose option 2
echo - Enter file path
echo.
echo ============================================================
echo.
pause

cd /d "%~dp0"
python gmail_draft_generator_improved.py

echo.
pause
