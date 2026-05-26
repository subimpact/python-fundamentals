"""
=============================================================
  LESSON 01: Variables and Data Types 📦
  Where we learn how to store stuff — like a Tupperware for data!
=============================================================

In Python, variables are like containers (or Tupperware lah)
where you keep your data. No need to declare the type first —
Python is smart enough to figure it out. Pandai kan?

This lesson covers:
  - Creating variables
  - Data types: int, float, str, bool
  - type() function
  - Type conversion (casting)
  - Naming rules for variables
  - Constants (sort of)
  - Input from user
=============================================================
"""

# ============================================================
# PART 1: Creating Variables
# ============================================================
# In Python, you create a variable just by giving it a name
# and assigning a value with =. That's it. Senang gila!

name = "Ahmad"          # A string (text)
age = 25                # An integer (whole number)
height = 1.75           # A float (decimal number)
is_malaysian = True     # A boolean (True or False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Malaysian:", is_malaysian)

# You can also assign multiple variables in one line
# Like tapau-ing (packing) everything at once
x, y, z = 1, 2, 3
print("\nx =", x, "| y =", y, "| z =", z)

# Or give the same value to multiple variables
a = b = c = 0
print("a =", a, "| b =", b, "| c =", c)


# ============================================================
# PART 2: Data Types — The Four Musketeers
# ============================================================
# Python has several built-in data types. The main ones:

# 1. int — Integer (whole numbers, no decimal)
nasi_lemak_price = 5
print("\n--- Data Types ---")
print("Nasi lemak price:", nasi_lemak_price, "| Type:", type(nasi_lemak_price))

# 2. float — Floating point (numbers with decimals)
teh_tarik_price = 2.50
print("Teh tarik price:", teh_tarik_price, "| Type:", type(teh_tarik_price))

# 3. str — String (text, wrapped in quotes)
favourite_food = "Roti Canai"
print("Favourite food:", favourite_food, "| Type:", type(favourite_food))

# 4. bool — Boolean (True or False only)
is_spicy = True
print("Is spicy:", is_spicy, "| Type:", type(is_spicy))

# Pro tip: use type() to check what type a variable is!
# Very useful when you're debugging and something tak jadi (doesn't work)


# ============================================================
# PART 3: Type Conversion (Casting)
# ============================================================
# Sometimes you need to convert one type to another.
# It's like converting Ringgit to dollars — same value, different form.

print("\n--- Type Conversion ---")

# String to Integer
age_text = "30"
age_number = int(age_text)
print(f"'{age_text}' converted to int: {age_number} (type: {type(age_number).__name__})")

# Integer to Float
whole_number = 10
decimal_number = float(whole_number)
print(f"{whole_number} converted to float: {decimal_number}")

# Float to Integer (WARNING: this TRUNCATES, not rounds!)
pi = 3.99
pi_int = int(pi)
print(f"{pi} converted to int: {pi_int}  ← Alamak, it just chops off the decimal!")

# Anything to String
price = 12.50
price_str = str(price)
print(f"{price} converted to string: '{price_str}' (type: {type(price_str).__name__})")

# Boolean conversions — this one interesting!
print(f"\nint(True) = {int(True)}")    # True = 1
print(f"int(False) = {int(False)}")    # False = 0
print(f"bool(1) = {bool(1)}")         # Any non-zero number = True
print(f"bool(0) = {bool(0)}")         # Zero = False
print(f"bool('hello') = {bool('hello')}")  # Non-empty string = True
print(f"bool('') = {bool('')}")        # Empty string = False


# ============================================================
# PART 4: Variable Naming Rules
# ============================================================
# Python has some rules for naming variables — like how your
# IC number has a specific format, variables also got rules:
#
# ✅ CAN:
#   - Start with a letter or underscore: name, _secret
#   - Contain letters, numbers, underscores: my_var_2
#   - Use any length: short or panjang_gila_babi_punya_variable_name
#
# ❌ CANNOT:
#   - Start with a number: 2fast (WRONG!)
#   - Have spaces: my variable (WRONG! Use my_variable)
#   - Use special characters: my-var, my@var (WRONG!)
#   - Use Python keywords: if, for, while, class, etc. (RESERVED!)

# Naming conventions (not enforced, but everyone follows):
my_variable = "snake_case"       # ✅ Python standard for variables & functions
MY_CONSTANT = "UPPER_SNAKE"     # ✅ For constants (values that shouldn't change)
# MyClass = "PascalCase"        # ✅ For class names (we'll learn this later)

print("\n--- Naming Convention ---")
print(f"Variable style: {my_variable}")
print(f"Constant style: {MY_CONSTANT}")


# ============================================================
# PART 5: None — The "Takde Apa" Type
# ============================================================
# None is Python's way of saying "nothing" or "no value".
# It's not 0, it's not "", it's not False — it's literally nothing.
# Like when someone asks "What's in the fridge?" and the answer is... nothing.

result = None
print("\n--- None Type ---")
print(f"result = {result} | Type: {type(result).__name__}")
print(f"Is result None? {result is None}")


# ============================================================
# PART 6: Getting Input from User
# ============================================================
# The input() function lets you ask the user to type something.
# NOTE: input() ALWAYS returns a string! Even if they type a number.
# So if you want a number, you kena (must) convert it!

# Uncomment the lines below to try it out:
# user_name = input("What's your name? ")
# print(f"Hello, {user_name}! Welcome to Python! 🐍")

# For numbers, convert the input:
# user_age = int(input("How old are you? "))
# print(f"Wah, {user_age} years old already ah! Time flies!")


# ============================================================
# 🎉 NICE ONE!
# ============================================================
# Now you know how to store data in variables,
# what types of data Python supports, and how to convert between them.
# Next up: Lesson 02 — Operators
# We'll learn how to do math and comparisons. Jom!

print("\n✅ Lesson 01 complete! You're getting the hang of it lah! 💪")
