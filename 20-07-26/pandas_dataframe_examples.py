"""
Pandas Series/DataFrame walkthrough — series, loading CSV data, missing
values, filtering, columns, and groupby aggregations.
Run this file directly: py pandas_dataframe_examples.py
"""

import pandas as pd

print("pandas series")
ps = pd.Series(['g', 'e', 'e', 'k', 's'])
print(ps)
print()

print("pandas dataframe")

lst = ['g', 'e', 'e', 'k', 's']
df = pd.DataFrame(lst, columns=['Alphabets'])
print(df)
print()


print("loading data from csv file")
df = pd.read_csv("data.csv")
print(df.head())
print()
df.info()
print()

print("handling missing values")
print(df.isnull().sum())
df = df.fillna(0)
print(df.head())
print()

print("selecting and filtering data")
ages = df[df['age'] >= 25]
sales = df[df['sales'] > 150]

print(ages)
print()
print(sales)
print()

print("adding and removing columns")
df['total'] = df['a'] + df['b']
df['age + sales'] = df['age'] + df['sales']
print(df.head())
print()

print("grouping data")
grouped = df.groupby('category')['sales'].sum()
grouped_mean = df.groupby('category')['sales'].mean()
grouped_count = df.groupby('category')['sales'].count()
grouped_max = df.groupby('category')['sales'].max()
grouped_min = df.groupby('category')['sales'].min()
grouped_std = df.groupby('category')['sales'].std()
grouped_var = df.groupby('category')['sales'].var()
grouped_median = df.groupby('category')['sales'].median()
grouped_sum = df.groupby('category')['sales'].sum()
grouped_first = df.groupby('category')['sales'].first()
print(grouped)
print(grouped_mean)
print(grouped_count)
print(grouped_max)
print(grouped_min)
print(grouped_std)
print(grouped_var)
print(grouped_median)
print(grouped_sum)
print(grouped_first)