# Gmail OAuth Complete Setup Guide

## Problem
Getting "400. That's an error. The server cannot process the request" when trying to authenticate.

## Solution: Properly Configure Google Cloud Console

### Step 1: Create/Select Google Cloud Project

1. Go to: https://console.cloud.google.com/
2. Click on project dropdown (top left)
3. Click "NEW PROJECT"
4. Project name: "AI Employee System" (or any name)
5. Click "CREATE"
6. Wait for project to be created, then select it

### Step 2: Enable Gmail API

1. Go to: https://console.cloud.google.com/apis/library
2. Search for "Gmail API"
3. Click on "Gmail API"
4. Click "ENABLE" button
5. Wait for it to enable

### Step 3: Configure OAuth Consent Screen

1. Go to: https://console.cloud.google.com/apis/credentials/consent
2. Select "External" user type
3. Click "CREATE"

**Fill in the form:**
- App name: "AI Employee Gmail Watcher"
- User support email: (your email)
- Developer contact email: (your email)
- Click "SAVE AND CONTINUE"

**Scopes page:**
- Click "ADD OR REMOVE SCOPES"
- Search for "gmail.readonly"
- Check the box for: `https://www.googleapis.com/auth/gmail.readonly`
- Click "UPDATE"
- Click "SAVE AND CONTINUE"

**Test users page:**
- Click "ADD USERS"
- Enter YOUR Gmail address (the one you want to monitor)
- Click "ADD"
- Click "SAVE AND CONTINUE"

**Summary page:**
- Review and click "BACK TO DASHBOARD"

### Step 4: Create OAuth 2.0 Credentials

1. Go to: https://console.cloud.google.com/apis/credentials
2. Click "CREATE CREDENTIALS" (top)
3. Select "OAuth client ID"
4. Application type: **"Desktop app"** (IMPORTANT!)
5. Name: "Gmail Watcher Desktop"
6. Click "CREATE"

### Step 5: Download Credentials

1. You'll see a popup with Client ID and Client Secret
2. Click "DOWNLOAD JSON" button (download icon)
3. A file will download (name like: `client_secret_xxxxx.json`)
4. Save this file

### Step 6: Replace Credentials File

1. Rename the downloaded file to: `gmail_credentials.json`
2. Copy it to: `D:\LEEZA\HACKATHON 0\silver\AI_Employee_Vault\gmail_credentials.json`
3. Replace the existing file

### Step 7: Run Watcher

```powershell
cd "D:\LEEZA\HACKATHON 0\silver"
python AI_Employee_Vault/gmail_watcher.py
```

### Step 8: Authenticate

1. Browser will open automatically
2. Login with the Gmail account you added as test user
3. You'll see "Google hasn't verified this app" warning
4. Click "Advanced" (bottom left)
5. Click "Go to AI Employee Gmail Watcher (unsafe)"
6. Click "Continue"
7. Review permissions and click "Allow"
8. Browser will show "The authentication flow has completed"
9. Close browser
10. Watcher will start running in terminal!

---

## Troubleshooting

### "Access blocked: This app's request is invalid"
- Make sure you selected "Desktop app" type (not Web application)
- Make sure OAuth consent screen is configured
- Make sure your email is added as test user

### "400 error"
- Delete old `gmail_credentials.json`
- Download fresh credentials from Google Cloud Console
- Make sure Gmail API is enabled

### "redirect_uri_mismatch"
- Make sure application type is "Desktop app"
- Desktop app automatically handles redirects

### Browser doesn't open
- Copy the URL from terminal
- Paste in browser manually
- Complete authentication
- Copy the code shown
- Paste back in terminal

---

## Important Notes

1. **Test Users**: Your app is in "Testing" mode, so only test users can access it. Add your Gmail address as test user.

2. **Verification**: You don't need to verify the app for personal use. The "unsafe" warning is normal for unverified apps.

3. **Token Storage**: After first authentication, token is saved in `gmail_token.pickle`. You won't need to authenticate again unless token expires.

4. **Scopes**: We only use `gmail.readonly` scope - watcher can only READ emails, not send or delete.

---

## Quick Checklist

- [ ] Google Cloud project created
- [ ] Gmail API enabled
- [ ] OAuth consent screen configured
- [ ] Your email added as test user
- [ ] OAuth credentials created (Desktop app type)
- [ ] Credentials JSON downloaded
- [ ] File renamed to `gmail_credentials.json`
- [ ] File placed in `AI_Employee_Vault` folder
- [ ] Watcher started
- [ ] Browser authentication completed
- [ ] Watcher running successfully

---

**After successful setup, watcher will:**
- Check emails every 2 minutes
- Look for important keywords
- Create task files automatically
- Log all activity
