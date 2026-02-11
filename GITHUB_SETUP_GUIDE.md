# 💻 GitHub Repository Setup - Step by Step

**Time:** 10 minutes
**Required for:** Hackathon submission

---

## 🎯 Method 1: Using GitHub Desktop (Easiest)

### Step 1: Download GitHub Desktop (if not installed)
1. Go to: https://desktop.github.com
2. Download and install
3. Sign in with your GitHub account

### Step 2: Add Repository
1. Open GitHub Desktop
2. Click "File" → "Add local repository"
3. Click "Choose..." button
4. Navigate to: `D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault`
5. Click "Select Folder"

### Step 3: Initialize Repository
1. Click "create a repository" link
2. Name: `ai-employee-bronze-tier`
3. Description: `Bronze Tier Personal AI Employee - Hackathon 0`
4. Check "Initialize this repository with a README" (uncheck - we have one)
5. Git Ignore: None (we'll create custom)
6. License: MIT (optional)
7. Click "Create Repository"

### Step 4: Create .gitignore
1. Open Notepad
2. Add these lines:
```
__pycache__/
*.pyc
.env
*.log
Drop/*.txt
.DS_Store
Thumbs.db
```
3. Save as: `D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault\.gitignore`

### Step 5: Commit Files
1. GitHub Desktop will show all files
2. Check all files (should be checked by default)
3. Summary: `Bronze Tier: Complete AI Employee implementation`
4. Description:
```
- Obsidian vault with Dashboard and Handbook
- Working file watcher (file_watcher.py)
- Claude Code integration verified
- 3 Agent Skills implemented
- Complete documentation (23 files)
- Tested and verified

All Bronze Tier requirements met.
```
5. Click "Commit to main"

### Step 6: Publish to GitHub
1. Click "Publish repository" button
2. Name: `ai-employee-bronze-tier`
3. Description: `Bronze Tier Personal AI Employee - Hackathon 0`
4. Keep "Keep this code private" **UNCHECKED** (make it public)
5. Click "Publish Repository"

### Step 7: Copy Repository URL
1. Click "View on GitHub" button
2. Copy URL from browser
3. Format: `https://github.com/YOUR_USERNAME/ai-employee-bronze-tier`

---

## 🎯 Method 2: Using Command Line

### Step 1: Open Terminal
```powershell
cd "D:\LEEZA\HACKATHON 0\Bronze\AI_Employee_Vault"
```

### Step 2: Initialize Git
```bash
git init
```

### Step 3: Create .gitignore
```bash
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
echo "*.log" >> .gitignore
echo "Drop/*.txt" >> .gitignore
```

### Step 4: Add Files
```bash
git add .
```

### Step 5: Commit
```bash
git commit -m "Bronze Tier: Complete AI Employee implementation

- Obsidian vault with Dashboard and Handbook
- Working file watcher (file_watcher.py)
- Claude Code integration verified
- 3 Agent Skills implemented
- Complete documentation (23 files)
- Tested and verified

All Bronze Tier requirements met."
```

### Step 6: Create Repository on GitHub
1. Go to: https://github.com/new
2. Repository name: `ai-employee-bronze-tier`
3. Description: `Bronze Tier Personal AI Employee - Hackathon 0`
4. Public (not Private)
5. Don't initialize with README (we have one)
6. Click "Create repository"

### Step 7: Push to GitHub
```bash
# Copy these commands from GitHub (they'll show after creating repo)
git remote add origin https://github.com/YOUR_USERNAME/ai-employee-bronze-tier.git
git branch -M main
git push -u origin main
```

### Step 8: Verify
1. Refresh GitHub page
2. All files should be visible
3. Copy repository URL

---

## ✅ What Should Be in Repository

**Files to Include:**
- ✅ Dashboard.md
- ✅ Company_Handbook.md
- ✅ file_watcher.py
- ✅ requirements.txt
- ✅ README.md
- ✅ All documentation files
- ✅ Skills folder (3 skills)
- ✅ Folder structure (Inbox, Needs_Action, Done, etc.)

**Files to Exclude (.gitignore):**
- ❌ __pycache__/
- ❌ *.pyc
- ❌ .env
- ❌ Test files in Drop/
- ❌ Personal data

---

## 🔍 Verify Repository

**Check these:**
1. Go to your repository URL
2. Verify README.md displays correctly
3. Check all folders are present
4. Verify file_watcher.py is there
5. Check Skills folder has 3 files
6. Make sure .gitignore is working (no __pycache__)

---

## 📝 Update README (Optional but Recommended)

**Add to top of README.md:**
```markdown
# Bronze Tier AI Employee

**Status:** ✅ Complete
**Demo Video:** [Watch Demo](YOUR_YOUTUBE_URL)
**Hackathon:** Personal AI Employee Hackathon 0

---

[Rest of your README content]
```

---

## 🚨 Common Issues

### Issue 1: "Repository already exists"
**Solution:**
- Choose different name
- Or delete existing repo and recreate

### Issue 2: Push fails
**Solution:**
```bash
# Check remote
git remote -v

# If wrong, remove and re-add
git remote remove origin
git remote add origin YOUR_CORRECT_URL
git push -u origin main
```

### Issue 3: Large files error
**Solution:**
- Check .gitignore is working
- Remove large test files
- Don't commit videos

### Issue 4: Permission denied
**Solution:**
- Check GitHub credentials
- Use GitHub Desktop instead
- Or use Personal Access Token

---

## ✅ Checklist

**Before Moving to Next Step:**
- [ ] Repository created on GitHub
- [ ] All files pushed successfully
- [ ] Repository is Public (not Private)
- [ ] .gitignore is working
- [ ] README.md displays correctly
- [ ] Repository URL copied
- [ ] Verified in browser (open in incognito)

---

## 💡 Pro Tips

1. **Make it Public:** Judges need to access it
2. **Good README:** First impression matters
3. **Clean Commits:** Professional commit messages
4. **No Secrets:** Never commit .env or credentials
5. **Test URL:** Open in incognito to verify access

---

**Repository URL Format:**
```
https://github.com/YOUR_USERNAME/ai-employee-bronze-tier
```

**Save this URL** - you'll need it for hackathon form!

---

**Next Step:** Submit Hackathon Form (5 min)
