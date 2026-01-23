"""
=============================================================
WEEK 1 - DAY 1 (Part 2)
Topic: Terminal Commands + Setting Up VS Code & Python
=============================================================

TERMINAL COMMANDS CHEATSHEET
(Run these in your terminal/command prompt, NOT in Python)

NAVIGATION:
  cd foldername         → go into a folder
  cd ..                 → go back one folder
  cd ~                  → go to home folder
  pwd                   → print current folder path (Mac/Linux)
  dir                   → print current folder path (Windows)

FILES & FOLDERS:
  ls                    → list files in current folder (Mac/Linux)
  dir                   → list files in current folder (Windows)
  mkdir week1           → create a new folder called week1
  touch file.py         → create a new empty file (Mac/Linux)
  echo. > file.py       → create a new empty file (Windows)
  del file.py           → delete a file (Windows)
  rm file.py            → delete a file (Mac/Linux)
  copy src dst          → copy a file (Windows)
  cp src dst            → copy a file (Mac/Linux)

PYTHON:
  python --version      → check Python version
  python file.py        → run a Python file
  pip install requests  → install a library
  pip list              → see all installed libraries

VIRTUAL ENVIRONMENT:
  python -m venv venv   → create virtual environment
  venv\Scripts\activate → activate it (Windows)
  source venv/bin/activate → activate it (Mac/Linux)
  deactivate            → turn off virtual environment

=============================================================
"""

# -------------------------------------------------------
# This Python file DEMONSTRATES what those commands do
# It uses Python's built-in 'os' module to run shell commands
# -------------------------------------------------------

import os
import sys
import subprocess

print("=" * 50)
print("SYSTEM INFORMATION")
print("=" * 50)

# os.getcwd() = "get current working directory"
# Same as typing 'pwd' in terminal
current_folder = os.getcwd()
print(f"Current folder: {current_folder}")

# sys.version shows the Python version
print(f"Python version: {sys.version}")

# os.listdir() = lists files in a folder
# Same as typing 'ls' or 'dir' in terminal
print(f"\nFiles in current folder:")
files = os.listdir(".")
for f in files:
    print(f"  - {f}")

print("\n" + "=" * 50)
print("CREATING FOLDERS AND FILES WITH PYTHON")
print("=" * 50)

# os.makedirs() creates a folder
# exist_ok=True means "don't crash if folder already exists"
os.makedirs("practice_folder", exist_ok=True)
print("Created folder: practice_folder")

# Writing to a file
with open("practice_folder/my_notes.txt", "w") as f:
    f.write("Week 1 Notes\n")
    f.write("=============\n")
    f.write("Today I learned about the internet and terminal commands.\n")
    f.write("HTTP GET = fetch data\n")
    f.write("HTTP POST = send data\n")
print("Created file: practice_folder/my_notes.txt")

# Reading from a file
print("\nReading the file back:")
with open("practice_folder/my_notes.txt", "r") as f:
    content = f.read()
print(content)

# os.path functions are very useful
file_path = "practice_folder/my_notes.txt"
print(f"File exists?    {os.path.exists(file_path)}")
print(f"Is it a file?   {os.path.isfile(file_path)}")
print(f"Is it a folder? {os.path.isdir(file_path)}")
print(f"File size:      {os.path.getsize(file_path)} bytes")

print("\n Terminal commands understood!")
