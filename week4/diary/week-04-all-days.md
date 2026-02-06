# WEEK 4 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — SQL Basics with SQLite

First time writing real SQL! Creating tables, inserting rows, querying with WHERE and GROUP BY — it all felt like a new superpower. The fact that SQLite stores everything in a single file is incredibly convenient for learning.

`pd.read_sql_query()` was a revelation — I can run SQL and get a DataFrame back instantly.

**Ran today:** `day1/sql_basics.py`

---

## Day 2 — Advanced SQL: Joins and Subqueries

JOINs are the hardest SQL concept I've encountered. INNER JOIN vs LEFT JOIN — the difference matters a lot when some rows don't have a match. I accidentally lost rows until I understood LEFT JOIN keeps all rows from the left table.

Subqueries (SELECT inside SELECT) feel like nesting Python functions — powerful once you get the pattern.

**Ran today:** `day2/advanced_sql.py`

---

## Day 3 — REST APIs with requests

APIs are how the modern internet talks. Today I made real HTTP calls from Python, parsed JSON responses, and even POSTed data. The `raise_for_status()` trick is now part of my standard toolkit.

The country info API was the most fun — getting real data about India and Japan from a live server felt impressive.

**Ran today:** `day3/rest_apis.py`

---

## Day 4 — Building a Flask API

I flipped to the other side today — instead of calling APIs, I built one. Flask makes it surprisingly simple. Six endpoints (GET, POST, PUT, DELETE) in one file, and my API was working in the browser.

Error handlers for 404 and 400 made the API feel production-quality.

**Ran today:** `day4/flask_api.py`

---

## Day 5 — Week 4 Final Project: Flask + SQLite

Combined Flask and SQLite into a real backend. Every request reads/writes from a real database file. The `row_factory = sqlite3.Row` trick so rows behave like dicts was a great discovery.

This is a mini version of what real web backends look like.

**Ran today:** `day5/week4_final_project.py`
