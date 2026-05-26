import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
=============================================================
  LESSON 10: f-strings and String Formatting ✨
  Making text look cantik (beautiful) — the Python way!
=============================================================

You've been seeing f-strings throughout this course.
Now let's properly deep-dive into ALL the ways Python
can format strings. From basic to advanced!

This lesson covers:
  - f-string basics (refresher)
  - f-strings with expressions and method calls
  - f-strings with dictionaries (quoting rules!)
  - Number formatting (decimals, padding, alignment)
  - The .format() method (older but still useful)
  - The .join() method for combining strings
  - Practical example: formatting structured data

📌 Content adapted from the original notebook (Sections 3.1–3.2)
=============================================================
"""

# ============================================================
# PART 1: f-string Basics
# ============================================================
# Add an 'f' before the string, then use {variable} inside.
# From the original notebook:

print("=== f-string Basics ===")

name = "John"
age = 30
greeting = f"Hello, {name}. You are {age} years old."
print(greeting)

# You can put ANY expression inside {}
print(f"Next year you'll be {age + 1} years old.")
print(f"Your name has {len(name)} letters.")
print(f"Uppercase: {name.upper()}")
print(f"2 + 2 = {2 + 2}")


# ============================================================
# PART 2: f-strings with Dictionaries
# ============================================================
# From the original notebook — this is IMPORTANT!
# When using dict keys in f-strings, you must use DIFFERENT
# quote types for the outer string and the dict keys.

print("\n=== f-strings with Dictionaries ===")

person = {"name": "Ahmad", "age": 25, "city": "Penang"}

# ✅ CORRECT: Double quotes outside, single quotes for keys
print(f"Name: {person['name']}, Age: {person['age']}")

# ✅ ALSO CORRECT: Single quotes outside, double quotes for keys
print(f"City: {person['city']}")

# ❌ WRONG: Same quotes → SyntaxError!
# print(f"Name: {person["name"]}")  ← This will crash!

# Pro tip: For Python 3.12+, you can actually use the same quotes
# inside f-strings! But for compatibility, better mix them.


# ============================================================
# PART 3: Number Formatting
# ============================================================
# This is where f-strings really shine!
# Format: {value:specification}

print("\n=== Number Formatting ===")

price = 42.5
pi = 3.14159265358979

# Decimal places
print(f"Price: RM{price:.2f}")        # 2 decimal places → RM42.50
print(f"Pi (2dp): {pi:.2f}")          # → 3.14
print(f"Pi (5dp): {pi:.5f}")          # → 3.14159

# Thousands separator
population = 32000000
print(f"Population: {population:,}")   # → 32,000,000
print(f"Also works: {population:_}")   # → 32_000_000

# Percentage
score = 0.847
print(f"Score: {score:.1%}")           # → 84.7%

# Padding and alignment
# > right-align, < left-align, ^ center
print("\n--- Alignment ---")
for item, cost in [("Nasi Lemak", 5.5), ("Roti", 2.5), ("Teh Tarik", 1.8)]:
    print(f"  {item:<15} RM{cost:>6.2f}")

# With fill character
num = 42
print(f"\nPadded: {num:0>5}")       # → 00042 (pad with zeros)
print(f"Center: {'MENU':*^20}")     # → ********MENU********

# Scientific notation
big_number = 6022000000000000000000000
print(f"Avogadro: {big_number:.2e}")  # → 6.02e+23

# Binary, octal, hex
n = 255
print(f"\n255 in binary:  {n:b}")     # 11111111
print(f"255 in octal:   {n:o}")       # 377
print(f"255 in hex:     {n:x}")       # ff
print(f"255 in hex (upper): {n:X}")   # FF


# ============================================================
# PART 4: The .format() Method
# ============================================================
# Before f-strings (Python 3.6+), people used .format().
# Still useful and you'll see it in older code.
# From the original notebook:

print("\n=== .format() Method ===")

# Basic usage
template = "Hello, {}! You are {} years old."
print(template.format("Siti", 28))

# Numbered placeholders (reusable!)
template = "{0} is from {1}. {0} loves {1}!"
print(template.format("Ahmad", "Penang"))

# Named placeholders
template = "Name: {name}, Age: {age}, E-mail: {email}, Location: {location}"
print(template.format(name="Alice", age=28, email="alice@mail.com", location="KL"))


# ============================================================
# PART 5: Practical Example from Notebook
# ============================================================
# From the original notebook — formatting a list of dictionaries
# into readable output. This pattern is used EVERYWHERE!

print("\n=== Practical Example ===")

people = [
    {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice.johnson@example.com",
        "location": "New York, NY"
    },
    {
        "name": "Michael Smith",
        "age": 34,
        "email": "michael.smith@example.com",
        "location": "Los Angeles, CA"
    },
    {
        "name": "Emily Davis",
        "age": 22,
        "email": "emily.davis@example.com",
        "location": "Austin, TX"
    },
    {
        "name": "John Brown",
        "age": 45,
        "email": "john.brown@example.com",
        "location": "Chicago, IL"
    },
    {
        "name": "Sarah Wilson",
        "age": 31,
        "email": "sarah.wilson@example.com",
        "location": "Seattle, WA"
    }
]

# Method 1: Using f-strings (from notebook)
print("--- Method 1: f-strings ---")
t = []
for person_info_dict in people:
    layout_string = f"Name: {person_info_dict['name']}, Age: {person_info_dict['age']}, E-mail: {person_info_dict['email']}, Location: {person_info_dict['location']}"
    t.append(layout_string)
formatted_string = "\n".join(t)
print(formatted_string)

# Method 2: Using .format() (from notebook)
print("\n--- Method 2: .format() ---")
template = "Name: {name}, Age: {age}, E-mail: {email}, Location: {location}"
t = []
for person_info_dict in people:
    layout_string = template.format(
        name=person_info_dict['name'],
        age=person_info_dict['age'],
        email=person_info_dict['email'],
        location=person_info_dict['location']
    )
    t.append(layout_string)
formatted_string = "\n".join(t)
print(formatted_string)

# Method 3: Even cleaner with ** unpacking! (Boss mode 💪)
print("\n--- Method 3: ** unpacking (cleanest!) ---")
template = "Name: {name}, Age: {age}, E-mail: {email}, Location: {location}"
lines = [template.format(**person) for person in people]
print("\n".join(lines))


# ============================================================
# PART 6: The .join() Method — Putting It All Together
# ============================================================
# .join() combines a list of strings with a separator.
# separator.join(list_of_strings)

print("\n=== .join() Method ===")

words = ["Python", "is", "the", "best"]
print(" ".join(words))               # Python is the best
print(" → ".join(words))             # Python → is → the → best
print(", ".join(words))              # Python, is, the, best

# Creating a CSV line
data = ["Ahmad", "25", "Penang", "Developer"]
csv_line = ",".join(data)
print(f"CSV: {csv_line}")

# Building a path
parts = ["home", "user", "documents", "file.txt"]
path = "/".join(parts)
print(f"Path: {path}")


# ============================================================
# PART 7: Multi-line f-strings
# ============================================================
# Use triple quotes for multi-line formatted strings.

print("\n=== Multi-line f-strings ===")

name = "Ahmad"
age = 25
cgpa = 3.75

report = f"""
╔══════════════════════════════╗
║       STUDENT REPORT         ║
╠══════════════════════════════╣
║  Name:  {name:<20} ║
║  Age:   {age:<20} ║
║  CGPA:  {cgpa:<20.2f} ║
╚══════════════════════════════╝
"""
print(report)


# ============================================================
# PART 8: f-string Tips & Tricks
# ============================================================

print("=== Tips & Tricks ===")

# Debug with = (Python 3.8+) — prints variable name AND value!
x = 42
y = "hello"
print(f"{x = }")    # x = 42
print(f"{y = }")    # y = 'hello'

# Expressions in debug mode
items = [1, 2, 3]
print(f"{len(items) = }")  # len(items) = 3

# Date formatting
from datetime import datetime
now = datetime.now()
print(f"\nDate: {now:%Y-%m-%d}")
print(f"Time: {now:%H:%M:%S}")
print(f"Full: {now:%A, %d %B %Y}")

# Repr vs str
text = "hello\tworld"
print(f"\nstr:  {text}")        # hello    world
print(f"repr: {text!r}")       # 'hello\tworld'


# ============================================================
# 🎉 FORMAT MASTER!
# ============================================================
# You now know ALL the ways to format strings in Python!
# Next up: Lesson 11 — File I/O!
# We'll learn how to read and write files.

print("\n✅ Lesson 10 complete! String formatting — cantik! ✨")
