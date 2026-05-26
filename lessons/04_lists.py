"""
=============================================================
  LESSON 04: Lists 📋
  Python's most popular data structure — like a shopping list!
=============================================================

Lists are ordered collections that can hold anything — numbers,
strings, even other lists! Think of it as your mamak order list:
"Roti canai satu, teh tarik dua, maggi goreng satu..."

This lesson covers:
  - Creating lists
  - Accessing elements (indexing & slicing)
  - Modifying lists (append, remove, insert, pop)
  - Return values of list methods
  - List comprehensions (the Python power move!)
  - Nested lists
  - Useful list functions (len, sorted, min, max, sum)

📌 Content adapted from the original notebook (Sections 1.1–1.2)
=============================================================
"""

# ============================================================
# PART 1: Creating Lists
# ============================================================
# Lists use square brackets [] and items are separated by commas.

print("=== Creating Lists ===")

# A list of strings
mamak_order = ["roti canai", "teh tarik", "maggi goreng"]
print(f"Mamak order: {mamak_order}")

# A list of numbers
prices = [2.50, 1.80, 7.00]
print(f"Prices: {prices}")

# A list with mixed types — Python don't care, all also can!
mixed = ["Ahmad", 25, True, 3.14, None]
print(f"Mixed list: {mixed}")

# Empty list — two ways
empty1 = []
empty2 = list()
print(f"Empty list: {empty1}")


# ============================================================
# PART 2: Accessing Elements
# ============================================================
# Same indexing rules as strings!
# Index starts from 0, negative index counts from behind.

print("\n=== Accessing Elements ===")

fruits = ["durian", "rambutan", "mangosteen", "jackfruit", "papaya"]
print(f"List: {fruits}")
print(f"First item (index 0): {fruits[0]}")       # durian
print(f"Last item (index -1): {fruits[-1]}")       # papaya
print(f"Third item (index 2): {fruits[2]}")        # mangosteen

# Slicing — same as strings!
print(f"\nSlice [1:3]: {fruits[1:3]}")    # ['rambutan', 'mangosteen']
print(f"Slice [:3]:  {fruits[:3]}")       # First 3 items
print(f"Slice [2:]:  {fruits[2:]}")       # From index 2 onwards
print(f"Reversed:    {fruits[::-1]}")     # Reversed list


# ============================================================
# PART 3: Modifying Lists
# ============================================================
# Unlike strings, lists are MUTABLE — you can change them!
# Like editing your order at the mamak.

print("\n=== Modifying Lists ===")

# From the original notebook:
l1 = ['RAG', 'is', 'awesome']
print(f"Original list: {l1}")

# .append() — Add to the end
l1.append('!')
print(f"After append('!'): {l1}")

# .remove() — Remove first occurrence of a value
l1.remove('awesome')
print(f"After remove('awesome'): {l1}")

# .insert(index, item) — Add at specific position
l1.insert(2, 'very cool')
print(f"After insert(2, 'very cool'): {l1}")

# .pop() — Remove and RETURN the last item (or by index)
popped = l1.pop()
print(f"After pop(): {l1} (popped item: '{popped}')")

popped_index = l1.pop(0)
print(f"After pop(0): {l1} (popped item: '{popped_index}')")

# Direct assignment — change an item at specific index
l1[0] = "Python"
print(f"After l1[0] = 'Python': {l1}")

# .extend() — Add all items from another list
l1.extend(["is", "great"])
print(f"After extend(['is', 'great']): {l1}")

# .clear() — Remove everything
backup = l1.copy()  # Save a copy first!
l1.clear()
print(f"After clear(): {l1}")
l1 = backup  # Restore


# ============================================================
# PART 4: Return Values — PENTING (Important)!
# ============================================================
# .append() and .remove() change the list IN PLACE
# and return None! This is a VERY common gotcha!

print("\n=== Return Values (Common Gotcha!) ===")

