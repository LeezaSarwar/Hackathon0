# Demo Script - AI Employee Vault (Bronze Tier)

**Duration:** 5-10 minutes
**Audience:** Hackathon judges/reviewers
**Goal:** Demonstrate working Bronze Tier implementation

---

## 🎬 Demo Flow

### Part 1: System Overview (1 minute)

**Show:** Vault structure
```bash
cd AI_Employee_Vault
ls -la
```

**Say:**
> "This is my Bronze Tier AI Employee implementation. It consists of an Obsidian vault with automated file monitoring, task processing, and Claude Code integration. The system has 7 main folders, a file watcher script, and 3 Agent Skills."

**Show:** Dashboard
```bash
cat Dashboard.md
```

**Say:**
> "The Dashboard provides real-time status of all tasks, system health, and recent activity."

---

### Part 2: File Watcher Demo (2 minutes)

**Action:** Start the watcher
```bash
python file_watcher.py
```

**Say:**
> "The file watcher monitors the Drop folder for new files. Let me demonstrate by dropping a test file."

**Action:** In a new terminal, create test file
```bash
echo "This is an urgent customer request that needs immediate attention." > Drop/urgent_customer_request.txt
```

**Show:** Watcher output
> "Notice the watcher immediately detected the file and logged the activity."

**Show:** Created task
```bash
ls Needs_Action/
cat Needs_Action/task_urgent_customer_request_*.md
```

**Say:**
> "A task file was automatically created with metadata, priority detection (P0 because of 'urgent' keyword), and a processing checklist."

---

### Part 3: Claude Code Integration (3 minutes)

**Action:** Ask Claude to read dashboard
```bash
claude "Read Dashboard.md and tell me what tasks are pending"
```

**Say:**
> "Claude Code can read directly from the vault and understand the current state."

**Action:** Ask Claude to analyze the task
```bash
claude "Read the urgent customer request task in Needs_Action and tell me what it contains"
```

**Say:**
> "Claude can analyze task files and understand what needs to be done."

**Action:** Ask Claude to update dashboard
```bash
claude "Update Dashboard.md to reflect that we're now processing the urgent customer request task"
```

**Show:** Updated dashboard
```bash
cat Dashboard.md
```

**Say:**
> "Claude can write to the vault, updating the dashboard with current status."

---

### Part 4: Agent Skills Demo (2 minutes)

**Show:** Skills folder
```bash
ls Skills/
```

**Say:**
> "I've defined 3 Agent Skills that guide Claude's behavior:"

**Show:** Process Inbox Skill
```bash
head -n 30 Skills/process_inbox_skill.md
```

**Say:**
> "The Process Inbox skill defines how to analyze tasks, determine actions, and handle approval requirements."

**Show:** Company Handbook
```bash
head -n 50 Company_Handbook.md
```

**Say:**
> "The Company Handbook defines rules for prioritization, approval requirements, and AI behavior. For example, P0 tasks can be acted on immediately, while P2 tasks require approval for significant changes."

---

### Part 5: Complete Workflow (2 minutes)

**Action:** Drop another file
```bash
echo "Project plan for Q1 2026" > Drop/project_plan.txt
```

**Say:**
> "Let me demonstrate the complete workflow with a new file."

**Wait:** 2 seconds for watcher to process

**Show:** New task created
```bash
ls -lt Needs_Action/ | head -n 3
```

**Action:** Ask Claude to process it
```bash
claude "Process the project_plan task: read the file, create a summary, and move it to Done"
```

**Show:** Results
```bash
ls Done/
cat Done/project_plan_summary_*.md
```

**Say:**
> "Claude processed the task, created a summary, and moved it to the Done folder. The dashboard would be updated with this completion."

---

## 🎯 Key Points to Emphasize

### Bronze Tier Requirements Met

1. ✅ **Obsidian Vault Structure**
   - Dashboard.md with real-time status
   - Company_Handbook.md with rules
   - Organized folder structure

2. ✅ **Working Watcher Script**
   - Monitors Drop folder
   - Creates task files automatically
   - Logs all activity
   - Priority detection

3. ✅ **Claude Code Integration**
   - Reads from vault
   - Writes to vault
   - Understands context
   - Follows handbook rules

4. ✅ **Agent Skills**
   - Process Inbox
   - Update Dashboard
   - Create Task Plan
   - All documented with examples

---

## 💡 Talking Points

### What Makes This Special

**Automation:**
> "The watcher runs continuously, so files are processed within seconds of being dropped. No manual intervention needed."

**Intelligence:**
> "Priority detection is built-in. Files with 'urgent' or 'critical' in the name are automatically flagged as P0."

**Safety:**
> "The Company Handbook defines clear approval rules. Claude won't delete files or make system changes without approval."

**Extensibility:**
> "The Agent Skills are modular. I can add new skills for email processing, calendar integration, or custom workflows."

---

## 🚀 Advanced Demo (If Time Permits)

### Show Priority Handling
```bash
echo "Low priority backlog item" > Drop/low_priority_task.txt
echo "CRITICAL SECURITY ISSUE" > Drop/critical_security_alert.txt
```

Show how different priorities are assigned.

### Show Logging
```bash
cat Logs/watcher_log_$(date +%Y%m%d).md
```

Demonstrate audit trail.

### Show Plan Creation
```bash
claude "Create an action plan for implementing a new feature based on the Company Handbook approval rules"
```

Show how Claude creates structured plans.

---

## 🎤 Closing Statement

> "This Bronze Tier implementation demonstrates a fully functional AI Employee system. The file watcher provides automated monitoring, Claude Code provides intelligent processing, and the Agent Skills provide structured guidance. The system is ready for real-world testing and can be extended to Silver and Gold tiers with email integration, advanced automation, and multi-agent coordination."

---

## 📊 Metrics to Highlight

- **Setup Time:** ~4 hours (under Bronze tier estimate)
- **Files Created:** 10+ (vault structure, skills, docs)
- **Lines of Code:** ~400 (watcher script)
- **Automation Level:** Fully automated file detection and task creation
- **Claude Integration:** Bidirectional (read and write)

---

## 🐛 Backup Plans

### If Watcher Fails
- Show the code and explain how it works
- Manually create a task file to demonstrate format
- Show logs from previous successful runs

### If Claude Code Has Issues
- Show the vault structure and files
- Explain how Claude would process tasks
- Demonstrate reading files manually

### If Demo Environment Issues
- Have screenshots prepared
- Have pre-recorded video backup
- Walk through code and documentation

---

## ✅ Pre-Demo Checklist

- [ ] Python dependencies installed
- [ ] Watcher script tested
- [ ] Drop folder empty and ready
- [ ] Dashboard shows clean state
- [ ] Test files prepared
- [ ] Claude Code working
- [ ] All paths correct
- [ ] Backup demo materials ready

---

**Good luck with the demo! 🚀**
