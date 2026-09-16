# GitHub Setup Instructions

## Quick Start - Copy & Paste These Commands

Run these commands one at a time in PowerShell (opened in your project folder):

### Step 1: Initialize Git
```powershell
cd "C:\Users\LENOVO\Desktop\Power Bi\project 1"
git init
```

### Step 2: Configure Git (if you haven't already)
```powershell
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### Step 3: Add All Files
```powershell
git add .
```

### Step 4: Create Initial Commit
```powershell
git commit -m "Initial commit: Amazon Sales Dashboard project

- Power BI dashboard with interactive visualizations
- Python data cleaning and analysis scripts
- Multiple export formats (CSV, JSON, HTML)
- Comprehensive documentation"
```

### Step 5: Rename Branch to Main
```powershell
git branch -m main
```

### Step 6: Add Remote Repository
First, create a new repository on GitHub:
1. Go to https://github.com/new
2. Name: `amazon-sales-dashboard`
3. Description: "Interactive Power BI dashboard analyzing Amazon sales data"
4. Choose **Public**
5. Click **Create repository**

Then run (replace YOUR-REPO-NAME with your actual repo name):
```powershell
git remote add origin https://github.com/gshakir-ops/YOUR-REPO-NAME.git
```

### Step 7: Push to GitHub
```powershell
git push -u origin main
```

---

## ✅ Done!

Your project is now on GitHub! You can:
- View it at: https://github.com/gshakir-ops/YOUR-REPO-NAME
- Share the link with others
- Continue updating it with `git add . && git commit -m "message" && git push`

---

## Troubleshooting

**Error: "fatal: not a git repository"**
- Make sure you're in the correct folder: `cd "C:\Users\LENOVO\Desktop\Power Bi\project 1"`

**Error: "rejected... You must change your repository password"**
- Use a Personal Access Token instead of your password
- Go to https://github.com/settings/tokens and create a new token
- Use it as the password when prompted

**Error: "fatal: the current branch main has no upstream branch"**
- Run: `git push -u origin main`

**Everything worked but files look wrong:**
- Check your `.gitignore` file - some files may be intentionally excluded
- The `.pbix` file is excluded by default (it's binary and large)