# From the original notebook — this is a classic mistake:
test_list = ["nasi", "lemak"]
result = test_list.append("ayam")
print(f"Return value of .append(): {result}")  # None! Alamak!
print(f"But the list IS modified: {test_list}")  # ['nasi', 'lemak', 'ayam']

# DON'T DO THIS:
# my_list = my_list.append("something")  ← This makes my_list = None!
# Always just call .append() without assigning the return value.


# ============================================================
# PART 5: List Comprehensions — The Power Move! 💪
# ============================================================
# List comprehensions are a Pythonic way to create lists.
# Once you get it, you'll use it EVERYWHERE. Confirm addictive!

print("\n=== List Comprehensions ===")

# From the original notebook:
# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(f"Squares (0-9): {squares}")

# The same thing with a regular for loop (more lines, same result):
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)
print(f"Squares (loop): {squares_loop}")

# With condition: [expression for item in iterable if condition]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares:   {even_squares}")

# The same thing with a for loop:
even_squares_loop = []
for x in range(10):
    if x % 2 == 0:
        even_squares_loop.append(x**2)
print(f"Even sq (loop): {even_squares_loop}")

# More practical examples:
print("\n--- More List Comprehension Examples ---")

# Convert list of strings to uppercase
foods = ["nasi lemak", "roti canai", "char kuey teow"]
foods_upper = [food.upper() for food in foods]
print(f"Uppercase: {foods_upper}")

# Filter: only items that start with 'r'
r_foods = [food for food in foods if food.startswith("r")]
print(f"Foods starting with 'r': {r_foods}")

# Transform: get the length of each word
lengths = [len(food) for food in foods]
print(f"Lengths: {lengths}")


# ============================================================
# PART 6: Nested Lists (Lists in Lists)
# ============================================================
# Lists can contain other lists — like a matrix or a table.

print("\n=== Nested Lists ===")

# A simple 3x3 grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Grid: {grid}")
print(f"Row 0: {grid[0]}")
print(f"Element at [1][2]: {grid[1][2]}")  # Row 1, Column 2 → 6


# ============================================================
# PART 7: Useful List Functions & Methods
# ============================================================

print("\n=== Useful Functions ===")

numbers = [42, 7, 15, 3, 99, 23]
print(f"List: {numbers}")
print(f"Length:  {len(numbers)}")
print(f"Min:     {min(numbers)}")
print(f"Max:     {max(numbers)}")
print(f"Sum:     {sum(numbers)}")
print(f"Sorted:  {sorted(numbers)}")          # Returns NEW list
print(f"Reverse sorted: {sorted(numbers, reverse=True)}")

# .sort() — sorts IN PLACE (modifies original list)
numbers.sort()
print(f"After .sort(): {numbers}")

# .reverse() — reverses IN PLACE
numbers.reverse()
print(f"After .reverse(): {numbers}")

# .index() — find position of an item
print(f"Index of 42: {numbers.index(42)}")

# .count() — count occurrences
letters = ['a', 'b', 'a', 'c', 'a', 'b']
print(f"\n{letters}.count('a') → {letters.count('a')}")

# 'in' operator — check if item exists
print(f"'a' in {letters}? {'a' in letters}")


# ============================================================
# PART 8: Copying Lists — Be Careful!
# ============================================================
# Assignment (=) creates a REFERENCE, not a copy!
# Both variables point to the SAME list!

print("\n=== Copying Lists ===")

original = [1, 2, 3]
reference = original       # NOT a copy!
real_copy = original.copy() # A proper copy

reference.append(999)
print(f"Original after modifying reference: {original}")  # [1, 2, 3, 999] — Alamak!
print(f"Real copy (unaffected): {real_copy}")             # [1, 2, 3] — Safe!


# ============================================================
# 🎉 LIST MASTER!
# ============================================================
# Lists are one of the most important data structures in Python.
# Next up: Lesson 05 — Tuples and Sets!

print("\n✅ Lesson 04 complete! Lists? No problem lah! 📋")
