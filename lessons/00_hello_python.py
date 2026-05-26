"""
=============================================================
  LESSON 00: Hello Python! 🐍🇲🇾
  Your first steps into Python — confirm shiok one!
=============================================================

Eh, welcome welcome! So you want to learn Python ah?
Good choice lah! Python is like the nasi lemak of programming
languages — simple, satisfying, and everyone loves it.

This lesson covers:
  - What is Python (and why it's so popular)
  - How to run Python on your computer
  - Your first Python program
  - Comments (how to leave notes for yourself)
  - The print() function

HOW TO RUN THIS FILE:
  Open your terminal/command prompt, navigate to this folder, and type:
    python lessons/00_hello_python.py

  If that doesn't work, try:
    python3 lessons/00_hello_python.py

  Don't have Python yet? Go download from https://www.python.org/downloads/
  (Make sure to tick "Add Python to PATH" during installation ah!)
=============================================================
"""

import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# ============================================================
# PART 1: Your First Python Program
# ============================================================
# In many languages you need to write a lot of boilerplate code
# just to print "Hello, World!" — but Python? Senang je (easy only)!

print("Hello, World!")

# That's it. One line. No semicolons, no curly braces, no main() function.
# Confirm easier than ordering teh tarik, right?


# ============================================================
# PART 2: Comments — Leaving Notes for Future You
# ============================================================
# This line right here? It's a comment!
# Python ignores anything after the # symbol.
# Use comments to explain your code — future you will thank you.

# Single line comment — just use #
# Like ordering food: one line, one thought

"""
This is a multi-line comment (technically a docstring).
Use triple quotes (''' or \"\"\") when you need to write
a longer explanation. Like writing a review for your
favourite mamak stall — sometimes one line not enough lah!
"""


# ============================================================
# PART 3: print() — Your Best Friend
# ============================================================
# print() is how Python talks to you. Whatever you put inside
# the brackets, Python will display it on screen.

print("Selamat datang ke Python!")  # You can print any text
print(42)                           # Numbers also can!
print(3.14)                         # Decimal numbers? Boleh!
print(True)                         # Even True/False values (booleans)

# You can print multiple things separated by commas
print("My name is", "Python", "and I am", 30, "years old")

# The sep parameter changes what goes between items
print("Nasi", "Lemak", "Ayam", sep=" + ")
# Output: Nasi + Lemak + Ayam

# The end parameter changes what goes at the end (default is newline)
print("Loading", end="...")
print("Done!")
# Output: Loading...Done!


# ============================================================
# PART 4: Python as a Calculator
# ============================================================
# You can use Python like a calculator straight away.
# No need to declare anything — just type and go!

print("\n--- Python as a Calculator ---")
print("2 + 3 =", 2 + 3)        # Addition
print("10 - 4 =", 10 - 4)      # Subtraction
print("5 * 6 =", 5 * 6)        # Multiplication
print("15 / 4 =", 15 / 4)      # Division (always gives float)
print("15 // 4 =", 15 // 4)    # Floor division (round down)
print("15 % 4 =", 15 % 4)      # Modulo (remainder)
print("2 ** 10 =", 2 ** 10)    # Power (2 to the power of 10)


# ============================================================
# PART 5: Python is Indentation-Sensitive!
# ============================================================
# One thing that makes Python special: it uses INDENTATION (spaces)
# to structure code, not curly braces {} like other languages.
# This means spacing matters! Don't simply campak (throw) spaces anywhere.
#
# We'll see this more in the control flow lesson, but for now just remember:
# Python is very particular about its spaces — like how your mak
# is particular about the sambal in her nasi lemak. Don't mess with it!


# ============================================================
# 🎉 CONGRATULATIONS!
# ============================================================
# You just ran your first Python lesson! Not bad lah!
# Next up: Lesson 01 — Variables and Data Types
# We'll learn how to store things in Python's memory.
#
# Jom (let's go)! 🚀

print("\n✅ Lesson 00 complete! You're on your way, boss! 🎉")
