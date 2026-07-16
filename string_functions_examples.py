"""
Python String Functions — 4 meaningful examples for each
Run this file directly: python string_functions_examples.py
"""

# ------------------------------------------------------------------
# 1. upper()  -> converts all characters to UPPERCASE
# ------------------------------------------------------------------
print("upper()")
print("hello".upper())                     # HELLO
print("Amogh".upper())                     # AMOGH
print("shout this!".upper())               # SHOUT THIS!
print("mix3d Case123".upper())             # MIX3D CASE123
print()

# ------------------------------------------------------------------
# 2. lower()  -> converts all characters to lowercase
# ------------------------------------------------------------------
print("lower()")
print("HELLO".lower())                     # hello
print("Amogh Ukkadgatri".lower())          # amogh ukkadgatri
print("PYTHON3.12".lower())                # python3.12
print("Mixed CASE Text".lower())           # mixed case text
print()

# ------------------------------------------------------------------
# 3. strip()  -> removes leading/trailing whitespace (or given chars)
# ------------------------------------------------------------------
print("strip()")
print("   hello world   ".strip())         # "hello world"
print("###important###".strip("#"))        # "important"
print("\n\tData\n".strip())                # "Data"
print("xxHelloxx".strip("x"))              # "Hello"
print()

# ------------------------------------------------------------------
# 4. replace(old, new)  -> replaces occurrences of a substring
# ------------------------------------------------------------------
print("replace()")
print("I like cats".replace("cats", "dogs"))          # I like dogs
print("2023-01-01".replace("-", "/"))                 # 2023/01/01
print("aaaa".replace("a", "b", 2))                     # bbaa (limit=2)
print("Hello World".replace(" ", "_"))                 # Hello_World
print()

# ------------------------------------------------------------------
# 5. split(separator)  -> splits string into a list
# ------------------------------------------------------------------
print("split()")
print("apple,banana,orange".split(","))     # ['apple', 'banana', 'orange']
print("one two three".split())              # ['one', 'two', 'three']
print("2026-07-16".split("-"))              # ['2026', '07', '16']
print("a=1;b=2;c=3".split(";"))             # ['a=1', 'b=2', 'c=3']
print()

# ------------------------------------------------------------------
# 6. join(iterable)  -> joins a list of strings using a separator
# ------------------------------------------------------------------
print("join()")
print(", ".join(["apple", "banana", "orange"]))   # apple, banana, orange
print("-".join(["2026", "07", "16"]))             # 2026-07-16
print("".join(["H", "e", "l", "l", "o"]))         # Hello
print(" | ".join(["Name", "Age", "City"]))        # Name | Age | City
print()

# ------------------------------------------------------------------
# 7. find(substring)  -> returns index of first match, or -1
# ------------------------------------------------------------------
print("find()")
print("hello world".find("world"))          # 6
print("hello world".find("xyz"))            # -1 (not found)
print("banana".find("a"))                   # 1 (first occurrence)
print("banana".find("a", 2))                # 3 (search starting at index 2)
print()

# ------------------------------------------------------------------
# 8. startswith() / endswith()  -> check prefix/suffix
# ------------------------------------------------------------------
print("startswith() / endswith()")
print("report_final.pdf".endswith(".pdf"))      # True
print("report_final.pdf".endswith(".docx"))     # False
print("https://example.com".startswith("https"))# True
print("image.png".startswith("img"))            # False
print()

# ------------------------------------------------------------------
# 9. format() / f-strings  -> insert values into a string template
# ------------------------------------------------------------------
print("format()")
name = "Amogh"
age = 25
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")
print("Pi is approximately {:.2f}".format(3.14159))   # Pi is approximately 3.14
print("{0} + {1} = {2}".format(2, 3, 2 + 3))          # 2 + 3 = 5
print()

# ------------------------------------------------------------------
# 10. count(substring)  -> counts non-overlapping occurrences
# ------------------------------------------------------------------
print("count()")
print("mississippi".count("s"))             # 4
print("banana".count("an"))                 # 2
print("hello world hello".count("hello"))   # 2
print("aaaa".count("aa"))                   # 2 (non-overlapping)
