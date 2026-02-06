# =============================================================================
# WEEK 3 - DAY 2: Pandas — Data Analysis Library
# Intern: ISHAAN GARG
# Topic: Series, DataFrames, loading CSV, filtering, groupby
# =============================================================================

import pandas as pd
import numpy as np

print("=" * 50)
print("SECTION 1: SERIES")
print("=" * 50)

# A Series is a labeled 1D array
scores = pd.Series([85, 92, 78, 95, 88], index=["Navkiran", "Alice", "Bob", "Charlie", "Diana"])
print("Scores:\n", scores)
print("\nNavkiran's score:", scores["Navkiran"])
print("Above 90:\n", scores[scores > 90])

print("\n" + "=" * 50)
print("SECTION 2: DATAFRAME")
print("=" * 50)

# A DataFrame is a 2D table (like an Excel spreadsheet)
data = {
    "Name":       ["Navkiran", "Alice", "Bob", "Charlie", "Diana"],
    "Age":        [21, 22, 23, 21, 24],
    "City":       ["Ludhiana", "Delhi", "Mumbai", "Chennai", "Pune"],
    "Score":      [85, 92, 78, 95, 88],
    "Department": ["AI", "Web", "Data", "AI", "Web"]
}
df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("dtypes:\n", df.dtypes)

print("\n" + "=" * 50)
print("SECTION 3: EXPLORING DATA")
print("=" * 50)

print("First 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nDescribe (stats):\n", df.describe())
print("\nInfo:")
df.info()

print("\n" + "=" * 50)
print("SECTION 4: SELECTING DATA")
print("=" * 50)

# Select a column
print("Names:\n", df["Name"])

# Select multiple columns
print("\nName & Score:\n", df[["Name", "Score"]])

# Select rows by index
print("\nRow 0:\n", df.iloc[0])
print("\nRows 1-3:\n", df.iloc[1:4])

# Select by label/condition
print("\nAI department:\n", df[df["Department"] == "AI"])
print("\nScore > 85:\n", df[df["Score"] > 85])
print("\nAI AND Score > 85:\n", df[(df["Department"] == "AI") & (df["Score"] > 85)])

print("\n" + "=" * 50)
print("SECTION 5: ADDING & MODIFYING DATA")
print("=" * 50)

df["Grade"] = df["Score"].apply(lambda s: "A" if s >= 90 else ("B" if s >= 80 else "C"))
print("With Grade column:\n", df)

df["Score_Boosted"] = df["Score"] * 1.05
df["Score_Boosted"] = df["Score_Boosted"].round(1)
print("\nWith Boosted Score:\n", df[["Name", "Score", "Score_Boosted"]])

print("\n" + "=" * 50)
print("SECTION 6: GROUPBY AND AGGREGATION")
print("=" * 50)

grouped = df.groupby("Department")["Score"].mean()
print("Average score per department:\n", grouped)

grouped2 = df.groupby("Department").agg({"Score": ["mean", "max", "min"], "Age": "mean"})
print("\nFull aggregation:\n", grouped2)

print("\n" + "=" * 50)
print("SECTION 7: SORTING AND MISSING DATA")
print("=" * 50)

sorted_df = df.sort_values("Score", ascending=False)
print("Sorted by Score (desc):\n", sorted_df[["Name", "Score"]])

# Handling missing data
df_missing = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Score": [85, None, 90, None],
    "City": ["Delhi", "Mumbai", None, "Pune"]
})
print("\nWith missing values:\n", df_missing)
print("\nNull counts:\n", df_missing.isnull().sum())

df_filled = df_missing.fillna({"Score": df_missing["Score"].mean(), "City": "Unknown"})
print("\nAfter filling NaN:\n", df_filled)

print("\n" + "=" * 50)
print("SECTION 8: SAVE AND LOAD CSV")
print("=" * 50)

df.to_csv("students.csv", index=False)
print("Saved to students.csv")

loaded = pd.read_csv("students.csv")
print("Loaded back:\n", loaded.head())

import os; os.remove("students.csv")
print("Cleaned up.")

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("pd.Series()       → 1D labeled array")
print("pd.DataFrame()    → 2D table")
print("df.head()/tail()  → preview data")
print("df[condition]     → filter rows")
print("df.groupby()      → group and aggregate")
print("df.fillna()       → handle missing values")
print("df.to_csv()       → save to file")
