"""
=============================================================
WEEK 1 - DAY 2
Topic: Git & GitHub — Version Control Basics
=============================================================

WHAT IS GIT?
------------
Git is a tool that tracks changes in your code.
Think of it like a "save history" for your project.

Every time you make a change and "commit" it,
Git saves a snapshot. You can go back to any snapshot anytime.

WHY DO WE NEED IT?
------------------
Without Git:
  - You save file as: code_v1.py, code_v2.py, code_FINAL.py, code_FINAL2.py...
  - You can't easily see WHAT changed between versions
  - If you break something, it's hard to go back

With Git:
  - One file, full history of every change
  - You can see exactly what changed and when
  - You can go back to any previous version instantly
  - Multiple people can work on same code without conflicts

WHAT IS GITHUB?
---------------
GitHub = Cloud storage for Git repositories
Just like Google Drive stores your files,
GitHub stores your Git repositories (projects).

GIT COMMANDS TO RUN IN YOUR TERMINAL:
--------------------------------------
(These are terminal commands, not Python code)

INITIAL SETUP (do once):
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"

START A PROJECT:
  git init                    → start git tracking in current folder
  git clone <url>             → download a project from GitHub

DAILY WORKFLOW:
  git status                  → see what files changed
  git add filename.py         → stage one file for commit
  git add .                   → stage ALL changed files
  git commit -m "what I did"  → save a snapshot with a message
  git push origin main        → upload commits to GitHub
  git pull origin main        → download latest changes from GitHub

CHECK HISTORY:
  git log                     → see all commits
  git log --oneline           → see commits in short format
  git diff                    → see exactly what lines changed

=============================================================
"""

# -------------------------------------------------------
# This Python file simulates what Git does internally
# to help you UNDERSTAND the concept
# (In real life you run git commands in terminal)
# -------------------------------------------------------

import os
import json
import hashlib
from datetime import datetime

print("=" * 55)
print("UNDERSTANDING GIT CONCEPTS WITH PYTHON")
print("=" * 55)

# -------------------------------------------------------
# CONCEPT 1: What a "commit" actually is
# A commit = a snapshot of your code at a point in time
# Git identifies each commit by a unique hash (like a fingerprint)
# -------------------------------------------------------

print("\n--- CONCEPT 1: What is a Commit? ---")

def simulate_commit(message, files_changed):
    """
    Simulates what git does when you run: git commit -m "message"
    A commit stores: who made it, when, what changed, and a unique ID
    """
    commit = {
        "message": message,
        "author": "Ishaan Garg",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "files": files_changed,
    }

    # Git creates a unique hash for each commit
    # This hash is based on the content of the commit
    # That's why commit IDs look like: a3f9b2c1d...
    commit_string = json.dumps(commit)
    commit_hash = hashlib.sha1(commit_string.encode()).hexdigest()[:7]
    commit["hash"] = commit_hash

    return commit

# Simulating 3 commits like a real project
commit_history = []

c1 = simulate_commit("Initial commit — added main.py", ["main.py"])
commit_history.append(c1)
print(f"Commit 1: [{c1['hash']}] {c1['message']}")

c2 = simulate_commit("Added hello function to main.py", ["main.py"])
commit_history.append(c2)
print(f"Commit 2: [{c2['hash']}] {c2['message']}")

c3 = simulate_commit("Added requirements.txt", ["requirements.txt"])
commit_history.append(c3)
print(f"Commit 3: [{c3['hash']}] {c3['message']}")

print(f"\nTotal commits in history: {len(commit_history)}")

# -------------------------------------------------------
# CONCEPT 2: The 3 stages of Git
# Working Directory → Staging Area → Repository
# -------------------------------------------------------

print("\n--- CONCEPT 2: The 3 Stages of Git ---")
print("""
  [Working Directory]  →  git add  →  [Staging Area]  →  git commit  →  [Repository]
       (your files)                    (files ready                      (saved history)
                                        to commit)

  Example:
  1. You edit main.py         → it's in Working Directory (modified)
  2. git add main.py          → it moves to Staging Area (ready)
  3. git commit -m "my work"  → it's saved in Repository (committed)
  4. git push origin main     → it's uploaded to GitHub (pushed)
""")

# -------------------------------------------------------
# CONCEPT 3: Good commit messages
# Bad vs Good examples
# -------------------------------------------------------

print("--- CONCEPT 3: Writing Good Commit Messages ---")

bad_messages = [
    "fix",
    "changes",
    "updated stuff",
    "asdfgh",
    "final fix hopefully",
]

good_messages = [
    "Add user login endpoint with JWT authentication",
    "Fix CORS error by allowing localhost:3000 in origins",
    "Replace in-memory storage with SQLite database",
    "Add Hindi language support to TTS service",
    "Update README with installation instructions",
]

print("\n BAD commit messages (don't do this):")
for msg in bad_messages:
    print(f"  git commit -m \"{msg}\"")

print("\n GOOD commit messages (do this):")
for msg in good_messages:
    print(f"  git commit -m \"{msg}\"")

print("\nRule: A good commit message completes the sentence:")
print("      'If applied, this commit will... [your message]'")

# -------------------------------------------------------
# CONCEPT 4: .gitignore — files Git should NOT track
# -------------------------------------------------------

print("\n--- CONCEPT 4: .gitignore file ---")

gitignore_content = """# .gitignore file
# These files/folders will NOT be uploaded to GitHub

# Virtual environment — contains thousands of library files
# No need to share these, others can recreate with: pip install -r requirements.txt
venv/
.venv/
env/

# Environment variables — NEVER share API keys on GitHub!
.env

# Python cache files — auto-generated, not needed
__pycache__/
*.pyc
*.pyo

# VS Code settings — personal to your machine
.vscode/

# Generated audio files — too large for GitHub
audio_output/
*.mp3

# OS generated files
.DS_Store        # Mac
Thumbs.db        # Windows
"""

# Save the .gitignore file
with open("/tmp/week1/day2/.gitignore", "w") as f:
    f.write(gitignore_content)

print("Created .gitignore file!")
print("\nContents of .gitignore:")
print(gitignore_content)

# -------------------------------------------------------
# CONCEPT 5: Step by step — creating your first GitHub repo
# -------------------------------------------------------

print("--- CONCEPT 5: Your First GitHub Repo (Terminal Steps) ---")
print("""
Run these commands in your terminal one by one:

  # 1. Create a new folder for your internship diary
  mkdir podgen-internship
  cd podgen-internship

  # 2. Start Git tracking
  git init

  # 3. Create your first file
  echo "# PodGen AI Internship" > README.md

  # 4. Stage the file
  git add README.md

  # 5. Make your first commit
  git commit -m "Initial commit — start of internship diary"

  # 6. Go to github.com → New Repository → name it podgen-internship
  #    Copy the URL it gives you

  # 7. Connect your local folder to GitHub
  git remote add origin https://github.com/YourUsername/podgen-internship.git

  # 8. Push to GitHub
  git push -u origin main

  # Done! Refresh GitHub and you'll see your file there.
""")

print(" Day 2 Complete! Git and GitHub basics learned.")
