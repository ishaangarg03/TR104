# WEEK 3 — INTERNSHIP DIARY
# Intern: ISHAAN GARG

---

## Day 1 — NumPy Basics

Jumped into the data science stack today. NumPy arrays feel like supercharged lists — the element-wise operations are something plain Python lists can't do. No loops needed for math on 1000 elements.

Boolean indexing was my favorite concept: `arr[arr > 10]` — you just write the condition and it returns only the matching elements. That feels like magic.

**Ran today:** `day1/numpy_basics.py`

---

## Day 2 — Pandas DataFrames

Pandas is what makes Python feel like Excel on steroids. I created DataFrames from dictionaries, filtered rows with conditions, added computed columns, and grouped data by department.

`groupby()` was the most powerful thing I learned. In one line I got the average score per department — that would take many lines manually.

**Ran today:** `day2/pandas_basics.py`

---

## Day 3 — Data Visualization

Charts really do communicate what raw numbers can't. I built line charts, bar charts, scatter plots with trend lines, and a full dashboard with 4 subplots in one figure. Seaborn's boxplot shows outliers instantly — no calculation needed.

The `savefig()` function means I can embed charts in any report automatically.

**Ran today:** `day3/data_visualization.py`

---

## Day 4 — Data Cleaning & EDA

This was humbling. I always assumed data in files would be clean. Today I simulated real-world messy data — inconsistent casing, invalid ages like 150, salaries with ₹ signs and commas, missing values, invalid emails. Cleaning took longer than the analysis itself.

Key lesson: always audit data first with `isnull()`, `describe()`, and `value_counts()` before doing anything else.

**Ran today:** `day4/data_cleaning_eda.py`

---

## Day 5 — Week 3 Final Project: Sales Analysis Pipeline

Built a complete end-to-end pipeline: generate raw data → clean it → engineer features (NetRevenue, DiscountAmt) → analyze by region/product → visualize into a dashboard → export a text report.

This is the closest thing to a real data analyst's daily work. The fact that I built the whole thing from scratch using only what I learned this week is very satisfying.

**Ran today:** `day5/week3_final_project.py`
