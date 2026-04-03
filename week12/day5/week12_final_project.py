# =============================================================================
# WEEK 12 - DAY 5: FINAL PROJECT — Internship Portfolio Generator
# Intern: ISHAAN GARG
# Topic: Generate a complete HTML portfolio report for the 12-week internship
# =============================================================================

import os
from datetime import datetime

print("=" * 60)
print("  WEEK 12 FINAL PROJECT: PORTFOLIO GENERATOR")
print("  Intern: ISHAAN GARG")
print("=" * 60)

# ─── Internship Data ─────────────────────────────────────────────
INTERN_NAME = "ISHAAN GARG"
COMPANY     = "TechCorp AI"

WEEKS = [
    {
        "week": 1, "title": "Python Foundations",
        "topics": ["HTTP & Internet", "Git & GitHub", "Python Environments", "AI/ML Concepts", "API Integration"],
        "skills": ["Python", "Git", "Virtual Environments", "REST APIs"],
        "project": "Multi-API Data Report",
        "highlight": "Called 3 real APIs, saved structured JSON report",
    },
    {
        "week": 2, "title": "Python Intermediate",
        "topics": ["Data Structures", "Functions & File I/O", "OOP", "Error Handling", "Python Modules"],
        "skills": ["OOP", "File Handling", "Error Handling", "json/os/datetime"],
        "project": "Learning Dashboard with XP System",
        "highlight": "CLI app with JSON persistence, XP tracking, report generation",
    },
    {
        "week": 3, "title": "Data Science Foundations",
        "topics": ["NumPy", "Pandas", "Matplotlib & Seaborn", "Data Cleaning & EDA", "Analysis Pipeline"],
        "skills": ["NumPy", "Pandas", "Matplotlib", "Seaborn", "EDA"],
        "project": "Sales Data Analysis Pipeline",
        "highlight": "End-to-end pipeline: generate → clean → analyze → visualize",
    },
    {
        "week": 4, "title": "Databases & APIs",
        "topics": ["SQL Basics", "Advanced SQL", "REST APIs (requests)", "Flask API", "Flask + SQLite"],
        "skills": ["SQLite", "SQL JOINs", "requests", "Flask", "REST API Design"],
        "project": "Flask + SQLite REST API",
        "highlight": "Full CRUD backend with SQL database, tested via test client",
    },
    {
        "week": 5, "title": "Machine Learning",
        "topics": ["Intro to ML & KNN", "Linear/Logistic Regression", "Trees & Forests", "Clustering & PCA", "Model Comparison"],
        "skills": ["scikit-learn", "KNN", "Regression", "Random Forest", "Cross-validation"],
        "project": "6-Model Comparison Pipeline",
        "highlight": "Trained KNN, LR, DT, RF, GBM, SVM — ranked by accuracy & F1",
    },
    {
        "week": 6, "title": "Deep Learning & NLP",
        "topics": ["Neural Networks (Keras)", "CNNs & MNIST", "Transfer Learning", "NLP & TF-IDF", "Sentiment Analysis"],
        "skills": ["TensorFlow/Keras", "CNNs", "Transfer Learning", "NLP", "TF-IDF"],
        "project": "3-Class Sentiment Analyzer",
        "highlight": "Positive/neutral/negative classifier with 90%+ accuracy",
    },
    {
        "week": 7, "title": "Scraping, Automation & Concurrency",
        "topics": ["BeautifulSoup", "File Automation", "Regex", "Threading & Multiprocessing", "Concurrent Pipeline"],
        "skills": ["BeautifulSoup", "Regex", "threading", "multiprocessing", "glob/shutil"],
        "project": "Threaded Web Data Pipeline",
        "highlight": "Fetched 10 users + 100 posts concurrently — 4x faster than sequential",
    },
    {
        "week": 8, "title": "Docker & Deployment",
        "topics": ["Docker Concepts", "Production Flask", "Testing & CI/CD", "Cloud Services (AWS)", "Production ML API"],
        "skills": ["Docker", "Gunicorn", "unittest", "GitHub Actions", "AWS concepts"],
        "project": "Production ML API with Dockerfile",
        "highlight": "Sentiment API with tests, health check, batch endpoint, Docker-ready",
    },
    {
        "week": 9, "title": "LLMs & Prompt Engineering",
        "topics": ["LLM Concepts & APIs", "Prompt Engineering", "RAG Pipeline", "AI Agents & Tool Use", "AI Chatbot"],
        "skills": ["Prompt Engineering", "RAG", "TF-IDF Retrieval", "Agent Design", "LLM APIs"],
        "project": "AI Study Assistant Chatbot",
        "highlight": "RAG chatbot with 12-doc knowledge base, calculator tool, quiz mode",
    },
    {
        "week": 10, "title": "System Design",
        "topics": ["System Design Fundamentals", "Design Patterns", "Redis & Caching", "Message Queues", "URL Shortener"],
        "skills": ["System Design", "Design Patterns", "Caching", "Message Queues", "Async Processing"],
        "project": "Scalable URL Shortener",
        "highlight": "Cache-aside + async analytics queue + hash-based short codes",
    },
    {
        "week": 11, "title": "Capstone Project",
        "topics": ["Architecture Planning", "DB Layer + CRUD", "AI Analysis Service", "Analytics + Tests", "Integration"],
        "skills": ["Full-stack Integration", "API Design", "AI Feature Engineering", "Test Suite"],
        "project": "JobTracker AI (Full-Stack App)",
        "highlight": "Flask + SQLite + ML: job tracker with skill extraction, priority scoring, analytics",
    },
    {
        "week": 12, "title": "Career Preparation",
        "topics": ["DSA & Interview Prep", "Python Interview Q&A", "Resume & GitHub", "Learning Roadmaps", "Portfolio"],
        "skills": ["DSA", "Interview Prep", "Technical Communication", "Career Planning"],
        "project": "Portfolio Generator",
        "highlight": "Auto-generated HTML internship portfolio with all 12 weeks",
    },
]

