import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
=============================================================
  LESSON 07: Control Flow 🚦
  Making decisions — Python style!
=============================================================

Control flow is how your program makes decisions.
Like when you reach a traffic light:
  - Green? Go!
  - Yellow? Slow down (or speed up if Malaysian 😂)
  - Red? Stop lah!

This lesson covers:
  - if, elif, else statements
  - Comparison and logical operators in conditions
  - Nested conditions
  - Ternary operator (one-liner if/else)
  - match/case (Python 3.10+)
  - Truthy and Falsy values
=============================================================
"""

# ============================================================
# PART 1: The Basics — if, elif, else
# ============================================================
# Python uses INDENTATION to define code blocks.
# After the condition, put a colon : and indent the next line(s).

print("=== if / elif / else ===")

temperature = 35

if temperature > 40:
    print("Alamak, too hot! Stay inside!")
elif temperature > 30:
    print("Normal Malaysian weather lah. 🌞")
elif temperature > 20:
    print("Wah, sejuk (cold) today!")
else:
    print("Where got so cold in Malaysia?!")

# Key points:
# - 'if' is required (at least one)
# - 'elif' is optional (can have many)
# - 'else' is optional (catches everything else)
# - Conditions are checked TOP to BOTTOM
# - ONLY the first matching block runs


# ============================================================
# PART 2: Conditions with Logical Operators
# ============================================================

print("\n=== Combining Conditions ===")

age = 20
has_license = True
is_tired = False

# Using 'and' — both must be True
if age >= 18 and has_license:
    print("Can drive! 🚗")
else:
    print("Cannot drive yet.")

# Using 'or' — at least one must be True
if is_tired or age > 60:
    print("Maybe take a rest.")
else:
    print("Still got energy! Jom!")

# Using 'not' — flip the condition
if not is_tired:
    print("Not tired — let's go mamak!")

# Complex condition with brackets for clarity
balance = 50
item_price = 30
has_discount = True

if (balance >= item_price) and (has_discount or item_price < 20):
    print("Boleh beli! (Can buy!)")


# ============================================================
# PART 3: Checking Multiple Values
# ============================================================

print("\n=== Checking Multiple Values ===")

# Check if value is in a collection
day = "Saturday"
if day in ("Saturday", "Sunday"):
    print(f"{day} — It's the weekend! Lepak time! 🎉")
else:
    print(f"{day} — Work day... 😩")

# Check string content
user_input = "Nasi Lemak Special"
if "nasi" in user_input.lower():
    print("Ah, a person of culture! 🍛")

# Checking None
result = None
if result is None:
    print("No result yet. Sabar (patience)!")

# Checking empty collections
my_list = []
if not my_list:
    print("List is empty — nothing to process.")


# ============================================================
# PART 4: Nested Conditions
# ============================================================
# You can put if/else inside another if/else.
# But don't go too deep — code becomes hard to read!
# (We call it "nesting hell" — or "inception lah")

print("\n=== Nested Conditions ===")

has_money = True
money_amount = 15
is_hungry = True

if is_hungry:
    if has_money:
        if money_amount >= 20:
            print("Full meal at restaurant! 🍽️")
        elif money_amount >= 10:
            print("Mamak it is! 🫓")
        else:
            print("Can afford maggi cup only lah 🍜")
    else:
        print("Hungry but no money... cook at home 😢")
else:
    print("Not hungry. Rare for Malaysian.")

# Better approach — flatten with 'and':
if is_hungry and has_money and money_amount >= 10:
    print("(Flattened version: Mamak time!)")


# ============================================================
# PART 5: Ternary Operator — One-Liner if/else
# ============================================================
# value_if_true if condition else value_if_false
# Short and sweet — like ordering "teh tarik kurang manis"

print("\n=== Ternary Operator ===")

age = 17
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# With print
score = 85
print(f"Result: {'Pass ✅' if score >= 50 else 'Fail ❌'}")

# In list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(f"Labels: {labels}")


# ============================================================
# PART 6: Truthy and Falsy Values
# ============================================================
# In Python, many things can be evaluated as True or False.
# You don't always need explicit == True or == False checks!

print("\n=== Truthy and Falsy ===")

# FALSY values (treated as False):
falsy_things = [False, None, 0, 0.0, "", [], {}, set()]
print("Falsy values:")
for thing in falsy_things:
    print(f"  bool({repr(thing):>10}) → {bool(thing)}")

# Everything else is TRUTHY:
truthy_things = [True, 1, -1, 3.14, "hello", [1], {"a": 1}]
print("\nTruthy values:")
for thing in truthy_things:
    print(f"  bool({repr(thing):>15}) → {bool(thing)}")

# Practical usage — clean Pythonic code:
name = "Ahmad"
items = []

# Instead of: if name != "":
if name:
    print(f"\nHello, {name}!")

# Instead of: if len(items) == 0:
if not items:
    print("Shopping cart is empty.")


# ============================================================
# PART 7: match/case (Python 3.10+)
# ============================================================
# Like switch/case in other languages.
# If you're using Python 3.10 or later, you can use this!

print("\n=== match/case (Python 3.10+) ===")

# Uncomment the block below if you have Python 3.10+:
http_status = 404

match http_status:
    case 200:
        print("OK — Everything fine!")
    case 301:
        print("Redirect — Moved already lah")
    case 404:
        print("Not Found — Where got?!")
    case 500:
        print("Server Error — Backend team kena already")
    case _:
        print(f"Unknown status: {http_status}")


# ============================================================
# 🎉 DECISION MAKER!
# ============================================================
# Now your programs can think and make decisions!
# Next up: Lesson 08 — Loops!
# We'll learn how to repeat things without copy-pasting.

print("\n✅ Lesson 07 complete! Control flow — can handle! 🚦")
