"""
=============================================================
  LESSON 13: Modules and Imports 📦
  Using other people's code — work smart, not hard!
=============================================================

Why build everything from scratch when someone already did it?
That's the power of modules! Python has a MASSIVE library of
pre-built tools — like a free hardware store. Just import and use!

This is like going to IKEA — you don't build the shelf from
raw wood, you just assemble the parts. Smart, right?

This lesson covers:
  - What are modules?
  - import, from...import, import...as
  - Python Standard Library (built-in goodies)
  - Useful standard modules (math, random, datetime, os, json)
  - Installing third-party packages with pip
  - Creating your own modules
=============================================================
"""

# ============================================================
# PART 1: Importing Modules
# ============================================================
# A module is just a .py file with functions, classes, and variables.
# You can import it and use its stuff!

print("=== Import Basics ===")

# Method 1: import the whole module
import math
print(f"Pi: {math.pi}")
print(f"Square root of 144: {math.sqrt(144)}")

# Method 2: import specific things
from math import ceil, floor
print(f"ceil(3.2): {ceil(3.2)}")    # Round up → 4
print(f"floor(3.8): {floor(3.8)}")  # Round down → 3

# Method 3: import with an alias (nickname)
import datetime as dt
now = dt.datetime.now()
print(f"Right now: {now}")

# Method 4: import everything (NOT recommended — pollutes namespace!)
# from math import *  ← Avoid this! You won't know where functions came from.


# ============================================================
# PART 2: The math Module — Calculator on Steroids!
# ============================================================

print("\n=== math Module ===")

import math

print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")
print(f"sqrt(25): {math.sqrt(25)}")
print(f"pow(2, 10): {math.pow(2, 10)}")
print(f"log(100, 10): {math.log(100, 10)}")  # Log base 10
print(f"factorial(5): {math.factorial(5)}")    # 5! = 120
print(f"gcd(12, 8): {math.gcd(12, 8)}")       # Greatest common divisor
print(f"ceil(3.1): {math.ceil(3.1)}")
print(f"floor(3.9): {math.floor(3.9)}")


# ============================================================
# PART 3: The random Module — Luck of the Draw! 🎲
# ============================================================

print("\n=== random Module ===")

import random

# Random float between 0 and 1
print(f"random(): {random.random():.4f}")

# Random integer in range
print(f"randint(1, 6): {random.randint(1, 6)}")  # Dice roll!

# Random choice from a list
foods = ["nasi lemak", "roti canai", "char kuey teow", "laksa", "satay"]
print(f"Random food: {random.choice(foods)}")

# Random sample (multiple unique choices)
team = random.sample(["Ahmad", "Siti", "Raj", "Mei", "Kumar"], 3)
print(f"Random team of 3: {team}")

# Shuffle a list in place
cards = ["A♠", "K♥", "Q♦", "J♣", "10♠"]
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# Random float in range
price = random.uniform(1.0, 10.0)
print(f"Random price: RM{price:.2f}")

# Practical: Generate a random password
import string
chars = string.ascii_letters + string.digits + "!@#$%"
password = ''.join(random.choice(chars) for _ in range(12))
print(f"Random password: {password}")


# ============================================================
# PART 4: The datetime Module — Time is Money! ⏰
# ============================================================

print("\n=== datetime Module ===")

from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(f"Now: {now}")
print(f"Date: {now.date()}")
print(f"Time: {now.time()}")

# Formatted output
print(f"Formatted: {now.strftime('%d/%m/%Y %H:%M')}")
print(f"Full: {now.strftime('%A, %d %B %Y')}")

# Create specific date
merdeka = date(1957, 8, 31)
print(f"\nMerdeka Day: {merdeka}")
print(f"Day of week: {merdeka.strftime('%A')}")

# Date arithmetic
today = date.today()
future = today + timedelta(days=30)
print(f"\nToday: {today}")
print(f"30 days from now: {future}")

# Days between dates
days_since_merdeka = (today - merdeka).days
print(f"Days since Merdeka: {days_since_merdeka:,}")


# ============================================================
# PART 5: The os Module — File System Navigator! 📂
# ============================================================

print("\n=== os Module ===")

import os

# Current working directory
print(f"Current directory: {os.getcwd()}")

# List files in a directory (current)
# print(f"Files here: {os.listdir('.')}")

# Path manipulation (cross-platform!)
path = os.path.join("users", "ahmad", "documents", "report.txt")
print(f"Joined path: {path}")
print(f"Filename: {os.path.basename(path)}")
print(f"Directory: {os.path.dirname(path)}")
print(f"Extension: {os.path.splitext(path)[1]}")

# Environment variables
print(f"Username: {os.environ.get('USERNAME', 'Unknown')}")


# ============================================================
# PART 6: The json Module — Data Exchange Format! 📄
# ============================================================

print("\n=== json Module ===")

import json

# Python dict → JSON string (serialization)
data = {
    "name": "Ahmad",
    "age": 25,
    "hobbies": ["coding", "gaming", "makan"],
    "address": {
        "city": "Penang",
        "country": "Malaysia"
    }
}

