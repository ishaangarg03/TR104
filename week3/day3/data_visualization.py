# =============================================================================
# WEEK 3 - DAY 3: Data Visualization — Matplotlib & Seaborn
# Intern: ISHAAN GARG
# Topic: Charts, plots, and visual insights from data
# =============================================================================

# pip install matplotlib seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import os

print("=" * 50)
print("SECTION 1: BASIC MATPLOTLIB PLOTS")
print("=" * 50)

# --- Line Chart ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1200, 1500, 1100, 1800, 2100, 1750]

plt.figure(figsize=(8, 4))
plt.plot(months, sales, marker="o", color="steelblue", linewidth=2, label="Sales")
plt.title("Monthly Sales (Navkiran's Store)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()
print("Saved: line_chart.png")

# --- Bar Chart ---
departments = ["AI", "Web", "Data", "Backend"]
avg_scores = [88, 82, 90, 85]
colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0"]

plt.figure(figsize=(7, 4))
bars = plt.bar(departments, avg_scores, color=colors, edgecolor="black", alpha=0.8)
plt.title("Average Score by Department")
plt.xlabel("Department")
plt.ylabel("Avg Score")
plt.ylim(75, 95)
for bar, score in zip(bars, avg_scores):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(score), ha="center", va="bottom", fontweight="bold")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()
print("Saved: bar_chart.png")

# --- Pie Chart ---
skills = ["Python", "Git", "APIs", "OOP", "Data Analysis"]
percentages = [30, 15, 20, 20, 15]
explode = (0.05,) * len(skills)

plt.figure(figsize=(6, 6))
plt.pie(percentages, labels=skills, autopct="%1.1f%%", explode=explode,
        startangle=90, shadow=True)
plt.title("Navkiran's Skill Distribution")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.close()
print("Saved: pie_chart.png")

# --- Scatter Plot ---
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 50)
exam_scores = study_hours * 7 + np.random.normal(0, 5, 50)

plt.figure(figsize=(7, 4))
plt.scatter(study_hours, exam_scores, alpha=0.6, color="coral", edgecolors="black", s=60)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)
m, b = np.polyfit(study_hours, exam_scores, 1)
x_line = np.linspace(1, 10, 100)
plt.plot(x_line, m * x_line + b, color="red", linestyle="--", label="Trend line")
plt.legend()
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()
print("Saved: scatter_plot.png")

print("\n" + "=" * 50)
print("SECTION 2: SUBPLOTS — MULTIPLE CHARTS IN ONE FIGURE")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Navkiran's Week 3 Dashboard", fontsize=14, fontweight="bold")

# Plot 1: Line
axes[0, 0].plot(months, sales, marker="o", color="steelblue")
axes[0, 0].set_title("Monthly Sales")
axes[0, 0].set_ylabel("Sales (₹)")

# Plot 2: Bar
axes[0, 1].bar(departments, avg_scores, color=colors, alpha=0.8)
axes[0, 1].set_title("Dept Scores")
axes[0, 1].set_ylim(75, 95)

# Plot 3: Scatter
axes[1, 0].scatter(study_hours, exam_scores, alpha=0.5, color="coral")
axes[1, 0].set_title("Study vs Score")

# Plot 4: Histogram
axes[1, 1].hist(exam_scores, bins=10, color="purple", alpha=0.7, edgecolor="black")
axes[1, 1].set_title("Score Distribution")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=100)
plt.close()
print("Saved: dashboard.png")

print("\n" + "=" * 50)
print("SECTION 3: SEABORN — BEAUTIFUL STATISTICAL PLOTS")
print("=" * 50)

# Create a sample DataFrame
df = pd.DataFrame({
    "Name": [f"Student{i}" for i in range(1, 31)],
    "Score": np.random.normal(75, 12, 30).clip(50, 100).round(1),
    "Department": np.random.choice(["AI", "Web", "Data"], 30),
    "Study_Hours": np.random.uniform(2, 9, 30).round(1)
})

sns.set_style("whitegrid")
sns.set_palette("husl")

# Seaborn boxplot
plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x="Department", y="Score")
plt.title("Score Distribution by Department (Boxplot)")
plt.tight_layout()
plt.savefig("seaborn_boxplot.png")
plt.close()
print("Saved: seaborn_boxplot.png")

# Seaborn heatmap (correlation matrix)
numeric_df = df[["Score", "Study_Hours"]].copy()
numeric_df["Random"] = np.random.rand(30)
corr = numeric_df.corr()

plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.close()
print("Saved: heatmap.png")

# Cleanup
for f in ["line_chart.png", "bar_chart.png", "pie_chart.png",
          "scatter_plot.png", "dashboard.png", "seaborn_boxplot.png", "heatmap.png"]:
    if os.path.exists(f):
        os.remove(f)

print("\nAll charts generated and cleaned up.")
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print("plt.plot()      → line chart")
print("plt.bar()       → bar chart")
print("plt.pie()       → pie chart")
print("plt.scatter()   → scatter plot")
print("plt.hist()      → histogram")
print("plt.subplots()  → multiple charts")
print("sns.boxplot()   → seaborn box plot")
print("sns.heatmap()   → correlation heatmap")
print("plt.savefig()   → save chart to file")
