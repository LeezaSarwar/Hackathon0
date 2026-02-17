@echo off
echo ============================================================
echo WhatsApp Diagnostic Tool
echo ============================================================
echo.
echo This will:
echo 1. Open WhatsApp Web
echo 2. Show you what chats are visible
echo 3. Check if your messages have keywords
echo 4. Help identify the problem
echo.
echo Make sure:
echo - WhatsApp watcher is STOPPED (Ctrl+C if running)
echo - Your sister's message is still unread (or send a new one)
echo.
pause

python diagnose_whatsapp.py

echo.
echo ============================================================
echo Diagnostic complete! Check the output above.
echo ============================================================
pause
