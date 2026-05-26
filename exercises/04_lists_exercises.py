import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 04: Lists
  Run: python exercises/04_lists_exercises.py
"""

# Exercise 1: Create a list of 5 Malaysian foods, then:
# a) Add "cendol" to the end
# b) Insert "laksa" at position 2
# c) Remove the first item
# d) Print the final list and its length

# TODO: foods = [???]


# Exercise 2: List comprehension — create a list of cubes (x³) for 1 to 10
# Expected: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# TODO: cubes = ???


# Exercise 3: Filter — using list comprehension, get only words longer than 4 chars
words = ["nasi", "roti", "maggi", "teh", "milo", "laksa", "satay", "cendol"]
# TODO: long_words = ???
# print(f"Long words: {long_words}")


# Exercise 4: From the list below, create a NEW list with only unique values (no duplicates)
# Hint: You can use set() to help!
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# TODO: unique = ???
# print(f"Unique: {unique}")


# Exercise 5: Sort this list of tuples by the SECOND element (price)
menu = [("nasi lemak", 5.50), ("roti canai", 2.50), ("teh tarik", 1.80), ("laksa", 8.00)]
# TODO: sorted_menu = sorted(menu, key=???)
# for item, price in sorted_menu:
#     print(f"  {item}: RM{price}")


# Exercise 6: Flatten this nested list into a single list
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# TODO: flat = ???  (try using list comprehension!)


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
check_var("foods", list, check_fn=lambda v: len(v) == 6 and "cendol" in v and "laksa" in v, val_msg="foods list should have 6 items, including 'cendol' and 'laksa'!")

# Check Exercise 2
check_var("cubes", list, check_fn=lambda v: v == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000], val_msg="cubes list values are incorrect! Make sure you did x**3 for x from 1 to 10.")

# Check Exercise 3
check_var("long_words", list, check_fn=lambda v: set(v) == {"maggi", "laksa", "satay", "cendol"}, val_msg="long_words should only contain words with > 4 characters!")

# Check Exercise 4
check_var("unique", list, check_fn=lambda v: set(v) == {1, 2, 3, 4, 5, 6, 9}, val_msg="unique list should only contain unique numbers from the original list!")

# Check Exercise 5
check_var("sorted_menu", list, check_fn=lambda v: [x[0] for x in v] == ["teh tarik", "roti canai", "nasi lemak", "laksa"], val_msg="sorted_menu is not sorted correctly by price!")

# Check Exercise 6
check_var("flat", list, check_fn=lambda v: v == [1, 2, 3, 4, 5, 6, 7, 8, 9], val_msg="flat list should contain numbers 1 to 9 in order!")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! You are the list master weh! 📋")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Go double check your index or list methods! ☕")
print("="*55)
print("🏃 Check: python solutions/04_lists_solutions.py")

