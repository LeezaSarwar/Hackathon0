# AI Employee Vault - Bronze Tier

**Version:** 1.0
**Created:** 2026-02-11
**Hackathon:** Personal AI Employee Challenge

---

## 🎯 Overview

This is a Bronze Tier implementation of a Personal AI Employee system using Obsidian, Claude Code, and automated file monitoring. The system automatically processes files dropped into a monitored folder, creates actionable tasks, and maintains a real-time dashboard.

---

## 📁 Vault Structure

```
AI_Employee_Vault/
├── Dashboard.md              # Real-time status dashboard
├── Company_Handbook.md       # AI behavior rules and guidelines
├── file_watcher.py          # Automated file monitoring script
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── Inbox/                  # Initial file landing zone
├── Needs_Action/           # Tasks requiring processing
├── Done/                   # Completed tasks
├── Plans/                  # Action plans awaiting approval
├── Logs/                   # System activity logs
├── Skills/                 # Agent skill definitions
│   ├── process_inbox_skill.md
│   ├── update_dashboard_skill.md
│   └── create_task_plan_skill.md
└── Drop/                   # Monitored folder for new files
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Obsidian (optional, for viewing vault)
- Claude Code CLI

### Installation

1. **Install Python Dependencies**
   ```bash
   cd AI_Employee_Vault
   pip install -r requirements.txt
   ```

2. **Start the File Watcher**
   ```bash
   python file_watcher.py
   ```

   The watcher will monitor the `Drop/` folder and automatically create tasks for new files.

3. **Open Vault in Obsidian** (Optional)
   - Open Obsidian
   - Open folder as vault: `AI_Employee_Vault`
   - View `Dashboard.md` for current status

---

## 🔄 Workflow

### Automated File Processing

1. **Drop a file** into the `Drop/` folder
2. **Watcher detects** the new file within seconds
3. **Task created** automatically in `Needs_Action/`
4. **Claude processes** the task using Agent Skills
5. **Dashboard updated** with results
6. **File moved** to `Done/` when complete

### Manual Processing with Claude Code

```bash
# Read the dashboard
claude "Read Dashboard.md and show me pending tasks"

# Process a specific task
claude "Process the task in Needs_Action/task_example_20260211.md"

# Update dashboard
claude "Update Dashboard.md with current status"

# Create an action plan
claude "Create a plan for the urgent task in Needs_Action"
```

---

## 📋 Agent Skills

The system includes three core Agent Skills:

### 1. Process Inbox (`process_inbox_skill.md`)
- Analyzes tasks in Needs_Action folder
- Determines required actions
- Executes safe operations automatically
- Requests approval for restricted actions

### 2. Update Dashboard (`update_dashboard_skill.md`)
- Maintains real-time task counts
- Shows system status
- Logs recent activity
- Provides quick overview

### 3. Create Task Plan (`create_task_plan_skill.md`)
- Generates detailed action plans
- Identifies risks and dependencies
- Provides multiple options
- Requests user approval

---

## 🎮 Testing the System

### Test 1: Basic File Detection

1. Start the watcher:
   ```bash
   python file_watcher.py
   ```

2. Create a test file:
   ```bash
   echo "This is a test file" > Drop/test_document.txt
   ```

3. Check `Needs_Action/` folder - a task file should appear within seconds

4. View the task:
   ```bash
   cat Needs_Action/task_test_document_*.md
   ```

### Test 2: Claude Code Integration

1. Ask Claude to read the dashboard:
   ```bash
   claude "Read Dashboard.md and summarize the current status"
   ```

2. Ask Claude to process a task:
   ```bash
   claude "Read the task file in Needs_Action and tell me what needs to be done"
   ```

3. Ask Claude to update the dashboard:
   ```bash
   claude "Update Dashboard.md with the current task count"
   ```

### Test 3: Priority Detection

Create files with priority keywords:
```bash
echo "Urgent matter" > Drop/urgent_report.txt
echo "Low priority item" > Drop/low_priority_note.txt
```

The watcher will automatically assign priorities based on filename keywords.

---

## 📖 Company Handbook

The `Company_Handbook.md` defines:
- Working hours and availability
- Task prioritization rules (P0-P3)
- Approval requirements
- File organization standards
- AI behavior guidelines

**Key Rules:**
- P0 (Critical): Act immediately, no approval needed
- P1 (High): Same day, log actions
- P2 (Medium): This week, approval for significant changes
- P3 (Low): Backlog, always requires approval

---

## 🔧 Configuration

### Watcher Settings

Edit `file_watcher.py` to customize:
- Monitored folder location
- File processing rules
- Priority detection keywords
- Log file location

### Dashboard Refresh

The dashboard can be updated:
- Automatically after task processing
- On-demand via Claude Code
- Scheduled (add to cron/Task Scheduler)

---

## 📊 Monitoring

### View Logs
```bash
# Today's watcher log
cat Logs/watcher_log_20260211.md

