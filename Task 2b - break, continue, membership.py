"""
Task 2 (part 2 of 2) — 4 examples each: break, continue, for loop with 'in',
for loop with if, for loop with 'not in', if with 'in', if with 'not in'
Run this file directly: py "Task 2b - break, continue, membership.py"
"""

# ------------------------------------------------------------------
# 8. break
# ------------------------------------------------------------------
print("8. break")

for n in [3, 7, 2, 9, 4]:
    if n == 9:
        print("Found 9, stopping")
        break
    print(n)                          # 3 7 2 Found 9, stopping

for n in [5, 3, -1, 8, 2]:
    if n < 0:
        break
    print(n)                          # 5 3

count = 0
while True:
    count += 1
    if count == 4:
        break
print(count)                          # 4

for n in range(1, 100):
    if n % 7 == 0:
        print(n)
        break                          # 7
print()

# ------------------------------------------------------------------
# 9. continue
# ------------------------------------------------------------------
print("9. continue")

for n in range(1, 8):
    if n % 2 == 0:
        continue
    print(n)                           # 1 3 5 7

total3 = 0
for n in [4, -2, 7, -5, 3]:
    if n < 0:
        continue
    total3 += n
print(total3)                          # 14

word2 = "hello"
consonants = ""
for ch in word2:
    if ch in "aeiou":
        continue
    consonants += ch
print(consonants)                      # hll

for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
print()                                # 1 2 4 5 7 8 10
print()

# ------------------------------------------------------------------
# 10. for loop with 'in' operator
# ------------------------------------------------------------------
print("10. for loop with 'in' operator")

allowed = [10, 20, 30, 40]
candidates = [10, 15, 20, 25]
for c in candidates:
    if c in allowed:
        print(c, "is allowed")         # 10 is allowed / 20 is allowed

liked = ["mango", "apple"]
fruits2 = ["mango", "grape", "apple", "kiwi"]
for f in fruits2:
    if f in liked:
        print(f, "is a favorite")       # mango is a favorite / apple is a favorite

vowels_found = []
for ch in "hello world":
    if ch in "aeiou":
        vowels_found.append(ch)
print(vowels_found)                      # ['e', 'o', 'o']

student_scores = {"Amogh": 88, "Riya": 92}
for name in student_scores:
    if name in ["Amogh"]:
        print(name, "found in records")  # Amogh found in records
print()

# ------------------------------------------------------------------
# 11. for loop with if statement
# ------------------------------------------------------------------
print("11. for loop with if statement")

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    if n % 2 == 0:
        print(n, end=" ")
print()                                   # 2 4 6 8

for n in [-3, 5, -1, 8, -9, 2]:
    if n > 0:
        print(n, end=" ")
print()                                   # 5 8 2

words = ["cat", "elephant", "dog", "hippopotamus"]
for w in words:
    if len(w) > 4:
        print(w)                          # elephant hippopotamus

for n in range(1, 20):
    if n % 3 == 0:
        print(n, end=" ")
print()                                   # 3 6 9 12 15 18
print()

# ------------------------------------------------------------------
# 12. for loop with 'not in' operator
# ------------------------------------------------------------------
print("12. for loop with 'not in' operator")

excluded = ["banana", "grape"]
fruits3 = ["apple", "banana", "cherry", "grape", "mango"]
for f in fruits3:
    if f not in excluded:
        print(f)                          # apple cherry mango

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
diff = []
for n in list_a:
    if n not in list_b:
        diff.append(n)
print(diff)                                # [1, 2]

consonants2 = ""
for ch in "python":
    if ch not in "aeiou":
        consonants2 += ch
print(consonants2)                         # pythn

banned = [13, 7]
allowed_nums = []
for n in range(1, 15):
    if n not in banned:
        allowed_nums.append(n)
print(allowed_nums)                        # [1,2,3,4,5,6,8,9,10,11,12,14]
print()

# ------------------------------------------------------------------
# 13. if with 'in' operator
# ------------------------------------------------------------------
print("13. if with 'in' operator")

basket = ["apple", "banana", "cherry"]
if "banana" in basket:
    print("Banana is in the basket")        # Banana is in the basket

vowel_ch = "e"
if vowel_ch in "aeiou":
    print(vowel_ch, "is a vowel")             # e is a vowel

student = {"name": "Amogh", "age": 25}
if "name" in student:
    print("Key 'name' exists")                # Key 'name' exists

sentence = "The quick brown fox"
if "quick" in sentence:
    print("Substring found")                  # Substring found
print()

# ------------------------------------------------------------------
# 14. if with 'not in' operator
# ------------------------------------------------------------------
print("14. if with 'not in' operator")

basket2 = ["apple", "banana", "cherry"]
if "mango" not in basket2:
    print("Mango is not in the basket")        # Mango is not in the basket

ch2 = "z"
if ch2 not in "aeiou":
    print(ch2, "is not a vowel")                # z is not a vowel

student2 = {"name": "Amogh", "age": 25}
if "email" not in student2:
    print("Key 'email' does not exist")         # Key 'email' does not exist

sentence2 = "The quick brown fox"
if "lazy" not in sentence2:
    print("Substring not found")                # Substring not found