ALL_SKILLS = sorted(set(
    skill for w in WEEKS for skill in w["skills"]
))

# ─── Stats ────────────────────────────────────────────────────────
total_topics   = sum(len(w["topics"]) for w in WEEKS)
total_projects = len(WEEKS)
total_skills   = len(ALL_SKILLS)

# ─── HTML Report Generator ────────────────────────────────────────
def generate_html():
    skill_badges = "".join(
        f'<span style="display:inline-block;background:#e0f2fe;color:#0369a1;'
        f'padding:4px 12px;border-radius:20px;margin:3px;font-size:13px;'
        f'font-weight:500;">{s}</span>'
        for s in ALL_SKILLS
    )

    week_cards = ""
    for w in WEEKS:
        topics_html = "".join(f"<li>{t}</li>" for t in w["topics"])
        skill_tags  = "".join(
            f'<span style="background:#f0fdf4;color:#166534;padding:2px 8px;'
            f'border-radius:12px;font-size:12px;margin:2px;display:inline-block;">{s}</span>'
            for s in w["skills"]
        )
        week_cards += f"""
        <div style="background:white;border-radius:12px;padding:24px;margin:16px 0;
                    box-shadow:0 2px 8px rgba(0,0,0,0.08);border-left:4px solid #3b82f6;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                <h3 style="margin:0;color:#1e293b;">Week {w['week']}: {w['title']}</h3>
                <span style="background:#dbeafe;color:#1d4ed8;padding:4px 12px;border-radius:20px;font-size:13px;">
                    W{w['week']:02d}
                </span>
            </div>
            <ul style="color:#475569;margin:8px 0 12px 16px;font-size:14px;">{topics_html}</ul>
            <div style="background:#f8fafc;border-radius:8px;padding:12px;margin-bottom:12px;">
                <strong style="color:#0f172a;">🚀 Project:</strong>
                <span style="color:#1d4ed8;font-weight:600;"> {w['project']}</span><br>
                <span style="color:#64748b;font-size:13px;">✨ {w['highlight']}</span>
            </div>
            <div>{skill_tags}</div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{INTERN_NAME} — Internship Portfolio</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: #f1f5f9; color: #334155; line-height: 1.6; }}
  .container {{ max-width: 900px; margin: 0 auto; padding: 32px 24px; }}
  .header {{ background: linear-gradient(135deg, #1e40af, #7c3aed);
             color: white; border-radius: 16px; padding: 40px; text-align: center; margin-bottom: 32px; }}
  .header h1 {{ font-size: 32px; margin-bottom: 8px; }}
  .header p  {{ opacity: 0.85; font-size: 16px; }}
  .stats {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 32px; }}
  .stat  {{ background: white; border-radius: 12px; padding: 24px; text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  .stat-num {{ font-size: 36px; font-weight: 700; color: #3b82f6; }}
  .stat-lbl {{ color: #64748b; font-size: 14px; margin-top: 4px; }}
  h2 {{ font-size: 22px; color: #1e293b; margin: 32px 0 16px; }}
  .skills-box {{ background: white; border-radius: 12px; padding: 24px;
                 box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 32px; }}
  .footer {{ text-align: center; color: #94a3b8; font-size: 13px; margin-top: 48px; padding: 24px; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>🎓 {INTERN_NAME}</h1>
    <p>Software Development Internship — {COMPANY}</p>
    <p style="margin-top:8px;opacity:0.7;font-size:14px;">
      12 Weeks · {total_topics} Topics · {total_projects} Projects · {total_skills} Skills
    </p>
  </div>

  <div class="stats">
    <div class="stat"><div class="stat-num">12</div><div class="stat-lbl">Weeks Completed</div></div>
    <div class="stat"><div class="stat-num">{total_topics}</div><div class="stat-lbl">Topics Covered</div></div>
    <div class="stat"><div class="stat-num">{total_skills}</div><div class="stat-lbl">Skills Acquired</div></div>
  </div>

  <div class="skills-box">
    <h2 style="margin:0 0 16px;">🛠️ Full Skill Set</h2>
    {skill_badges}
  </div>

  <h2>📅 Week-by-Week Journey</h2>
  {week_cards}

  <div class="footer">
    <p>Generated by Portfolio Generator · {INTERN_NAME} · {datetime.now().strftime('%B %Y')}</p>
    <p style="margin-top:4px;">Built with Python, Flask, scikit-learn, and 12 weeks of hard work 🚀</p>
  </div>
</div>
</body>
</html>"""
    return html

