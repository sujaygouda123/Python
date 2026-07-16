"""
Task 2 (part 1 of 2) — 4 examples each: while loop, for loop, if else,
if elif else, and user-defined functions (plain / with for / with for+if)
Run this file directly: py "Task 2a - loops, conditionals, functions.py"
"""

# ------------------------------------------------------------------
# 1. while loop
# ------------------------------------------------------------------
print("1. while loop")

i = 1
while i <= 5:
    print(i * i)          # 1 4 9 16 25 (squares)
    i += 1

n = 10
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print(total)               # 55 (sum of 1..10)

num = 1234
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(reversed_num)        # 4321

n2 = 5
fact = 1
i = 1
while i <= n2:
    fact *= i
    i += 1
print(fact)                # 120 (5!)
print()

# ------------------------------------------------------------------
# 2. for loop
# ------------------------------------------------------------------
print("2. for loop")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)            # apple banana cherry

numbers = [4, 8, 15, 16, 23, 42]
total2 = 0
for num2 in numbers:
    total2 += num2
print(total2)                # 108

for i in range(1, 6):
    print(f"5 x {i} = {5 * i}")   # 5x1..5x5 table

word = "programming"
length = 0
for ch in word:
    length += 1
print(length)                 # 11
print()

# ------------------------------------------------------------------
# 3. if else
# ------------------------------------------------------------------
print("3. if else")

num3 = 7
if num3 % 2 == 0:
    print("Even")
else:
    print("Odd")               # Odd

num4 = -5
if num4 >= 0:
    print("Non-negative")
else:
    print("Negative")          # Negative

num5 = 20
if num5 % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")  # Divisible by 5

marks = 35
if marks >= 40:
    print("Pass")
else:
    print("Fail")               # Fail
print()

# ------------------------------------------------------------------
# 4. if elif else
# ------------------------------------------------------------------
print("4. if elif else")

score = 82
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(grade)                   # B

value = 0
if value > 0:
    print("Positive")
elif value < 0:
    print("Negative")
else:
    print("Zero")               # Zero

day = "Saturday"
if day == "Saturday":
    print("Weekend")
elif day == "Sunday":
    print("Weekend")
else:
    print("Weekday")            # Weekend

signal = "yellow"
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
else:
    print("Go")                 # Get Ready
print()

# ------------------------------------------------------------------
# 5. user-defined functions (no loop, no if)
# ------------------------------------------------------------------
print("5. user-defined functions (no loop, no if)")

def add(a, b):
    return a + b
print(add(4, 7))                # 11

def square(n):
    return n * n
print(square(6))                # 36

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
print(celsius_to_fahrenheit(37))  # 98.6

def area_of_circle(radius):
    return 3.14159 * radius * radius
print(area_of_circle(3))         # 28.274309999999996 (float rounding)
print()

# ------------------------------------------------------------------
# 6. user-defined functions with for loop
# ------------------------------------------------------------------
print("6. user-defined functions with for loop")

def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total
print(sum_list([1, 2, 3, 4, 5]))     # 15

def count_length(text):
    count = 0
    for _ in text:
        count += 1
    return count
print(count_length("hello"))          # 5

def multiply_all(nums):
    product = 1
    for n in nums:
        product *= n
    return product
print(multiply_all([1, 2, 3, 4]))     # 24

def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
print(reverse_string("python"))       # nohtyp
print()

# ------------------------------------------------------------------
# 7. user-defined functions with for loop and if condition
# ------------------------------------------------------------------
print("7. user-defined functions with for loop and if")

def count_even(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count
print(count_even([1, 2, 3, 4, 5, 6]))     # 3

def filter_positive(nums):
    result = []
    for n in nums:
        if n > 0:
            result.append(n)
    return result
print(filter_positive([-3, 5, -1, 8, 0])) # [5, 8]

def find_max(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest
print(find_max([3, 9, 2, 7]))              # 9

def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count += 1
    return count
print(count_vowels("education"))           # 5
