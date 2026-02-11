# 🎬 Demo Video Script - Bronze Tier AI Employee

**Duration:** 7-8 minutes
**Language:** English (ya jo comfortable ho)
**Recording Tool:** OBS Studio / Windows Game Bar (Win+G)

---

## 🎯 Video Structure

### Part 1: Introduction (0:00 - 0:30)
### Part 2: System Overview (0:30 - 2:00)
### Part 3: Live Watcher Demo (2:00 - 4:30)
### Part 4: Claude Integration (4:30 - 6:30)
### Part 5: Agent Skills (6:30 - 7:30)
### Part 6: Conclusion (7:30 - 8:00)

---

## 📝 Detailed Script with Screen Actions

### Part 1: Introduction (30 seconds)

**Screen:** Show yourself (optional) or desktop

**Say:**
```
"Hello! I'm [Your Name], and this is my Bronze Tier submission
for the Personal AI Employee Hackathon.

I've built a fully automated AI Employee system that:
- Monitors files 24/7
- Creates tasks automatically
- Integrates with Claude Code
- Uses Agent Skills for intelligent behavior

Let me show you how it works."
```

**Action:** None, just introduction

---

### Part 2: System Overview (1.5 minutes)

**Screen 1: Show Folder Structure**

**Action:**
```bash
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
ls -la
```

**Say:**
```
"Here's my Obsidian vault structure. You can see:
- Dashboard.md - for real-time status
- Company_Handbook.md - with AI behavior rules
- file_watcher.py - the monitoring script
- And organized folders for different stages"
```

**Screen 2: Show Dashboard**

**Action:**
```bash
cat Dashboard.md
```

**Say:**
```
"The Dashboard shows:
- Pending tasks with priorities
- Completed tasks today
- System status
- Recent activity
- Quick statistics

Everything updates in real-time."
```

**Screen 3: Show Company Handbook (briefly)**

**Action:**
```bash
head -n 30 Company_Handbook.md
```

**Say:**
```
"The Company Handbook defines rules like:
- Priority levels (P0 to P3)
- What actions need approval
- How to handle different file types
- Security and safety guidelines"
```

**Screen 4: Show Folder Structure**

**Action:**
```bash
ls -la Inbox/ Needs_Action/ Done/ Skills/
```

**Say:**
```
"The folder structure includes:
- Inbox for initial files
- Needs_Action for pending tasks
- Done for completed work
- Skills for Agent definitions
- Plus Logs, Plans, and Drop folders"
```

---

### Part 3: Live Watcher Demo (2.5 minutes)

**Screen 1: Start Watcher**

**Action:**
```bash
# Open terminal
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
python file_watcher.py
```

**Say:**
```
"Now let me start the file watcher. This script runs continuously
and monitors the Drop folder for new files."

[Wait for watcher to start]

"You can see it's now running and waiting for files."
```

**Screen 2: Open Second Terminal**

**Action:**
```bash
# Open new terminal window
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
```

**Say:**
```
"In a second terminal, I'll drop a test file to demonstrate
the automated detection."
```

**Screen 3: Create Test File**

**Action:**
```bash
echo "URGENT: Customer complaint about delayed shipment. Need immediate response." > Drop/urgent_customer_issue.txt
```

**Say:**
```
"I'm creating a file with 'URGENT' in the name to test
priority detection."
```

**Screen 4: Show Watcher Response**

**Action:**
- Switch to watcher terminal
- Show the log output

**Say:**
```
"Look at the watcher console - within 2 seconds:
- It detected the new file
- Created a task file
- Logged the activity

This happens automatically, no manual intervention needed."
```

**Screen 5: Show Created Task**

**Action:**
```bash
# In second terminal
ls -lt Needs_Action/ | head -n 3
cat Needs_Action/task_urgent_customer_issue_*.md
```

**Say:**
```
"Here's the automatically created task file. Notice:
- Priority is P0 - Critical (because of 'urgent' keyword)
- File metadata is extracted (size, timestamps)
- A processing checklist is included
- Suggested actions are listed

All of this was generated automatically by the watcher."
```

**Screen 6: Show Activity Log**

**Action:**
```bash
tail -n 10 Logs/watcher_log_$(date +%Y%m%d).md
```

**Say:**
```
"And everything is logged for audit purposes.
You can see the complete activity trail."
```

---

### Part 4: Claude Integration (2 minutes)

**Screen 1: Read Dashboard with Claude**

**Action:**
```bash
claude "Read Dashboard.md and tell me what tasks are pending"
```

**Say:**
```
"Now let's use Claude Code to interact with the vault.
I'm asking Claude to read the Dashboard and show pending tasks."

[Wait for response]

"Claude successfully read the Dashboard and identified
the urgent task we just created."
```

**Screen 2: Analyze Task with Claude**

