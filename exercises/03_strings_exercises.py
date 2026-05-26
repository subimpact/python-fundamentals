import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  EXERCISE 03: Strings
  Run: python exercises/03_strings_exercises.py
"""

# Exercise 1: Extract the word "Python" from this string using slicing
text = "I love Python programming"
# TODO: extracted = text[???]
# print(f"Extracted: {extracted}")


# Exercise 2: Reverse this string
original = "MALAYSIA"
# TODO: reversed_str = ???
# print(f"Reversed: {reversed_str}")


# Exercise 3: Clean up this messy string
messy = "   hELLO, wORLD!   "
# TODO: Make it "Hello, World!" (proper capitalization, no extra spaces)
# clean = ???
# print(f"Clean: '{clean}'")


# Exercise 4: Count how many times "a" appears in the string (case-insensitive)
sentence = "A cat sat on a mat at Alamanda"
# TODO: count = ???
# print(f"Letter 'a' appears {count} times")


# Exercise 5: Split this CSV string and print each item
csv_data = "Ahmad,25,Penang,Developer"
# TODO: Split and print each field on a new line
# Expected:
#   Name: Ahmad
#   Age: 25
#   City: Penang
#   Job: Developer


# Exercise 6: Join these words with " → " between them
steps = ["Wake up", "Mandi", "Breakfast", "Code", "Sleep"]
# TODO: result = ???
# print(result)
# Expected: Wake up → Mandi → Breakfast → Code → Sleep


# Exercise 7: Check if the filename ends with .py or .txt
filename = "my_script.py"
# TODO: Write code to print whether it's a Python file, text file, or other
# Hint: use .endswith()


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
check_var("extracted", str, check_fn=lambda v: v == "Python", val_msg="extracted should be 'Python' weh!")

# Check Exercise 2
check_var("reversed_str", str, check_fn=lambda v: v == "AISYALAM", val_msg="reversed_str should be 'AISYALAM'!")

# Check Exercise 3
check_var("clean", str, check_fn=lambda v: v == "Hello, World!", val_msg="clean should be 'Hello, World!' exactly.")

# Check Exercise 4
check_var("count", int, check_fn=lambda v: v == 8, val_msg="count should be 8! Did you remember to make it case-insensitive?")

# Check Exercise 6
check_var("result", str, check_fn=lambda v: v == "Wake up → Mandi → Breakfast → Code → Sleep", val_msg="result formatting is incorrect! Check the separator.")

print("="*55)
if errors == 0:
    print("🎉 TAHNIAH! All checks passed! You are the string master! 🧵")
else:
    print(f"⚠️ Alamak, got {errors} error(s). Clean your strings and try again! ☕")
print("="*55)
print("🏃 Check: python solutions/03_strings_solutions.py")

