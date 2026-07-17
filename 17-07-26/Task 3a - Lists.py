"""
Python Data Structures — Lists
Run this file directly: py "Task 3a - Lists.py"
"""

# ------------------------------------------------------------------
# 1. Creating and indexing a list
# ------------------------------------------------------------------
print("create / index")
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)                              # ['apple', 'banana', 'cherry', 'date']
print(fruits[0])                           # apple
print(fruits[-1])                          # date
print(fruits[1:3])                         # ['banana', 'cherry']
print()

# ------------------------------------------------------------------
# 2. append() / insert()  -> add items
# ------------------------------------------------------------------
print("append() / insert()")
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)                             # [1, 2, 3, 4]
numbers.insert(0, 0)
print(numbers)                             # [0, 1, 2, 3, 4]
print()

# ------------------------------------------------------------------
# 3. remove() / pop()  -> delete items
# ------------------------------------------------------------------
print("remove() / pop()")
letters = ["a", "b", "c", "d"]
letters.remove("b")
print(letters)                             # ['a', 'c', 'd']
popped = letters.pop()
print(popped)                              # d
print(letters)                             # ['a', 'c']
print()

# ------------------------------------------------------------------
# 4. sort() / reverse()  -> reorder in place
# ------------------------------------------------------------------
print("sort() / reverse()")
scores = [42, 7, 19, 3]
scores.sort()
print(scores)                              # [3, 7, 19, 42]
scores.reverse()
print(scores)                              # [42, 19, 7, 3]
print()

# ------------------------------------------------------------------
# 5. list comprehension  -> build a new list from an iterable
# ------------------------------------------------------------------
print("list comprehension")
squares = [n * n for n in range(1, 6)]
print(squares)                             # [1, 4, 9, 16, 25]
evens = [n for n in range(1, 10) if n % 2 == 0]
print(evens)                               # [2, 4, 6, 8]