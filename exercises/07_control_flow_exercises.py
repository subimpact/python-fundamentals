import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 07: Control Flow
  Run: python exercises/07_control_flow_exercises.py
"""

# Exercise 1: Grade calculator
# Given a score (0-100), print the grade:
# A: 80-100, B: 60-79, C: 40-59, D: 20-39, F: 0-19
score = 75
# TODO: Use if/elif/else to set grade = ???
# print(f"Score {score} → Grade: {grade}")


# Exercise 2: FizzBuzz! (Classic interview question)
# Write a function fizzbuzz(n) that returns:
# - "FizzBuzz" if divisible by 3 AND 5
# - "Fizz" if divisible by 3 only
# - "Buzz" if divisible by 5 only
# - the number itself (as int) otherwise
# TODO: def fizzbuzz(n): ...
# Then call it for numbers 1 to 20 and print the results


# Exercise 3: Use ternary operator
# Set drink to "teh tarik" if temperature > 30, else "milo ais"
temperature = 35
# TODO: drink = ???
# print(f"At {temperature}°C, I'll have: {drink}")


# Exercise 4: Check if a year is a leap year
# Rules: divisible by 4 AND (not divisible by 100 OR divisible by 400)
year = 2024
# TODO: is_leap = ???
# print(f"{year} is a leap year: {is_leap}")


# Exercise 5: Simple login check
# Write a function login(username, password) that returns:
# - "success" if username == "admin" and password == "python123"
# - "wrong password" if username is right but password is wrong
# - "unknown user" otherwise
username = "admin"
password = "python123"
# TODO: def login(username, password): ...


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
check_var("grade", str, check_fn=lambda v: v == "B", val_msg="grade for score 75 should be 'B'!")

# Check Exercise 2 — FizzBuzz function
if "fizzbuzz" not in globals():
    print("❌ fizzbuzz: Ayo, where is the function? Cannot find weh!")
    errors += 1
else:
    fb = globals()["fizzbuzz"]
    fb_cases = [(15, "FizzBuzz"), (9, "Fizz"), (10, "Buzz"), (7, 7), (30, "FizzBuzz")]
    fb_ok = True
    for n, expected in fb_cases:
        try:
            got = fb(n)
            if got != expected:
                print(f"❌ fizzbuzz({n}): expected {expected!r}, got {got!r}")
                fb_ok = False
        except Exception as e:
            print(f"❌ fizzbuzz({n}): crashed with {type(e).__name__}: {e}")
            fb_ok = False
    if fb_ok:
        print("✅ fizzbuzz: Steady lah! Fizz, Buzz, FizzBuzz all correct.")
    else:
        errors += 1

# Check Exercise 3
check_var("drink", str, check_fn=lambda v: v == "teh tarik", val_msg="drink should be 'teh tarik' for temp > 30!")

# Check Exercise 4
check_var("is_leap", bool, check_fn=lambda v: v is True, val_msg="is_leap for 2024 should be True!")

# Check Exercise 5 — login function
if "login" not in globals():
    print("❌ login: Ayo, where is the function? Cannot find weh!")
    errors += 1
else:
    lg = globals()["login"]
    lg_cases = [
        ("admin", "python123", "success"),
        ("admin", "wrongpass", "wrong password"),
        ("bob", "python123", "unknown user"),
    ]
    lg_ok = True
    for u, p, expected in lg_cases:
        try:
            got = lg(u, p)
            if got != expected:
                print(f"❌ login({u!r}, ...): expected {expected!r}, got {got!r}")
                lg_ok = False
        except Exception as e:
            print(f"❌ login({u!r}, ...): crashed with {type(e).__name__}: {e}")
            lg_ok = False
    if lg_ok:
        print("✅ login: Steady lah! All three cases handled correctly.")
    else:
        errors += 1

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Control flow is in your control weh! 🚦")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Re-route your code logic and try again! ☕")
print("="*55)
print("🏃 Check: python solutions/07_control_flow_solutions.py")
