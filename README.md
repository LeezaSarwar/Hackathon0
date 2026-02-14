# AI Employee - Brozen Tier

A comprehensive AI-powered employee system that monitors Gmail, WhatsApp, and LinkedIn, with human-in-the-loop approval workflows and automated task management.

## 🎯 Features

### Silver Tier Capabilities
- ✅ Complete Obsidian vault structure with Dashboard and Handbook
- ✅ Three watcher scripts (Gmail, WhatsApp, LinkedIn)
- ✅ Automated LinkedIn posting for business growth
- ✅ Claude reasoning loop with Plan.md generation
- ✅ Email MCP server for external actions
- ✅ Human-in-the-loop approval workflow
- ✅ Scheduling via cron/Task Scheduler
- ✅ All AI functionality as Agent Skills

## 📁 Project Structure

```
silver/
├── AI_Employee_Vault/
│   ├── Inbox/              # New items awaiting review
│   ├── Needs_Action/       # Tasks requiring work
│   ├── Done/               # Completed tasks
│   ├── Plans/              # Action plans
│   ├── Logs/               # Activity logs
│   ├── Skills/             # Agent skill definitions
│   ├── Pending_Approval/   # Actions awaiting approval
│   ├── Approved/           # Approved actions
│   ├── Rejected/           # Rejected actions
│   ├── LinkedIn_Queue/     # Scheduled LinkedIn posts
│   ├── LinkedIn_Ideas/     # Content ideas
│   ├── LinkedIn_Posted/    # Posted content archive
│   ├── Dashboard.md        # Real-time status dashboard
│   ├── Company_Handbook.md # Guidelines and rules
│   ├── Business_Goals.md   # Business strategy
│   ├── file_watcher.py     # Drop folder monitor
│   ├── gmail_watcher.py    # Gmail monitoring
│   ├── whatsapp_watcher.py # WhatsApp monitoring
│   ├── linkedin_automation.py # LinkedIn automation
│   ├── orchestrator.py     # Approval workflow manager
│   ├── generate_briefing.py # Morning briefing
│   ├── generate_summary.py  # End-of-day summary
│   └── prepare_linkedin.py  # LinkedIn content prep
├── email_mcp_server/       # MCP server for email actions
│   ├── index.js
│   └── package.json
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── mcp_config.json        # MCP server configuration
├── ecosystem.config.js    # PM2 process management
├── task_scheduler_*.xml   # Windows Task Scheduler configs
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 18+
- Gmail account with API access
- LinkedIn account
- WhatsApp account

### Installation

```bash
# 1. Clone or navigate to the project
cd silver

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium

# 4. Install MCP server dependencies
cd email_mcp_server
npm install
cd ..

# 5. Copy environment template
cp .env.example .env
# Edit .env with your credentials
```

### Gmail API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials as `gmail_credentials.json`
6. Place in `AI_Employee_Vault/` folder

### First Run Authentication

```bash
# Gmail authentication
python AI_Employee_Vault/gmail_watcher.py
# Follow OAuth flow in browser

# WhatsApp authentication
python AI_Employee_Vault/whatsapp_watcher.py
# Scan QR code with your phone

# LinkedIn authentication
python AI_Employee_Vault/linkedin_automation.py
# Login manually in the browser window
```

## 🎮 Usage

### Running Individual Components

```bash
# File Watcher (monitors Drop folder)
python AI_Employee_Vault/file_watcher.py

# Gmail Watcher (checks every 2 minutes)
python AI_Employee_Vault/gmail_watcher.py

# WhatsApp Watcher (checks every 30 seconds)
python AI_Employee_Vault/whatsapp_watcher.py

# LinkedIn Automation (checks every 5 minutes)
python AI_Employee_Vault/linkedin_automation.py

# Orchestrator (processes approvals every minute)
python AI_Employee_Vault/orchestrator.py
```

### Running All Components with PM2

```bash
# Install PM2
npm install -g pm2

# Start all services
pm2 start ecosystem.config.js

# View status
pm2 status

# View logs
pm2 logs

# Stop all
pm2 stop all

# Restart all
pm2 restart all
```

### Windows Task Scheduler Setup

```bash
# Import scheduled tasks
schtasks /create /xml task_scheduler_morning_briefing.xml /tn "AI Employee - Morning Briefing"
schtasks /create /xml task_scheduler_eod_summary.xml /tn "AI Employee - EOD Summary"
schtasks /create /xml task_scheduler_linkedin_prep.xml /tn "AI Employee - LinkedIn Prep"

