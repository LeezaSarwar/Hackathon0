# 🎬 Demo Video Commands - Copy Paste Ready

**Duration:** 7-8 minutes
**Terminals:** 2 (side by side)

---

## 🎯 TERMINAL 1 (Left Side) - Watcher

### Command 1: Navigate
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
```

### Command 2: Start Watcher (Keep Running!)
```powershell
python file_watcher.py
```

**Expected Output:**
```
============================================================
AI Employee File Watcher
============================================================
Monitoring: D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault\Drop
Press Ctrl+C to stop
```

**⚠️ IMPORTANT: Don't close this! Keep it running!**

---

## 🎯 TERMINAL 2 (Right Side) - Commands

### Part 1: Introduction (30 sec)

**Say:** "Hello! Main [Name] hoon. Yeh mera Bronze Tier AI Employee hai."

---

### Part 2: Show System (1.5 min)

**Command 1: Navigate**
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
```

**Command 2: Show Folders**
```powershell
ls
```
**Say:** "Yeh mera vault structure hai."

**Command 3: Show Dashboard**
```powershell
cat Dashboard.md
```
**Say:** "Dashboard mein real-time status hai."

**Command 4: Show Folders Detail**
```powershell
ls Inbox, Needs_Action, Done, Skills
```
**Say:** "Organized folders hain."

---

### Part 3: LIVE DEMO (2.5 min) ⭐ MOST IMPORTANT

**Command 5: Create NEW File**
```powershell
echo "URGENT: Customer complaint about delayed shipment. Need immediate response." > Drop/live_demo_test.txt
```

**Say:** "Ab main ek URGENT file drop karta hoon."

**⏸️ PAUSE - Switch to Terminal 1**

**Show Watcher Output:**
```
[2026-02-12 XX:XX:XX] [NEW] New file detected: live_demo_test.txt
[2026-02-12 XX:XX:XX] [OK] Created task file: task_live_demo_test_*.md
[2026-02-12 XX:XX:XX] [OK] Task created successfully
```

**Say:** "Dekho! 2 seconds mein file detect ho gayi aur task ban gaya!"

**⏸️ PAUSE - Switch back to Terminal 2**

**Command 6: Show Created Task**
```powershell
ls Needs_Action | Sort-Object LastWriteTime -Descending | Select-Object -First 1
```
**Say:** "Yeh automatically created task file hai."

**Command 7: Show Task Content**
```powershell
cat Needs_Action/task_live_demo_test_*.md
```
**Say:** "Dekho - Priority P0 hai kyunki URGENT word tha. Sab automatic!"

**Command 8: Show Log**
```powershell
Get-Content Logs/watcher_log_20260212.md -Tail 5
```
**Say:** "Aur sab log bhi ho gaya."

---

### Part 4: Claude Integration (2 min)

**Command 9: Claude - Read Dashboard**
```powershell
claude "Read Dashboard.md and tell me what tasks are pending"
```
**Say:** "Ab Claude se puchte hain kya pending hai."
**⏸️ Wait for Claude response**
**Say:** "Claude ne Dashboard read kar liya."

**Command 10: Claude - Analyze Task**
```powershell
claude "Read the live demo test task in Needs_Action and tell me what the file contains"
```
**Say:** "Ab task file analyze karte hain."
**⏸️ Wait for Claude response**
**Say:** "Claude ne content samajh liya."

**Command 11: Claude - Create Report**
```powershell
claude "Create a detailed analysis report for the live demo test task and save it in the Done folder"
```
**Say:** "Ab detailed report banate hain."
**⏸️ Wait for Claude to work**

**Command 12: Show Report**
```powershell
ls Done | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Get-Content Done/live_demo_test_report_*.md -Head 30
```
**Say:** "Dekho, Claude ne complete report bana di. Yeh hai bidirectional integration."

---

### Part 5: Agent Skills (1 min)

**Command 13: Show Skills**
```powershell
ls Skills
```
**Say:** "Maine 3 Agent Skills banaye hain."

