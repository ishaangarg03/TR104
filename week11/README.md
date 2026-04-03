# Week 11 — Capstone Project: JobTracker AI
## Intern: ISHAAN GARG

| Day | File | Topic |
|-----|------|-------|
| Day 1 | `day1/capstone_planning.py` | Architecture, schema, API design, AI features plan |
| Day 5 | `day5/week11_capstone.py` | Full implementation: Flask + SQLite + AI + Tests |

## What This Project Covers
- Flask REST API (CRUD for job applications)
- SQLite database with relational schema
- AI job description analyzer (skill extraction, seniority detection)
- Priority scoring based on salary + match score
- Analytics endpoint (funnel stats)
- Full unittest test suite (6 tests)
- Health check endpoint

## Setup
```bash
pip install flask scikit-learn numpy
python day5/week11_capstone.py
```

## Sample API Calls
```bash
# Add a job
curl -X POST http://localhost:5000/api/v1/jobs \
  -H "Content-Type: application/json" \
  -d '{"company":"Google","role":"ML Engineer","job_desc":"python tensorflow docker"}'

# List all jobs
curl http://localhost:5000/api/v1/jobs

# Get analytics
curl http://localhost:5000/api/v1/analytics
```
