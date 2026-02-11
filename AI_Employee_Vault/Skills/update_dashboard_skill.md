# Agent Skill: Update Dashboard

**Skill ID:** `update_dashboard`
**Version:** 1.0
**Category:** Reporting & Status
**Priority:** Medium

---

## 📋 Description

This skill updates the Dashboard.md file with current task status, system metrics, and recent activity. It provides a real-time view of the AI Employee's work and system health.

---

## 🎯 Purpose

- Maintain accurate task counts and status
- Display recent activity and completions
- Show system health metrics
- Provide quick overview for user
- Track daily progress

---

## 📥 Input Requirements

### Required Inputs
- Access to all vault folders (Inbox, Needs_Action, Done, etc.)
- Current timestamp
- Read access to task files

### Optional Inputs
- Specific update type (full refresh vs. incremental)
- Custom message to add to activity log
- Force refresh flag

---

## 📤 Output Format

### Updated Dashboard Structure
```markdown
# AI Employee Dashboard

**Last Updated:** [timestamp]

---

## 📋 Pending Tasks

[List of tasks in Needs_Action with priority]

---

## ✅ Completed Today

[List of tasks completed today]

---

## 🔧 System Status

- Vault Status: [Active/Inactive]
- Watcher Status: [Running/Stopped]
- Last Sync: [timestamp]
- Tasks in Inbox: [count]
- Tasks Needing Action: [count]
- Tasks Completed: [count]

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| Total Tasks Today | [count] |
| Pending | [count] |
| In Progress | [count] |
| Completed | [count] |

---

## 🔔 Recent Activity

[Last 10 activities with timestamps]
```

---

## 🔧 Update Logic

### Step 1: Gather Metrics
```python
# Count files in each folder
inbox_count = count_files("/Inbox")
needs_action_count = count_files("/Needs_Action")
done_today_count = count_files_today("/Done")

# Check watcher status
watcher_status = check_watcher_running()

# Get recent activity from logs
recent_activity = get_recent_logs(limit=10)
```

### Step 2: Parse Task Files
```python
# Read all task files in Needs_Action
pending_tasks = []
for task_file in list_files("/Needs_Action"):
    task_data = parse_task_file(task_file)
    pending_tasks.append({
        'name': task_data['name'],
        'priority': task_data['priority'],
        'status': task_data['status'],
        'created': task_data['created']
    })

# Sort by priority
pending_tasks.sort(key=lambda x: x['priority'])
```

### Step 3: Format Dashboard Content
```python
# Build pending tasks section
pending_section = format_pending_tasks(pending_tasks)

# Build completed section
completed_section = format_completed_tasks(done_today_count)

# Build system status
system_status = format_system_status(metrics)

# Build activity log
activity_section = format_recent_activity(recent_activity)
```

### Step 4: Write Dashboard
```python
# Combine all sections
dashboard_content = build_dashboard(
    pending_section,
    completed_section,
    system_status,
    activity_section
)

# Write to Dashboard.md
write_file("Dashboard.md", dashboard_content)
```

---

## 💡 Example Usage

### Example 1: Full Dashboard Refresh

**Trigger:** User requests status update

**Actions:**
1. Scan all folders for current counts
2. Read all task files in Needs_Action
3. Parse recent log entries
4. Check watcher process status
5. Generate complete dashboard
6. Write to Dashboard.md

**Result:**
```markdown
# AI Employee Dashboard

**Last Updated:** 2026-02-11 15:30:45

---

## 📋 Pending Tasks

### High Priority
- **[P1]** Process urgent_report.pdf (Created: 2026-02-11 14:20)
- **[P1]** Review code_changes.py (Created: 2026-02-11 15:10)

### Medium Priority
- **[P2]** Organize meeting_notes.txt (Created: 2026-02-11 13:45)

---

## ✅ Completed Today

- ✓ Processed customer_feedback.csv (15:25)
- ✓ Created summary for project_plan.md (14:50)
- ✓ Organized 5 files from Drop folder (13:30)

---

## 🔧 System Status

- **Vault Status:** Active
- **Watcher Status:** Running
- **Last Sync:** 2026-02-11 15:30
- **Tasks in Inbox:** 0
- **Tasks Needing Action:** 3
- **Tasks Completed:** 3

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| Total Tasks Today | 6 |
| Pending | 3 |
| In Progress | 0 |
| Completed | 3 |

---

## 🔔 Recent Activity

- [15:25] ✓ Completed task: customer_feedback.csv
- [15:10] → New task detected: code_changes.py
- [14:50] ✓ Completed task: project_plan.md
- [14:20] → New task detected: urgent_report.pdf
- [13:45] → New task detected: meeting_notes.txt
```

### Example 2: Incremental Update (Add Activity)

**Trigger:** Task completed, need to log activity

**Actions:**
1. Read current Dashboard.md
2. Add new activity to Recent Activity section
3. Update completion count
4. Update timestamp
5. Write back to Dashboard.md

**Result:** Dashboard updated with new activity entry, counts incremented

---

## 🚨 Error Handling

### Dashboard File Missing
```
- Create new dashboard from template
- Log warning in /Logs
- Continue with update
```

### Folder Access Error
```
- Log error with folder name
- Use cached counts if available
- Mark affected metrics as "Unknown"
- Continue with partial update
```

### Parse Error in Task File
```
- Log error with task filename
- Skip problematic task
- Continue processing other tasks
- Add error note to dashboard
```

---

## 📊 Success Criteria

- ✅ Dashboard.md updated successfully
- ✅ All metrics accurate and current
- ✅ Timestamp reflects update time
- ✅ Recent activity shows last 10 entries
- ✅ Task counts match folder contents
- ✅ No data loss from previous version

---

## 🔄 Integration Points

### Reads From:
- `/Inbox/*.md` - Inbox tasks
- `/Needs_Action/*.md` - Pending tasks
- `/Done/*.md` - Completed tasks
- `/Logs/*.md` - Activity logs
- System process list (for watcher status)

### Writes To:
- `Dashboard.md` - Main dashboard file

### Triggers:
- After processing tasks (via process_inbox_skill)
- After watcher creates new task
- Manual user request
- Scheduled refresh (every 15 minutes)

---

## 📝 Notes

- Keep dashboard concise and scannable
- Limit recent activity to 10 entries
- Use emoji for visual clarity
- Update timestamp on every change
- Cache metrics to reduce file I/O
- Validate all counts before writing

---

## 🎨 Formatting Guidelines

### Priority Display
- P0: 🔴 Critical
- P1: 🟠 High
- P2: 🟡 Medium
- P3: 🟢 Low

### Status Icons
- ✓ Completed
- → In Progress
- ⏸ Paused
- ✗ Failed
- ⏳ Waiting

### Time Format
- Timestamps: `YYYY-MM-DD HH:MM:SS`
- Relative times: "2 hours ago" for recent items
- Dates: `YYYY-MM-DD` for older items

---

**Last Updated:** 2026-02-11
