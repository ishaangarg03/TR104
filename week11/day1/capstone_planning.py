# =============================================================================
# WEEK 11 - DAY 1: Capstone Project Planning & Architecture
# Intern: ISHAAN GARG
# Topic: Plan and architect a full-stack AI project
# =============================================================================

print("=" * 60)
print("  WEEK 11 — CAPSTONE PROJECT: AI-POWERED JOB TRACKER")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
PROJECT: JobTracker AI
=======================
A full-stack app where job seekers can:
  1. Add job applications (company, role, status)
  2. Get AI-powered resume suggestions
  3. Track application status (applied, interview, offer, rejected)
  4. View analytics on their job search
  5. Get smart reminders for follow-ups

TECH STACK:
  Backend:  Flask + SQLite (REST API)
  AI Layer: Sentiment + keyword analysis (scikit-learn)
  Frontend: HTML/CSS served by Flask (no JS framework needed)
  Testing:  unittest
  Deployment-ready: Dockerfile included

WHY THIS PROJECT?
  Combines ALL 10 weeks of learning:
  Week 1-2  → Python, OOP, file handling
  Week 3    → Data analysis (pandas, stats)
  Week 4    → SQL database + Flask API
  Week 5-6  → ML model for job description analysis
  Week 7    → Web scraping + automation concepts
  Week 8    → Testing, Docker, production patterns
  Week 9    → LLM/AI assistant concepts
  Week 10   → System design, caching, design patterns
""")

print("=" * 60)
print("SECTION 1: DATA MODEL")
print("=" * 60)

SCHEMA = """
CREATE TABLE jobs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    company      TEXT    NOT NULL,
    role         TEXT    NOT NULL,
    status       TEXT    DEFAULT 'applied',   -- applied/interview/offer/rejected
    applied_on   TEXT,
    salary_min   INTEGER,
    salary_max   INTEGER,
    location     TEXT,
    job_desc     TEXT,
    notes        TEXT,
    priority     INTEGER DEFAULT 2,           -- 1=high 2=medium 3=low
    match_score  REAL    DEFAULT 0,           -- AI-computed score
    created_at   TEXT    DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE interviews (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id     INTEGER REFERENCES jobs(id),
    round      TEXT,   -- phone/technical/hr/final
    scheduled  TEXT,
    notes      TEXT,
    outcome    TEXT
);

CREATE TABLE skills (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT UNIQUE
);

CREATE TABLE job_skills (
    job_id   INTEGER REFERENCES jobs(id),
    skill_id INTEGER REFERENCES skills(id),
    PRIMARY KEY (job_id, skill_id)
);
"""

print("Database Schema:")
print(SCHEMA)

print("=" * 60)
print("SECTION 2: API ENDPOINTS DESIGN")
print("=" * 60)

endpoints = [
    ("GET",    "/api/v1/jobs",              "List all jobs (filter by status)"),
    ("POST",   "/api/v1/jobs",              "Add new job application"),
    ("GET",    "/api/v1/jobs/<id>",         "Get job details"),
    ("PUT",    "/api/v1/jobs/<id>",         "Update job (status, notes)"),
    ("DELETE", "/api/v1/jobs/<id>",         "Delete a job"),
    ("POST",   "/api/v1/jobs/<id>/analyze", "AI analysis of job description"),
    ("GET",    "/api/v1/analytics",         "Dashboard stats"),
    ("GET",    "/api/v1/analytics/funnel",  "Application funnel data"),
    ("POST",   "/api/v1/interviews",        "Schedule an interview"),
    ("GET",    "/health",                   "Health check"),
]

print(f"{'Method':6s} | {'Endpoint':35s} | Description")
print("-" * 75)
for method, path, desc in endpoints:
    print(f"  {method:6s} | {path:35s} | {desc}")

print("\n" + "=" * 60)
print("SECTION 3: AI FEATURES PLAN")
print("=" * 60)

print("""
AI Feature 1: Job Description Analyzer
  Input:  Raw job description text
  Output: Required skills, seniority level, match score
  How:    TF-IDF keyword extraction + rule-based skill detection

AI Feature 2: Application Priority Scorer
  Input:  Company, role, salary, description
  Output: Priority score (1-10) 
  How:    Weighted scoring based on keywords + salary range

AI Feature 3: Smart Notes Generator
  Input:  Job description + your resume keywords
  Output: Suggested talking points for interview
  How:    Keyword overlap analysis

AI Feature 4: Status Prediction
  Input:  Time since applied, follow-up count, company size
  Output: Predicted outcome probability
  How:    Logistic regression on historical data
""")

print("=" * 60)
print("SECTION 4: PROJECT FILE STRUCTURE")
print("=" * 60)

structure = """
job_tracker/
├── app.py                 ← Flask application entry point
├── config.py              ← Configuration (DB path, secrets)
├── requirements.txt       ← Dependencies
├── Dockerfile             ← Container definition
├── README.md              ← Setup instructions
│
├── models/
│   ├── __init__.py
│   ├── database.py        ← SQLite connection, init_db()
│   └── job.py             ← Job class (OOP model)
│
├── routes/
│   ├── __init__.py
│   ├── jobs.py            ← CRUD endpoints
│   ├── analytics.py       ← Stats endpoints
│   └── ai_features.py     ← ML/AI endpoints
│
├── services/
│   ├── ai_analyzer.py     ← Job description analysis
│   └── scoring.py         ← Priority scoring
│
└── tests/
    ├── test_jobs.py        ← Unit + integration tests
    └── test_ai.py          ← AI feature tests
"""
print(structure)

print("=" * 60)
print("SECTION 5: DEVELOPMENT PLAN (DAYS 2-5)")
print("=" * 60)
print("""
Day 2: Database layer + OOP model + CRUD API
Day 3: AI analysis service + scoring
Day 4: Analytics endpoints + full test suite
Day 5: Integration, polish, README, Dockerfile
""")

print("Week 11 Day 1 complete — Architecture planned!")
print("=" * 60)
