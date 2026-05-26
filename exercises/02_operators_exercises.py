import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 02: Operators
  Run: python exercises/02_operators_exercises.py
"""

# Exercise 1: What will each expression evaluate to? 
# Write your prediction first, then uncomment the print to check!

# a) 17 // 3 = ???
# b) 17 % 3 = ???
# c) 2 ** 5 = ???
# d) 10 / 3 = ???
# e) True + True + False = ???

# print(f"a) {17 // 3}")
# print(f"b) {17 % 3}")
# print(f"c) {2 ** 5}")
# print(f"d) {10 / 3}")
# print(f"e) {True + True + False}")


# Exercise 2: Write an expression that checks:
# "Is the number even AND greater than 10?"
number = 24
# TODO: is_even_and_big = ???
# print(f"{number} is even and > 10: {is_even_and_big}")


# Exercise 3: Temperature converter
# Convert 98.6°F to Celsius using the formula: C = (F - 32) * 5/9
fahrenheit = 98.6
# TODO: celsius = ???
# print(f"{fahrenheit}°F = {celsius:.1f}°C")


# Exercise 4: Use the 'in' operator to check if "durian" is in the list
fruits = ["rambutan", "mangosteen", "durian", "papaya"]
# TODO: has_durian = ???
# print(f"Has durian? {has_durian}")


# Exercise 5: Operator precedence — what's the result WITHOUT running it first?
# a) 2 + 3 * 4 - 1 = ???
# b) (2 + 3) * (4 - 1) = ???
# c) 10 > 5 and 3 < 1 = ???
# d) not (5 > 3 and 2 > 4) = ???

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
check_var("is_even_and_big", bool, check_fn=lambda v: v is True, val_msg="24 is even and greater than 10, so it must be True!")

# Check Exercise 3
check_var("celsius", float, check_fn=lambda v: abs(v - 37.0) < 0.1, val_msg="celsius value is wrong! Formula: C = (F - 32) * 5/9. Should be around 37.0.")

# Check Exercise 4
check_var("has_durian", bool, check_fn=lambda v: v is True, val_msg="durian is in the fruits list, so this must be True!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! You are the operator king weh! 👑")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Review operators and try again! ☕")
print("="*55)
print("🏃 Check: python solutions/02_operators_solutions.py")

