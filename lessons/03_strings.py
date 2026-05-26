"""
=============================================================
  LESSON 03: Strings 🔤
  Text manipulation — because words matter lah!
=============================================================

Strings are how Python handles text. Whether it's someone's name,
a hawker stall menu, or a WhatsApp message — it's all strings.
Master this and you can manipulate text macam pro!

This lesson covers:
  - Creating strings (single, double, triple quotes)
  - String indexing and slicing
  - String methods (upper, lower, strip, split, join, replace, find)
  - String concatenation and repetition
  - Escape characters
  - Checking string content
=============================================================
"""

# ============================================================
# PART 1: Creating Strings
# ============================================================
# You can create strings with single quotes, double quotes,
# or triple quotes. All also boleh!

print("=== Creating Strings ===")

single = 'Hello lah'
double = "Hello lah"
triple = """This is a
multi-line string.
Boleh span across
multiple lines!"""

print(single)
print(double)
print(triple)

# When to use which?
# - Single or double: either one, just be consistent
# - Use double when your string has an apostrophe: "It's raining"
# - Use single when your string has double quotes: 'She said "hello"'
# - Use triple for multi-line text or docstrings

contains_apostrophe = "It's a beautiful day"
contains_quotes = 'He said "Wah, shiok!"'
print(f"\n{contains_apostrophe}")
print(contains_quotes)


# ============================================================
# PART 2: String Indexing
# ============================================================
# Each character in a string has a position (index).
# Python starts counting from 0! (Not 1 — don't get confused ah!)
#
#  M  A  L  A  Y  S  I  A
#  0  1  2  3  4  5  6  7    ← positive index
# -8 -7 -6 -5 -4 -3 -2 -1   ← negative index (count from behind)

print("\n=== String Indexing ===")

country = "MALAYSIA"
print(f"String: '{country}'")
print(f"First character (index 0): '{country[0]}'")     # M
print(f"Last character (index -1): '{country[-1]}'")    # A
print(f"Third character (index 2): '{country[2]}'")     # L


# ============================================================
# PART 3: String Slicing
# ============================================================
# Slicing lets you grab a portion of a string.
# Format: string[start:stop:step]
# - start: where to begin (inclusive)
# - stop: where to end (EXCLUSIVE — this one penting!)
# - step: how many to skip

print("\n=== String Slicing ===")

food = "NASI LEMAK"
print(f"String: '{food}'")

print(f"food[0:4]  → '{food[0:4]}'")    # NASI (index 0,1,2,3)
print(f"food[5:]   → '{food[5:]}'")     # LEMAK (from index 5 to end)
print(f"food[:4]   → '{food[:4]}'")     # NASI (from start to index 3)
print(f"food[-5:]  → '{food[-5:]}'")    # LEMAK (last 5 characters)

# Step — grab every Nth character
print(f"food[::2]  → '{food[::2]}'")    # NS EA (every 2nd character)

# Reverse a string — classic trick!
print(f"food[::-1] → '{food[::-1]}'")   # KAMEL ISAN (reversed!)


# ============================================================
# PART 4: String Methods — The Useful Ones
# ============================================================
# Strings come with loads of built-in methods.
# Here are the ones you'll use ALL THE TIME:

print("\n=== String Methods ===")

messy = "  Hello, Kuala Lumpur!  "

# .strip() — Remove whitespace from both sides
print(f"Original: '{messy}'")
print(f".strip():  '{messy.strip()}'")
print(f".lstrip(): '{messy.lstrip()}'")   # Left side only
print(f".rstrip(): '{messy.rstrip()}'")   # Right side only

# .upper() and .lower() — Change case
greeting = "Selamat Pagi"
print(f"\n'{greeting}'.upper() → '{greeting.upper()}'")
print(f"'{greeting}'.lower() → '{greeting.lower()}'")
print(f"'{greeting}'.title() → '{greeting.title()}'")   # Capitalize Each Word
print(f"'hello world'.capitalize() → '{'hello world'.capitalize()}'")  # First letter only

