"""
=============================================================
  LESSON 02: Operators ➕➖✖️➗
  Math, comparisons, and logic — the tools of the trade!
=============================================================

Operators are like the utensils at a mamak stall — you need
different ones for different jobs. Spoon for curry, fork for
noodles, hands for roti canai. Same concept lah!

This lesson covers:
  - Arithmetic operators (+, -, *, /, //, %, **)
  - Comparison operators (==, !=, <, >, <=, >=)
  - Logical operators (and, or, not)
  - Assignment operators (=, +=, -=, etc.)
  - Membership operators (in, not in)
  - Identity operators (is, is not)
=============================================================
"""

# ============================================================
# PART 1: Arithmetic Operators
# ============================================================
# Basic math — you already saw some in Lesson 00!

print("=== Arithmetic Operators ===")
a = 15
b = 4

print(f"{a} + {b} = {a + b}")       # Addition → 19
print(f"{a} - {b} = {a - b}")       # Subtraction → 11
print(f"{a} * {b} = {a * b}")       # Multiplication → 60
print(f"{a} / {b} = {a / b}")       # Division → 3.75 (always float!)
print(f"{a} // {b} = {a // b}")     # Floor division → 3 (chop off decimal)
print(f"{a} % {b} = {a % b}")       # Modulo → 3 (remainder, like baki)
print(f"{a} ** {b} = {a ** b}")     # Power → 50625 (15 to the power of 4)

# Fun fact: // and % are super useful for many things!
# Example: Is a number even or odd?
number = 7
print(f"\nIs {number} even? {number % 2 == 0}")  # Odd number → False
print(f"Is {number} odd? {number % 2 != 0}")     # Odd number → True


# ============================================================
# PART 2: Comparison Operators
# ============================================================
# These compare two values and return True or False.
# Like asking "Is this nasi lemak better than that one?"

print("\n=== Comparison Operators ===")
x = 10
y = 20

print(f"{x} == {y} → {x == y}")    # Equal to? → False
print(f"{x} != {y} → {x != y}")    # Not equal to? → True
print(f"{x} > {y}  → {x > y}")     # Greater than? → False
print(f"{x} < {y}  → {x < y}")     # Less than? → True
print(f"{x} >= {y} → {x >= y}")    # Greater than or equal? → False
print(f"{x} <= {y} → {x <= y}")    # Less than or equal? → True

# IMPORTANT: == is comparison, = is assignment!
# Don't mix them up — very common mistake for beginners!
# x == 5  ← "Is x equal to 5?" (returns True/False)
# x = 5   ← "Set x to 5" (assigns value)


# ============================================================
# PART 3: Logical Operators
# ============================================================
# Combine multiple conditions — like checking multiple things
# before deciding where to makan (eat).
# "Is it halal AND is it nearby AND is it cheap?"

print("\n=== Logical Operators ===")

has_money = True
is_hungry = True
is_raining = False

# 'and' — Both must be True
can_eat_out = has_money and is_hungry
print(f"Has money AND hungry? {can_eat_out}")  # True

# 'or' — At least one must be True
will_go_out = is_hungry or is_raining
print(f"Hungry OR raining? {will_go_out}")  # True (hungry is True)

# 'not' — Flip the value
print(f"NOT raining? {not is_raining}")  # True (because is_raining is False)

# Combining them — order matters! 'not' first, then 'and', then 'or'
# Use brackets to be safe and clear!
go_mamak = (has_money and is_hungry) and (not is_raining)
print(f"Should go mamak? {go_mamak}")  # True — jom!


# ============================================================
# PART 4: Assignment Operators
# ============================================================
# Shortcuts for updating a variable's value.
# Like adding more sambal — you're modifying what's already there.

print("\n=== Assignment Operators ===")

score = 100
print(f"Starting score: {score}")

score += 10   # Same as: score = score + 10
print(f"After += 10: {score}")   # 110

score -= 30   # Same as: score = score - 30
print(f"After -= 30: {score}")   # 80

score *= 2    # Same as: score = score * 2
print(f"After *= 2: {score}")    # 160

score //= 3   # Same as: score = score // 3
print(f"After //= 3: {score}")   # 53

score %= 10   # Same as: score = score % 10
print(f"After %= 10: {score}")   # 3

score **= 4   # Same as: score = score ** 4
print(f"After **= 4: {score}")   # 81


# ============================================================
# PART 5: Membership Operators (in, not in)
# ============================================================
# Check if something is inside a collection.
# Like checking "Ada tak nasi lemak dalam menu?" (Is nasi lemak on the menu?)

print("\n=== Membership Operators ===")

menu = ["nasi lemak", "roti canai", "teh tarik", "milo dinosaur"]

print(f"'nasi lemak' in menu? {'nasi lemak' in menu}")         # True
print(f"'sushi' in menu? {'sushi' in menu}")                   # False
print(f"'sushi' not in menu? {'sushi' not in menu}")           # True

# Also works with strings!
greeting = "Selamat pagi"
print(f"'pagi' in greeting? {'pagi' in greeting}")             # True


# ============================================================
# PART 6: Identity Operators (is, is not)
# ============================================================
# Check if two variables point to the SAME object in memory.
# It's different from == which checks if VALUES are equal!

print("\n=== Identity Operators ===")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b? {a == b}")       # True — same values
print(f"a is b? {a is b}")       # False — different objects in memory!
print(f"a is c? {a is c}")       # True — c points to the same object as a

# Most common use: checking for None
result = None
print(f"result is None? {result is None}")  # True — this is the correct way!


# ============================================================
# PART 7: Operator Precedence
# ============================================================
# Just like in math class (BODMAS/PEMDAS), Python has an order:
# 1. ** (power)
# 2. *, /, //, % (multiplication, division)
# 3. +, - (addition, subtraction)
# 4. ==, !=, <, >, <=, >= (comparison)
# 5. not, and, or (logical)
#
# When in doubt, USE BRACKETS! Clearer for you and everyone else.

print("\n=== Operator Precedence ===")
result = 2 + 3 * 4    # 3 * 4 first, then + 2
print(f"2 + 3 * 4 = {result}")  # 14, not 20!

result = (2 + 3) * 4  # Brackets force addition first
print(f"(2 + 3) * 4 = {result}")  # 20 — brackets are your friend!


# ============================================================
# 🎉 POWER LAH!
# ============================================================
# You now know all the major operators in Python.
# Next up: Lesson 03 — Strings
# We'll learn how to manipulate text like a pro!

print("\n✅ Lesson 02 complete! Operators — settled! 🧮")
