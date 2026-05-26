import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 10: f-strings and Formatting
  Run: python exercises/10_fstrings_exercises.py
"""

# Exercise 1: Format this price to 2 decimal places with RM prefix
price = 42.5
# TODO: print(f"???")  # Expected: "Price: RM42.50"


# Exercise 2: Format this large number with comma separators
population = 32365999
# TODO: print(f"???")  # Expected: "Population: 32,365,999"


# Exercise 3: Create a formatted table from this data
# Use alignment specifiers (<, >, ^) to make it look nice
items = [
    ("Nasi Lemak", 5.50, 2),
    ("Roti Canai", 2.50, 3),
    ("Teh Tarik", 1.80, 5),
    ("Maggi Goreng", 7.00, 1),
]
# Expected output (something like):
#   Item             Price    Qty    Total
#   ─────────────────────────────────────
#   Nasi Lemak       RM 5.50    2   RM11.00
#   Roti Canai       RM 2.50    3   RM 7.50
#   ...
# TODO:


# Exercise 4: Format this decimal as a percentage
pass_rate = 0.8725
# TODO: print(f"???")  # Expected: "Pass rate: 87.3%"  (1 decimal place)


# Exercise 5: Using .join(), create a comma-separated string from this list
# But the last item should use "and" instead of a comma
fruits = ["durian", "rambutan", "mangosteen", "papaya"]
# Expected: "durian, rambutan, mangosteen and papaya"
# TODO:


# Exercise 6: Create a multi-line receipt using f-strings
# Include: store name, items, subtotal, tax (6%), total
# Make it look professional with proper alignment!
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

# Check Exercise 5
check_var("result", str, check_fn=lambda v: v.replace(" ", "") == "durian,rambutan,mangosteenandpapaya".replace(" ", ""), val_msg="result string values are incorrect! Check join or string concatenation.")

# Check Exercise 6
check_var("receipt", str, check_fn=lambda v: "MAMAK CORNER" in v and "TOTAL" in v and "Subtotal" in v, val_msg="receipt string is missing required elements (MAMAK CORNER, Subtotal, or TOTAL)!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! You are the f-string wizard! 🪄")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Align your formatters and try again! ☕")
print("="*55)
print("🏃 Check: python solutions/10_fstrings_solutions.py")

