# Silver Tier - Quick Start Guide

Get your AI Employee system up and running in 15 minutes!

## ⚡ Prerequisites Check

Before starting, ensure you have:
- [ ] Python 3.8+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Gmail account
- [ ] Git installed (optional, for version control)

## 🚀 Installation (5 minutes)

### Step 1: Install Dependencies

```bash
# Navigate to project
cd "D:\LEEZA\HACKATHON 0\silver"

# Install Python packages
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Install MCP server dependencies
cd email_mcp_server
npm install
cd ..
```

### Step 2: Configure Environment

```bash
# Copy environment template
copy .env.example .env

# Edit .env file (use notepad or your preferred editor)
notepad .env
```

**Minimal .env configuration:**
```
DRY_RUN=true
DEFAULT_APPROVAL_EXPIRY_HOURS=24
```

## 🔑 Gmail API Setup (5 minutes)

### Option 1: Quick Test (Skip Gmail for now)
You can test the system without Gmail initially. Skip to Step 3.

### Option 2: Full Setup
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "AI Employee"
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download as `gmail_credentials.json`
6. Move to `AI_Employee_Vault/` folder

## 🧪 Test the System (5 minutes)

### Test 1: File Watcher

```bash
# Terminal 1: Start file watcher
python AI_Employee_Vault/file_watcher.py
```

```bash
# Terminal 2: Create test file
echo "This is an urgent test task" > AI_Employee_Vault/Drop/urgent_test.txt
```

**Expected result:** Task file created in `Needs_Action/`

### Test 2: Helper Scripts

```bash
# Generate morning briefing
python AI_Employee_Vault/generate_briefing.py

# Generate end-of-day summary
python AI_Employee_Vault/generate_summary.py

# Prepare LinkedIn content
python AI_Employee_Vault/prepare_linkedin.py
```

**Expected result:** Files created in `Logs/` folder

### Test 3: Approval Workflow

```bash
# Terminal 1: Start orchestrator
python AI_Employee_Vault/orchestrator.py
```

```bash
# Terminal 2: Create test approval
python AI_Employee_Vault/prepare_linkedin.py
# This creates an approval request in Pending_Approval/

# Move to Approved folder to test
move AI_Employee_Vault\Pending_Approval\linkedin_post_approval_*.md AI_Employee_Vault\Approved\
```

**Expected result:** Orchestrator processes and moves to LinkedIn_Posted/

## 🎯 Next Steps

### For Development/Testing
```bash
# Run individual watchers in separate terminals
python AI_Employee_Vault/file_watcher.py
python AI_Employee_Vault/orchestrator.py
```

### For Production (24/7 operation)
```bash
# Install PM2
npm install -g pm2

# Start all services
pm2 start ecosystem.config.js

# View status
pm2 status

# View logs
pm2 logs
```

## 📊 Verify Installation

Run the test suite:
```bash
python AI_Employee_Vault/test_system.py
```

**Expected output:** All tests should pass

## 🔧 Common Issues

### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Playwright not installed"
**Solution:**
```bash
playwright install chromium
```

### Issue: "Permission denied"
**Solution:** Run terminal as Administrator (Windows)

### Issue: "Port already in use"
**Solution:** Stop other instances with `pm2 stop all`

## 📚 What's Next?

1. **Configure Gmail API** (if skipped)
2. **Set up WhatsApp** - Run `python AI_Employee_Vault/whatsapp_watcher.py`
3. **Set up LinkedIn** - Run `python AI_Employee_Vault/linkedin_automation.py`
4. **Configure Scheduling** - Import Task Scheduler XMLs
5. **Customize Business_Goals.md** - Add your business info
6. **Customize Company_Handbook.md** - Add your preferences

## 🎓 Learning the System

### Key Files to Understand
1. `Dashboard.md` - System status
2. `Company_Handbook.md` - Rules and guidelines
3. `Business_Goals.md` - Business strategy
4. `Skills/*.md` - AI agent capabilities

### Key Folders
- `Drop/` - Place files here for processing
- `Needs_Action/` - Tasks requiring attention
- `Pending_Approval/` - Actions awaiting your approval
- `Approved/` - Approved actions (auto-executed)
- `Done/` - Completed tasks
- `Logs/` - All activity logs

## 🎉 You're Ready!

Your AI Employee system is now set up. Start by:
1. Dropping a test file in `Drop/` folder
2. Checking `Dashboard.md` for status
3. Reviewing tasks in `Needs_Action/`
4. Approving actions in `Pending_Approval/`

**Need help?** Check the full README.md or review the logs in `Logs/` folder.

---

**Setup Time:** ~15 minutes
**Difficulty:** Beginner-friendly
**Support:** Check logs and README.md for troubleshooting
