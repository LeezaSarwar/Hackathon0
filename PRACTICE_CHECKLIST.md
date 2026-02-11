# 🎬 Demo Practice Checklist

**Time:** 10 minutes
**Goal:** Test all commands before recording

---

## ✅ Pre-Practice Checklist

- [x] Location verified: AI_Employee_Vault
- [x] Dashboard.md exists
- [x] file_watcher.py exists
- [x] Skills folder ready
- [ ] Terminal font size increased
- [ ] Desktop cleaned
- [ ] Commands tested

---

## 🎯 Practice Commands (Copy-Paste Ready)

### Command 1: Show Folder Structure
```bash
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
ls -la
```

### Command 2: Show Dashboard
```bash
cat Dashboard.md
```

### Command 3: Show Company Handbook (first 30 lines)
```bash
head -n 30 Company_Handbook.md
```

### Command 4: Show Folders
```bash
ls -la Inbox/ Needs_Action/ Done/ Skills/
```

### Command 5: Start Watcher (Terminal 1)
```bash
python file_watcher.py
```

### Command 6: Create Test File (Terminal 2)
```bash
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
echo "URGENT: Customer complaint about delayed shipment. Need immediate response." > Drop/urgent_demo_test.txt
```

### Command 7: Check Task Created
```bash
ls -lt Needs_Action/ | head -n 3
```

### Command 8: Show Task File
```bash
cat Needs_Action/task_urgent_demo_test_*.md
```

### Command 9: Show Activity Log
```bash
tail -n 10 Logs/watcher_log_$(date +%Y%m%d).md
```

### Command 10: Claude - Read Dashboard
```bash
claude "Read Dashboard.md and tell me what tasks are pending"
```

### Command 11: Claude - Analyze Task
```bash
claude "Read the urgent demo test task in Needs_Action and tell me what the file contains"
```

### Command 12: Show Skills
```bash
ls -la Skills/
head -n 40 Skills/process_inbox_skill.md
```

---

## 🎬 Practice Run Steps

### Step 1: Prepare Desktop (2 min)
- [ ] Close unnecessary windows
- [ ] Open 2 terminal windows
- [ ] Increase terminal font size
- [ ] Position windows side by side

### Step 2: Test Commands (5 min)
- [ ] Run Command 1-4 (show structure)
- [ ] Run Command 5 (start watcher in Terminal 1)
- [ ] Run Command 6 (create test file in Terminal 2)
- [ ] Verify watcher detected file
- [ ] Run Command 7-9 (show results)
- [ ] Stop watcher (Ctrl+C)

### Step 3: Test Claude (2 min)
- [ ] Run Command 10 (Claude reads dashboard)
- [ ] Run Command 11 (Claude analyzes task)
- [ ] Verify Claude responses work

### Step 4: Test Skills Display (1 min)
- [ ] Run Command 12 (show skills)
- [ ] Verify files display correctly

---

## ⏱️ Timing Check

**Target Times:**
- Introduction: 30 sec
- System Overview: 1.5 min
- Watcher Demo: 2.5 min
- Claude Integration: 2 min
- Agent Skills: 1 min
- Conclusion: 30 sec

**Total:** 7-8 minutes

---

## 🚨 Common Issues & Fixes

### Issue 1: Watcher doesn't start
**Fix:**
```bash
pip install -r requirements.txt
python file_watcher.py
```

### Issue 2: File not detected
**Fix:**
- Wait 2-3 seconds
- Check watcher is running
- Verify Drop folder path

### Issue 3: Claude command not found
**Fix:**
```bash
# Check Claude is installed
claude --version

# If not, install
npm install -g @anthropic/claude-code
```

### Issue 4: Task file not showing
**Fix:**
```bash
# Use wildcard to find it
ls Needs_Action/task_urgent_demo_test_*
```

---

## ✅ Practice Complete Checklist

After practice run:
- [ ] All commands work
- [ ] Watcher detects files
- [ ] Tasks are created
- [ ] Claude responds correctly
- [ ] Timing is good (under 10 min)
- [ ] Ready to record

---

**Next Step:** Record the actual demo video

**Time Needed:** 20 minutes for recording
