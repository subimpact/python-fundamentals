"""
=============================================================
  LESSON 06: Dictionaries 📖
  Key-value pairs — like a menu with prices!
=============================================================

Dictionaries store data as key:value pairs. Think of a real
dictionary — you look up a WORD (key) to find its MEANING (value).
Or like a mamak menu: "Roti Canai" → RM2.50, "Teh Tarik" → RM1.80.

This lesson covers:
  - Creating dictionaries
  - Accessing, adding, updating values
  - Iterating with .items(), .keys(), .values()
  - Dictionary methods (.get(), .pop(), .update())
  - Nested dictionaries
  - Dictionary comprehensions

📌 Content adapted from the original notebook (Sections 2.1–2.2)
=============================================================
"""

# ============================================================
# PART 1: Creating Dictionaries
# ============================================================
# Use curly braces {} with key:value pairs.

print("=== Creating Dictionaries ===")

# From the original notebook:
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
print(f"Person dictionary: {person}")

# Malaysian-style example 🇲🇾
mamak_menu = {
    "roti canai": 2.50,
    "teh tarik": 1.80,
    "maggi goreng": 7.00,
    "nasi lemak": 5.50,
    "milo dinosaur": 4.00
}
print(f"\nMamak menu: {mamak_menu}")

# Empty dictionary
empty = {}
print(f"Empty dict: {empty}")


# ============================================================
# PART 2: Accessing Values
# ============================================================
# Use the KEY inside square brackets to get the VALUE.

print("\n=== Accessing Values ===")

# From the original notebook:
print(f"Name: {person['name']}")

# Using our mamak menu:
print(f"Roti canai price: RM{mamak_menu['roti canai']}")
print(f"Teh tarik price: RM{mamak_menu['teh tarik']}")

# WARNING: If the key doesn't exist, you get a KeyError!
# mamak_menu['sushi']  ← This will crash! No sushi at mamak lah!

# Safer way: use .get() — returns None if key not found
sushi_price = mamak_menu.get("sushi")
print(f"\nSushi price: {sushi_price}")  # None (no error!)

# You can set a default value with .get()
sushi_price = mamak_menu.get("sushi", "Not available lah!")
print(f"Sushi price (with default): {sushi_price}")


# ============================================================
# PART 3: Adding and Updating
# ============================================================

print("\n=== Adding & Updating ===")

# From the original notebook:
person['email'] = 'alice@example.com'
print(f"Updated person dictionary: {person}")

# Adding new items
mamak_menu["ayam goreng"] = 8.00
print(f"After adding ayam goreng: {mamak_menu}")

# Updating existing items (same syntax as adding)
mamak_menu["roti canai"] = 3.00  # Inflation hits mamak too 😢
print(f"After price increase: roti canai = RM{mamak_menu['roti canai']}")

# .update() — merge another dictionary
mamak_menu.update({"bandung": 3.50, "air sirap": 2.00})
print(f"After update: {mamak_menu}")

# Removing items
removed_price = mamak_menu.pop("air sirap")
print(f"\nRemoved 'air sirap' (was RM{removed_price})")
print(f"Menu now: {mamak_menu}")

# .pop() with default (no error if key missing)
result = mamak_menu.pop("pizza", "Takde (not found)")
print(f"Tried to remove 'pizza': {result}")


# ============================================================
# PART 4: Iterating Over Dictionaries
# ============================================================
# This is where .items() becomes your best friend!

print("\n=== Iterating ===")

# From the original notebook — using .items()
print("--- Using .items() (key AND value) ---")
for key, value in person.items():
    print(f"Key: {key}\tValue: {value}")

# From the original notebook — iterating directly gets KEYS only
print("\n--- Iterating directly (keys only) ---")
for val in person:
    print(val)

# .keys() — get all keys
print(f"\n--- .keys() ---")
print(f"Keys: {list(mamak_menu.keys())}")

# .values() — get all values
print(f"\n--- .values() ---")
print(f"Values: {list(mamak_menu.values())}")

# Practical example: formatted menu
print("\n--- Formatted Menu ---")
print("🍽️  MAMAK MENU  🍽️")
print("-" * 30)
for item, price in mamak_menu.items():
    print(f"  {item:<20} RM{price:.2f}")
print("-" * 30)
total = sum(mamak_menu.values())
print(f"  {'Total (if order all)':<20} RM{total:.2f}")


# ============================================================
# PART 5: Dictionary Methods
# ============================================================

print("\n=== Useful Methods ===")

d = {"a": 1, "b": 2, "c": 3}
print(f"Original: {d}")

# Check if key exists
print(f"'a' in d? {'a' in d}")        # True
print(f"'z' in d? {'z' in d}")        # False

# .setdefault() — get value if exists, set it if not
d.setdefault("d", 4)  # 'd' doesn't exist, so it sets it
d.setdefault("a", 999)  # 'a' exists, so nothing happens
print(f"After setdefault: {d}")

# len() — number of key-value pairs
print(f"Number of items: {len(d)}")

# .copy() — shallow copy (same warning as lists!)
d_copy = d.copy()
print(f"Copy: {d_copy}")

# .clear() — empty the dict
d_copy.clear()
print(f"After clear: {d_copy}")


# ============================================================
# PART 6: Nested Dictionaries
# ============================================================
# Dictionaries can contain other dictionaries!
# Like a folder inside a folder.

print("\n=== Nested Dictionaries ===")

students = {
    "Ahmad": {
        "age": 20,
        "course": "Computer Science",
        "cgpa": 3.5
    },
    "Siti": {
        "age": 21,
        "course": "Engineering",
        "cgpa": 3.8
    },
    "Raj": {
        "age": 19,
        "course": "Business",
        "cgpa": 3.2
    }
}

# Accessing nested values
print(f"Ahmad's CGPA: {students['Ahmad']['cgpa']}")
print(f"Siti's course: {students['Siti']['course']}")

# Looping through nested dict
print("\n--- All Students ---")
for name, info in students.items():
    print(f"{name}: {info['course']} (CGPA: {info['cgpa']})")


# ============================================================
# PART 7: Dictionary Comprehensions
# ============================================================
# Just like list comprehensions, but for dicts!
# {key_expr: value_expr for item in iterable}

print("\n=== Dictionary Comprehensions ===")

# Create a dict of squares
squares = {x: x**2 for x in range(6)}
print(f"Squares: {squares}")

# From a list of tuples
pairs = [("name", "Ahmad"), ("age", 25), ("city", "KL")]
info = {k: v for k, v in pairs}
print(f"From tuples: {info}")

# Filter a dictionary
affordable = {item: price for item, price in mamak_menu.items() if price < 5}
print(f"Affordable items (<RM5): {affordable}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")


# ============================================================
# 🎉 DICTIONARY BOSS!
# ============================================================
# You now know how to use Python's most versatile data structure!
# Dictionaries + Lists together are super powerful — used everywhere.
# Next up: Lesson 07 — Control Flow (if/elif/else)!

print("\n✅ Lesson 06 complete! Dictionaries — senang je! 📖")
