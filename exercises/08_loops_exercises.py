import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 08: Loops
  Run: python exercises/08_loops_exercises.py
"""

# Exercise 1: Print a countdown from 10 to 1, then "Blast off! 🚀"
# Use a for loop with range()
# TODO: countdown = []   # build the list [10, 9, 8, ..., 1]
# TODO: blast_off = ""   # the message to print at the end

# Exercise 2: Sum all numbers from 1 to 100 using a while loop
# TODO: total = 0
# TODO: (while loop that adds to total)
# print(f"Sum: {total}")  # Expected: 5050


# Exercise 3: Using enumerate(), print each item with its number (starting from 1)
states = ["Penang", "Selangor", "Johor", "Sabah", "Sarawak", "Perak"]
# Expected:
#   1. Penang
#   2. Selangor
#   ... etc
# TODO: numbered = []  # list of "1. Penang" style strings


# Exercise 4: Using zip(), combine names and scores, then print
names = ["Ahmad", "Siti", "Raj", "Mei"]
scores = [85, 92, 78, 95]
# Expected: "Ahmad scored 85", "Siti scored 92", etc.
# TODO: report = []  # list of "Ahmad scored 85" style strings


# Exercise 5: Find the first number in the list divisible by both 3 and 7
# Use a for loop with break!
numbers = [2, 5, 11, 14, 18, 21, 28, 42, 50]
# TODO: found = None   # set this to the number you find, then break
# print(f"Found: {found}")


# Exercise 6: Print only the ODD numbers from 1 to 20 using continue
# TODO: odd_numbers = []  # collect the odd numbers here


# Exercise 7: Multiplication table — print the 7 times table (7x1 to 7x12)
# Expected format: "7 x  1 =  7"
# TODO: times_table = []  # list of "7 x  1 =  7" style strings


# ============================================================
# 🧪 AUTOMATED CHECKER (No cheat ah!)
# ============================================================
print("\n" + "="*55)
print("🧐 Checking your answers... Let's see if can pass or not...")
print("="*55)
errors = 0

def check_var(name, expected_type, check_fn=None, missing_msg=None, type_msg=None, val_msg=None):
    global errors
    if name not in globals() and name not in locals():
        print(f"❌ {name}: {missing_msg or 'Ayo, variable not found! Did you delete it?'}")
        errors += 1
        return False
    val = globals().get(name, locals().get(name))
    if expected_type is not None and not isinstance(val, expected_type):
        print(f"❌ {name}: {type_msg or f'Wrong type! Should be {expected_type.__name__}, got {type(val).__name__} lah.'}")
        errors += 1
        return False
    if check_fn is not None and not check_fn(val):
        print(f"❌ {name}: {val_msg or 'Ayo, answer is wrong! Try again.'}")
        errors += 1
        return False
    print(f"✅ {name}: Steady lah! Passed.")
    return True

# Check Exercise 1
check_var("countdown", list, check_fn=lambda v: v == list(range(10, 0, -1)), val_msg="countdown should be [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] — did you use range(10, 0, -1)?")
check_var("blast_off", str, check_fn=lambda v: "blast" in v.lower(), val_msg="blast_off should contain 'Blast off!'")

# Check Exercise 2
check_var("total", int, check_fn=lambda v: v == 5050, val_msg="total sum from 1 to 100 should be 5050!")

# Check Exercise 3
check_var("numbered", list, check_fn=lambda v: len(v) == 6 and v[0] == "1. Penang" and v[1] == "2. Selangor", val_msg="numbered should be ['1. Penang', '2. Selangor', ...] — did you use enumerate(states, 1)?")

# Check Exercise 4
check_var("report", list, check_fn=lambda v: len(v) == 4 and v[0] == "Ahmad scored 85" and v[3] == "Mei scored 95", val_msg="report should be ['Ahmad scored 85', 'Siti scored 92', ...] — did you use zip(names, scores)?")

# Check Exercise 5
check_var("found", int, check_fn=lambda v: v == 21, val_msg="found should be 21 — the FIRST number divisible by both 3 and 7 (did you break after finding it?)")

# Check Exercise 6
check_var("odd_numbers", list, check_fn=lambda v: v == list(range(1, 20, 2)), val_msg="odd_numbers should be [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] — did you use continue to skip evens?")

# Check Exercise 7
check_var("times_table", list, check_fn=lambda v: len(v) == 12 and "7 x  1 =  7" in v and "7 x 12 = 84" in v, val_msg="times_table should have 12 entries from '7 x  1 =  7' to '7 x 12 = 84' — try f\"7 x {i:>2} = {7*i:>2}\"")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Loop-de-loop and pass! 🔄")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Review loops condition! ☕")
print("="*55)
print("🏃 Check: python solutions/08_loops_solutions.py")
