"""
Python Data Structures — Dictionaries
Run this file directly: py "Task 3c - Dictionaries.py"
"""

# ------------------------------------------------------------------
# 1. Creating and accessing a dictionary
# ------------------------------------------------------------------
print("create / access")
student = {"name": "Amogh", "age": 25, "course": "Python"}
print(student)                             # {'name': 'Amogh', 'age': 25, 'course': 'Python'}
print(student["name"])                     # Amogh
print(student.get("grade", "N/A"))         # N/A (key missing, default used)
print()

# ------------------------------------------------------------------
# 2. Adding / updating / removing keys
# ------------------------------------------------------------------
print("add / update / remove")
student["grade"] = "A"
print(student)                             # {..., 'grade': 'A'}
student["age"] = 26
print(student["age"])                      # 26
del student["grade"]
print(student)                             # {'name': 'Amogh', 'age': 26, 'course': 'Python'}
print()

# ------------------------------------------------------------------
# 3. keys() / values() / items()
# ------------------------------------------------------------------
print("keys() / values() / items()")
print(list(student.keys()))                # ['name', 'age', 'course']
print(list(student.values()))              # ['Amogh', 26, 'Python']
print(list(student.items()))               # [('name', 'Amogh'), ('age', 26), ('course', 'Python')]
print()

# ------------------------------------------------------------------
# 4. Looping through a dictionary
# ------------------------------------------------------------------
print("loop")
for key, value in student.items():
    print(f"{key}: {value}")
# name: Amogh
# age: 26
# course: Python
print()

# ------------------------------------------------------------------
# 5. Dictionary comprehension
# ------------------------------------------------------------------
print("dict comprehension")
squares = {n: n * n for n in range(1, 6)}
print(squares)                             # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
