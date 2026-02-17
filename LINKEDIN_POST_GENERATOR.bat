@echo off
echo ============================================================
echo LINKEDIN POST GENERATOR
echo ============================================================
echo.
echo This tool creates professional LinkedIn posts
echo WITHOUT needing LinkedIn automation or browser!
echo.
echo Just enter your topic and get an AI-generated post.
echo.
echo ============================================================
echo.
pause

cd /d "%~dp0"
python linkedin_post_generator.py

echo.
pause
