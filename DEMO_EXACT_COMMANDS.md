# 🎬 Demo Video - Exact Commands (Urdu/English)

**Duration:** 7-8 minutes
**Terminals Needed:** 2

---

## 📺 Part 1: Introduction (30 seconds)

**Screen:** Desktop ya apna face (optional)

**Bolo:**
```
"Hello! Main [Your Name] hoon. Yeh mera Bronze Tier AI Employee
submission hai. Main aapko live demonstration dikhata hoon."
```

**Action:** Kuch nahi, bas introduction

---

## 📺 Part 2: System Overview (1.5 minutes)

### Terminal 1 - Show Files

**Commands:**
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
ls
```

**Bolo:**
```
"Yeh mera Obsidian vault hai. Dekho:
- Dashboard.md - real-time status
- Company_Handbook.md - AI rules
- file_watcher.py - monitoring script
- Aur organized folders"
```

**Show Dashboard:**
```powershell
cat Dashboard.md
```

**Bolo:**
```
"Dashboard mein pending tasks, completed tasks, aur system status hai."
```

**Show Folders:**
```powershell
ls Inbox, Needs_Action, Done, Skills
```

**Bolo:**
```
"Folders hain: Inbox, Needs_Action, Done, aur Skills."
```

---

## 📺 Part 3: Live Watcher Demo (2.5 minutes) ⭐ IMPORTANT

### Terminal 1 - Start Watcher

**Command:**
```powershell
python file_watcher.py
```

**Bolo:**
```
"Ab main file watcher start karta hoon. Yeh Drop folder ko
continuously monitor karega."
```

**Expected Output:**
```
============================================================
AI Employee File Watcher
============================================================
Monitoring: D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault\Drop
Press Ctrl+C to stop
```

**Bolo:**
```
"Dekho, watcher ab running hai aur files ka wait kar raha hai."
```

---

### Terminal 2 - Create NEW File (LIVE)

**⚠️ IMPORTANT: Yeh naya file banao, existing nahi dikhao!**

**Command:**
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"

echo "URGENT: Customer complaint about delayed shipment. Need immediate response." > Drop/live_demo_test.txt
```

**Bolo:**
```
"Ab main ek URGENT file drop karta hoon Drop folder mein.
Dekho kya hota hai..."
```

---

### Terminal 1 - Show Watcher Response

**Switch to Terminal 1 (watcher terminal)**

**Expected Output:**
```
[2026-02-12 XX:XX:XX] [NEW] New file detected: live_demo_test.txt
[2026-02-12 XX:XX:XX] [OK] Created task file: task_live_demo_test_*.md
[2026-02-12 XX:XX:XX] [OK] Task created successfully
```

**Bolo:**
```
"Dekho! 2 seconds mein:
- File detect ho gayi
- Task file ban gayi
- Activity log ho gayi
Sab automatic!"
```

---

### Terminal 2 - Show Created Task

**Command:**
```powershell
# Show latest task
ls Needs_Action | Sort-Object LastWriteTime -Descending | Select-Object -First 1

# Show task content
cat Needs_Action/task_live_demo_test_*.md
```

**Bolo:**
```
"Yeh automatically created task file hai. Dekho:
- Priority: P0 - Critical (kyunki 'URGENT' word tha)
- File details: size, timestamps
- Processing checklist
- Suggested actions

Sab automatic generate hua!"
```

---

### Terminal 2 - Show Activity Log

**Command:**
```powershell
Get-Content Logs/watcher_log_20260212.md -Tail 5
```

**Bolo:**
```
"Aur sab kuch log bhi ho gaya audit ke liye."
```

---

## 📺 Part 4: Claude Integration (2 minutes)

### Terminal 2 - Use Claude

**Command 1:**
```powershell
claude "Read Dashboard.md and tell me what tasks are pending"
```

**Bolo:**
```
"Ab Claude Code se interact karte hain. Main puchta hoon
Dashboard mein kya pending hai."
```

**Wait for Claude response**

**Bolo:**
```
"Claude ne Dashboard read kar liya aur pending tasks bata diye."
```

---

**Command 2:**
```powershell
claude "Read the live demo test task in Needs_Action and tell me what the file contains"
```

**Bolo:**
```
"Ab main Claude se puchta hoon ki task file mein kya hai."
```

**Wait for Claude response**

**Bolo:**
```
"Claude ne task file read kar li aur content samajh liya."
```

---

**Command 3:**
```powershell
claude "Create a detailed analysis report for the live demo test task and save it in the Done folder"
```

**Bolo:**
```
"Ab main Claude se kehta hoon detailed report banao."
```

**Wait for Claude to work**

**Bolo:**
```
"Claude report bana raha hai..."
```

---

### Terminal 2 - Show Generated Report

**Command:**
```powershell
# Show latest report
ls Done | Sort-Object LastWriteTime -Descending | Select-Object -First 1

# Show report content (first 30 lines)
Get-Content Done/live_demo_test_report_*.md -Head 30
```

