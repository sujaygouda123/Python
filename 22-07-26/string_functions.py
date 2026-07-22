# String Functions in Python
# For each function: 2 EASY examples + 2 DIFFERENT/TRICKY examples

print("=" * 50)
print("1. upper() - converts string to UPPERCASE")
print("=" * 50)
# Easy
print("hello".upper())              # HELLO
print("good morning".upper())       # GOOD MORNING
# Different / Tricky
print("Python3.9".upper())          # PYTHON3.9 (numbers unaffected)
print("already UPPER".upper())      # ALREADY UPPER (no change needed)


print("\n" + "=" * 50)
print("2. lower() - converts string to lowercase")
print("=" * 50)
# Easy
print("HELLO".lower())               # hello
print("GOOD MORNING".lower())        # good morning
# Different / Tricky
print("MixED CaSe 123".lower())      # mixed case 123
print("".lower())                    # "" (empty string, no error)


print("\n" + "=" * 50)
print("3. strip() - removes leading/trailing whitespace")
print("=" * 50)
# Easy
print("  hello  ".strip())           # "hello"
print("   welcome".strip())          # "welcome"
# Different / Tricky
print("xxhelloxx".strip("x"))        # "hello" (strips custom character)
print("\t\nhello world\n\t".strip()) # "hello world" (strips tabs/newlines)


print("\n" + "=" * 50)
print("4. replace(old, new) - replaces part of a string")
print("=" * 50)
# Easy
print("I like cats".replace("cats", "dogs"))     # I like dogs
print("2023-01-01".replace("-", "/"))            # 2023/01/01
# Different / Tricky
print("banana".replace("a", "o", 2))             # bonona (only first 2 replaced)
print("aaa".replace("a", "aa"))                   # aaaaaa (overlap behavior)


print("\n" + "=" * 50)
print("5. split() - breaks a string into a list")
print("=" * 50)
# Easy
print("apple,banana,mango".split(","))           # ['apple', 'banana', 'mango']
print("hello world".split())                     # ['hello', 'world']
# Different / Tricky
print("a  b   c".split())                        # ['a','b','c'] (handles extra spaces)
print("2023-07-16".split("-", 1))                # ['2023', '07-16'] (maxsplit=1)


print("\n" + "=" * 50)
print("6. join() - combines list items into a string")
print("=" * 50)
# Easy
print(", ".join(["apple", "banana", "mango"]))   # apple, banana, mango
print("-".join(["2023", "07", "16"]))            # 2023-07-16
# Different / Tricky
print("".join(["H", "e", "l", "l", "o"]))        # Hello (no separator)
print(" ".join(str(n) for n in range(5)))        # 0 1 2 3 4 (joining numbers)


print("\n" + "=" * 50)
print("7. find() - returns index of substring (-1 if not found)")
print("=" * 50)
# Easy
print("hello world".find("world"))               # 6
print("python".find("y"))                        # 1
# Different / Tricky
print("banana".find("a", 2))                     # 3 (search starting from index 2)
print("hello".find("z"))                         # -1 (not found, no error)


print("\n" + "=" * 50)
print("8. count() - counts occurrences of a substring")
print("=" * 50)
# Easy
print("banana".count("a"))                       # 3
print("hello world".count("o"))                  # 2
# Different / Tricky
print("aaaa".count("aa"))                        # 2 (non-overlapping matches)
print("Mississippi".count("ss"))                 # 2


print("\n" + "=" * 50)
print("9. startswith() / endswith() - check prefix/suffix")
print("=" * 50)
# Easy
print("hello.py".endswith(".py"))                # True
print("report.pdf".startswith("report"))         # True
# Different / Tricky
print("hello.PY".endswith(".py"))                # False (case-sensitive)
print("filename.txt".endswith((".txt", ".csv"))) # True (tuple of options)


print("\n" + "=" * 50)
print("10. isdigit() / isalpha() - check character type")
print("=" * 50)
# Easy
print("12345".isdigit())                         # True
print("hello".isalpha())                         # True
# Different / Tricky
print("12.5".isdigit())                          # False (decimal point breaks it)
print("hello123".isalpha())                      # False (mixed letters+numbers)


print("\n" + "=" * 50)
print("11. format() - inserts values into a string")
print("=" * 50)
# Easy
print("My name is {} and I am {} years old.".format("Amogh", 20))
print("{0} + {1} = {2}".format(2, 3, 5))
# Different / Tricky
print("{name} scored {marks:.2f}%".format(name="Amogh", marks=87.5))  # rounds to 2 decimals
print("{:>10}".format("hi"))                     # right-aligned in 10 spaces


print("\n" + "=" * 50)
print("12. title() / capitalize() - change letter casing")
print("=" * 50)
# Easy
print("hello world".title())                     # Hello World
print("python programming".capitalize())         # Python programming
# Different / Tricky
print("mc'donald 5th avenue".title())             # Mc'Donald 5Th Avenue (quirky edge case)
print("HELLO WORLD".capitalize())                 # Hello world (lowercases the rest)
