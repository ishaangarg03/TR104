# =============================================================================
# WEEK 4 - DAY 1: SQL with Python (SQLite)
# Intern: ISHAAN GARG
# Topic: Databases, tables, CRUD operations using sqlite3
# =============================================================================

import sqlite3
import os

print("=" * 50)
print("SECTION 1: CONNECTING TO A DATABASE")
print("=" * 50)

# SQLite creates a local .db file — no server needed
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()
print("Connected to internship.db")

print("\n" + "=" * 50)
print("SECTION 2: CREATE TABLE")
print("=" * 50)

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
    CREATE TABLE students (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT    NOT NULL,
        age         INTEGER,
        department  TEXT,
        score       REAL,
        city        TEXT
    )
""")
conn.commit()
print("Table 'students' created.")

print("\n" + "=" * 50)
print("SECTION 3: INSERT DATA")
print("=" * 50)

students = [
    ("Ishaan Garg", 21, "AI", 88.5, "Ludhiana"),
    ("Alice Singh",   22, "Web", 91.0, "Delhi"),
    ("Bob Sharma",    23, "Data", 78.3, "Mumbai"),
    ("Charlie Verma", 21, "AI", 95.0, "Chennai"),
    ("Diana Mehta",   24, "Web", 82.5, "Pune"),
    ("Eve Kapoor",    22, "Data", 74.0, "Bangalore"),
    ("Frank Nair",    23, "Backend", 87.0, "Kochi"),
]

cursor.executemany("""
    INSERT INTO students (name, age, department, score, city)
    VALUES (?, ?, ?, ?, ?)
""", students)
conn.commit()
print(f"Inserted {len(students)} students.")

print("\n" + "=" * 50)
print("SECTION 4: SELECT — READ DATA")
print("=" * 50)

# Select all
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(" ", row)

# Select specific columns
cursor.execute("SELECT name, score FROM students ORDER BY score DESC")
print("\nRanked by score:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

# Filter with WHERE
cursor.execute("SELECT name, score FROM students WHERE department = 'AI'")
print("\nAI department:")
for row in cursor.fetchall():
    print(" ", row)

# Aggregate
cursor.execute("SELECT department, AVG(score), MAX(score), COUNT(*) FROM students GROUP BY department")
print("\nDept stats (dept, avg, max, count):")
for row in cursor.fetchall():
    print(f"  {row[0]:10s} | Avg: {row[1]:.1f} | Max: {row[2]} | Count: {row[3]}")

print("\n" + "=" * 50)
print("SECTION 5: UPDATE AND DELETE")
print("=" * 50)

cursor.execute("UPDATE students SET score = 90.0 WHERE name = 'Bob Sharma'")
conn.commit()
cursor.execute("SELECT name, score FROM students WHERE name = 'Bob Sharma'")
print("Bob's updated score:", cursor.fetchone())

cursor.execute("DELETE FROM students WHERE score < 75")
conn.commit()
cursor.execute("SELECT COUNT(*) FROM students")
print("Rows after deleting low scorers:", cursor.fetchone()[0])

print("\n" + "=" * 50)
print("SECTION 6: PANDAS + SQL")
print("=" * 50)

import pandas as pd
df = pd.read_sql_query("SELECT * FROM students ORDER BY score DESC", conn)
print("Results as DataFrame:\n", df)

conn.close()
os.remove("internship.db")
print("\nDatabase closed and cleaned up.")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("CREATE TABLE  → define schema")
print("INSERT INTO   → add rows")
print("SELECT        → read data")
print("WHERE         → filter rows")
print("GROUP BY      → aggregate")
print("UPDATE        → modify rows")
print("DELETE        → remove rows")
print("pd.read_sql() → SQL result → DataFrame")
