@echo off
echo ============================================
echo Gmail API - OAuth Setup Links
echo ============================================
echo.
echo Project ID: gmail-api-system-487610
echo.
echo Opening required pages in browser...
echo.
echo ============================================
echo STEP 1: OAuth Consent Screen
echo ============================================
start https://console.cloud.google.com/apis/credentials/consent?project=gmail-api-system-487610
echo.
echo Do these things:
echo 1. Click "EDIT APP" if already exists, or configure new
echo 2. App name: AI Employee Gmail Watcher
echo 3. User support email: YOUR EMAIL
echo 4. Developer contact: YOUR EMAIL
echo 5. Click "SAVE AND CONTINUE"
echo.
echo 6. On Scopes page:
echo    - Click "ADD OR REMOVE SCOPES"
echo    - Search: gmail.readonly
echo    - Check the box
echo    - Click "UPDATE"
echo    - Click "SAVE AND CONTINUE"
echo.
echo 7. On Test Users page (MOST IMPORTANT!):
echo    - Click "ADD USERS"
echo    - Enter YOUR Gmail address (the one you want to monitor)
echo    - Click "ADD"
echo    - Click "SAVE AND CONTINUE"
echo.
echo 8. Review and click "BACK TO DASHBOARD"
echo.
pause
echo.
echo ============================================
echo STEP 2: Enable Gmail API
echo ============================================
start https://console.cloud.google.com/apis/library/gmail.googleapis.com?project=gmail-api-system-487610
echo.
echo Click "ENABLE" button if not already enabled
echo.
pause
echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Now run: START_GMAIL_WATCHER.bat
echo.
pause
