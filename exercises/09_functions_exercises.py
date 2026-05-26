import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 09: Functions
  Run: python exercises/09_functions_exercises.py
"""

# Exercise 1: Write a function called `greet` that takes a name
# and returns "Hello, {name}! Apa khabar?"
# TODO: def greet(name):
# Test: print(greet("Ahmad"))


# Exercise 2: Write a function `calculate_bmi` that takes weight (kg)
# and height (m), returns the BMI (weight / height²)
# Also return the category: Underweight (<18.5), Normal (18.5-24.9),
# Overweight (25-29.9), Obese (30+)
# TODO: def calculate_bmi(weight, height):
# Test: print(calculate_bmi(70, 1.75))


# Exercise 3: Write a function with a default parameter
# `make_drink(drink="teh tarik", ice=True)` that returns
# a string like "One teh tarik, with ice!" or "One kopi, no ice!"
# TODO:
# Test: print(make_drink())
# Test: print(make_drink("kopi", False))


# Exercise 4: Write a function using *args that accepts any number
# of food items and returns the total count and a formatted list
# TODO: def order_food(*items):
# Test: order_food("nasi lemak", "roti canai", "teh tarik")


# Exercise 5: Write a function that returns multiple values
# Given a list of numbers, return: min, max, average, and sum
# TODO: def list_stats(numbers):
# Test: print(list_stats([10, 20, 30, 40, 50]))


# Exercise 6: Use a lambda to sort this list of dicts by "name"
people = [
    {"name": "Siti", "age": 28},
    {"name": "Ahmad", "age": 25},
    {"name": "Raj", "age": 30},
    {"name": "Mei", "age": 22},
]
# TODO: sorted_people = sorted(people, key=???)


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
        print(f"❌ {name}: {missing_msg or 'Ayo, function/variable not found! Did you delete it?'}")
        errors += 1
        return False
    val = globals().get(name, locals().get(name))
    if expected_type is not None and not isinstance(val, expected_type):
        print(f"❌ {name}: {type_msg or f'Wrong type! Should be {expected_type.__name__}, got {type(val).__name__} lah.'}")
        errors += 1
        return False
    if check_fn is not None:
        try:
            if not check_fn(val):
                print(f"❌ {name}: {val_msg or 'Ayo, answer is wrong! Try again.'}")
                errors += 1
                return False
        except Exception as e:
            print(f"❌ {name}: Run error: {e}")
            errors += 1
            return False
    print(f"✅ {name}: Steady lah! Passed.")
    return True

# Check Exercise 1
check_var("greet", type(lambda: None), check_fn=lambda fn: fn("Abu") == "Hello, Abu! Apa khabar?", val_msg="greet function return string is wrong!")

# Check Exercise 2
check_var("calculate_bmi", type(lambda: None), check_fn=lambda fn: abs(fn(70, 1.75)[0] - 22.85) < 0.1 and fn(70, 1.75)[1] == "Normal", val_msg="calculate_bmi return values are incorrect!")

# Check Exercise 3
check_var("make_drink", type(lambda: None), check_fn=lambda fn: fn() == "One teh tarik, with ice!" and fn("kopi", False) == "One kopi, no ice!", val_msg="make_drink return values are incorrect!")

# Check Exercise 5
check_var("list_stats", type(lambda: None), check_fn=lambda fn: fn([10, 20, 30]) == (10, 30, 20.0, 60), val_msg="list_stats output statistics are incorrect!")

# Check Exercise 6
check_var("sorted_people", list, check_fn=lambda v: [p["name"] for p in v] == ["Ahmad", "Mei", "Raj", "Siti"], val_msg="sorted_people is not sorted correctly by name!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Function expert status unlocked! 🚀")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Debug your arguments or return statements! ☕")
print("="*55)
print("🏃 Check: python solutions/09_functions_solutions.py")