**Action:**
```bash
claude "Read the urgent customer issue task in Needs_Action and tell me what the file contains"
```

**Say:**
```
"Now I'm asking Claude to analyze the actual task file
and tell me what's in it."

[Wait for response]

"Claude read the task file, understood it's about a customer
complaint, and can see it needs immediate attention."
```

**Screen 3: Create Report with Claude**

**Action:**
```bash
claude "Create a detailed analysis report for the urgent customer issue task and save it in the Done folder"
```

**Say:**
```
"Now I'm asking Claude to create a comprehensive analysis report."

[Wait for Claude to work]

"Claude is processing the task, analyzing the content,
and generating a detailed report."
```

**Screen 4: Show Generated Report**

**Action:**
```bash
ls -lt Done/ | head -n 3
cat Done/urgent_customer_issue_report_*.md | head -n 50
```

**Say:**
```
"Here's the report Claude created. It includes:
- File analysis
- Content summary
- Recommended actions
- Security check
- Next steps

This demonstrates bidirectional integration - Claude can
both read from and write to the vault."
```

---

### Part 5: Agent Skills (1 minute)

**Screen 1: Show Skills Folder**

**Action:**
```bash
ls -la Skills/
```

**Say:**
```
"I've implemented all AI functionality as Agent Skills,
as required by Bronze Tier. I have 3 skills:"
```

**Screen 2: Show Process Inbox Skill**

**Action:**
```bash
head -n 40 Skills/process_inbox_skill.md
```

**Say:**
```
"The Process Inbox skill defines how to:
- Analyze tasks
- Determine required actions
- Check approval requirements
- Execute safe operations
- Handle errors

Each skill has detailed instructions, examples, and
integration points."
```

**Screen 3: Show Other Skills (briefly)**

**Action:**
```bash
ls -lh Skills/*.md
```

**Say:**
```
"The other two skills are:
- Update Dashboard - for maintaining real-time status
- Create Task Plan - for planning complex tasks

All three skills guide Claude's behavior and ensure
consistent, safe operations."
```

---

### Part 6: Conclusion (30 seconds)

**Screen:** Show Dashboard or folder structure

**Say:**
```
"To summarize, this Bronze Tier implementation includes:

✓ Obsidian vault with Dashboard and Handbook
✓ Working file watcher with automatic detection
✓ Claude Code integration - read and write
✓ Complete folder structure
✓ Three Agent Skills

All Bronze Tier requirements are met and tested.

The system is:
- Fully automated
- Production-ready
- Extensible to Silver and Gold tiers

Thank you for watching!"
```

**Action:** Show final screen with your name and GitHub link

---

## 🎥 Recording Setup

### Before Recording:

**1. Clean Your Desktop**
```bash
# Close unnecessary windows
# Clear terminal history
# Prepare all commands in a text file
```

**2. Test Your Setup**
```bash
# Test watcher works
cd AI_Employee_Vault
python file_watcher.py
# Ctrl+C to stop

# Test Claude works
claude "test"
```

**3. Prepare Test Files**
```bash
# Have commands ready to copy-paste
# Test file creation command ready
```

**4. Set Terminal Font Size**
- Increase font size for visibility
- Use clear color scheme
- Full screen terminal

---

## 🎬 Recording Tools

### Option 1: OBS Studio (Recommended)

**Download:** https://obsproject.com/

**Setup:**
1. Install OBS Studio
2. Add "Display Capture" source
3. Settings → Output → Recording Quality: High
4. Settings → Video → Base Resolution: 1920x1080
5. Click "Start Recording"
6. Do your demo
7. Click "Stop Recording"

**Output:** Video file in Videos folder

---

### Option 2: Windows Game Bar (Simple)

**Setup:**
1. Press Win+G
2. Click Record button (or Win+Alt+R)
3. Do your demo
4. Press Win+Alt+R to stop

**Output:** Video in Videos/Captures folder

---

### Option 3: Screen Recording Software

- **Camtasia** (paid, professional)
- **Loom** (free, easy)
- **ShareX** (free, open source)

---

## 📋 Recording Checklist

**Before Recording:**
- [ ] Desktop cleaned
- [ ] Terminal font size increased
- [ ] All commands tested
- [ ] Watcher script ready
- [ ] Test file command ready
- [ ] Claude Code working
- [ ] Recording software tested
- [ ] Microphone tested (if using voice)

**During Recording:**
- [ ] Speak clearly and slowly
- [ ] Pause between sections
- [ ] Show each step clearly
- [ ] Don't rush
- [ ] If you make a mistake, pause and restart that section

**After Recording:**
- [ ] Watch the video
- [ ] Check audio quality
- [ ] Verify all steps are visible
- [ ] Edit if needed (optional)
- [ ] Export in good quality (1080p)

---

## 🎤 Voice Recording Tips

