"""
=============================================================
  LESSON 05: Tuples and Sets 🎯
  The other collections — each got their own special power!
=============================================================

Lists are great, but Python has other collection types too.
Think of it like this:
  - List = your daily order (can change anytime)
  - Tuple = your IC number (fixed, cannot change)
  - Set = the unique foods you've tried (no duplicates!)

This lesson covers:
  - Tuples: creating, accessing, immutability, unpacking
  - Sets: creating, adding, removing, set operations
  - When to use what (list vs tuple vs set)
=============================================================
"""

# ============================================================
# PART 1: Tuples — The Immutable List
# ============================================================
# Tuples are like lists, but you CANNOT change them after creation.
# Use parentheses () instead of square brackets [].

print("=== Tuples ===")

# Creating tuples
coordinates = (3.14, 2.72)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
single_item = (42,)  # NOTE: Need trailing comma for single item!
not_a_tuple = (42)   # This is just a number in brackets!

print(f"Coordinates: {coordinates} (type: {type(coordinates).__name__})")
print(f"Days: {days}")
print(f"Single item tuple: {single_item} (type: {type(single_item).__name__})")
print(f"Not a tuple: {not_a_tuple} (type: {type(not_a_tuple).__name__})")

# Accessing — same as lists
print(f"\nFirst day: {days[0]}")
print(f"Last day: {days[-1]}")
print(f"Slice [1:3]: {days[1:3]}")

# IMMUTABLE — cannot change!
# days[0] = "Sunday"  ← This will ERROR! Tuples cannot be modified.
# That's the whole point — they're like a locked container.


# ============================================================
# PART 2: Tuple Unpacking — The Cool Trick! 😎
# ============================================================
# You can "unpack" a tuple into individual variables.
# Super useful and very Pythonic!

print("\n=== Tuple Unpacking ===")

# Basic unpacking
person = ("Ahmad", 25, "Penang")
name, age, city = person  # Each variable gets one value
print(f"Name: {name}, Age: {age}, City: {city}")

# Swap variables without a temp variable — legendary move!
a = "Teh Tarik"
b = "Kopi O"
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a  # Tuples behind the scenes!
print(f"After swap:  a={a}, b={b}")

# Using * to capture remaining items
first, *rest = (1, 2, 3, 4, 5)
print(f"\nfirst = {first}, rest = {rest}")

head, *middle, tail = (1, 2, 3, 4, 5)
print(f"head = {head}, middle = {middle}, tail = {tail}")

# Functions returning multiple values (actually returning a tuple!)
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"\nMin: {low}, Max: {high}")


# ============================================================
# PART 3: Tuple Methods
# ============================================================
# Since tuples are immutable, they only have 2 methods:

print("\n=== Tuple Methods ===")
scores = (85, 92, 78, 92, 95, 92)

print(f"Tuple: {scores}")
print(f".count(92): {scores.count(92)}")   # How many 92s? → 3
print(f".index(78): {scores.index(78)}")   # Where is 78? → 2


# ============================================================
# PART 4: Sets — No Duplicates Allowed! 🚫
# ============================================================
# Sets are UNordered collections with NO DUPLICATE elements.
# Use curly braces {} to create them.
# Perfect for removing duplicates or checking membership fast!

print("\n=== Sets ===")

# Creating sets
unique_fruits = {"durian", "rambutan", "mangosteen", "durian", "rambutan"}
print(f"Set (duplicates removed!): {unique_fruits}")

# Create from a list — instant duplicate removal!
order = ["teh tarik", "roti canai", "teh tarik", "nasi lemak", "teh tarik"]
unique_order = set(order)
print(f"\nOriginal list: {order}")
print(f"As set (unique): {unique_order}")

# Empty set — use set(), NOT {}!
empty_set = set()     # ✅ Correct
empty_dict = {}       # ❌ This creates a dict, not a set!
print(f"\nType of set(): {type(empty_set).__name__}")
print(f"Type of {{}}: {type(empty_dict).__name__}")


