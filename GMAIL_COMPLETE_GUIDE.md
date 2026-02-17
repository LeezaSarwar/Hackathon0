# GMAIL WATCHER - COMPLETE SETUP (Urdu/English)

## Current Status: 400 Error - OAuth Not Configured

## Fix Karne Ke Liye (3 Simple Steps):

### STEP 1: Google Cloud Console Setup (5 minutes)

**Link 1 - OAuth Consent Screen:**
https://console.cloud.google.com/apis/credentials/consent?project=gmail-api-system-487610

Ye karo:
1. "EDIT APP" button par click karo (ya "CREATE" agar naya hai)
2. Form fill karo:
   - App name: AI Employee Gmail Watcher
   - User support email: leezasarwar0@gmail.com (dropdown se select)
   - Developer contact: leezasarwar0@gmail.com
   - Click "SAVE AND CONTINUE"

3. Scopes page par:
   - "ADD OR REMOVE SCOPES" button click karo
   - Search box mein type: gmail.readonly
   - Checkbox check karo: ☑ https://www.googleapis.com/auth/gmail.readonly
   - "UPDATE" button click karo
   - "SAVE AND CONTINUE" click karo

4. **Test Users page (MOST IMPORTANT!):**
   - "ADD USERS" button click karo
   - Type: leezasarwar0@gmail.com
   - "ADD" button click karo
   - "SAVE AND CONTINUE" click karo

5. Summary page:
   - "BACK TO DASHBOARD" click karo

**Link 2 - Enable Gmail API:**
https://console.cloud.google.com/apis/library/gmail.googleapis.com?project=gmail-api-system-487610

- "ENABLE" button click karo (agar already enabled hai to skip)

---

### STEP 2: Wait 2-3 Minutes

Google ko settings update karne do. Chai pi lo! ☕

---

### STEP 3: Run Watcher

PowerShell mein ye command:

```powershell
cd "D:\LEEZA\HACKATHON 0\silver"
.\START_GMAIL_FRESH.bat
```

Ya file par double-click karo:
- File Explorer: D:\LEEZA\HACKATHON 0\silver
- START_GMAIL_FRESH.bat par double-click

---

## What Will Happen:

1. ✅ Terminal window khulegi
2. ✅ Browser automatically khulega
3. ✅ Google login page dikhega
4. ✅ Login karo: leezasarwar0@gmail.com
5. ⚠️ Warning dikhegi: "This app isn't verified"
   - Click: "Advanced" (bottom left)
   - Click: "Go to AI Employee Gmail Watcher (unsafe)"
   - Ye safe hai - tumhari apni app hai!
6. ✅ Permissions page:
   - Review karo
   - Click "Allow"
7. ✅ Browser mein: "The authentication flow has completed"
8. ✅ Browser close karo
9. ✅ Terminal mein watcher chal raha hoga!

---

## Success Messages (Terminal mein ye dikhega):

```
[2026-02-16 XX:XX:XX] Gmail Watcher initialized
[2026-02-16 XX:XX:XX] ============================================================
[2026-02-16 XX:XX:XX] Gmail Watcher Started
[2026-02-16 XX:XX:XX] Check interval: 120 seconds
[2026-02-16 XX:XX:XX] ============================================================
[2026-02-16 XX:XX:XX] Starting OAuth flow...
[2026-02-16 XX:XX:XX] Authentication successful
[2026-02-16 XX:XX:XX] No new unread emails
```

Watcher har 2 minutes mein emails check karega!

---

## Troubleshooting:

### Still Getting 400 Error?
- Check: Test user (leezasarwar0@gmail.com) add kiya hai?
- Check: Gmail API enabled hai?
- Wait: 5 minutes aur try karo (Google ko time chahiye)

### Browser Nahi Khul Raha?
- Terminal mein URL dikhega
- Copy karo aur manually browser mein paste karo
- Login karke allow karo

### "Access Blocked" Error?
- OAuth consent screen mein test user add karna bhool gaye
- Wapas jao aur test user add karo

---

## Quick Verification Checklist:

Before running watcher, verify:
- [ ] OAuth consent screen configured
- [ ] App name set: "AI Employee Gmail Watcher"
- [ ] Scope added: gmail.readonly
- [ ] Test user added: leezasarwar0@gmail.com ← CRITICAL!
- [ ] Gmail API enabled
- [ ] Waited 2-3 minutes after setup

---

## After Successful Setup:

Watcher will:
- ✅ Check emails every 2 minutes
- ✅ Look for keywords: urgent, invoice, meeting, etc.
- ✅ Create task files in: AI_Employee_Vault/Needs_Action/
- ✅ Log activity in: AI_Employee_Vault/Logs/

---

## Stop Watcher:

Press: Ctrl + C in terminal

---

## Need Help?

If still not working, tell me:
1. Kya OAuth consent screen configure ho gaya?
2. Kya test user add ho gaya?
3. Kya Gmail API enable hai?
4. Kya error message aa raha hai?