# View scheduled tasks
schtasks /query /tn "AI Employee*"
```

## 📊 Monitoring

### Dashboard
```bash
# View current status
cat AI_Employee_Vault/Dashboard.md

# Or open in your editor
code AI_Employee_Vault/Dashboard.md
```

### Logs
```bash
# View today's logs
ls AI_Employee_Vault/Logs/*$(date +%Y%m%d)*

# Tail orchestrator log
tail -f AI_Employee_Vault/Logs/orchestrator_$(date +%Y%m%d).md

# View morning briefing
cat AI_Employee_Vault/Logs/morning_briefing_$(date +%Y%m%d).md
```

## 🔄 Workflows

### Email Workflow
1. Gmail watcher detects important email
2. Creates task in `/Needs_Action`
3. Claude analyzes and drafts response
4. Creates approval request in `/Pending_Approval`
5. User reviews and moves to `/Approved`
6. Orchestrator sends email via MCP server
7. Task moved to `/Done`

### LinkedIn Workflow
1. Claude generates post based on Business_Goals
2. Creates approval request with content
3. User reviews and approves
4. Orchestrator queues post
5. LinkedIn automation publishes
6. Engagement tracked and logged

### WhatsApp Workflow
1. WhatsApp watcher detects message with keywords
2. Creates task with message details
3. Claude drafts response using templates
4. Approval requested if needed
5. Response sent (manual or automated)
6. Task completed and logged

## 🎓 Agent Skills

All AI functionality is defined as skills in `/Skills`:
- `email_triage_skill.md` - Email analysis and response
- `whatsapp_response_skill.md` - WhatsApp message handling
- `linkedin_post_skill.md` - LinkedIn content generation
- `approval_request_skill.md` - Approval workflow management
- `create_task_plan_skill.md` - Task planning
- `update_dashboard_skill.md` - Dashboard updates
- `process_inbox_skill.md` - Inbox processing

## 🔐 Security

- All credentials stored in `.env` (never commit)
- Approval required for sensitive actions
- Dry-run mode available for testing
- Audit logging for all actions
- Session data stored locally
- `.gitignore` prevents credential leaks

## 🔧 Troubleshooting

### Gmail API Issues
```bash
# Check credentials
ls AI_Employee_Vault/gmail_credentials.json

# Remove token and re-authenticate
rm AI_Employee_Vault/gmail_token.pickle
python AI_Employee_Vault/gmail_watcher.py
```

### WhatsApp Connection Issues
```bash
# Clear session and re-authenticate
rm -rf AI_Employee_Vault/whatsapp_session_data
python AI_Employee_Vault/whatsapp_watcher.py
```

### LinkedIn Automation Issues
```bash
# Clear session and re-authenticate
rm -rf AI_Employee_Vault/linkedin_session_data
python AI_Employee_Vault/linkedin_automation.py
```

### MCP Server Issues
```bash
# Test server manually
node email_mcp_server/index.js

# Check Node version
node --version  # Should be 18+

# Reinstall dependencies
cd email_mcp_server
rm -rf node_modules package-lock.json
npm install
```

## 📈 Performance Metrics

Track in Dashboard:
- Tasks processed per day
- Average response time
- Approval rate
- LinkedIn engagement
- Email response rate

## 🧪 Testing

```bash
# Test file watcher
echo "Test task" > AI_Employee_Vault/Drop/test.txt

# Test morning briefing
python AI_Employee_Vault/generate_briefing.py

# Test end-of-day summary
python AI_Employee_Vault/generate_summary.py

# Test LinkedIn content prep
python AI_Employee_Vault/prepare_linkedin.py
```

## 📝 Configuration

### Environment Variables (.env)
```bash
GMAIL_CLIENT_ID=your_client_id
GMAIL_CLIENT_SECRET=your_client_secret
DRY_RUN=false
DEFAULT_APPROVAL_EXPIRY_HOURS=24
```

### MCP Server (mcp_config.json)
```json
{
  "mcpServers": {
    "email": {
      "command": "node",
      "args": ["path/to/email_mcp_server/index.js"]
    }
  }
}
```

## 🤝 Contributing

This is a hackathon project. Feel free to extend and customize for your needs.

## 📄 License

MIT License

## 🆘 Support

For issues:
- Check logs in `/Logs` folder
- Review Company_Handbook.md
- Consult skill definitions in `/Skills`

---

**Built for the Personal AI Employee Hackathon - Silver Tier**

**Time Investment:** 20-30 hours
**Complexity:** Intermediate to Advanced
**Technologies:** Python, Node.js, Playwright, Gmail API, MCP Protocol
