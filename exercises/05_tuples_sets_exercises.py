import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 05: Tuples and Sets
  Run: python exercises/05_tuples_sets_exercises.py
"""

# Exercise 1: Unpack this tuple into variables
coordinates = (3.1415, 2.7182, 1.6180)
# TODO: Unpack into x, y, z
# print(f"x={x}, y={y}, z={z}")


# Exercise 2: From this list, get only UNIQUE items using a set
orders = ["teh tarik", "roti canai", "teh tarik", "nasi lemak", "roti canai", "teh tarik"]
# TODO: unique_orders = ???
# print(f"Unique orders: {unique_orders}")
# Also: how many unique items? print(f"Count: {???}")


# Exercise 3: Find items that BOTH Ali and Abu ordered (intersection)
ali = {"nasi lemak", "teh tarik", "roti canai", "milo"}
abu = {"teh tarik", "maggi goreng", "milo", "bandung"}
# TODO: both_ordered = ???
# print(f"Both ordered: {both_ordered}")


# Exercise 4: Find items that ONLY Ali ordered (difference)
# TODO: ali_only = ???
# print(f"Ali only: {ali_only}")


# Exercise 5: Using tuple unpacking, swap a and b in one line
a = 100
b = 200
# TODO: Swap them
# print(f"a={a}, b={b}")  # Expected: a=200, b=100


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
check_var("x", float, check_fn=lambda v: v == 3.1415, val_msg="x value is incorrect!")
check_var("y", float, check_fn=lambda v: v == 2.7182, val_msg="y value is incorrect!")
check_var("z", float, check_fn=lambda v: v == 1.6180, val_msg="z value is incorrect!")

# Check Exercise 2
check_var("unique_orders", set, check_fn=lambda v: v == {"teh tarik", "roti canai", "nasi lemak"}, val_msg="unique_orders should be a set containing 'teh tarik', 'roti canai', 'nasi lemak'!")

# Check Exercise 3
check_var("both_ordered", set, check_fn=lambda v: v == {"teh tarik", "milo"}, val_msg="both_ordered is incorrect intersection!")

# Check Exercise 4
check_var("ali_only", set, check_fn=lambda v: v == {"nasi lemak", "roti canai"}, val_msg="ali_only is incorrect difference!")

# Check Exercise 5
check_var("a", int, check_fn=lambda v: v == 200, val_msg="a should be 200 after swap!")
check_var("b", int, check_fn=lambda v: v == 100, val_msg="b should be 100 after swap!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! Tuples & Sets are in your DNA now weh! 🧬")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Review sets and tuples behavior! ☕")
print("="*55)
print("🏃 Check: python solutions/05_tuples_sets_solutions.py")

