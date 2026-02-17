@echo off
echo Checking latest WhatsApp task files...
echo ============================================================
echo.
dir /O-D /B "AI_Employee_Vault\Needs_Action\whatsapp_*.md" | findstr /R "whatsapp_.*_2026" | head -5
echo.
echo ============================================================
echo Latest file content:
echo.
type "AI_Employee_Vault\Needs_Action\whatsapp_*.md" 2>nul | head -50
echo.
pause