# All logs
ls -la Logs/
```

### Check System Status
```bash
# View dashboard
cat Dashboard.md

# Count pending tasks
ls Needs_Action/ | wc -l

# Count completed tasks
ls Done/ | wc -l
```

---

## 🐛 Troubleshooting

### Watcher Not Detecting Files

**Problem:** Files dropped but no tasks created

**Solutions:**
1. Check watcher is running: `ps aux | grep file_watcher`
2. Check Drop folder permissions
3. View watcher logs in `Logs/`
4. Restart watcher: `python file_watcher.py`

### Task Files Not Created

**Problem:** Watcher running but no task files

**Solutions:**
1. Check `Needs_Action/` folder exists
2. Verify write permissions
3. Check watcher logs for errors
4. Try dropping a simple .txt file

### Claude Code Can't Read Files

**Problem:** Claude reports file not found

**Solutions:**
1. Use absolute paths
2. Verify file exists: `ls -la AI_Employee_Vault/`
3. Check file permissions
4. Try reading Dashboard.md first as a test

---

## 🎯 Bronze Tier Checklist

- ✅ Obsidian vault with folder structure
- ✅ Dashboard.md with real-time status
- ✅ Company_Handbook.md with rules
- ✅ File system watcher (Python script)
- ✅ Three Agent Skills defined
- ✅ Claude Code integration ready
- ✅ Basic workflow documented
- ✅ Testing instructions included

---

## 🚀 Next Steps (Silver/Gold Tiers)

### Silver Tier Ideas
- Gmail integration for email monitoring
- Automated report generation
- Multi-file task processing
- Advanced priority algorithms

### Gold Tier Ideas
- Full email response automation
- Calendar integration
- Multi-agent coordination
- Custom MCP server

---

## 📝 Usage Examples

### Example 1: Processing Meeting Notes

```bash
# Drop meeting notes
cp meeting_notes.txt Drop/

# Watcher creates task automatically
# Claude processes and extracts action items
claude "Process the meeting notes task and extract action items"

# View results
cat Done/meeting_notes_summary_*.md
```

### Example 2: Code Review Request

```bash
# Drop code file
cp bugfix.py Drop/

# Watcher detects and creates task
# Claude analyzes and creates plan
claude "Review the bugfix.py task and create an action plan"

# View plan
cat Plans/bugfix_proposal_*.md
```

### Example 3: Daily Status Check

```bash
# Ask Claude for status
claude "Read Dashboard.md and give me a summary of today's activity"

# Process all pending tasks
claude "Process all tasks in Needs_Action folder"

# Generate daily report
claude "Create a summary of all completed tasks today"
```

---

## 🤝 Contributing

This is a hackathon project. Feel free to:
- Add new Agent Skills
- Improve the watcher script
- Enhance the dashboard
- Create additional automation

---

## 📄 License

MIT License - Feel free to use and modify

---

## 🙏 Acknowledgments

- Built for the Personal AI Employee Hackathon
- Powered by Claude Code and Anthropic's Claude AI
- Inspired by the Obsidian knowledge management system

---

**Status:** Bronze Tier Complete ✅
**Demo Ready:** Yes
**Production Ready:** Prototype (requires testing)