**If Recording Voice:**
- Use a decent microphone (or headset)
- Record in a quiet room
- Speak clearly and at moderate pace
- Don't worry about perfect English
- Enthusiasm is more important than perfection

**If Not Recording Voice:**
- Add text overlays explaining each step
- Use captions/subtitles
- Background music (optional, keep it subtle)

---

## 📤 Upload Options

### Option 1: YouTube (Recommended)

**Steps:**
1. Go to youtube.com
2. Click "Create" → "Upload Video"
3. Select your video file
4. Title: "Bronze Tier AI Employee - Hackathon 0"
5. Description: Brief description of your project
6. Visibility: **Unlisted** (not public, but accessible via link)
7. Click "Publish"
8. Copy the link

**Pros:** Easy, reliable, judges can watch easily

---

### Option 2: Google Drive

**Steps:**
1. Go to drive.google.com
2. Click "New" → "File Upload"
3. Select your video
4. Right-click → "Share"
5. Change to "Anyone with the link can view"
6. Copy the link

**Pros:** Simple, no YouTube account needed

---

### Option 3: Vimeo

**Steps:**
1. Go to vimeo.com
2. Upload video
3. Set privacy to "Unlisted"
4. Copy link

**Pros:** Professional, good quality

---

## 🎯 What Judges Want to See

**Must Show:**
1. ✅ File watcher detecting files automatically
2. ✅ Task creation with priority detection
3. ✅ Claude Code reading from vault
4. ✅ Claude Code writing to vault
5. ✅ Agent Skills documentation
6. ✅ Complete folder structure

**Nice to Have:**
- Your face (builds connection)
- Enthusiasm and confidence
- Clear explanations
- Professional presentation

**Don't Worry About:**
- Perfect video editing
- Hollywood production quality
- Mistakes (you can edit or re-record)
- Accent or language

---

## ⏱️ Time Management

**Total: 7-8 minutes**

- Introduction: 30 sec
- System Overview: 1.5 min
- Watcher Demo: 2.5 min
- Claude Integration: 2 min
- Agent Skills: 1 min
- Conclusion: 30 sec

**If Running Long:**
- Skip showing full file contents
- Show less of the logs
- Summarize instead of reading

**If Running Short:**
- Show more examples
- Explain features in more detail
- Show additional documentation

---

## 🚀 Quick Start Recording

**Fastest Way to Record (15 minutes):**

1. **Prepare** (5 min)
   - Clean desktop
   - Open terminals
   - Test commands

2. **Record** (8 min)
   - Press Win+G to start
   - Follow script above
   - Don't worry about perfection

3. **Upload** (2 min)
   - Upload to YouTube (unlisted)
   - Copy link
   - Done!

---

## 💡 Pro Tips

**Tip 1: Practice First**
- Do a dry run without recording
- Time yourself
- Adjust script if needed

**Tip 2: Use Two Monitors**
- Script on one screen
- Demo on other screen
- Or print the script

**Tip 3: Edit Mistakes**
- If you make a mistake, pause
- Say "Let me try that again"
- Continue from that point
- Edit out mistakes later (optional)

**Tip 4: Show Enthusiasm**
- Smile (if showing face)
- Use positive language
- Show you're proud of your work

**Tip 5: Keep It Simple**
- Don't over-explain
- Show, don't just tell
- Let the system speak for itself

---

## 📝 Sample Opening Lines

**Option 1 (Confident):**
```
"Hi! I'm [Name] and I've built a fully automated AI Employee
that monitors files, creates tasks, and integrates with Claude Code.
Let me show you how it works."
```

**Option 2 (Friendly):**
```
"Hello everyone! This is my Bronze Tier submission for the
AI Employee Hackathon. I'm excited to show you what I've built."
```

**Option 3 (Direct):**
```
"This is my Bronze Tier AI Employee system. It includes automated
file monitoring, Claude Code integration, and Agent Skills.
Here's a live demonstration."
```

---

## 🎬 Final Checklist

**Before Submitting Video:**
- [ ] Video is 5-10 minutes long
- [ ] All Bronze Tier features shown
- [ ] Audio is clear (if using voice)
- [ ] Video quality is good (720p minimum)
- [ ] Uploaded to YouTube/Drive
- [ ] Link is accessible (test in incognito)
- [ ] Link copied for submission form

---

## 🚀 Ready to Record?

**Your video should show:**
1. ✅ System overview
2. ✅ Live file detection
3. ✅ Automatic task creation
4. ✅ Claude integration
5. ✅ Agent Skills
6. ✅ Professional presentation

**Time needed:** 20-30 minutes total
- Preparation: 5 min
- Recording: 10 min
- Upload: 5 min
- Buffer: 10 min

---

**Good luck with your demo video!** 🎬

Remember: Judges want to see that your system works, not Hollywood production quality. Show your work with confidence!
