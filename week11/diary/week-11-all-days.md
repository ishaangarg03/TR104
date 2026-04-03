# WEEK 11 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — Capstone Planning

Spent the day designing the JobTracker AI project. Planning before coding is something I now understand deeply — the schema design, endpoint list, and AI features plan saved hours of rework. The file structure mirrors a real production codebase layout.

**Ran today:** `day1/capstone_planning.py`

---

## Day 2 — Database Layer & OOP Model

Implemented the SQLite schema, connection handling, and Job ORM class. The `conn.row_factory = sqlite3.Row` pattern means I never have to manually map columns to dict keys. All 4 CRUD operations working and tested.

**Ran today:** (Day 2 code is in `day5/week11_capstone.py` — all integrated)

---

## Day 3 — AI Analysis Service

The job description analyzer extracts skills using keyword matching — simple but effective. The seniority detection (junior/senior/mid) plus match score gives users actionable information instantly. Computed priority score using multiple signals: salary, match score, remote option.

**Ran today:** (Day 3 code integrated in capstone)

---

## Day 4 — Analytics & Tests

Built analytics endpoints showing funnel statistics (applied → interview → offer). Wrote 6 unit tests covering all major paths. The test suite caught a bug in the status filter endpoint before I shipped it.

**Ran today:** (Day 4 code integrated in capstone)

---

## Day 5 — Integration & Polish

Everything came together: Flask API + SQLite + AI analysis + tests + Dockerfile reference. The live demo adding 4 jobs and seeing the AI-computed priorities and skill lists was genuinely impressive. This is a project I could put on a resume.

**Ran today:** `day5/week11_capstone.py`
