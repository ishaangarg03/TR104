# =============================================================================
# WEEK 2 - DAY 1: Python Data Structures Deep Dive
# Topic: Lists, Tuples, Dictionaries, Sets — with real examples
# =============================================================================

# -----------------------------------------------------------------------------
# SECTION 1: LISTS
# A list is an ordered, mutable (changeable) collection.
# Think of it like a to-do list you can add/remove items from.
# -----------------------------------------------------------------------------

print("=" * 50)
print("SECTION 1: LISTS")
print("=" * 50)

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]
print("Original list:", fruits)

# Accessing items (indexing starts at 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])   # -1 means last item

# Adding items
fruits.append("grapes")           # adds to the end
fruits.insert(1, "blueberry")     # inserts at position 1
print("After adding:", fruits)

# Removing items
fruits.remove("banana")           # removes by value
popped = fruits.pop()             # removes last item and returns it
print("After removing:", fruits)
print("Popped item:", popped)

# Slicing a list [start:end] — end is NOT included
print("First 3 fruits:", fruits[0:3])
print("From index 2 onwards:", fruits[2:])

# Looping through a list
print("\nAll fruits:")
for fruit in fruits:
    print(" -", fruit)

# List comprehension — a shorter way to create lists
squares = [x ** 2 for x in range(1, 6)]
print("\nSquares of 1-5:", squares)

# Useful list methods
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print("\nSorted numbers:", numbers)
print("Length:", len(numbers))
print("Max:", max(numbers), "| Min:", min(numbers))

# -----------------------------------------------------------------------------
# SECTION 2: TUPLES
# A tuple is like a list BUT it cannot be changed (immutable).
# Use tuples when data should NOT change — like coordinates, RGB colors.
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 2: TUPLES")
print("=" * 50)

# Creating a tuple (uses parentheses instead of square brackets)
coordinates = (28.6139, 77.2090)   # latitude, longitude of Delhi
print("Coordinates:", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# Tuples can be unpacked into variables
lat, lon = coordinates
print(f"Unpacked — Lat: {lat}, Lon: {lon}")

# Tuples are faster and safer than lists for fixed data
rgb_red = (255, 0, 0)
rgb_green = (0, 255, 0)
rgb_blue = (0, 0, 255)
print("\nRed color RGB:", rgb_red)

# You CANNOT do: rgb_red[0] = 100  <-- This would throw a TypeError
# That's the point — the data is protected.

# Count occurrences in a tuple
grades = (90, 85, 90, 78, 90, 65)
print("\nGrades tuple:", grades)
print("How many 90s:", grades.count(90))
print("Index of first 78:", grades.index(78))

# -----------------------------------------------------------------------------
# SECTION 3: DICTIONARIES
# A dictionary stores data as key-value pairs.
# Think of it like a real dictionary: word (key) → meaning (value)
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 3: DICTIONARIES")
print("=" * 50)

# Creating a dictionary
student = {
    "name": "Ishaan Garg",
    "age": 21,
    "city": "Ludhiana",
    "skills": ["Python", "Git", "APIs"]
}
print("Student info:", student)

# Accessing values by key
print("\nName:", student["name"])
print("City:", student["city"])

# Safe access using .get() — won't crash if key doesn't exist
print("GPA:", student.get("gpa", "Not available"))

# Adding / updating keys
student["role"] = "Intern"          # adds new key
student["age"] = 22                  # updates existing key
print("\nUpdated student:", student)

# Removing a key
del student["age"]
print("After deleting age:", student)

# Looping through a dictionary
print("\nAll student info:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["python", "java", "javascript"]}
print("\nWord lengths:", word_lengths)

# Nested dictionary (dictionary inside dictionary)
company = {
    "name": "TechCorp",
    "intern": {
        "name": "Navkiran",
        "department": "AI"
    }
}
print("\nIntern department:", company["intern"]["department"])

# -----------------------------------------------------------------------------
# SECTION 4: SETS
# A set is an unordered collection with NO duplicates.
# Use sets when you want unique values only.
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SECTION 4: SETS")
print("=" * 50)

# Creating a set
tags = {"python", "ai", "ml", "python", "data", "ai"}
print("Tags (duplicates removed):", tags)

# Adding and removing
tags.add("deep_learning")
tags.discard("ml")         # won't crash even if item doesn't exist
print("Updated tags:", tags)

# Set operations — very useful for comparing data
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nSet A:", set_a)
print("Set B:", set_b)
print("Union (all elements):", set_a | set_b)
print("Intersection (common):", set_a & set_b)
print("Difference (in A but not B):", set_a - set_b)

# Real-world use: find unique visitors
visitors_day1 = {"Alice", "Bob", "Charlie", "Alice", "Bob"}
visitors_day2 = {"Bob", "Diana", "Eve"}
unique_day1 = set(visitors_day1)
print("\nUnique visitors day 1:", unique_day1)
print("Visitors on both days:", unique_day1 & visitors_day2)
print("New visitors on day 2:", visitors_day2 - unique_day1)

# -----------------------------------------------------------------------------
# SUMMARY
# -----------------------------------------------------------------------------

print("\n" + "=" * 50)
print("SUMMARY: When to use which?")
print("=" * 50)
print("LIST   → ordered, changeable, allows duplicates  → [1, 2, 3]")
print("TUPLE  → ordered, unchangeable, allows duplicates → (1, 2, 3)")
print("DICT   → key-value pairs, fast lookup            → {'key': 'val'}")
print("SET    → unordered, unique values only           → {1, 2, 3}")
