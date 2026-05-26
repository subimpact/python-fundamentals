import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
=============================================================
  LESSON 08: Loops 🔄
  Repeat things — without copy-pasting like a noob!
=============================================================

Loops let you run code multiple times. Without loops, if you
wanted to print numbers 1 to 100, you'd need 100 print statements.
Mati lah! (Die lah!) With a loop? Just 2 lines. Shiok!

This lesson covers:
  - for loops (iterate over sequences)
  - range() function
  - while loops (repeat until condition is false)
  - break, continue, pass
  - enumerate() — loop with index
  - zip() — loop over multiple lists
  - Nested loops
  - Loop-else (Python's secret weapon!)
=============================================================
"""

# ============================================================
# PART 1: for Loops
# ============================================================
# for loops iterate over any sequence (list, string, range, etc.)

print("=== for Loops ===")

# Looping through a list
foods = ["nasi lemak", "roti canai", "char kuey teow", "satay"]
print("Today's menu:")
for food in foods:
    print(f"  🍽️ {food}")

# Looping through a string
print("\nSpelling 'MAKAN':")
for letter in "MAKAN":
    print(f"  → {letter}")


# ============================================================
# PART 2: range() — Generate Numbers
# ============================================================
# range(stop)           → 0 to stop-1
# range(start, stop)    → start to stop-1
# range(start, stop, step) → start to stop-1, jumping by step

print("\n=== range() ===")

# range(5) → 0, 1, 2, 3, 4
print("range(5):", list(range(5)))

# range(1, 6) → 1, 2, 3, 4, 5
print("range(1, 6):", list(range(1, 6)))

# range(0, 20, 5) → 0, 5, 10, 15
print("range(0, 20, 5):", list(range(0, 20, 5)))

# Countdown!
print("\nCountdown:")
for i in range(5, 0, -1):
    print(f"  {i}...")
print("  🚀 Blast off!")


# ============================================================
# PART 3: while Loops
# ============================================================
# while loops keep going as long as the condition is True.
# Be careful — if the condition never becomes False, infinite loop!
# (Like waiting for food at a slow mamak — forever!)

print("\n=== while Loops ===")

# Basic while loop
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1  # Don't forget this! Otherwise infinite loop!

# Practical example: simple countdown
print("\nAnother countdown:")
fuel = 3
while fuel > 0:
    print(f"  Fuel remaining: {fuel}")
    fuel -= 1
print("  No more fuel! Need to refill at petrol station.")


# ============================================================
# PART 4: break — Emergency Exit! 🚪
# ============================================================
# break immediately exits the loop. Like pressing the
# emergency stop button. No more iterations.

print("\n=== break ===")

# Find the first number divisible by 7 in a list
numbers = [3, 11, 25, 42, 56, 70, 88]
print(f"Looking for first number divisible by 7 in {numbers}...")
for num in numbers:
    if num % 7 == 0:
        print(f"  Found it! {num} is divisible by 7.")
        break  # Stop searching — already found!
    print(f"  Checking {num}... not divisible by 7.")


# ============================================================
# PART 5: continue — Skip This Round! ⏭️
# ============================================================
# continue skips the REST of the current iteration
# and jumps to the next one.

print("\n=== continue ===")

# Print only odd numbers
print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}", end=" ")
print()  # New line


# ============================================================
# PART 6: pass — Do Nothing (For Now) 🤷
# ============================================================
# pass is a placeholder. Use it when you need a code block
# but haven't written the logic yet.

print("\n=== pass ===")

for i in range(5):
    if i == 3:
        pass  # TODO: Handle the special case later
    else:
        print(f"  Processing item {i}")

# Also used for empty functions/classes:
# def my_function():
#     pass  # Will implement later


# ============================================================
# PART 7: enumerate() — Loop with Index
# ============================================================
# Want to know the index AND the value? enumerate() is your friend!
# No more doing "i = 0; i += 1" manually — that's so last year.

print("\n=== enumerate() ===")

states = ["Penang", "Selangor", "Johor", "Sabah", "Sarawak"]
print("Malaysian states:")
for index, state in enumerate(states):
    print(f"  {index}: {state}")

# Start counting from 1 instead of 0
print("\nWith start=1:")
for index, state in enumerate(states, start=1):
    print(f"  {index}. {state}")


# ============================================================
# PART 8: zip() — Loop Over Multiple Lists
# ============================================================
# zip() pairs up items from multiple lists. Like matching
# people with their food orders.

print("\n=== zip() ===")

names = ["Ahmad", "Siti", "Raj"]
orders = ["Nasi Lemak", "Roti Canai", "Thosai"]
prices = [5.50, 2.50, 4.00]

print("Orders:")
for name, order, price in zip(names, orders, prices):
    print(f"  {name} ordered {order} (RM{price:.2f})")

# zip stops at the shortest list!
short = [1, 2]
long = [10, 20, 30, 40]
print(f"\nzip with unequal lists: {list(zip(short, long))}")
# Only 2 pairs — shorter list determines the length


# ============================================================
# PART 9: Nested Loops
# ============================================================
# A loop inside a loop. Like a clock — the minute hand
# goes around 60 times for every 1 round of the hour hand.

print("\n=== Nested Loops ===")

# Multiplication table (2 to 4)
print("Mini Multiplication Table:")
for i in range(2, 5):
    row = ""
    for j in range(1, 6):
        row += f"{i}x{j}={i*j:>2}  "
    print(f"  {row}")


# ============================================================
# PART 10: Loop-Else — Python's Secret Weapon! 🤫
# ============================================================
# Python has a unique feature: else on a loop!
# The else block runs ONLY if the loop completed without
# hitting a break. Most people don't know about this!

print("\n=== Loop-Else ===")

# Example: Check if a number is prime
def is_prime(n):
    """Check if n is prime using loop-else."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"  {n} is NOT prime (divisible by {i})")
            break
    else:
        # This runs ONLY if break was NOT triggered
        print(f"  {n} IS prime!")
        return True
    return False

print("Prime check:")
for num in [7, 12, 23, 45, 97]:
    is_prime(num)


# ============================================================
# PART 11: Common Loop Patterns
# ============================================================

print("\n=== Common Patterns ===")

# Pattern 1: Accumulator (sum up values)
prices = [5.50, 2.50, 7.00, 4.00, 1.80]
total = 0
for price in prices:
    total += price
print(f"Total bill: RM{total:.2f}")

# Pattern 2: Counter
words = "nasi lemak is the best food in malaysia and nasi lemak is life"
word_list = words.split()
count = 0
for word in word_list:
    if word == "nasi":
        count += 1
print(f"'nasi' appears {count} times")

# Pattern 3: Building a new list (but prefer list comprehension!)
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for n in original:
    if n % 2 == 0:
        evens.append(n)
print(f"Even numbers: {evens}")

# List comprehension version (preferred):
evens_lc = [n for n in original if n % 2 == 0]
print(f"Even (comprehension): {evens_lc}")


# ============================================================
# 🎉 LOOP MASTER!
# ============================================================
# Now you can make Python repeat anything!
# Next up: Lesson 09 — Functions!
# We'll learn how to organize code into reusable blocks.

print("\n✅ Lesson 08 complete! Loops — pusing pusing, all settled! 🔄")
