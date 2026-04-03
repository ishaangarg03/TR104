# =============================================================================
# WEEK 11 - DAYS 2-5: Capstone Implementation — JobTracker AI
# Intern: ISHAAN GARG
# Topic: Full-stack AI-powered job application tracker
# =============================================================================

import sqlite3, os, json, re, unittest
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# ─── Config ──────────────────────────────────────────────────────
DB_PATH = "jobtracker.db"
app = Flask(__name__)

# ─── Database Layer ───────────────────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
    DROP TABLE IF EXISTS interviews;
    DROP TABLE IF EXISTS jobs;

    CREATE TABLE jobs (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        company     TEXT NOT NULL,
        role        TEXT NOT NULL,
        status      TEXT DEFAULT 'applied',
        applied_on  TEXT,
        salary_min  INTEGER,
        salary_max  INTEGER,
        location    TEXT,
        job_desc    TEXT,
        notes       TEXT,
        priority    INTEGER DEFAULT 2,
        match_score REAL DEFAULT 0,
        created_at  TEXT DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE interviews (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id    INTEGER REFERENCES jobs(id),
        round     TEXT,
        scheduled TEXT,
        notes     TEXT,
        outcome   TEXT DEFAULT 'pending'
    );
    """)
    conn.commit()
    conn.close()

# ─── AI Service ───────────────────────────────────────────────────
TECH_SKILLS = [
    "python","java","javascript","react","node","sql","nosql","flask","django",
    "fastapi","docker","kubernetes","aws","gcp","azure","git","ml","deep learning",
    "nlp","tensorflow","pytorch","pandas","numpy","scikit-learn","redis","postgresql",
    "mongodb","rest","api","microservices","ci/cd","agile","scrum","linux","bash",
]

def analyze_job_description(job_desc: str) -> dict:
    """Extract skills, estimate seniority, compute match score."""
    if not job_desc:
        return {"skills": [], "seniority": "unknown", "match_score": 0}
    text = job_desc.lower()
    found_skills = [s for s in TECH_SKILLS if s in text]
    senior_keywords = ["senior","lead","staff","principal","architect","manager"]
    junior_keywords = ["junior","entry","graduate","intern","fresher","trainee"]
    if any(k in text for k in senior_keywords):
        seniority = "senior"
    elif any(k in text for k in junior_keywords):
        seniority = "junior"
    else:
        seniority = "mid"
    match_score = min(100, len(found_skills) * 8 + (20 if seniority == "junior" else 10))
    salary_match = re.search(r"\d[\d,]*\s*(?:lpa|lakh|k|per annum)", text)
    return {
        "skills":       found_skills,
        "skill_count":  len(found_skills),
        "seniority":    seniority,
        "match_score":  round(match_score, 1),
        "salary_hint":  salary_match.group() if salary_match else None,
    }

def compute_priority(job_data: dict) -> int:
    """Compute priority: 1=high, 2=medium, 3=low."""
    score = 0
    if job_data.get("salary_max") and job_data["salary_max"] > 1000000: score += 2
    if job_data.get("match_score", 0) > 70: score += 2
    if job_data.get("location", "").lower() in ["remote", "wfh"]: score += 1
    if score >= 4: return 1
    if score >= 2: return 2
    return 3

# ─── Job Routes ───────────────────────────────────────────────────
@app.route("/api/v1/jobs", methods=["GET"])
def get_jobs():
    status = request.args.get("status")
    conn = get_db()
    if status:
        rows = conn.execute("SELECT * FROM jobs WHERE status=? ORDER BY priority, created_at DESC",
                            (status,)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM jobs ORDER BY priority, created_at DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route("/api/v1/jobs", methods=["POST"])
def add_job():
    body = request.get_json()
    if not body or not body.get("company") or not body.get("role"):
        return jsonify({"error": "company and role are required"}), 400
    analysis = analyze_job_description(body.get("job_desc", ""))
    priority = compute_priority({**body, "match_score": analysis["match_score"]})
    conn = get_db()
    cur = conn.execute("""
        INSERT INTO jobs (company, role, status, applied_on, salary_min, salary_max,
                         location, job_desc, notes, priority, match_score)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """, (body["company"], body["role"], body.get("status","applied"),
          body.get("applied_on", datetime.now().strftime("%Y-%m-%d")),
          body.get("salary_min"), body.get("salary_max"), body.get("location"),
          body.get("job_desc"), body.get("notes"), priority, analysis["match_score"]))
    conn.commit()
    row = conn.execute("SELECT * FROM jobs WHERE id=?", (cur.lastrowid,)).fetchone()
    conn.close()
    return jsonify({**dict(row), "ai_analysis": analysis}), 201

@app.route("/api/v1/jobs/<int:job_id>", methods=["GET"])
def get_job(job_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
    conn.close()
    if not row: return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))

@app.route("/api/v1/jobs/<int:job_id>", methods=["PUT"])
def update_job(job_id):
    body = request.get_json()
    conn = get_db()
    allowed = ["status","notes","salary_min","salary_max","location","priority"]
    for field, val in body.items():
        if field in allowed:
            conn.execute(f"UPDATE jobs SET {field}=? WHERE id=?", (val, job_id))
    conn.commit()
    row = conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
    conn.close()
    if not row: return jsonify({"error":"Not found"}), 404
    return jsonify(dict(row))

@app.route("/api/v1/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    conn = get_db()
    conn.execute("DELETE FROM jobs WHERE id=?", (job_id,))
    conn.commit(); conn.close()
    return jsonify({"message": f"Job {job_id} deleted"})

@app.route("/api/v1/jobs/<int:job_id>/analyze", methods=["POST"])
def analyze_job(job_id):
    conn = get_db()
    row = conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
    conn.close()
    if not row: return jsonify({"error":"Not found"}), 404
    analysis = analyze_job_description(row["job_desc"] or "")
    return jsonify({"job_id": job_id, "analysis": analysis})

# ─── Analytics Routes ─────────────────────────────────────────────
@app.route("/api/v1/analytics")
def analytics():
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]
    by_status = conn.execute("SELECT status, COUNT(*) as cnt FROM jobs GROUP BY status").fetchall()
    avg_score = conn.execute("SELECT AVG(match_score) FROM jobs").fetchone()[0]
    high_pri  = conn.execute("SELECT COUNT(*) FROM jobs WHERE priority=1").fetchone()[0]
    conn.close()
    return jsonify({
        "total_applications": total,
        "by_status": {r["status"]: r["cnt"] for r in by_status},
        "avg_match_score": round(avg_score or 0, 1),
        "high_priority_count": high_pri,
    })

@app.route("/health")
def health():
    return jsonify({"status":"healthy","version":"1.0.0","intern":"Ishaan Garg"})

# ─── Tests ────────────────────────────────────────────────────────
class TestJobTracker(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_add_job(self):
        r = self.client.post("/api/v1/jobs", json={
            "company": "TechCorp", "role": "AI Engineer",
            "job_desc": "Python, machine learning, deep learning, docker, kubernetes"
        })
        self.assertEqual(r.status_code, 201)
        d = r.get_json()
        self.assertEqual(d["company"], "TechCorp")
        self.assertIn("ai_analysis", d)
        self.assertGreater(len(d["ai_analysis"]["skills"]), 0)

    def test_list_jobs(self):
        self.client.post("/api/v1/jobs", json={"company": "A", "role": "Dev"})
        self.client.post("/api/v1/jobs", json={"company": "B", "role": "ML"})
        r = self.client.get("/api/v1/jobs")
        self.assertEqual(r.status_code, 200)
        self.assertGreaterEqual(len(r.get_json()), 2)

    def test_update_status(self):
        r = self.client.post("/api/v1/jobs", json={"company": "X", "role": "Y"})
        job_id = r.get_json()["id"]
        r2 = self.client.put(f"/api/v1/jobs/{job_id}", json={"status": "interview"})
        self.assertEqual(r2.get_json()["status"], "interview")

    def test_analytics(self):
        self.client.post("/api/v1/jobs", json={"company": "A", "role": "Dev"})
        r = self.client.get("/api/v1/analytics")
        d = r.get_json()
        self.assertIn("total_applications", d)
        self.assertGreaterEqual(d["total_applications"], 1)

    def test_ai_analysis(self):
        desc = "We need a Python developer with scikit-learn, pandas, and REST API experience."
        result = analyze_job_description(desc)
        self.assertIn("python", result["skills"])
        self.assertGreater(result["match_score"], 0)

    def test_health(self):
        r = self.client.get("/health")
        self.assertEqual(r.status_code, 200)

# ─── Main ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("  WEEK 11 CAPSTONE: JobTracker AI")
    print("  Intern: ISHAAN GARG")
    print("=" * 60)

    init_db()
    print("\n--- Running Tests ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJobTracker)
    unittest.TextTestRunner(verbosity=2).run(suite)

    init_db()
    print("\n--- Live Demo ---")
    with app.test_client() as client:
        jobs_to_add = [
            {"company": "Google DeepMind", "role": "ML Engineer",
             "job_desc": "Python, tensorflow, pytorch, deep learning, ml, docker, kubernetes",
             "location": "Remote", "salary_max": 3000000},
            {"company": "Flipkart", "role": "Data Scientist",
             "job_desc": "Python, pandas, scikit-learn, sql, postgresql, ml",
             "location": "Bangalore", "salary_max": 1800000},
            {"company": "Startup XYZ", "role": "Junior Python Developer",
             "job_desc": "junior python flask rest api git docker entry level",
             "location": "Remote", "salary_max": 800000},
            {"company": "TCS", "role": "Backend Developer",
             "job_desc": "java python sql rest api microservices agile",
             "location": "Ludhiana", "salary_max": 1200000},
        ]
        for job in jobs_to_add:
            r = client.post("/api/v1/jobs", json=job)
            d = r.get_json()
            print(f"\n  Added: {d['company']} — {d['role']}")
            print(f"    Priority: {d['priority']} | Match Score: {d['match_score']}")
            print(f"    Skills: {d['ai_analysis']['skills'][:5]}")

        client.put("/api/v1/jobs/1", json={"status": "interview",
                   "notes": "Phone screen went well, technical round next week"})
        print("\n  Updated Google job status → interview")

        r = client.get("/api/v1/analytics")
        print("\n--- Analytics ---")
        print(json.dumps(r.get_json(), indent=2))

    if os.path.exists(DB_PATH): os.remove(DB_PATH)
    print("\n✅ Week 11 Capstone Complete — Full-stack AI app built!")
    print("=" * 60)
