# =============================================================================
# WEEK 3 - DAY 5: Final Project — Sales Data Analysis Pipeline
# Intern: ISHAAN GARG
# Topic: End-to-end data pipeline: generate → clean → analyze → report
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

print("=" * 55)
print("  ISHAAN GARG — SALES DATA ANALYSIS PIPELINE")
print("=" * 55)

# --- Step 1: Generate raw sales data ---
np.random.seed(42)
n = 200

regions = ["North", "South", "East", "West"]
products = ["Laptop", "Phone", "Tablet", "Headphones", "Watch"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

raw = pd.DataFrame({
    "OrderID":    range(1001, 1001 + n),
    "Month":      np.random.choice(months, n),
    "Region":     np.random.choice(regions, n),
    "Product":    np.random.choice(products, n),
    "Units":      np.random.randint(1, 20, n),
    "UnitPrice":  np.random.choice([15000, 8000, 25000, 2000, 5000], n),
    "Discount":   np.random.choice([0, 5, 10, 15, 20], n),
    "CustomerAge": np.append(np.random.randint(20, 55, n-5), [-1, 200, None, None, None])
})

# Introduce some mess
raw.loc[0:4, "Region"] = raw.loc[0:4, "Region"].str.lower()
raw.loc[5:8, "Product"] = raw.loc[5:8, "Product"].str.upper()

print(f"\nRaw data: {raw.shape[0]} rows, {raw.shape[1]} cols")
print(raw.head(5))

# --- Step 2: Clean ---
print("\n--- Cleaning ---")
df = raw.copy()
df["Region"] = df["Region"].str.title().str.strip()
df["Product"] = df["Product"].str.title().str.strip()
df = df.dropna(subset=["CustomerAge"])
df = df[(df["CustomerAge"] >= 18) & (df["CustomerAge"] <= 80)]
df = df.reset_index(drop=True)
print(f"Clean data: {df.shape[0]} rows")

# --- Step 3: Feature Engineering ---
df["Revenue"] = df["Units"] * df["UnitPrice"]
df["DiscountAmt"] = (df["Revenue"] * df["Discount"] / 100).round(0)
df["NetRevenue"] = df["Revenue"] - df["DiscountAmt"]

# --- Step 4: Analysis ---
print("\n--- Analysis ---")
total_revenue = df["NetRevenue"].sum()
total_units = df["Units"].sum()
avg_order = df["NetRevenue"].mean()

print(f"Total Net Revenue : ₹{total_revenue:,.0f}")
print(f"Total Units Sold  : {total_units}")
print(f"Avg Order Value   : ₹{avg_order:,.0f}")

print("\nRevenue by Region:")
by_region = df.groupby("Region")["NetRevenue"].sum().sort_values(ascending=False)
for region, rev in by_region.items():
    print(f"  {region:8s}: ₹{rev:>12,.0f}")

print("\nTop Product by Units:")
by_product = df.groupby("Product")["Units"].sum().sort_values(ascending=False)
for prod, units in by_product.items():
    print(f"  {prod:12s}: {units} units")

print("\nAvg Revenue by Discount Level:")
by_discount = df.groupby("Discount")["NetRevenue"].mean().round(0)
print(by_discount)

# --- Step 5: Visualization ---
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("Ishaan Garg — Sales Analysis Dashboard", fontsize=14, fontweight="bold")

# Chart 1: Revenue by region
by_region.plot(kind="bar", ax=axes[0, 0], color=["#4CAF50","#2196F3","#FF9800","#9C27B0"], alpha=0.85)
axes[0, 0].set_title("Net Revenue by Region")
axes[0, 0].set_ylabel("₹")
axes[0, 0].tick_params(axis='x', rotation=0)

# Chart 2: Units by product
by_product.plot(kind="barh", ax=axes[0, 1], color="steelblue", alpha=0.8)
axes[0, 1].set_title("Units Sold by Product")

# Chart 3: Revenue distribution
axes[1, 0].hist(df["NetRevenue"], bins=20, color="coral", edgecolor="black", alpha=0.8)
axes[1, 0].set_title("Order Value Distribution")
axes[1, 0].set_xlabel("₹")

# Chart 4: Revenue by discount level
by_discount_rev = df.groupby("Discount")["NetRevenue"].sum()
by_discount_rev.plot(kind="bar", ax=axes[1, 1], color="teal", alpha=0.8)
axes[1, 1].set_title("Revenue by Discount %")
axes[1, 1].set_ylabel("₹")
axes[1, 1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=100)
plt.close()
print("\nDashboard saved: sales_dashboard.png")

# --- Step 6: Text Report ---
report = f"""
SALES ANALYSIS REPORT
Intern: ISHAAN GARG
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
{'=' * 45}

SUMMARY
  Total Net Revenue : ₹{total_revenue:,.0f}
  Total Units Sold  : {total_units}
  Avg Order Value   : ₹{avg_order:,.0f}
  Orders Processed  : {len(df)}

REVENUE BY REGION
{by_region.to_string()}

UNITS BY PRODUCT
{by_product.to_string()}

AVG ORDER VALUE BY DISCOUNT
{by_discount.to_string()}

{'=' * 45}
END OF REPORT
"""

with open("sales_report.txt", "w") as f:
    f.write(report)
print("Text report saved: sales_report.txt")

# Cleanup
for fname in ["sales_dashboard.png", "sales_report.txt"]:
    if os.path.exists(fname):
        os.remove(fname)

print("\n✅ Pipeline complete! Week 3 done — great work, Navkiran!")
print("=" * 55)
