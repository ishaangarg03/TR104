# =============================================================================
# WEEK 2 - DAY 4: Error Handling & Python Modules
# Topic: try/except, raising errors, and using Python's built-in modules
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: WHY ERROR HANDLING?
# Real programs face unexpected situations — bad input, missing files, etc.
# Without error handling, your program crashes with a scary traceback.
# With it, you catch the problem, handle it gracefully, and keep running.
# -----------------------------------------------------------------------------

print("=" * 50)
print("SECTION 1: TRY / EXCEPT BASICS")
print("=" * 50)

# Without error handling — this would crash:
# result = 10 / 0   → ZeroDivisionError

# With error handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught it! You can't divide by zero.")

# Another example — bad type
try:
    number = int("hello")
except ValueError as e:
    print(f"ValueError caught: {e}")

# Multiple except blocks — catch different error types
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Both values must be numbers!")
        return None

print("\nsafe_divide(10, 2):", safe_divide(10, 2))
print("safe_divide(10, 0):", safe_divide(10, 0))
print('safe_divide(10, "x"):', safe_divide(10, "x"))

# -----------------------------------------------------------------------------
# SECTION 2: ELSE AND FINALLY
# else  → runs if NO exception occurred
# finally → ALWAYS runs, even if there was an exception
# Use finally for cleanup (closing files, connections, etc.)
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 2: ELSE AND FINALLY")
print("=" * 50)

def read_number(value):
    try:
        num = int(value)
    except ValueError:
        print(f"'{value}' is not a valid number.")
    else:
        print(f"Success! The number is: {num}")
    finally:
        print("(This always runs — like cleanup code)\n")

read_number("42")
read_number("abc")

# -----------------------------------------------------------------------------
# SECTION 3: RAISING YOUR OWN ERRORS
# You can raise errors intentionally to enforce rules in your code.
# This is how libraries signal that you're using them wrong.
# -----------------------------------------------------------------------------

print("=" * 50)
print("SECTION 3: RAISING CUSTOM ERRORS")
print("=" * 50)

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0 or age > 120:
        raise ValueError(f"Age {age} is out of valid range (0–120).")
    print(f"Age set to: {age}")

# Test valid age
try:
    set_age(21)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Test invalid age
try:
    set_age(-5)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Test wrong type
try:
    set_age("twenty")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Custom exception class
class InternError(Exception):
    """Custom exception for intern-related issues."""
    pass

def assign_task(task, intern_name):
    if not task:
        raise InternError(f"Cannot assign an empty task to {intern_name}.")
    print(f"Task '{task}' assigned to {intern_name}.")

try:
    assign_task("", "Navkiran")
except InternError as e:
    print(f"InternError: {e}")

try:
    assign_task("Build API", "Navkiran")
except InternError as e:
    print(f"InternError: {e}")

# -----------------------------------------------------------------------------
# SECTION 4: PYTHON BUILT-IN MODULES
# Python comes with hundreds of modules — you don't need to install them.
# Just import and use!
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 4: BUILT-IN MODULES")
print("=" * 50)

# --- math module ---
import math

print("math.sqrt(144):", math.sqrt(144))
print("math.pi:", math.pi)
print("math.ceil(4.3):", math.ceil(4.3))    # rounds UP
print("math.floor(4.9):", math.floor(4.9))  # rounds DOWN
print("math.factorial(5):", math.factorial(5))

# --- random module ---
import random

print("\n--- random ---")
print("Random int 1-10:", random.randint(1, 10))
print("Random float:", round(random.random(), 4))

colors = ["red", "blue", "green", "yellow"]
print("Random choice:", random.choice(colors))

deck = list(range(1, 11))
random.shuffle(deck)
print("Shuffled deck:", deck)

# --- datetime module ---
from datetime import datetime, timedelta

print("\n--- datetime ---")
now = datetime.now()
print("Current datetime:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Just the date:", now.strftime("%d %B %Y"))
print("Just the time:", now.strftime("%H:%M"))

# timedelta — do math with dates
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print("Tomorrow:", tomorrow.strftime("%d %B %Y"))
print("Last week:", last_week.strftime("%d %B %Y"))

# --- os module ---
import os

print("\n--- os module ---")
print("Current directory:", os.getcwd())
print("Files here:", os.listdir(".")[:5])    # first 5 files

# Environment variables (safe way to store secrets)
os.environ["MY_NAME"] = "Navkiran"
print("Env variable MY_NAME:", os.environ.get("MY_NAME", "Not set"))

# --- json module ---
import json

print("\n--- json module ---")
# Python dict → JSON string (for APIs, files)
data = {
    "intern": "Ishaan Garg",
    "week": 2,
    "topics": ["OOP", "File Handling", "Modules"]
}

json_string = json.dumps(data, indent=2)
print("Dict to JSON:\n", json_string)

# JSON string → Python dict
parsed = json.loads(json_string)
print("JSON to Dict:", parsed["intern"])

# Save JSON to file
with open("week2_data.json", "w") as f:
    json.dump(data, f, indent=2)
print("JSON saved to week2_data.json")

with open("week2_data.json", "r") as f:
    loaded = json.load(f)
print("Loaded from file:", loaded)

os.remove("week2_data.json")

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("try/except        → catch errors gracefully")
print("except TypeError  → catch specific error types")
print("else              → runs only if no error")
print("finally           → always runs (cleanup)")
print("raise ValueError  → trigger an error on purpose")
print("import math       → math functions")
print("import random     → random numbers and choices")
print("from datetime...  → dates and times")
print("import os         → files, directories, env vars")
print("import json       → read/write JSON data")
