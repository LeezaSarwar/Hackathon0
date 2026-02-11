# Agent Skill: Process Inbox

**Skill ID:** `process_inbox`
**Version:** 1.0
**Category:** Task Processing
**Priority:** High

---

## 📋 Description

This skill processes tasks from the `/Needs_Action` folder, analyzes their content, determines appropriate actions, and updates the task status. It's the core workflow skill for handling incoming work items.

---

## 🎯 Purpose

- Review pending tasks in the Needs_Action folder
- Analyze file contents and determine required actions
- Execute safe, approved actions automatically
- Flag items requiring user approval
- Update task status and move completed items

---

## 📥 Input Requirements

### Required Inputs
- Access to `/Needs_Action` folder
- Access to source files referenced in tasks
- Read access to `Company_Handbook.md` for approval rules

### Optional Inputs
- Specific task file to process (if not provided, processes all pending)
- Priority filter (process only P0/P1 tasks)

---

## 📤 Output Format

### Task Analysis Report
```markdown
## Task Processing Report
**Task:** [task_name]
**Processed:** [timestamp]
**Status:** [Completed/Needs Approval/Blocked]

### Analysis
- File Type: [type]
- Content Summary: [brief summary]
- Recommended Action: [action]

### Actions Taken
- [x] Action 1
- [x] Action 2
- [ ] Action 3 (requires approval)

### Next Steps
[What needs to happen next]
```

---

## 🔧 Processing Logic

### Step 1: Scan Needs_Action Folder
```
1. List all .md files in /Needs_Action
2. Sort by priority (P0 > P1 > P2 > P3)
3. Filter by status (Pending only)
```

### Step 2: Analyze Each Task
```
1. Read task file
2. Extract file location from task
3. Read source file (if exists)
4. Determine file type and content
5. Assess required actions
```

### Step 3: Determine Action Path
```
IF action requires approval (per handbook):
    - Create approval request in /Plans
    - Update task status to "Awaiting Approval"
    - Notify user via Dashboard
ELSE:
    - Execute safe actions
    - Log all actions in /Logs
    - Update task status
```

### Step 4: Execute Actions
```
Safe actions (no approval needed):
- Reading and analyzing files
- Creating summaries
- Organizing files
- Updating dashboard
- Creating plans

Requires approval:
- Deleting files
- Modifying code
- External communications
- System changes
```

### Step 5: Update Status
```
1. Update task file with results
2. Move to /Done if completed
3. Update Dashboard.md
4. Log activity in /Logs
```

---

## 💡 Example Usage

### Example 1: Processing a Text Document

**Input Task:** `task_meeting_notes_20260211.md`

**Source File:** `meeting_notes.txt` (in Drop folder)

**Processing Steps:**
1. Read task file → Extract file location
2. Read meeting_notes.txt → Identify as meeting notes
3. Analyze content → Extract action items
4. Create summary → No approval needed
5. Update task → Mark as completed
6. Move to Done → Archive task

**Output:**
- Summary created in `/Done/meeting_notes_summary_20260211.md`
- Dashboard updated with completion
- Task moved to `/Done`

### Example 2: Processing Code File (Requires Approval)

**Input Task:** `task_bugfix_urgent_20260211.md`

**Source File:** `app.py` (in Drop folder)

**Processing Steps:**
1. Read task file → Extract file location
2. Read app.py → Identify as Python code
3. Analyze content → Bug fix needed
4. Check handbook → Code modification requires approval
5. Create plan → Generate fix proposal in `/Plans`
6. Update task → Status = "Awaiting Approval"
7. Update dashboard → Flag for user review

**Output:**
- Plan created: `/Plans/bugfix_proposal_20260211.md`
- Task status: "Awaiting Approval"
- Dashboard notification added

---

## 🚨 Error Handling

### File Not Found
```
- Log error in /Logs
- Update task with error status
- Move to /Needs_Action with error flag
- Notify via Dashboard
```

### Permission Denied
```
- Log permission error
- Create approval request
- Update task status
- Notify user
```

### Processing Timeout
```
- Log timeout
- Save partial results
- Mark task as "In Progress"
- Schedule retry
```

---

## 📊 Success Criteria

- ✅ All pending tasks reviewed
- ✅ Actions determined for each task
- ✅ Safe actions executed automatically
- ✅ Approval requests created for restricted actions
- ✅ Dashboard updated with current status
- ✅ All activities logged

---

## 🔄 Integration Points

### Reads From:
- `/Needs_Action/*.md` - Task files
- `/Drop/*` - Source files
- `Company_Handbook.md` - Approval rules

### Writes To:
- `/Done/*.md` - Completed tasks
- `/Plans/*.md` - Approval requests
- `/Logs/*.md` - Activity logs
- `Dashboard.md` - Status updates

### Triggers:
- Manual invocation by user
- Scheduled execution (every 15 minutes)
- After watcher creates new task

---

## 📝 Notes

- Always check Company_Handbook.md before taking actions
- Log every action for audit trail
- When in doubt, request approval
- Prioritize P0/P1 tasks first
- Keep processing time under 5 minutes per task

---

**Last Updated:** 2026-02-11