**Command 14: Show One Skill**
```powershell
Get-Content Skills/process_inbox_skill.md -Head 30
```
**Say:** "Har skill mein detailed instructions hain."

---

### Part 6: Conclusion (30 sec)

**Say:**
```
"To summarize:
✓ Obsidian vault with Dashboard
✓ Working file watcher - automatic detection
✓ Claude Code integration
✓ Complete folder structure
✓ Teen Agent Skills

Sab Bronze Tier requirements complete hain.
Thank you!"
```

---

## 📋 Quick Reference Card

### Terminal 1 (Watcher):
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
python file_watcher.py
# Keep running!
```

### Terminal 2 (Commands):
```powershell
# Navigate
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"

# Show structure
ls
cat Dashboard.md
ls Inbox, Needs_Action, Done, Skills

# CREATE NEW FILE (LIVE DEMO)
echo "URGENT: Customer complaint about delayed shipment. Need immediate response." > Drop/live_demo_test.txt

# Show results
ls Needs_Action | Sort-Object LastWriteTime -Descending | Select-Object -First 1
cat Needs_Action/task_live_demo_test_*.md
Get-Content Logs/watcher_log_20260212.md -Tail 5

# Claude commands
claude "Read Dashboard.md and tell me what tasks are pending"
claude "Read the live demo test task in Needs_Action and tell me what the file contains"
claude "Create a detailed analysis report for the live demo test task and save it in the Done folder"

# Show report
ls Done | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Get-Content Done/live_demo_test_report_*.md -Head 30

# Show skills
ls Skills
Get-Content Skills/process_inbox_skill.md -Head 30
```

---

## ⚠️ IMPORTANT POINTS

### ✅ DO THIS:
1. Terminal 1 mein watcher START karo aur RUNNING rakho
2. Terminal 2 mein NAYA file banao (live_demo_test.txt)
3. Terminal 1 mein detection message dikho
4. Terminal 2 mein created task dikho
5. Claude ke 3 commands run karo
6. Skills dikho

### ❌ DON'T DO THIS:
1. Existing task files mat dikhao
2. Watcher ko band mat karo jaldi
3. Commands skip mat karo
4. Bahut fast mat bolo

---

## 🎬 Recording Steps

### Before Recording:
1. Open 2 PowerShell windows
2. Increase font size (Ctrl + Mouse Wheel)
3. Position side by side
4. Clean desktop

### Start Recording:
1. Press `Win+G`
2. Click Record button (red circle)
3. Start speaking and running commands

### Stop Recording:
1. Press `Win+Alt+R`
2. Video saved in: `C:\Users\[YourName]\Videos\Captures\`

---

## ⏱️ Timing

- Introduction: 30 sec
- System Overview: 1.5 min
- **Live Demo: 2.5 min** ⭐ (Most important)
- Claude Integration: 2 min
- Agent Skills: 1 min
- Conclusion: 30 sec

**Total:** 7-8 minutes

---

## 🎯 Most Important Part

**This 1-minute sequence is KEY:**

```
Terminal 1: python file_watcher.py (running)
           ↓
Terminal 2: echo "URGENT: Test" > Drop/live_demo_test.txt
           ↓
Terminal 1: [Shows detection message] ⭐
           ↓
Terminal 2: cat Needs_Action/task_live_demo_test_*.md
```

**Yeh dikhata hai ki system LIVE kaam kar raha hai!**

---

## 💡 Pro Tips

1. **Speak Slowly** - Jaldi mat bolo
2. **Pause Between Commands** - Har command ke baad 2-3 seconds wait
3. **Show Terminal 1** - Watcher ka response zaroor dikho
4. **Don't Worry About Mistakes** - Agar galti ho, continue karo
5. **Be Confident** - Aap ne achha kaam kiya hai!

---

## 🚀 Ready to Record?

**Steps:**
1. Open this file on one screen
2. Open 2 terminals on other screen
3. Press Win+G
4. Follow commands above
5. Press Win+Alt+R when done

**Video will be in:** Videos/Captures folder

---

**Good luck! Aap kar sakte ho!** 🎬
