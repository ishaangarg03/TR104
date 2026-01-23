"""
=============================================================
WEEK 1 - DAY 3
Topic: VS Code Setup + Python Environment Setup

=============================================================

WHAT IS A VIRTUAL ENVIRONMENT?
-------------------------------
Imagine you are cooking two dishes:
  - Dish 1 needs Salt (version 1)
  - Dish 2 needs Salt (version 2)

You can't use both in the same kitchen.
So you have TWO separate kitchens — one for each dish.

In Python:
  - Project 1 needs requests version 2.28
  - Project 2 needs requests version 2.32
  - A virtual environment = a separate "kitchen" per project
  - Each project has its own libraries, independent of others

HOW TO CREATE ONE (terminal commands):
  python -m venv venv          → creates the virtual environment
  venv\Scripts\activate        → activates it (Windows)
  source venv/bin/activate     → activates it (Mac/Linux)
  pip install requests         → installs ONLY for this project
  pip freeze > requirements.txt → saves list of all libraries
  deactivate                   → deactivates the environment

=============================================================
"""

import sys
import os
import subprocess
import platform

# -------------------------------------------------------
# CHECKING YOUR PYTHON SETUP
# -------------------------------------------------------

print("=" * 50)
print("PYTHON ENVIRONMENT CHECK")
print("=" * 50)

# sys.version = full Python version string
print(f"\nPython Version:     {sys.version}")

# sys.executable = path to the Python being used right now
print(f"Python Location:    {sys.executable}")

# Check if we are inside a virtual environment
# When venv is active, sys.prefix != sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print(f"Inside virtualenv?: {'YES' if in_venv else 'NO (activate your venv!)'}")

# Platform info
print(f"Operating System:   {platform.system()} {platform.release()}")
print(f"Machine:            {platform.machine()}")

# -------------------------------------------------------
# CHECKING INSTALLED PACKAGES
# -------------------------------------------------------

print("\n" + "=" * 50)
print("CHECKING INSTALLED PACKAGES")
print("=" * 50)

# These are the packages we will use in Week 1
packages_to_check = [
    "requests",
    "beautifulsoup4",
]

for package in packages_to_check:
    try:
        # Try importing the package
        __import__(package.replace("-", "_").split("[")[0])
        print(f"  ✓ {package} — installed")
    except ImportError:
        print(f"  ✗ {package} — NOT installed (run: pip install {package})")

# -------------------------------------------------------
# HOW pip WORKS
# -------------------------------------------------------

print("\n" + "=" * 50)
print("UNDERSTANDING pip")
print("=" * 50)

print("""
pip = Python's package installer
It downloads libraries from PyPI (Python Package Index)
PyPI is like an app store for Python libraries

COMMANDS:
  pip install requests          → install a library
  pip install requests==2.28.0  → install a SPECIFIC version
  pip install -r requirements.txt → install all libraries from file
  pip uninstall requests        → remove a library
  pip list                      → see all installed libraries
  pip show requests             → details about one library
  pip freeze                    → list all installed with versions
  pip freeze > requirements.txt → save the list to a file
""")

# -------------------------------------------------------
# CREATING A requirements.txt FILE
# -------------------------------------------------------

print("=" * 50)
print("CREATING requirements.txt")
print("=" * 50)

# This is what a requirements.txt looks like
# When someone else clones your project, they run:
# pip install -r requirements.txt
# And get all the exact same libraries

requirements_content = """# Week 1 requirements
# Install all of these with: pip install -r requirements.txt

requests==2.32.3          # For making HTTP requests
beautifulsoup4==4.12.3    # For scraping websites
"""

with open("/tmp/week1/requirements.txt", "w") as f:
    f.write(requirements_content)

print("\nCreated requirements.txt:")
print(requirements_content)

# -------------------------------------------------------
# VS CODE EXTENSIONS TO INSTALL
# -------------------------------------------------------

print("=" * 50)
print("RECOMMENDED VS CODE EXTENSIONS")
print("=" * 50)

extensions = [
    ("Python", "ms-python.python", "Python language support, debugging, IntelliSense"),
    ("Pylance", "ms-python.vscode-pylance", "Faster Python type checking and autocomplete"),
    ("GitLens", "eamodio.gitlens", "See Git blame, history inline in code"),
    ("Prettier", "esbenp.prettier-vscode", "Auto-formats your code neatly"),
    ("indent-rainbow", "oderwat.indent-rainbow", "Colors indentation levels — helps in Python"),
    ("Thunder Client", "rangav.vscode-thunder-client", "Test APIs like Postman, inside VS Code"),
]

print("\nInstall these in VS Code (Ctrl+Shift+X → search name):\n")
for name, id_, desc in extensions:
    print(f"  {name}")
    print(f"    ID:   {id_}")
    print(f"    Why:  {desc}\n")

print(" Day 3 Complete! Python environment fully set up.")
