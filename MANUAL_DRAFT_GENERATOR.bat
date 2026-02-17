@echo off
echo ============================================================
echo MANUAL WHATSAPP DRAFT GENERATOR
echo ============================================================
echo.
echo This tool lets you create AI drafts WITHOUT needing
echo WhatsApp Web login or QR code scanning!
echo.
echo Just paste the message you received and get an AI draft.
echo.
echo ============================================================
echo.
pause

cd /d "%~dp0"
python manual_draft_generator.py

echo.
pause
