"""
Python Data Structures — Sets
Run this file directly: py "Task 3d - Sets.py"
"""

# ------------------------------------------------------------------
# 1. Creating a set  -> unordered, no duplicates
# ------------------------------------------------------------------
print("create")
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)                              # {'apple', 'banana', 'cherry'} (duplicate dropped, order may vary)
print(len(fruits))                         # 3
print()

# ------------------------------------------------------------------
# 2. add() / remove()
# ------------------------------------------------------------------
print("add() / remove()")
fruits.add("date")
print("date" in fruits)                    # True
fruits.remove("banana")
print("banana" in fruits)                  # False
print()

# ------------------------------------------------------------------
# 3. union() / intersection()
# ------------------------------------------------------------------
print("union() / intersection()")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))                          # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))                   # {3, 4}
print()

# ------------------------------------------------------------------
# 4. difference() / symmetric_difference()
# ------------------------------------------------------------------
print("difference() / symmetric_difference()")
print(a.difference(b))                     # {1, 2}
print(a.symmetric_difference(b))           # {1, 2, 5, 6}
print()

# ------------------------------------------------------------------
# 5. Deduplicating a list  -> common practical use of a set
# ------------------------------------------------------------------
print("dedupe a list")
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = list(set(numbers))
unique_numbers.sort()
print(unique_numbers)                      # [1, 2, 3, 4]
