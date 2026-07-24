"""
Python Library — matplotlib (plotting)
Requires: pip install matplotlib
Run this file directly: py "Task 3g - matplotlib.py"

Charts are saved as PNG files next to this script instead of calling
plt.show(), so the script can run to completion without waiting on a
GUI window. Swap savefig(...) for plt.show() to view them interactively.
"""

import os

import matplotlib
matplotlib.use("Agg")  # non-interactive backend, needed for savefig-only runs
import matplotlib.pyplot as plt

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------
# 1. Line plot
# ------------------------------------------------------------------
print("line plot -> matplotlib_line.png")
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.figure()
plt.plot(x, y, marker="o")
plt.title("Line Plot: y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib_line.png"))
plt.close()

# ------------------------------------------------------------------
# 2. Bar chart
# ------------------------------------------------------------------
print("bar chart -> matplotlib_bar.png")
categories = ["A", "B", "C", "D"]
values = [23, 45, 12, 38]
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart")
plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib_bar.png"))
plt.close()

# ------------------------------------------------------------------
# 3. Scatter plot
# ------------------------------------------------------------------
print("scatter plot -> matplotlib_scatter.png")
xs = [5, 7, 8, 2, 17, 2, 9]
ys = [99, 86, 87, 88, 100, 86, 103]
plt.figure()
plt.scatter(xs, ys)
plt.title("Scatter Plot")
plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib_scatter.png"))
plt.close()

# ------------------------------------------------------------------
# 4. Multiple lines on one figure with a legend
# ------------------------------------------------------------------
print("multi-line plot -> matplotlib_multiline.png")
plt.figure()
plt.plot(x, [v for v in y], label="y = x^2")
plt.plot(x, [v * 2 for v in x], label="y = 2x")
plt.legend()
plt.title("Multiple Lines")
plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib_multiline.png"))
plt.close()

# ------------------------------------------------------------------
# 5. Pie chart
# ------------------------------------------------------------------
print("pie chart -> matplotlib_pie.png")

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars, autopct='%1.1f%%')
plt.title(" Pie Chart")
plt.savefig(os.path.join(OUTPUT_DIR, "matplotlib_pie.png"))
plt.close()