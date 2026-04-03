# =============================================================================
# WEEK 12 - DAY 3: Career Profile — Resume, GitHub, LinkedIn
# Intern: ISHAAN GARG
# Topic: Build a standout developer profile
# =============================================================================

print("=" * 60)
print("  WEEK 12 DAY 3: CAREER PROFILE BUILDING")
print("  Intern: ISHAAN GARG")
print("=" * 60)

print("""
YOUR THREE DIGITAL PROFILES:
  1. GitHub  → shows what you can BUILD
  2. LinkedIn → shows your professional journey
  3. Resume  → your 1-page highlight reel
""")

print("=" * 60)
print("SECTION 1: GITHUB PROFILE BEST PRACTICES")
print("=" * 60)

github_checklist = """
PROFILE SETUP:
  ✓ Professional photo
  ✓ Full name (not just username)
  ✓ Short bio mentioning your focus area
  ✓ Location, email, LinkedIn link
  ✓ Pinned repositories (your best 6 projects)

EACH REPOSITORY SHOULD HAVE:
  ✓ Clear, descriptive name (not "project1" or "test")
  ✓ Proper README.md with:
      - What the project does (2-3 sentences)
      - Technologies used
      - How to install and run
      - Screenshots or output examples
  ✓ requirements.txt or package.json
  ✓ .gitignore (no __pycache__, .env, venv)
  ✓ Meaningful commit messages (not "fix" or "update")
  ✓ Regular commits — show active development

COMMIT MESSAGE GUIDE:
  Bad:  "fix", "update", "changes", "final final v2"
  Good: "Add pagination to /api/v1/jobs endpoint"
        "Fix KeyError when job_desc is None in analyzer"
        "Add unittest suite for JobTracker API"
        "Refactor: extract AI analyzer into separate service"

YOUR TOP PROJECTS TO PIN (from this internship):
  1. jobtracker-ai       → Week 11 capstone (Flask + SQLite + ML)
  2. sales-dashboard     → Week 3 data analysis pipeline
  3. sentiment-api       → Week 8 production ML API with Docker
  4. ai-study-chatbot    → Week 9 RAG chatbot
  5. url-shortener       → Week 10 system design project
  6. ml-model-comparison → Week 5 multi-classifier pipeline
"""
print(github_checklist)

print("=" * 60)
print("SECTION 2: LINKEDIN PROFILE")
print("=" * 60)

linkedin_guide = """
HEADLINE:
  ❌ "Student at XYZ University"
  ✓  "AI/ML Intern | Python | Flask | scikit-learn | Open to full-time"
  ✓  "Software Developer Intern | Building ML-powered backends"

ABOUT SECTION (3-5 sentences):
  Start with: what you do and what you're passionate about
  Middle: key skills and technologies
  End: what you're looking for next

  Example:
  "I'm an AI/ML enthusiast currently completing a 3-month
  hands-on internship at TechCorp, where I built production-
  grade Python APIs, ML pipelines, and a full-stack job tracker
  application. I'm skilled in Python, Flask, scikit-learn,
  pandas, SQL, and Docker. I'm passionate about building AI
  systems that solve real problems. Actively seeking full-time
  SDE / ML Engineer roles."

EXPERIENCE SECTION:
  Company: TechCorp AI (or your company name)
  Role: Software Development Intern (AI/ML)
  Duration: [start] – [end]
  
  Bullet points (use numbers when possible):
  • Built a production Flask REST API serving ML sentiment analysis
    with 97%+ accuracy on 500+ test samples
  • Developed a full-stack JobTracker AI app combining Flask,
    SQLite, and scikit-learn for automated job description analysis
  • Implemented concurrent web scraping pipeline using Python
    threading, reducing data collection time by 4x
  • Wrote 50+ unit tests achieving 90% code coverage across
    3 major project modules

SKILLS SECTION (add all of these):
  Python, Flask, FastAPI, SQL, SQLite, PostgreSQL, REST APIs,
  Machine Learning, scikit-learn, pandas, NumPy, Matplotlib,
  TensorFlow/Keras, Natural Language Processing, Docker,
  Git, GitHub, HTML/CSS, Data Analysis, Unit Testing, Linux

EDUCATION:
  Add your degree. Under it, add relevant coursework:
  "Relevant: Data Structures, Database Management, Statistics"
"""
print(linkedin_guide)