**Bolo:**
```
"Dekho, Claude ne complete report bana di:
- File analysis
- Content summary
- Recommendations
- Security check

Yeh hai bidirectional integration - Claude read aur write dono kar sakta hai."
```

---

## 📺 Part 5: Agent Skills (1 minute)

### Terminal 2 - Show Skills

**Command:**
```powershell
ls Skills
```

**Bolo:**
```
"Maine 3 Agent Skills banaye hain jo Claude ko guide karti hain."
```

**Command:**
```powershell
Get-Content Skills/process_inbox_skill.md -Head 30
```

**Bolo:**
```
"Process Inbox skill define karti hai:
- Tasks kaise analyze karein
- Actions kaise determine karein
- Approval kab chahiye
- Errors kaise handle karein

Har skill mein detailed instructions aur examples hain."
```

---

## 📺 Part 6: Conclusion (30 seconds)

**Screen:** Dashboard ya folder structure

**Bolo:**
```
"To summarize, is Bronze Tier implementation mein hai:

✓ Obsidian vault with Dashboard aur Handbook
✓ Working file watcher - automatic detection
✓ Claude Code integration - read aur write
✓ Complete folder structure
✓ Teen Agent Skills

Sab Bronze Tier requirements complete hain aur tested hain.

System fully automated hai, production-ready hai, aur
Silver aur Gold tiers tak extend ho sakta hai.

Thank you!"
```

---

## 🎯 KEY POINTS - Zaroor Dikhao

### ✅ MUST SHOW (Important):

1. **Live File Creation** ⭐
   - Terminal 2 mein NAYA file banao
   - Watcher ka response dikho
   - Yeh sabse important part hai!

2. **Automatic Task Creation** ⭐
   - Task file automatically bani
   - Priority automatically assign hui
   - Metadata automatically extract hua

3. **Claude Integration** ⭐
   - Claude Dashboard read kare
   - Claude task analyze kare
   - Claude report banaye

4. **Agent Skills** ⭐
   - Skills folder dikho
   - Ek skill ka content dikho

---

## ❌ GALAT Tarika (Don't Do This)

**Galat:**
```powershell
# Existing task file dikhana
cat Needs_Action/task_urgent_demo_test_*.md
```

**Kyun Galat:**
- Yeh existing file hai
- Live demonstration nahi hai
- Judges ko LIVE process dekhna hai

---

## ✅ SAHI Tarika (Do This)

**Sahi:**
```powershell
# Step 1: Watcher start karo (Terminal 1)
python file_watcher.py

# Step 2: NAYA file banao (Terminal 2)
echo "URGENT: Test" > Drop/live_demo_test.txt

# Step 3: Watcher ka response dikho (Terminal 1)
# [Automatic detection message]

# Step 4: Created task dikho (Terminal 2)
cat Needs_Action/task_live_demo_test_*.md
```

**Kyun Sahi:**
- Live demonstration hai
- Process dikha rahe ho
- Judges dekh sakte hain kaise kaam karta hai

---

## 📋 Quick Checklist

**Terminal 1 (Watcher):**
- [ ] `cd` to vault
- [ ] `python file_watcher.py` (start)
- [ ] Show detection messages
- [ ] Keep running throughout demo

**Terminal 2 (Commands):**
- [ ] Show folder structure
- [ ] Show Dashboard
- [ ] **CREATE new file** (most important!)
- [ ] Show created task
- [ ] Use Claude (3 commands)
- [ ] Show generated report
- [ ] Show Agent Skills

---

## ⏱️ Time Breakdown

- Introduction: 30 sec
- System Overview: 1.5 min
- **Live Watcher Demo: 2.5 min** ⭐ (Most important)
- Claude Integration: 2 min
- Agent Skills: 1 min
- Conclusion: 30 sec

**Total:** 7-8 minutes

---

## 🚨 Common Mistakes to Avoid

### Mistake 1: Existing Files Dikhana
**Wrong:** Purani task files dikhana
**Right:** NAYA file create karna aur process dikhana

### Mistake 2: Watcher Band Karna
**Wrong:** Watcher start karke turant band kar dena
**Right:** Watcher running rakhna jab tak file create nahi hoti

### Mistake 3: Claude Skip Karna
**Wrong:** Claude integration nahi dikhana
**Right:** Claude ke saath 2-3 commands run karna

---

## 💡 Pro Tip

**Sabse Important Part:**
```
Terminal 1: python file_watcher.py (running)
Terminal 2: echo "URGENT: Test" > Drop/new_file.txt
Terminal 1: [Shows detection message]
Terminal 2: cat Needs_Action/task_new_file_*.md
```

**Yeh 1 minute ka sequence sabse important hai!**
Yeh dikhata hai ki system LIVE kaam kar raha hai.

---

## 🎬 Ready to Record?

**Yaad Rakho:**
1. ✅ Terminal 1 mein watcher START karo
2. ✅ Terminal 2 mein NAYA file banao
3. ✅ Watcher ka response dikho
4. ✅ Created task dikho
5. ✅ Claude use karo
6. ✅ Skills dikho

**Bas itna hi! Simple hai.**

---

**File:** Save this as reference during recording