# ─── Generate and Save ────────────────────────────────────────────
html_content = generate_html()
output_file = "navkiran_portfolio.html"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

size_kb = os.path.getsize(output_file) / 1024
print(f"\n✅ Portfolio HTML generated: {output_file} ({size_kb:.1f} KB)")
print(f"\nPortfolio Summary:")
print(f"  Intern     : {INTERN_NAME}")
print(f"  Company    : {COMPANY}")
print(f"  Weeks      : 12")
print(f"  Topics     : {total_topics}")
print(f"  Projects   : {total_projects}")
print(f"  Skills     : {total_skills}")
print(f"\nAll skills learned:")
for i, skill in enumerate(ALL_SKILLS):
    end = "\n" if (i+1) % 6 == 0 else ""
    print(f"  {skill:25s}", end=end)

os.remove(output_file)
print(f"\n\n{'=' * 60}")
print(f"  🎉 INTERNSHIP COMPLETE!")
print(f"  {'=' * 56}")
print(f"  Ishaan Garg has completed 12 weeks of intensive")
print(f"  software development training, building real projects")
print(f"  across Python, Data Science, ML, Deep Learning, APIs,")
print(f"  Web Scraping, Docker, LLMs, and System Design.")
print(f"  {'=' * 56}")
print(f"  From 'Hello World' to production-grade AI systems.")
print(f"  The journey continues. 🚀")
print(f"{'=' * 60}")
