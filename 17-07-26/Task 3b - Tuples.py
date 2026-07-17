"""
Python Data Structures — Tuples
Run this file directly: py "Task 3b - Tuples.py"
"""

# ------------------------------------------------------------------
# 1. Creating and indexing a tuple
# ------------------------------------------------------------------
print("create / index")
point = (3, 7)
colors = ("red", "green", "blue")
print(point)                               # (3, 7)
print(colors[1])                           # green
print(colors[-1])                          # blue
print(colors[0:2])                         # ('red', 'green')
print()

# ------------------------------------------------------------------
# 2. Immutability  -> tuples cannot be changed after creation
# ------------------------------------------------------------------
print("immutability")
try:
    colors[0] = "yellow"
except TypeError as e:
    print(f"TypeError: {e}")               # TypeError: 'tuple' object does not support item assignment
print()

# ------------------------------------------------------------------
# 3. Packing / unpacking
# ------------------------------------------------------------------
print("packing / unpacking")
person = ("Amogh", 25, "Bengaluru")
name, age, city = person
print(name)                                # Amogh
print(age)                                 # 25
print(city)                                # Bengaluru
print(person)
print()

# ------------------------------------------------------------------
# 4. count() / index()
# ------------------------------------------------------------------
print("count() / index()")
nums = (1, 2, 2, 3, 2, 4)
print(nums.count(2))                       # 3
print(nums.index(3))                       # 3
print()

# ------------------------------------------------------------------
# 5. Tuple as a dictionary key  -> only immutable types can be keys
# ------------------------------------------------------------------
print("tuple as dict key")
distances = {("Delhi", "Mumbai"): 1400, ("Delhi", "Chennai"): 2200}
print(distances[("Delhi", "Mumbai")])      # 1400
