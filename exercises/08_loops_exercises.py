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
# TODO:


# Exercise 2: Sum all numbers from 1 to 100 using a while loop
# TODO:
# print(f"Sum: {total}")  # Expected: 5050


# Exercise 3: Using enumerate(), print each item with its number (starting from 1)
states = ["Penang", "Selangor", "Johor", "Sabah", "Sarawak", "Perak"]
# Expected:
#   1. Penang
#   2. Selangor
#   ... etc
# TODO:


# Exercise 4: Using zip(), combine names and scores, then print
names = ["Ahmad", "Siti", "Raj", "Mei"]
scores = [85, 92, 78, 95]
# Expected: "Ahmad scored 85", "Siti scored 92", etc.
# TODO:


# Exercise 5: Find the first number in the list divisible by both 3 and 7
# Use a for loop with break!
numbers = [2, 5, 11, 14, 18, 21, 28, 42, 50]
# TODO:


# Exercise 6: Print only the ODD numbers from 1 to 20 using continue
# TODO:


# Exercise 7: Multiplication table — print the 7 times table (7x1 to 7x12)
# Expected format: "7 x  1 =  7"
# TODO:


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

# Check Exercise 2
check_var("total", int, check_fn=lambda v: v == 5050, val_msg="total sum from 1 to 100 should be 5050!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Loop-de-loop and pass! 🔄")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Review loops condition! ☕")
print("="*55)
print("🏃 Check: python solutions/08_loops_solutions.py")

