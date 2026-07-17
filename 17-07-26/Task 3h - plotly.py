"""
Python Library — plotly (interactive plotting)
Requires: pip install plotly
Run this file directly: py "Task 3h - plotly.py"

Charts are saved as HTML files next to this script instead of calling
fig.show(), so the script can run to completion without opening a
browser tab. Open the HTML files to view the interactive charts.
"""

import os

import plotly.express as px
import plotly.graph_objects as go

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------
# 1. Line chart
# ------------------------------------------------------------------
print("line chart -> plotly_line.html")
fig = px.line(x=[1, 2, 3, 4, 5], y=[1, 4, 9, 16, 25], title="Line Chart: y = x^2")
fig.write_html(os.path.join(OUTPUT_DIR, "plotly_line.html"))

# ------------------------------------------------------------------
# 2. Bar chart
# ------------------------------------------------------------------
print("bar chart -> plotly_bar.html")
fig = px.bar(x=["A", "B", "C", "D"], y=[23, 45, 12, 38], title="Bar Chart")
fig.write_html(os.path.join(OUTPUT_DIR, "plotly_bar.html"))

# ------------------------------------------------------------------
# 3. Scatter chart with color grouping
# ------------------------------------------------------------------
print("scatter chart -> plotly_scatter.html")
fig = px.scatter(
    x=[5, 7, 8, 2, 17, 2, 9],
    y=[99, 86, 87, 88, 100, 86, 103],
    color=["low", "low", "high", "low", "high", "low", "high"],
    title="Scatter Chart",
)
fig.write_html(os.path.join(OUTPUT_DIR, "plotly_scatter.html"))

# ------------------------------------------------------------------
# 4. Pie chart
# ------------------------------------------------------------------
print("pie chart -> plotly_pie.html")
fig = px.pie(names=["Python", "SQL", "JavaScript"], values=[50, 30, 20], title="Language Usage")
fig.write_html(os.path.join(OUTPUT_DIR, "plotly_pie.html"))

# ------------------------------------------------------------------
# 5. Building a figure directly with graph_objects
# ------------------------------------------------------------------
print("graph_objects figure -> plotly_go.html")
fig = go.Figure(data=go.Bar(x=["Q1", "Q2", "Q3", "Q4"], y=[10, 25, 18, 30]))
fig.update_layout(title="Quarterly Sales")
fig.write_html(os.path.join(OUTPUT_DIR, "plotly_go.html"))

print("done: 5 HTML files written to", OUTPUT_DIR)
