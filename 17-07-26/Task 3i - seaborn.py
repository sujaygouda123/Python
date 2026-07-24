"""
Python Library — seaborn (statistical plotting, built on matplotlib)
Requires: pip install seaborn
Run this file directly: py "Task 3i - seaborn.py"

Charts are saved as PNG files next to this script instead of calling
plt.show(), so the script can run to completion without waiting on a
GUI window.
"""

import os

import matplotlib
matplotlib.use("Agg")  # non-interactive backend, needed for savefig-only runs
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

tips_like = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59, 25.29, 8.77, 26.88],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61, 4.71, 2.00, 3.12],
    "day": ["Sun", "Sun", "Sun", "Sun", "Sat", "Sat", "Sat", "Sat"],
}

# ------------------------------------------------------------------
# 1. Scatter plot with regression line
# ------------------------------------------------------------------
print("regplot -> seaborn_regplot.png")
plt.figure()
sns.regplot(x=tips_like["total_bill"], y=tips_like["tip"])
plt.title("Tip vs Total Bill")
plt.savefig(os.path.join(OUTPUT_DIR, "seaborn_regplot.png"))
plt.close()

# ------------------------------------------------------------------
# 2. Bar plot grouped by category
# ------------------------------------------------------------------
print("barplot -> seaborn_barplot.png")
plt.figure()
sns.barplot(x=tips_like["day"], y=tips_like["total_bill"])
plt.title("Average Bill by Day")
plt.savefig(os.path.join(OUTPUT_DIR, "seaborn_barplot.png"))
plt.close()

# ------------------------------------------------------------------
# 3. Box plot  -> shows distribution and outliers
# ------------------------------------------------------------------
print("boxplot -> seaborn_boxplot.png")
plt.figure()
sns.boxplot(x=tips_like["day"], y=tips_like["total_bill"])
plt.title("Bill Distribution by Day")
plt.savefig(os.path.join(OUTPUT_DIR, "seaborn_boxplot.png"))
plt.close()

# ------------------------------------------------------------------
# 4. Histogram with kernel density estimate
# ------------------------------------------------------------------
print("histplot -> seaborn_histplot.png")
plt.figure()
sns.histplot(tips_like["total_bill"], kde=True, bins=5)
plt.title("Total Bill Distribution")
plt.savefig(os.path.join(OUTPUT_DIR, "seaborn_histplot.png"))
plt.close()
