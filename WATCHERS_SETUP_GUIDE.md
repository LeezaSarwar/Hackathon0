# SILVER TIER - WATCHERS SETUP GUIDE
# Quick setup to get Gmail, WhatsApp, LinkedIn working

═══════════════════════════════════════════════════════════════
OPTION 1: WHATSAPP WATCHER (EASIEST - 5 MINUTES)
═══════════════════════════════════════════════════════════════

Requirements:
✓ Internet connection
✓ WhatsApp on your phone
✓ 5 minutes

Steps:
1. Make sure you have internet connection
2. Run: python AI_Employee_Vault/whatsapp_watcher.py
3. QR code will appear in browser
4. Scan with WhatsApp on your phone (WhatsApp > Settings > Linked Devices)
5. Done! Watcher will start monitoring

Test:
- Send yourself a WhatsApp message with "urgent"
- Watcher will create a task in Needs_Action


═══════════════════════════════════════════════════════════════
OPTION 2: GMAIL WATCHER (MEDIUM - 20 MINUTES)
═══════════════════════════════════════════════════════════════

Requirements:
✓ Google account
✓ Internet connection
✓ 20 minutes

Steps:

STEP 1: Create Google Cloud Project (10 min)
1. Go to: https://console.cloud.google.com/
2. Click: "Create Project"
3. Name: "AI Employee"
4. Click: "Create"

STEP 2: Enable Gmail API (2 min)
1. In project, go to: "APIs & Services" > "Library"
2. Search: "Gmail API"
3. Click: "Enable"

STEP 3: Create OAuth Credentials (5 min)
1. Go to: "APIs & Services" > "Credentials"
2. Click: "Create Credentials" > "OAuth client ID"
3. If asked, configure consent screen:
   - User Type: External
   - App name: "AI Employee"
   - User support email: Your email
   - Developer email: Your email
   - Click: "Save and Continue" (skip scopes)
4. Back to Create OAuth client ID:
   - Application type: "Desktop app"
   - Name: "AI Employee Desktop"
   - Click: "Create"
5. Click: "Download JSON"
6. Rename downloaded file to: gmail_credentials.json
7. Move to: D:\LEEZA\HACKATHON 0\silver\AI_Employee_Vault\

STEP 4: Run Gmail Watcher (3 min)
1. Run: python AI_Employee_Vault/gmail_watcher.py
2. Browser will open for OAuth
3. Login with your Google account
4. Click: "Allow"
5. Done! Watcher will start monitoring

Test:
- Send yourself an email with "urgent" in subject
- Watcher will create a task in Needs_Action


═══════════════════════════════════════════════════════════════
OPTION 3: LINKEDIN AUTOMATION (MEDIUM - 10 MINUTES)
═══════════════════════════════════════════════════════════════

Requirements:
✓ LinkedIn account
✓ Internet connection
✓ 10 minutes

Steps:
1. Run: python AI_Employee_Vault/linkedin_automation.py
2. Browser will open to LinkedIn
3. Login manually
4. Session will be saved
5. Done! Automation will start

Test:
- Create a post draft in LinkedIn_Queue folder
- Automation will post it (after approval)


═══════════════════════════════════════════════════════════════
RECOMMENDED: START WITH WHATSAPP (FASTEST)
═══════════════════════════════════════════════════════════════

For demo, I recommend:
1. ✅ WhatsApp (5 min) - Easiest, most impressive
2. ✅ File watcher (already working) - Shows the pattern
3. ⏸️ Gmail (20 min) - If you have time
4. ⏸️ LinkedIn (10 min) - If you have time

With WhatsApp + File watcher working, you have:
- 2 watchers running live ✅
- Code for all 3 watchers ✅
- Silver tier requirement met ✅


═══════════════════════════════════════════════════════════════
QUICK DEMO STRATEGY
═══════════════════════════════════════════════════════════════

If you only have 30 minutes before demo:

OPTION A: Setup WhatsApp only (5 min)
- Show file watcher live
- Show WhatsApp watcher live
- Show Gmail/LinkedIn code and explain

OPTION B: Setup all three (35 min)
- Takes longer but shows everything working
- More impressive but riskier if something fails

OPTION C: Show code only (0 min setup)
- Show all three watcher code files
- Explain they need authentication
- Use file watcher as proof
- Still meets Silver tier requirements


═══════════════════════════════════════════════════════════════
WHAT DO YOU WANT TO DO?
═══════════════════════════════════════════════════════════════

1. Setup WhatsApp now (5 min) - RECOMMENDED
2. Setup Gmail now (20 min)
3. Setup all three (35 min)
4. Just show code and record demo (0 min)

Tell me which option you want!
