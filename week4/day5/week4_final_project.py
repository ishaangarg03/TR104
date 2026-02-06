# =============================================================================
# WEEK 4 - DAY 5: Final Project — Flask API with SQLite Backend
# Intern: ISHAAN GARG
# Topic: Connect Flask routes to a real database
# =============================================================================

# pip install flask

# Run: python day5/week4_final_project.py
# Then visit: http://127.0.0.1:5000/

from flask import Flask, jsonify, request, abort
import sqlite3
import os

DB_PATH = "students.db"
app = Flask(__name__)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row    # makes rows act like dicts
    return conn


def init_db():
    conn = get_db()
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
        CREATE TABLE students (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT    NOT NULL,
            department TEXT    NOT NULL,
            score      REAL    NOT NULL,
            city       TEXT
        )
    """)
    conn.executemany("INSERT INTO students (name, department, score, city) VALUES (?,?,?,?)", [
        ("Ishaan Garg", "AI",      88.5, "Ludhiana"),
        ("Alice Singh",   "Web",     91.0, "Delhi"),
        ("Bob Sharma",    "Data",    78.3, "Mumbai"),
        ("Charlie Verma", "AI",      95.0, "Chennai"),
        ("Diana Mehta",   "Web",     82.5, "Pune"),
    ])
    conn.commit()
    conn.close()
    print("Database initialized with seed data.")


@app.route("/")
def home():
    return jsonify({"api": "Student DB API", "intern": "Ishaan Garg",
                    "routes": ["/students", "/students/<id>", "/stats", "/top"]})


@app.route("/students", methods=["GET"])
def get_all():
    conn = get_db()
    dept = request.args.get("dept")
    if dept:
        rows = conn.execute("SELECT * FROM students WHERE department=? ORDER BY score DESC",
                            (dept,)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM students ORDER BY score DESC").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/students/<int:sid>", methods=["GET"])
def get_one(sid):
    conn = get_db()
    row = conn.execute("SELECT * FROM students WHERE id=?", (sid,)).fetchone()
    conn.close()
    if not row:
        abort(404, description=f"Student {sid} not found.")
    return jsonify(dict(row))


@app.route("/students", methods=["POST"])
def add_student():
    body = request.get_json()
    if not body:
        abort(400, description="JSON body required.")
    for field in ["name", "department", "score"]:
        if field not in body:
            abort(400, description=f"Missing field: {field}")
    conn = get_db()
    cur = conn.execute(
        "INSERT INTO students (name, department, score, city) VALUES (?,?,?,?)",
        (body["name"], body["department"], body["score"], body.get("city"))
    )
    conn.commit()
    new_id = cur.lastrowid
    row = conn.execute("SELECT * FROM students WHERE id=?", (new_id,)).fetchone()
    conn.close()
    return jsonify(dict(row)), 201


@app.route("/students/<int:sid>", methods=["PUT"])
def update_student(sid):
    body = request.get_json()
    conn = get_db()
    row = conn.execute("SELECT * FROM students WHERE id=?", (sid,)).fetchone()
    if not row:
        conn.close()
        abort(404)
    allowed = ["name", "department", "score", "city"]
    updates = {k: v for k, v in body.items() if k in allowed}
    for col, val in updates.items():
        conn.execute(f"UPDATE students SET {col}=? WHERE id=?", (val, sid))
    conn.commit()
    row = conn.execute("SELECT * FROM students WHERE id=?", (sid,)).fetchone()
    conn.close()
    return jsonify(dict(row))


@app.route("/students/<int:sid>", methods=["DELETE"])
def delete_student(sid):
    conn = get_db()
    result = conn.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    conn.close()
    if result.rowcount == 0:
        abort(404)
    return jsonify({"message": f"Student {sid} deleted."})


@app.route("/stats", methods=["GET"])
def stats():
    conn = get_db()
    rows = conn.execute("""
        SELECT department, COUNT(*) as count, AVG(score) as avg_score
        FROM students GROUP BY department
    """).fetchall()
    overall = conn.execute("SELECT COUNT(*), AVG(score), MAX(score), MIN(score) FROM students").fetchone()
    conn.close()
    return jsonify({
        "total": overall[0],
        "avg_score": round(overall[1], 2),
        "max_score": overall[2],
        "min_score": overall[3],
        "by_department": [dict(r) for r in rows]
    })


@app.route("/top", methods=["GET"])
def top_students():
    n = int(request.args.get("n", 3))
    conn = get_db()
    rows = conn.execute("SELECT * FROM students ORDER BY score DESC LIMIT ?", (n,)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404

@app.errorhandler(400)
def bad_req(e):
    return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    init_db()
    print("\nFlask + SQLite API running!")
    print("Visit: http://127.0.0.1:5000/students")
    print("Visit: http://127.0.0.1:5000/stats")
    print("Visit: http://127.0.0.1:5000/top?n=3\n")
    try:
        app.run(debug=True)
    finally:
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
