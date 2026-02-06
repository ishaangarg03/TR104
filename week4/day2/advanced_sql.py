# =============================================================================
# WEEK 4 - DAY 2: Advanced SQL — Joins, Subqueries, Views
# Intern: ISHAAN GARG
# Topic: Combining tables, nested queries, and stored views
# =============================================================================

import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Build two related tables
cursor.executescript("""
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS projects;

CREATE TABLE departments (
    dept_id   INTEGER PRIMARY KEY,
    dept_name TEXT,
    budget    INTEGER
);

CREATE TABLE employees (
    emp_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT,
    dept_id   INTEGER,
    salary    INTEGER,
    manager   INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE projects (
    proj_id  INTEGER PRIMARY KEY,
    title    TEXT,
    dept_id  INTEGER,
    status   TEXT
);
""")

cursor.executemany("INSERT INTO departments VALUES (?,?,?)", [
    (1, "AI Research", 500000),
    (2, "Web Dev", 300000),
    (3, "Data Science", 400000),
    (4, "Backend", 350000),
])

cursor.executemany("INSERT INTO employees (name, dept_id, salary, manager) VALUES (?,?,?,?)", [
    ("Ishaan Garg", 1, 30000, None),
    ("Alice",         2, 32000, None),
    ("Bob",           3, 28000, None),
    ("Charlie",       1, 35000, 1),
    ("Diana",         2, 31000, 2),
    ("Eve",           3, 29000, 3),
    ("Frank",         4, 33000, None),
    ("Grace",         4, 27000, 7),
])

cursor.executemany("INSERT INTO projects VALUES (?,?,?,?)", [
    (1, "LLM Chatbot", 1, "Active"),
    (2, "Portfolio Site", 2, "Done"),
    (3, "Analytics Dashboard", 3, "Active"),
    (4, "REST API", 4, "Active"),
    (5, "Image Classifier", 1, "Planning"),
])
conn.commit()

print("=" * 50)
print("SECTION 1: INNER JOIN")
print("=" * 50)

q = """
SELECT e.name, d.dept_name, e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
ORDER BY e.salary DESC
"""
df = pd.read_sql_query(q, conn)
print(df)

print("\n" + "=" * 50)
print("SECTION 2: LEFT JOIN (include employees even without dept)")
print("=" * 50)

q = """
SELECT e.name, d.dept_name, p.title as project
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN projects p ON e.dept_id = p.dept_id
"""
df = pd.read_sql_query(q, conn)
print(df.head(10))

print("\n" + "=" * 50)
print("SECTION 3: AGGREGATE JOINS")
print("=" * 50)

q = """
SELECT d.dept_name,
       COUNT(e.emp_id) as headcount,
       AVG(e.salary) as avg_salary,
       d.budget
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC
"""
df = pd.read_sql_query(q, conn)
print(df)

print("\n" + "=" * 50)
print("SECTION 4: SUBQUERIES")
print("=" * 50)

# Employees earning above company average
q = """
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY salary DESC
"""
df = pd.read_sql_query(q, conn)
print("Above average salary:\n", df)

# Departments with active projects
q = """
SELECT dept_name FROM departments
WHERE dept_id IN (
    SELECT dept_id FROM projects WHERE status = 'Active'
)
"""
df = pd.read_sql_query(q, conn)
print("\nDepts with active projects:\n", df)

print("\n" + "=" * 50)
print("SECTION 5: VIEWS")
print("=" * 50)

cursor.execute("DROP VIEW IF EXISTS dept_summary")
cursor.execute("""
    CREATE VIEW dept_summary AS
    SELECT d.dept_name, COUNT(e.emp_id) as headcount, AVG(e.salary) as avg_sal
    FROM departments d
    LEFT JOIN employees e ON d.dept_id = e.dept_id
    GROUP BY d.dept_name
""")
conn.commit()

df = pd.read_sql_query("SELECT * FROM dept_summary", conn)
print("View dept_summary:\n", df)

print("\n" + "=" * 50)
print("SECTION 6: WINDOW FUNCTIONS (SQLite 3.25+)")
print("=" * 50)

q = """
SELECT name, salary, dept_id,
       RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as rank_in_dept
FROM employees
"""
try:
    df = pd.read_sql_query(q, conn)
    print("Rank within department:\n", df)
except Exception as e:
    print("Window functions not supported in this SQLite version:", e)

conn.close()
os.remove("company.db")
print("\nDone.")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("INNER JOIN   → rows with matches in both tables")
print("LEFT JOIN    → all left rows + matched right rows")
print("Subquery     → query inside a query")
print("CREATE VIEW  → save a query as a virtual table")
print("RANK() OVER  → window function for ranking")
