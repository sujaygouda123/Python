"""
Python Library — pandas (data analysis / tabular data)
Requires: pip install pandas
Run this file directly: py "Task 3e - pandas.py"
"""

import pandas as pd

# ------------------------------------------------------------------
# 1. Creating a DataFrame
# ------------------------------------------------------------------
print("create DataFrame")
df = pd.DataFrame({
    "name": ["Amogh", "Riya", "Kiran"],
    "age": [25, 30, 22],
    "city": ["Bengaluru", "Mumbai", "Delhi"],
})
print(df)
print()

# ------------------------------------------------------------------
# 2. Selecting columns / rows
# ------------------------------------------------------------------
print("select columns / rows")
print(df["name"])                          # Series of names
print(df.loc[1])                           # row at index 1 (Riya)
print()

# ------------------------------------------------------------------
# 3. Filtering rows
# ------------------------------------------------------------------
print("filter")
print(df[df["age"] > 24])                  # rows where age > 24
print()

# ------------------------------------------------------------------
# 4. Adding a column
# ------------------------------------------------------------------
print("add column")
df["age_next_year"] = df["age"] + 1
print(df)
print()

# ------------------------------------------------------------------
# 5. Summary statistics
# ------------------------------------------------------------------
print("describe()")
print(df["age"].describe())                # count, mean, std, min, max, etc.