# .replace() — Swap text
sentence = "I love durian"
print(f"\n'{sentence}'.replace('durian', 'mangosteen') → '{sentence.replace('durian', 'mangosteen')}'")

# .split() — Break string into a list
csv_data = "nasi,lemak,ayam,sambal"
parts = csv_data.split(",")
print(f"\n'{csv_data}'.split(',') → {parts}")

# .join() — Opposite of split! Join a list into a string
words = ["Python", "is", "the", "best"]
joined = " ".join(words)
print(f"' '.join({words}) → '{joined}'")

# .find() — Find position of substring (-1 if not found)
text = "Where got durian in this sentence?"
pos = text.find("durian")
print(f"\n'durian' found at index: {pos}")
print(f"'sushi' found at index: {text.find('sushi')}")  # -1 (tak jumpa!)

# .count() — Count occurrences
tongue_twister = "she sells sea shells by the sea shore"
print(f"\nCount of 'sea': {tongue_twister.count('sea')}")
print(f"Count of 'sh':  {tongue_twister.count('sh')}")


# ============================================================
# PART 5: String Concatenation & Repetition
# ============================================================
# + joins strings, * repeats them

print("\n=== Concatenation & Repetition ===")

first = "Teh"
second = "Tarik"

# Concatenation
drink = first + " " + second
print(f"Concatenation: '{drink}'")

# Repetition
echo = "Ha" * 5
print(f"Repetition: '{echo}'")  # HaHaHaHaHa

# WARNING: You can't concatenate string + number directly!
# This will ERROR: "I am " + 25
# You must convert: "I am " + str(25)
age = 25
intro = "I am " + str(age) + " years old"
print(f"String + number: '{intro}'")
# (Or just use f-strings — which we'll cover in Lesson 10!)


# ============================================================
# PART 6: Escape Characters
# ============================================================
# Sometimes you need special characters in your string.
# Use backslash \ to "escape" them.

print("\n=== Escape Characters ===")
print("New line: Hello\\nWorld →")
print("Hello\nWorld")

print("\nTab: Hello\\tWorld →")
print("Hello\tWorld")

print("\nBackslash: \\\\ →")
print("\\")

print("\nQuotes inside string: \\\" →")
print("She said \"Wah, best!\"")


# ============================================================
# PART 7: String Checking Methods
# ============================================================
# These return True/False — handy for validation!

print("\n=== String Checking ===")

print(f"'12345'.isdigit()    → {'12345'.isdigit()}")      # True
print(f"'Hello'.isalpha()    → {'Hello'.isalpha()}")      # True
print(f"'Hello123'.isalnum() → {'Hello123'.isalnum()}")   # True
print(f"'hello'.islower()    → {'hello'.islower()}")      # True
print(f"'HELLO'.isupper()    → {'HELLO'.isupper()}")      # True
print(f"'   '.isspace()      → {'   '.isspace()}")        # True

# .startswith() and .endswith()
filename = "report_2024.pdf"
print(f"\n'{filename}'.startswith('report') → {filename.startswith('report')}")
print(f"'{filename}'.endswith('.pdf')     → {filename.endswith('.pdf')}")


# ============================================================
# PART 8: Strings are IMMUTABLE!
# ============================================================
# Once created, you CANNOT change individual characters.
# You have to create a new string instead.

word = "Hello"
# word[0] = "J"  ← This will ERROR! Cannot change in place!

# Instead, create a new string:
new_word = "J" + word[1:]
print(f"\n=== Immutability ===")
print(f"Original: '{word}' → New: '{new_word}'")


# ============================================================
# 🎉 STRINGS? SETTLED!
# ============================================================
# You now know how to create, slice, and manipulate strings
# like a pro. Next up: Lesson 04 — Lists!
# (The real fun starts there 😏)

print("\n✅ Lesson 03 complete! String master already! 🎸")