print("=" * 60)
print("SECTION 3: RESUME TEMPLATE")
print("=" * 60)

resume_template = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ISHAAN GARG
Ludhiana, Punjab, India  |  nav@email.com  |  +91-XXXXXXXXXX
LinkedIn: linkedin.com/in/navkiran-kaur  |  GitHub: github.com/navkiran
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
AI/ML developer with hands-on experience building production-grade
Python applications, REST APIs, ML pipelines, and LLM-powered tools.
Proficient in Python, Flask, scikit-learn, SQL, and Docker.

SKILLS
Languages:   Python, SQL, HTML, Bash
Frameworks:  Flask, scikit-learn, TensorFlow/Keras, Pandas, NumPy
Tools:       Git, Docker, SQLite, Redis (concepts), Postman
ML/AI:       Classification, Regression, NLP, Neural Networks, RAG, LLMs
Practices:   REST API Design, Unit Testing, OOP, System Design

EXPERIENCE
Software Development Intern (AI/ML)               [Duration]
TechCorp AI, Ludhiana

• Built Flask + SQLite REST API for JobTracker AI with ML job
  description analyzer achieving 85%+ skill detection accuracy
• Developed 6-model ML comparison pipeline (KNN, LR, RF, SVM,
  GBM, DT) with automated cross-validation and report generation
• Implemented concurrent web scraping pipeline reducing data
  collection time by 4x using Python ThreadPoolExecutor
• Created production-ready sentiment analysis API with Dockerfile,
  health check endpoint, and full unittest coverage (6 test cases)
• Built RAG-based study chatbot combining TF-IDF retrieval with
  conversational interface over 12-document knowledge base

PROJECTS
JobTracker AI (github.com/navkiran/jobtracker-ai)
  Flask REST API + SQLite + scikit-learn | AI job description
  analyzer with skill extraction, seniority detection, priority scoring

Sales Analysis Pipeline (github.com/navkiran/sales-dashboard)
  Python + pandas + Matplotlib | End-to-end data pipeline
  cleaning, analyzing, and visualizing 200-row sales dataset

Sentiment Analysis API (github.com/navkiran/sentiment-api)
  Flask + TF-IDF + Logistic Regression | Production ML API
  with tests, Docker, health check, batch prediction endpoint

EDUCATION
[Your Degree], [Your University]                 [Year]
Relevant coursework: Data Structures, DBMS, Statistics, Algorithms

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
print(resume_template)

print("=" * 60)
print("SECTION 4: JOB SEARCH STRATEGY")
print("=" * 60)

print("""
WHERE TO APPLY:
  LinkedIn Jobs    → most jobs, easy apply
  Naukri.com       → India-specific, great for fresher roles
  Internshala      → internships + fresher jobs
  AngelList/Wellfound → startups
  Company career pages → direct (often less competition)
  GitHub Jobs      → developer-focused roles

APPLICATION TIPS:
  • Customize the first 2 lines of your cover letter for each role
  • Apply within 24 hours of posting (early applicants get seen first)
  • Follow up with a LinkedIn message after 1 week
  • Track applications in a spreadsheet (or your JobTracker app!)

NETWORKING:
  • Connect with every interviewer on LinkedIn after the round
  • Engage with posts by companies you want to work at
  • Attend local Python / ML meetups
  • Contribute to 1 open-source Python project (even small fixes)

SALARY NEGOTIATION:
  • Always ask for more than the first offer (10-20% higher)
  • "I'm very excited about this role. Based on my research and
     the skills I bring, I was hoping for [X]. Is there flexibility?"
  • Benefits matter: WFH, learning budget, health insurance
""")

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("GitHub  → pin 6 best projects, clean READMEs, regular commits")
print("LinkedIn → strong headline, number-driven experience bullets")
print("Resume  → 1 page, quantified achievements, relevant skills")
print("Apply   → LinkedIn + Naukri + direct, follow up after 1 week")