# ============================================================
# PART 5: Set Operations
# ============================================================
# This is where sets truly shine!
# Like comparing who went to which mamak stall.

print("\n=== Set Operations ===")

ali_foods = {"nasi lemak", "roti canai", "teh tarik", "milo"}
abu_foods = {"roti canai", "maggi goreng", "teh tarik", "bandung"}

print(f"Ali's foods:  {ali_foods}")
print(f"Abu's foods:  {abu_foods}")

# Union — ALL items from both (gabung semua)
print(f"\nUnion (both combined): {ali_foods | abu_foods}")
# Or: ali_foods.union(abu_foods)

# Intersection — items in BOTH (yang sama)
print(f"Intersection (both eat): {ali_foods & abu_foods}")
# Or: ali_foods.intersection(abu_foods)

# Difference — items in first but NOT second
print(f"Ali only: {ali_foods - abu_foods}")
# Or: ali_foods.difference(abu_foods)

print(f"Abu only: {abu_foods - ali_foods}")

# Symmetric difference — items in either but NOT both
print(f"Unique to each: {ali_foods ^ abu_foods}")


# ============================================================
# PART 6: Modifying Sets
# ============================================================
# Sets are mutable (can change), but individual items are NOT
# indexable — no set[0]! Sets don't have order.

print("\n=== Modifying Sets ===")

menu = {"roti canai", "nasi lemak"}
print(f"Original: {menu}")

# .add() — add one item
menu.add("teh tarik")
print(f"After add: {menu}")

# .update() — add multiple items
menu.update(["milo", "maggi goreng"])
print(f"After update: {menu}")

# .discard() — remove (no error if not found)
menu.discard("milo")
print(f"After discard('milo'): {menu}")

# .remove() — remove (ERROR if not found!)
# menu.remove("sushi")  ← This would crash! Use .discard() to be safe.

# .pop() — remove and return a random item (sets are unordered!)
popped = menu.pop()
print(f"After pop: {menu} (popped: '{popped}')")


# ============================================================
# PART 7: Membership Testing — Sets Are FAST!
# ============================================================
# Checking "is this item in the collection?" is much faster
# with sets than with lists. For big data, this matters A LOT.

print("\n=== Membership Testing ===")

big_list = list(range(1000000))
big_set = set(range(1000000))

# Both work, but set is O(1) vs list is O(n)
print(f"999999 in list? {999999 in big_list}")  # Slow for big lists
print(f"999999 in set?  {999999 in big_set}")   # Always fast!


# ============================================================
# PART 8: When to Use What? 🤔
# ============================================================
#
# ┌─────────────┬───────────┬───────────┬───────────┐
# │ Feature     │ List      │ Tuple     │ Set       │
# ├─────────────┼───────────┼───────────┼───────────┤
# │ Syntax      │ [1,2,3]   │ (1,2,3)   │ {1,2,3}   │
# │ Ordered?    │ ✅ Yes    │ ✅ Yes    │ ❌ No     │
# │ Mutable?    │ ✅ Yes    │ ❌ No     │ ✅ Yes    │
# │ Duplicates? │ ✅ Yes    │ ✅ Yes    │ ❌ No     │
# │ Indexable?  │ ✅ Yes    │ ✅ Yes    │ ❌ No     │
# └─────────────┴───────────┴───────────┴───────────┘
#
# Rules of thumb:
# - Need to change items? → List
# - Data shouldn't change? → Tuple (also slightly faster)
# - Need unique items? → Set
# - Need fast "is this in there?" checks? → Set
# - Returning multiple values from a function? → Tuple
# - Storing key-value pairs? → Dictionary (next lesson!)


# ============================================================
# 🎉 THREE COLLECTION TYPES DOWN!
# ============================================================
# Now you know lists, tuples, AND sets.
# Next up: Lesson 06 — Dictionaries!
# The most powerful collection type. Get ready!

print("\n✅ Lesson 05 complete! Tuples and sets — faham already! 🎯")
