# WEEK 7 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — Web Scraping with BeautifulSoup

Parsing HTML with BeautifulSoup feels like surgery — find the exact element you want and extract it. The `select()` method using CSS selectors was familiar from my HTML knowledge. Always check robots.txt before scraping anything real.

**Ran today:** `day1/web_scraping.py`

---

## Day 2 — Python Automation

Automating file organization feels immediately useful. Using `shutil.move()` and `glob.glob()` to sort files by extension into folders is something I could use in real life right now. The scheduled task concept — running a script every day at 9am — is how production ETL pipelines work.

**Ran today:** `day2/automation.py`

---

## Day 3 — Regular Expressions

Regex was intimidating at first but once I understood the symbols, it clicked. The password validator combining multiple checks (`[A-Z]`, `\d`, `[!@#$%]`) is something I'll reuse in every form I build.

**Ran today:** `day3/regex.py`

---

## Day 4 — Concurrency

The GIL concept was the most surprising thing this week — Python can't truly parallelize CPU code in threads, but it CAN parallelize I/O. The threading speedup demo was impressive: 5 fake API calls in 0.5s instead of 2.5s. `ProcessPoolExecutor` for prime counting showed real CPU speedup.

**Ran today:** `day4/concurrency.py`

---

## Day 5 — Week 7 Final Project: Threaded Pipeline

Combined scraping, concurrency, cleaning, and analysis into one pipeline. Fetching 10 users and their posts concurrently was genuinely faster than sequential. The enriched DataFrame showing post counts and avg title lengths per user felt like real data engineering work.

**Ran today:** `day5/week7_final_project.py`
