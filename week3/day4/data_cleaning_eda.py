# =============================================================================
# WEEK 3 - DAY 4: Data Cleaning & Exploratory Data Analysis (EDA)
# Intern: ISHAAN GARG
# Topic: Handle messy real-world data before using it
# =============================================================================

import pandas as pd
import numpy as np

print("=" * 50)
print("SECTION 1: SIMULATING MESSY DATA")
print("=" * 50)

# Real-world data is NEVER clean. Let's simulate a messy CSV.
raw_data = {
    "Name":       ["Navkiran", "alice", "BOB", "  Charlie  ", "Diana", "Eve", None, "Frank"],
    "Age":        [21, 22, None, 21, 150, 24, 23, -5],
    "Score":      [85.5, 92.0, 78.3, None, 88.1, 101.0, 70.0, 65.2],
    "Department": ["AI", "web", "DATA", "ai", "Web", "DATA", "AI", "Backend"],
    "Email":      ["nav@mail.com", "alice@mail.com", "bob@mail.com",
                   "charlie@mail.com", "diana@mail.com",
                   "not-an-email", "frank@mail.com", "frank@mail.com"],
    "Salary":     ["₹30000", "35000", "₹28000", "32,000", None, "40000", "31000", "₹29500"]
}

df = pd.DataFrame(raw_data)
print("Raw messy data:\n", df)
print("\nShape:", df.shape)

print("\n" + "=" * 50)
print("SECTION 2: AUDIT THE DATA")
print("=" * 50)

print("Missing values per column:\n", df.isnull().sum())
print("\nData types:\n", df.dtypes)
print("\nBasic stats:\n", df.describe())
print("\nDuplicate rows:", df.duplicated().sum())

print("\n" + "=" * 50)
print("SECTION 3: FIX MISSING VALUES")
print("=" * 50)

# Drop rows where Name is missing
df = df.dropna(subset=["Name"])
print("After dropping missing Name:", df.shape)

# Fill missing Age with median
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
print(f"Filled missing Age with median: {median_age}")

# Fill missing Score with mean
mean_score = df["Score"].mean()
df["Score"] = df["Score"].fillna(round(mean_score, 1))
print(f"Filled missing Score with mean: {round(mean_score, 1)}")

# Fill missing Salary with "Unknown"
df["Salary"] = df["Salary"].fillna("0")

print("\n" + "=" * 50)
print("SECTION 4: FIX DATA TYPES & INCONSISTENCIES")
print("=" * 50)

# Standardize name: strip whitespace, title case
df["Name"] = df["Name"].str.strip().str.title()
print("Fixed names:", list(df["Name"]))

# Standardize department: uppercase
df["Department"] = df["Department"].str.upper().str.strip()
print("Fixed departments:", list(df["Department"]))

# Clean Salary column: remove ₹, commas → convert to int
df["Salary"] = (df["Salary"].astype(str)
                             .str.replace("₹", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .str.strip()
                             .astype(float)
                             .astype(int))
print("Fixed Salary:", list(df["Salary"]))

print("\n" + "=" * 50)
print("SECTION 5: DETECT AND REMOVE OUTLIERS")
print("=" * 50)

print("Age range before clean:", df["Age"].min(), "–", df["Age"].max())
print("Score range before clean:", df["Score"].min(), "–", df["Score"].max())

# Remove invalid ages (must be 18–60 for interns)
df = df[(df["Age"] >= 18) & (df["Age"] <= 60)]
print(f"After removing invalid ages: {len(df)} rows")

# Cap score at 100 (score can't exceed 100)
df["Score"] = df["Score"].clip(upper=100)
print("Score after capping at 100:", list(df["Score"]))

print("\n" + "=" * 50)
print("SECTION 6: VALIDATE EMAILS")
print("=" * 50)

import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, str(email)))

df["Email_Valid"] = df["Email"].apply(is_valid_email)
print(df[["Name", "Email", "Email_Valid"]])

print("\n" + "=" * 50)
print("SECTION 7: FINAL CLEAN DATASET + EDA")
print("=" * 50)

print("Clean data:\n", df)
print("\nShape:", df.shape)
print("\nDept distribution:\n", df["Department"].value_counts())
print("\nMean score by dept:\n", df.groupby("Department")["Score"].mean().round(1))
print("\nScore quartiles:\n", df["Score"].quantile([0.25, 0.5, 0.75]))

# Correlation
print("\nSalary-Score correlation:", round(df["Score"].corr(df["Salary"]), 3))

print("\n" + "=" * 50)
print("SUMMARY — EDA Checklist")
print("=" * 50)
print("1. Check shape, dtypes, head()")
print("2. Count nulls: df.isnull().sum()")
print("3. Fill/drop missing values")
print("4. Standardize text: .str.strip().str.title()")
print("5. Fix data types")
print("6. Detect outliers (min/max, clip, filter)")
print("7. Validate formats (email, phone)")
print("8. Check value_counts() for categories")
print("9. Check correlations")