json_string = json.dumps(data, indent=2)
print("Python → JSON:")
print(json_string)

# JSON string → Python dict (deserialization)
parsed = json.loads(json_string)
print(f"\nJSON → Python: {parsed['name']} from {parsed['address']['city']}")

# Reading/writing JSON files
import os
json_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "temp_files", "data.json")
os.makedirs(os.path.dirname(json_file), exist_ok=True)

with open(json_file, "w") as f:
    json.dump(data, f, indent=2)
print(f"\n✅ JSON saved to: {json_file}")

with open(json_file, "r") as f:
    loaded = json.load(f)
print(f"✅ JSON loaded: {loaded['name']}")


# ============================================================
# PART 7: Other Useful Standard Modules
# ============================================================

print("\n=== Other Useful Modules ===")

# collections — advanced container types
from collections import Counter, defaultdict

# Counter — count occurrences
words = "nasi lemak nasi goreng nasi ayam roti canai roti john".split()
word_counts = Counter(words)
print(f"Word counts: {word_counts}")
print(f"Most common: {word_counts.most_common(3)}")

# defaultdict — dict with default values
scores = defaultdict(list)
scores["Ahmad"].append(85)
scores["Ahmad"].append(92)
scores["Siti"].append(90)
print(f"Scores: {dict(scores)}")

# itertools — iteration tools
from itertools import chain, combinations
print(f"\nChain: {list(chain([1,2], [3,4], [5,6]))}")
print(f"Combinations: {list(combinations('ABC', 2))}")

# sys — system stuff
import sys
print(f"\nPython version: {sys.version}")


# ============================================================
# PART 8: Installing Third-Party Packages
# ============================================================
# Python has PyPI (Python Package Index) — a massive repository
# of packages made by the community. Like an app store for Python!
#
# Install with pip (comes with Python):
#   pip install requests        # HTTP library
#   pip install pandas          # Data analysis
#   pip install flask           # Web framework
#   pip install pillow          # Image processing
#
# Or better yet, use a virtual environment:
#   python -m venv myenv        # Create virtual environment
#   myenv\Scripts\activate      # Activate (Windows)
#   pip install requests        # Install in this env only
#
# List installed packages:
#   pip list
#   pip freeze > requirements.txt  # Save to file

print("\n=== pip (Package Manager) ===")
print("To install packages, run in your terminal:")
print("  pip install package_name")
print("\nPopular packages:")
print("  requests  — HTTP requests made easy")
print("  pandas    — Data analysis & manipulation")
print("  flask     — Lightweight web framework")
print("  pytest    — Testing framework")
print("  numpy     — Numerical computing")


# ============================================================
# PART 9: Creating Your Own Module
# ============================================================
# Any .py file is a module! Just import it by filename.
#
# Example: Create a file called 'my_helpers.py':
#
#   # my_helpers.py
#   def greet(name):
#       return f"Hello, {name}!"
#
#   def add(a, b):
#       return a + b
#
# Then in another file:
#   import my_helpers
#   print(my_helpers.greet("Ahmad"))
#   print(my_helpers.add(1, 2))
#
# Or:
#   from my_helpers import greet
#   print(greet("Ahmad"))

print("\n=== Creating Your Own Module ===")
print("Any .py file can be imported as a module!")
print("Just put functions in a file and import them.")
print("See the comments in the code for examples!")


# ============================================================
# PART 10: The if __name__ == "__main__" Pattern
# ============================================================
# This is the most famous Python pattern!
# Code inside this block only runs when the file is
# executed directly, NOT when imported as a module.

print("\n=== if __name__ == '__main__' ===")

# __name__ is a special variable:
# - When running directly: __name__ == "__main__"
# - When imported: __name__ == "module_name"

print(f"Current __name__: {__name__}")

# In your modules, use this pattern:
# def my_function():
#     return "hello"
#
# if __name__ == "__main__":
#     # This only runs when you execute THIS file directly
#     print(my_function())
#     print("Running tests...")


# ============================================================
# 🎉 CONGRATULATIONS! YOU'VE COMPLETED ALL LESSONS! 🎓
# ============================================================
# You now have a solid foundation in Python fundamentals!
#
# From "Hello World" to modules and imports — you've covered:
#   ✅ Variables and Data Types
#   ✅ Operators
#   ✅ Strings
#   ✅ Lists, Tuples, and Sets
#   ✅ Dictionaries
#   ✅ Control Flow
#   ✅ Loops
#   ✅ Functions
#   ✅ f-strings and Formatting
#   ✅ File I/O
#   ✅ Error Handling
#   ✅ Modules and Imports
#
# What's next?
#   🔹 Try the exercises in the exercises/ folder!
#   🔹 Build a small project
#   🔹 Explore libraries like requests, pandas, flask
#   🔹 Keep coding and have fun!
#
# Remember: The best way to learn is by DOING.
# Jangan takut (don't be afraid) to experiment!

print("\n🎓 Lesson 13 complete — FINAL LESSON!")
print("🎉 TAHNIAH (CONGRATULATIONS)! You've completed Python Fundamentals!")
print("🚀 Now go build something awesome! 💪🇲🇾")
