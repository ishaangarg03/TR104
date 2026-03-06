# =============================================================================
# WEEK 7 - DAY 2: Python Automation — Files, Folders, Scheduling
# Intern: ISHAAN GARG
# Topic: Automate repetitive tasks with Python
# =============================================================================

import os
import shutil
import glob
import time
from datetime import datetime
import json
import re

print("=" * 55)
print("SECTION 1: FILE AND FOLDER AUTOMATION")
print("=" * 55)

# Create a test workspace
os.makedirs("workspace/reports", exist_ok=True)
os.makedirs("workspace/images", exist_ok=True)
os.makedirs("workspace/data", exist_ok=True)
os.makedirs("workspace/archive", exist_ok=True)

# Create dummy files
files_to_create = [
    ("workspace/report_jan.pdf",   "PDF report January"),
    ("workspace/report_feb.pdf",   "PDF report February"),
    ("workspace/data_export.csv",  "name,score\nNavkiran,88"),
    ("workspace/photo1.jpg",       "fake image data 1"),
    ("workspace/photo2.png",       "fake image data 2"),
    ("workspace/notes.txt",        "internship notes"),
    ("workspace/old_report.pdf",   "very old report"),
]
for path, content in files_to_create:
    with open(path, "w") as f:
        f.write(content)

print("Created test workspace:")
for f in os.listdir("workspace"):
    print(f"  {f}")

print("\n--- Organizing files by type ---")
rules = {".pdf": "reports", ".csv": "data", ".jpg": "images", ".png": "images"}
for fname in os.listdir("workspace"):
    ext = os.path.splitext(fname)[1].lower()
    if ext in rules:
        src = f"workspace/{fname}"
        dst = f"workspace/{rules[ext]}/{fname}"
        shutil.move(src, dst)
        print(f"  Moved {fname} → {rules[ext]}/")

print("\nAfter organizing:")
for folder in ["reports", "images", "data"]:
    files = os.listdir(f"workspace/{folder}")
    print(f"  workspace/{folder}/: {files}")

print("\n" + "=" * 55)
print("SECTION 2: BULK RENAME FILES")
print("=" * 55)

for i, fname in enumerate(os.listdir("workspace/reports"), 1):
    old_path = f"workspace/reports/{fname}"
    date_str = datetime.now().strftime("%Y%m%d")
    new_name = f"{date_str}_report_{i:02d}.pdf"
    new_path = f"workspace/reports/{new_name}"
    os.rename(old_path, new_path)
    print(f"  {fname} → {new_name}")

print("\n" + "=" * 55)
print("SECTION 3: FIND FILES WITH GLOB")
print("=" * 55)

all_pdfs = glob.glob("workspace/**/*.pdf", recursive=True)
print(f"All PDF files found ({len(all_pdfs)}):")
for f in all_pdfs:
    size = os.path.getsize(f)
    print(f"  {f} ({size} bytes)")

print("\n" + "=" * 55)
print("SECTION 4: AUTOMATED REPORT GENERATOR")
print("=" * 55)

def generate_daily_report(data):
    """Simulate generating a daily data report."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"workspace/data/daily_report_{timestamp}.json"
    report = {
        "generated_at": datetime.now().isoformat(),
        "records": len(data),
        "summary": {
            "total_score": sum(d["score"] for d in data),
            "avg_score":   round(sum(d["score"] for d in data) / len(data), 2),
        },
        "data": data
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    print(f"Report generated: {filename}")
    return filename

sample_data = [
    {"name": "Navkiran", "score": 88, "dept": "AI"},
    {"name": "Alice",    "score": 92, "dept": "Web"},
    {"name": "Bob",      "score": 78, "dept": "Data"},
]
report_file = generate_daily_report(sample_data)

with open(report_file) as f:
    loaded = json.load(f)
print(f"Loaded report: {loaded['records']} records, avg score {loaded['summary']['avg_score']}")

print("\n" + "=" * 55)
print("SECTION 5: SCHEDULED TASKS CONCEPT")
print("=" * 55)

print("""
To schedule tasks in Python:

Option 1 — schedule library (pip install schedule):

  import schedule, time

  def job():
      print("Running daily report...")

  schedule.every().day.at("09:00").do(job)
  schedule.every(10).minutes.do(job)
  schedule.every().monday.do(job)

  while True:
      schedule.run_pending()
      time.sleep(60)

Option 2 — cron (Linux/Mac):
  Add to crontab:  0 9 * * * python3 /path/to/script.py

Option 3 — Task Scheduler (Windows):
  Control Panel → Task Scheduler → create basic task
""")

print("=" * 55)
print("SECTION 6: ENVIRONMENT VARIABLES FOR CONFIG")
print("=" * 55)

os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"
os.environ["API_KEY"] = "secret_key_123"

def load_config():
    return {
        "db_host": os.environ.get("DB_HOST", "localhost"),
        "db_port": int(os.environ.get("DB_PORT", 5432)),
        "api_key": os.environ.get("API_KEY"),
        "debug":   os.environ.get("DEBUG", "false").lower() == "true",
    }

config = load_config()
print("Loaded config:", {k: ("***" if "key" in k else v) for k, v in config.items()})
print("(API key is masked for security)")

# Cleanup
shutil.rmtree("workspace")
print("\nWorkspace cleaned up.")

print("\n" + "=" * 55)
print("SUMMARY")
print("=" * 55)
print("os.makedirs()       → create directories")
print("shutil.move()       → move files")
print("os.rename()         → rename files")
print("glob.glob('**/*.x') → find files by pattern")
print("schedule library    → run functions on a schedule")
print("os.environ.get()    → read config from env vars")
