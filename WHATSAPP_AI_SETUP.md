# WhatsApp Watcher with AI Draft Replies - Setup Guide

## 🎯 What's New

WhatsApp Watcher ab automatically AI-powered draft replies generate karega har important message ke liye!

---

## 🔧 Setup Instructions

### Step 1: Set API Key

**Option A: Environment Variable (Recommended)**
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your-api-key-here"

# Windows (CMD)
set ANTHROPIC_API_KEY=your-api-key-here

# Linux/Mac
export ANTHROPIC_API_KEY="your-api-key-here"
```

**Option B: Create .env file**
```bash
cd "D:\LEEZA\HACKATHON 0\silver"
echo ANTHROPIC_API_KEY=your-api-key-here > .env
```

### Step 2: Run WhatsApp Watcher
```bash
cd "D:\LEEZA\HACKATHON 0\silver"
python "AI_Employee_Vault/whatsapp_watcher.py"
```

### Step 3: Scan QR Code
- Chrome browser khulega
- WhatsApp Web load hoga
- QR code scan karo (10 minutes ka time hai)
- "✅ LOGIN SUCCESSFUL!" message dikhe to ready!

---

## 📋 How It Works

```
WhatsApp Message Received
    ↓
Keyword Detection (urgent, pricing, etc.)
    ↓
Priority Assignment (P0/P1/P2)
    ↓
🤖 AI Draft Reply Generation
    ↓
Task File Created in Needs_Action/
    ↓
You Review & Send
```

---

## 📝 Example Output

When a message comes in, task file will look like:

```markdown
# WhatsApp Message: John Doe

**Priority:** P1 - High
**Status:** Pending

---

## 💬 Message Details
- **From:** John Doe
- **Received:** 14:30
- **Message:** "Hi, I need urgent pricing for 100 units"

---

## 🤖 AI-Generated Draft Reply

**Status:** Ready for Review

```
Hi John! 👋

Thanks for reaching out! I'd be happy to provide a quote for 100 units.

To give you the most accurate pricing, could you share:
• Which product/model are you interested in?
• Any specific customization requirements?
• Expected delivery timeline?

I can have a detailed proposal ready for you within 24 hours.

When would be a good time for a quick call to discuss?
```

**⚠️ IMPORTANT:** Review before sending
**Approval Required:** Yes - High priority

---

## 🎯 Next Steps
- [ ] Review draft reply
- [ ] Modify if needed
- [ ] Get approval (if required)
- [ ] Send via WhatsApp
```

---

## 🚨 Troubleshooting

### If AI Draft Not Generated:

**Check 1: API Key**
```bash
# Windows PowerShell
echo $env:ANTHROPIC_API_KEY

# Should show your API key
```

**Check 2: Log File**
```bash
# Check latest log
cat "AI_Employee_Vault/Logs/whatsapp_watcher_20260214.md"

# Look for:
# "⚠️ ANTHROPIC_API_KEY not set" - API key missing
# "🤖 Generating AI draft reply..." - Working!
# "✅ AI draft reply generated successfully" - Success!
```

**Check 3: Files Exist**
- Company_Handbook.md should exist
- Skills/whatsapp_response_skill.md should exist

---

## 💡 Features

### Smart Priority Detection
- **P0 (Critical):** urgent, emergency, critical, help, problem
- **P1 (High):** pricing, quote, order, payment, invoice
- **P2 (Medium):** question, inquiry, information, details

### Context-Aware Replies
- Uses Company_Handbook.md for guidelines
- Uses WhatsApp skill templates
- Matches sender's tone
- Appropriate for priority level

### Safety Features
- All drafts marked "Review Required"
- High priority = Approval Required
- Never auto-sends (human review always needed)

---

## 🎬 Demo Flow

1. **Start Watcher:**
   ```bash
   python AI_Employee_Vault/whatsapp_watcher.py
   ```

2. **Send Test Message:**
   - From another phone, send: "Hi, urgent pricing needed!"
   - Keywords: "urgent" + "pricing" = P0 Critical

3. **Check Output:**
   - Task file created in `Needs_Action/`
   - AI draft reply included
   - Ready for review

4. **Review & Send:**
   - Open task file
   - Review AI draft
   - Modify if needed
   - Copy and send via WhatsApp

---

## 📊 What Gets Logged

```
[2026-02-14 14:30:15] New important message detected
[2026-02-14 14:30:15] Priority: P1 - High
[2026-02-14 14:30:16] 🤖 Generating AI draft reply...
[2026-02-14 14:30:18] ✅ AI draft reply generated successfully
[2026-02-14 14:30:18] Created task: whatsapp_John_Doe_20260214_143015.md
```

---

## 🔒 Security Notes

- API key never logged
- Messages stored locally only
- No data sent to external services (except Claude API for draft generation)
- Session data encrypted by Playwright

---

## 🎯 Benefits for Demo

1. **Impressive:** AI automatically drafts intelligent replies
2. **Fast:** Responses ready within seconds
3. **Smart:** Context-aware, priority-based
4. **Safe:** Human review required
5. **Professional:** Uses company guidelines

---

**Last Updated:** 2026-02-14
**Feature Added By:** Claude Code
