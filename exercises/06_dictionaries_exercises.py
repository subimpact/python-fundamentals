import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 06: Dictionaries
  Run: python exercises/06_dictionaries_exercises.py
"""

# Exercise 1: Create a dictionary for a mamak menu with at least 4 items and prices
# Then print each item and its price in a formatted way
# TODO: menu = ???


# Exercise 2: Safely access a key that might not exist
student = {"name": "Ahmad", "age": 20, "course": "CS"}
# TODO: Get "email" from student. If it doesn't exist, return "No email provided"
# email = ???
# print(f"Email: {email}")


# Exercise 3: Merge these two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# TODO: merged = ??? (try multiple approaches!)


# Exercise 4: Dictionary comprehension — create a dict where
# keys are numbers 1-5 and values are their squares
# Expected: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# TODO: squares = ???


# Exercise 5: Count the frequency of each word in this sentence
sentence = "nasi lemak is the best and nasi goreng is also the best"
# TODO: Create a dictionary with word counts
# Expected: {"nasi": 2, "lemak": 1, "is": 2, "the": 2, "best": 2, ...}
# Hint: use a loop or collections.Counter


# Exercise 6: Invert this dictionary (swap keys and values)
original = {"Malaysia": "KL", "Singapore": "SG", "Thailand": "BKK"}
# TODO: inverted = ???
# Expected: {"KL": "Malaysia", "SG": "Singapore", "BKK": "Thailand"}


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
check_var("menu", dict, check_fn=lambda v: len(v) >= 4, val_msg="menu dictionary should have at least 4 items!")

# Check Exercise 2
check_var("email", str, check_fn=lambda v: v == "No email provided", val_msg="email should be 'No email provided'!")

# Check Exercise 3
check_var("merged", dict, check_fn=lambda v: v == {"a": 1, "b": 2, "c": 3, "d": 4}, val_msg="merged dictionary values are incorrect!")

# Check Exercise 4
check_var("squares", dict, check_fn=lambda v: v == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, val_msg="squares dict is incorrect!")

# Check Exercise 5
check_var("word_count", dict, check_fn=lambda v: v.get("nasi") == 2 and v.get("best") == 2 and v.get("lemak") == 1, val_msg="word_count values are incorrect!")

# Check Exercise 6
check_var("inverted", dict, check_fn=lambda v: v == {"KL": "Malaysia", "SG": "Singapore", "BKK": "Thailand"}, val_msg="inverted dict is incorrect!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Dictionary master status achieved! 📖")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Review dict methods or lookups! ☕")
print("="*55)
print("🏃 Check: python solutions/06_dictionaries_solutions.py")

