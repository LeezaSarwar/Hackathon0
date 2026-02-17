@echo off
cls
echo ============================================================
echo WhatsApp Watcher - DETAILED LOGGING MODE
echo ============================================================
echo.
echo This version shows EVERYTHING:
echo - Which chats are being checked
echo - What messages are found
echo - Which keywords match
echo - Why messages are processed or skipped
echo.
echo INSTRUCTIONS:
echo 1. Wait for "Already logged in" message
echo 2. Send test message from sister's phone with keywords:
echo    "urgent help with pricing"
echo 3. Wait 30 seconds for next check cycle
echo 4. Watch the detailed output below
echo.
echo Keywords being monitored:
echo - Urgent: urgent, asap, emergency, critical, help, problem
echo - Business: pricing, quote, order, payment, invoice, delivery
echo - Inquiry: question, inquiry, information, details, available
echo.
echo ============================================================
echo.
pause

cd "D:\LEEZA\HACKATHON 0\silver"
python AI_Employee_Vault/whatsapp_watcher.py

pause
