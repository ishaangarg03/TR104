# =============================================================================
# WEEK 4 - DAY 4: Build Your Own API with Flask
# Intern: ISHAAN GARG
# Topic: Create REST endpoints, handle routes, return JSON
# =============================================================================

# pip install flask

# -----------------------------------------------------------------------
# HOW TO RUN:
#   python day4/flask_api.py
#   Then open browser: http://127.0.0.1:5000/
#   Or use curl / Postman to test endpoints
# -----------------------------------------------------------------------

from flask import Flask, jsonify, request, abort
import json
from datetime import datetime

app = Flask(__name__)

# --- In-memory "database" ---
students = [
    {"id": 1, "name": "Ishaan Garg", "department": "AI",      "score": 88.5},
    {"id": 2, "name": "Alice Singh",   "department": "Web",     "score": 91.0},
    {"id": 3, "name": "Bob Sharma",    "department": "Data",    "score": 78.3},
    {"id": 4, "name": "Charlie Verma", "department": "AI",      "score": 95.0},
    {"id": 5, "name": "Diana Mehta",   "department": "Web",     "score": 82.5},
]
next_id = 6


# =============================================================================
# ROUTES
# =============================================================================

@app.route("/")
def home():
    """API root — shows available endpoints."""
    return jsonify({
        "api": "Internship Student API",
        "intern": "Ishaan Garg",
        "version": "1.0",
        "endpoints": {
            "GET  /students":         "List all students",
            "GET  /students/<id>":    "Get one student",
            "POST /students":         "Add a student",
            "PUT  /students/<id>":    "Update a student",
            "DELETE /students/<id>":  "Delete a student",
            "GET  /stats":            "Summary statistics",
        }
    })


@app.route("/students", methods=["GET"])
def get_students():
    """Return all students. Optional ?dept= filter."""
    dept = request.args.get("dept")
    if dept:
        filtered = [s for s in students if s["department"].lower() == dept.lower()]
        return jsonify({"count": len(filtered), "students": filtered})
    return jsonify({"count": len(students), "students": students})


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Return one student by ID."""
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        abort(404, description=f"Student with id {student_id} not found.")
    return jsonify(student)


@app.route("/students", methods=["POST"])
def add_student():
    """Add a new student. Body: {name, department, score}"""
    global next_id
    body = request.get_json()
    if not body:
        abort(400, description="Request body must be JSON.")

    required = ["name", "department", "score"]
    for field in required:
        if field not in body:
            abort(400, description=f"Missing required field: {field}")

    new_student = {
        "id":         next_id,
        "name":       body["name"],
        "department": body["department"],
        "score":      float(body["score"])
    }
    students.append(new_student)
    next_id += 1
    return jsonify(new_student), 201     # 201 = Created


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update a student's fields."""
    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        abort(404)
    body = request.get_json()
    student.update({k: v for k, v in body.items() if k != "id"})
    return jsonify(student)


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student."""
    global students
    original_count = len(students)
    students = [s for s in students if s["id"] != student_id]
    if len(students) == original_count:
        abort(404, description=f"Student {student_id} not found.")
    return jsonify({"message": f"Student {student_id} deleted."})


@app.route("/stats", methods=["GET"])
def stats():
    """Return summary statistics."""
    if not students:
        return jsonify({"message": "No data."})

    scores = [s["score"] for s in students]
    dept_counts = {}
    for s in students:
        dept_counts[s["department"]] = dept_counts.get(s["department"], 0) + 1

    return jsonify({
        "total_students": len(students),
        "avg_score":      round(sum(scores) / len(scores), 2),
        "max_score":      max(scores),
        "min_score":      min(scores),
        "by_department":  dept_counts,
        "timestamp":      datetime.now().strftime("%Y-%m-%d %H:%M")
    })


# --- Error handlers ---
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found", "message": str(e)}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request", "message": str(e)}), 400


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  Flask API — Ishaan Garg")
    print("  Server: http://127.0.0.1:5000")
    print("=" * 50)
    print("\nTest these URLs in your browser or curl:")
    print("  http://127.0.0.1:5000/")
    print("  http://127.0.0.1:5000/students")
    print("  http://127.0.0.1:5000/students/1")
    print("  http://127.0.0.1:5000/students?dept=AI")
    print("  http://127.0.0.1:5000/stats")
    print("\nPress Ctrl+C to stop the server.\n")
    app.run(debug=True)
