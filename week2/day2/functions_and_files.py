# =============================================================================
# WEEK 2 - DAY 2: Functions & File Handling
# Topic: Writing reusable functions + reading/writing files
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: FUNCTIONS — THE BASICS
# A function is a reusable block of code.
# Instead of writing the same logic 10 times, write it once and call it.
# -----------------------------------------------------------------------------

print("=" * 50)
print("SECTION 1: FUNCTIONS")
print("=" * 50)

# Defining a basic function
def greet(name):
    """This function greets a person by name."""
    print(f"Hello, {name}! Welcome to Week 2.")

greet("Navkiran")
greet("Everyone")

# Function with a return value
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(10, 25)
print(f"\n10 + 25 = {result}")

# Default parameter — used when no argument is passed
def power(base, exponent=2):
    """Returns base raised to exponent. Default exponent is 2 (square)."""
    return base ** exponent

print(f"\n3 squared = {power(3)}")           # uses default exponent=2
print(f"2 to the 10th = {power(2, 10)}")     # overrides default

# Multiple return values (Python returns them as a tuple)
def min_max(numbers):
    """Returns both the minimum and maximum of a list."""
    return min(numbers), max(numbers)

low, high = min_max([5, 2, 8, 1, 9, 3])
print(f"\nMin: {low}, Max: {high}")

# -----------------------------------------------------------------------------
# SECTION 2: ARGS AND KWARGS
# *args → variable number of positional arguments
# **kwargs → variable number of keyword arguments
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 2: *args AND **kwargs")
print("=" * 50)

# *args lets you pass any number of values
def total(*args):
    """Adds up all numbers passed in."""
    return sum(args)

print("Total of 1,2,3:", total(1, 2, 3))
print("Total of 10,20,30,40:", total(10, 20, 30, 40))

# **kwargs lets you pass any number of named values
def print_profile(**kwargs):
    """Prints a profile from keyword arguments."""
    print("\n-- Profile --")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_profile(name="Navkiran", role="Intern", city="Ludhiana", skill="Python")

# -----------------------------------------------------------------------------
# SECTION 3: LAMBDA FUNCTIONS
# A lambda is a tiny one-line anonymous function.
# Use when you need a quick function without naming it.
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 3: LAMBDA FUNCTIONS")
print("=" * 50)

# Regular function vs lambda
def square(x):
    return x * x

square_lambda = lambda x: x * x

print("Regular function:", square(5))
print("Lambda function:", square_lambda(5))

# Lambda is super useful with sorted(), filter(), map()
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]

# Sort by score using lambda
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nStudents sorted by score:")
for s in sorted_students:
    print(f"  {s['name']}: {s['score']}")

# Filter — keep only students who passed (score >= 80)
passed = list(filter(lambda s: s["score"] >= 80, students))
print("\nStudents who passed:")
for s in passed:
    print(f"  {s['name']}: {s['score']}")

# Map — multiply all scores by 1.1 (bonus)
boosted = list(map(lambda s: {**s, "score": round(s["score"] * 1.1, 1)}, students))
print("\nScores after 10% bonus:")
for s in boosted:
    print(f"  {s['name']}: {s['score']}")

# -----------------------------------------------------------------------------
# SECTION 4: FILE HANDLING
# Python can read and write files easily.
# This is essential for saving data, logs, reports, etc.
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 4: FILE HANDLING")
print("=" * 50)

import os

# --- Writing a file ---
# "w" mode: creates the file (or overwrites if exists)
with open("navkiran_notes.txt", "w") as f:
    f.write("Week 2 - Python Notes\n")
    f.write("=" * 30 + "\n")
    f.write("Day 1: Data Structures\n")
    f.write("Day 2: Functions & File Handling\n")
    f.write("Learning Python is going great!\n")

print("File written: navkiran_notes.txt")

# --- Reading the entire file ---
with open("navkiran_notes.txt", "r") as f:
    content = f.read()

print("\n--- File Contents ---")
print(content)

# --- Reading line by line ---
print("--- Line by Line ---")
with open("navkiran_notes.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"Line {i}: {line.strip()}")

# --- Appending to a file ---
# "a" mode: adds to the end without overwriting
with open("navkiran_notes.txt", "a") as f:
    f.write("Day 3: OOP coming next!\n")

print("\nAppended a new line.")

# --- Reading lines into a list ---
with open("navkiran_notes.txt", "r") as f:
    lines = f.readlines()   # returns a list of strings

print(f"\nTotal lines in file: {len(lines)}")

# --- Writing a CSV manually ---
data = [
    ["Name", "Score", "Grade"],
    ["Navkiran", 92, "A"],
    ["Alice", 85, "B"],
    ["Bob", 78, "C"],
]

with open("scores.csv", "w") as f:
    for row in data:
        f.write(",".join(str(item) for item in row) + "\n")

print("\nCSV file written: scores.csv")

with open("scores.csv", "r") as f:
    print("\n--- scores.csv Contents ---")
    print(f.read())

# --- Checking if a file exists ---
if os.path.exists("navkiran_notes.txt"):
    size = os.path.getsize("navkiran_notes.txt")
    print(f"navkiran_notes.txt exists | Size: {size} bytes")

# --- Clean up ---
os.remove("navkiran_notes.txt")
os.remove("scores.csv")
print("\nTemporary files cleaned up.")

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("def func()     → define a reusable function")
print("return         → send a value back from a function")
print("*args          → accept any number of arguments")
print("**kwargs       → accept any number of keyword arguments")
print("lambda         → one-line anonymous function")
print('open("f","w")  → write to a file')
print('open("f","r")  → read from a file')
print('open("f","a")  → append to a file')
print('with open(...) → auto-closes file safely (always use this!)')
