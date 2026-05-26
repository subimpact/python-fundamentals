import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
=============================================================
  EXERCISE 01: Variables and Data Types
  Test your knowledge! Complete the TODOs below.
=============================================================
  Run this file: python exercises/01_variables_exercises.py
  Check answers: python solutions/01_variables_solutions.py
=============================================================
"""

# -----------------------------------------------
# Exercise 1: Create variables
# -----------------------------------------------
# Create the following variables:
#   - my_name (your name as a string)
#   - my_age (your age as an integer)
#   - my_height (your height in meters as a float)
#   - is_student (True or False)

# TODO: Write your code below
# my_name = ???
# my_age = ???
# my_height = ???
# is_student = ???

# print(f"Name: {my_name}, Age: {my_age}, Height: {my_height}m, Student: {is_student}")


# -----------------------------------------------
# Exercise 2: Type checking
# -----------------------------------------------
# For each variable below, print its type using type().
# Expected output format: "42 is type: int"

mystery_a = 42
mystery_b = "hello"
mystery_c = 3.14
mystery_d = True
mystery_e = None

# TODO: Print the type of each variable
# Example: print(f"{mystery_a} is type: {type(mystery_a).__name__}")


# -----------------------------------------------
# Exercise 3: Type conversion
# -----------------------------------------------
# Convert the following and print the results:
# a) Convert the string "100" to an integer
# b) Convert the integer 25 to a float
# c) Convert the float 3.99 to an integer (what happens?)
# d) Convert the integer 0 to a boolean (what happens?)
# e) Convert the string "" (empty) to a boolean (what happens?)

# TODO: Write your code below


# -----------------------------------------------
# Exercise 4: Swap variables
# -----------------------------------------------
# Swap the values of x and y WITHOUT using a temporary variable.
# (Hint: Python makes this very easy!)

x = "Nasi Lemak"
y = "Roti Canai"

# TODO: Swap x and y here

# print(f"After swap: x = {x}, y = {y}")
# Expected: x = Roti Canai, y = Nasi Lemak


# -----------------------------------------------
# Exercise 5: Multiple assignment
# -----------------------------------------------
# In ONE line, create three variables:
#   - city = "Kuala Lumpur"
#   - country = "Malaysia"
#   - population = 32000000

# TODO: Write ONE line of code below

# print(f"{city}, {country} - Population: {population:,}")


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
        print(f"❌ {name}: {missing_msg or 'Ayo, where is the variable? Cannot find weh!'}")
        errors += 1
        return False
    val = globals().get(name, locals().get(name))
    if expected_type is not None and not isinstance(val, expected_type):
        print(f"❌ {name}: {type_msg or f'Wrong type! Should be {expected_type.__name__}, but you gave {type(val).__name__} lah.'}")
        errors += 1
        return False
    if check_fn is not None and not check_fn(val):
        print(f"❌ {name}: {val_msg or 'Ayo, value is wrong! Try again.'}")
        errors += 1
        return False
    print(f"✅ {name}: Steady lah! Passed.")
    return True

# Check Exercise 1
check_var("my_name", str, check_fn=lambda v: len(v) > 0, val_msg="Name cannot be empty string weh!")
check_var("my_age", int, check_fn=lambda v: 0 < v < 120, val_msg="Age looks weird, make sure it's a realistic age weh!")
check_var("my_height", float, check_fn=lambda v: 0.5 < v < 3.0, val_msg="Height should be in meters, e.g., 1.75!")
check_var("is_student", bool)

# Check Exercise 4
check_var("x", str, check_fn=lambda v: v == "Roti Canai", val_msg="Should be 'Roti Canai' after swap!")
check_var("y", str, check_fn=lambda v: v == "Nasi Lemak", val_msg="Should be 'Nasi Lemak' after swap!")

# Check Exercise 5
check_var("city", str, check_fn=lambda v: v == "Kuala Lumpur", val_msg="City must be 'Kuala Lumpur'!")
check_var("country", str, check_fn=lambda v: v == "Malaysia", val_msg="Country must be 'Malaysia'!")
check_var("population", int, check_fn=lambda v: v == 32000000, val_msg="Population must be 32000000!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! You are the real variable master weh! 🏆")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Relax, drink some teh tarik, and fix it! ☕")
print("="*55)
print("🏃 Run solutions file to compare code structures:")
print("   python solutions/01_variables_solutions.py")

