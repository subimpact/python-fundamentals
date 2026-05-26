"""
=============================================================
  LESSON 09: Functions 🏗️
  Build once, use forever — like a good roti canai recipe!
=============================================================

Functions are reusable blocks of code. Instead of writing the
same thing over and over (copy-paste warrior style), you write
it once as a function and call it whenever you need.

Like a roti canai recipe — you learn it once, then you can
make it 100 times without re-inventing the whole thing!

This lesson covers:
  - Defining and calling functions
  - Parameters and arguments
  - Return values
  - Default parameters
  - *args and **kwargs
  - Lambda functions
  - Scope (local vs global)
  - Docstrings
=============================================================
"""

# ============================================================
# PART 1: Defining a Function
# ============================================================
# Use the 'def' keyword, give it a name, add parentheses and a colon.

print("=== Defining Functions ===")

def greet():
    """A simple greeting function."""
    print("Selamat datang! Welcome to Python! 🐍")

# Calling the function — just use its name with ()
greet()
greet()  # Can call as many times as you want!


# ============================================================
# PART 2: Parameters and Arguments
# ============================================================
# Parameters = variables in the function definition
# Arguments = actual values you pass when calling

print("\n=== Parameters & Arguments ===")

def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}! Apa khabar? 😊")

greet_person("Ahmad")
greet_person("Siti")
greet_person("Raj")

# Multiple parameters
def calculate_total(item, price, quantity):
    """Calculate total cost for an item."""
    total = price * quantity
    print(f"{quantity}x {item} = RM{total:.2f}")

calculate_total("Roti Canai", 2.50, 3)
calculate_total("Teh Tarik", 1.80, 5)


# ============================================================
# PART 3: Return Values
# ============================================================
# Use 'return' to send a value back to the caller.
# Without return, the function returns None by default.

print("\n=== Return Values ===")

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(10, 20)
print(f"add(10, 20) = {result}")

# You can return anything — numbers, strings, lists, dicts!
def get_person_info(name, age):
    """Return a dictionary with person info."""
    return {
        "name": name,
        "age": age,
        "status": "adult" if age >= 18 else "minor"
    }

info = get_person_info("Ahmad", 25)
print(f"Person info: {info}")

# Multiple return values (actually returns a tuple!)
def min_max(numbers):
    """Return both min and max of a list."""
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {low}, Max: {high}")

# Early return — exit function based on condition
def check_age(age):
    """Check if old enough to drive."""
    if age < 0:
        return "Invalid age lah! 🤦"
    if age < 17:
        return "Too young to drive. Take the bus!"
    return "Can drive already! 🚗"

print(check_age(15))
print(check_age(21))


# ============================================================
# PART 4: Default Parameters
# ============================================================
# Give parameters a default value — if not provided, use the default.

print("\n=== Default Parameters ===")

def order_drink(drink="teh tarik", size="biasa", sugar_level="normal"):
    """Place a drink order with optional customization."""
    print(f"  Order: {drink} ({size}), sugar: {sugar_level}")

print("Drink orders:")
order_drink()                                    # All defaults
order_drink("milo")                              # Custom drink
order_drink("kopi o", "besar")                   # Custom drink + size
order_drink("teh tarik", sugar_level="kurang")   # Skip middle param!

# IMPORTANT: Default parameters must come AFTER non-default ones!
# def wrong(x=1, y):  ← This will ERROR!
# def correct(y, x=1):  ← This is fine!


# ============================================================
# PART 5: *args — Variable Number of Arguments
# ============================================================
# Sometimes you don't know how many arguments will be passed.
# *args collects extra positional arguments into a TUPLE.

print("\n=== *args ===")

def order_food(*items):
    """Accept any number of food items."""
    print(f"You ordered {len(items)} items:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

order_food("nasi lemak", "teh tarik")
order_food("roti canai", "maggi goreng", "milo", "pisang goreng")

# *args with regular parameters
def calculate_bill(tax_rate, *prices):
    """Calculate total bill with tax."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    print(f"  Subtotal: RM{subtotal:.2f}, Tax: RM{tax:.2f}, Total: RM{total:.2f}")

print("\nBill calculation:")
calculate_bill(0.06, 5.50, 2.50, 7.00)


# ============================================================
# PART 6: **kwargs — Keyword Arguments
# ============================================================
# **kwargs collects extra keyword arguments into a DICTIONARY.
# Like a flexible form that can accept any fields.

print("\n=== **kwargs ===")

def create_profile(**details):
    """Create a profile from any keyword arguments."""
    print("Profile:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile(name="Ahmad", age=25, city="Penang", hobby="coding")
print()
create_profile(name="Siti", occupation="engineer", favourite_food="laksa")

# Combining all three: regular, *args, **kwargs
def super_function(required_arg, *args, **kwargs):
    """A function that accepts everything!"""
    print(f"\n  Required: {required_arg}")
    print(f"  Extra args: {args}")
    print(f"  Keyword args: {kwargs}")

super_function("hello", 1, 2, 3, name="Ahmad", age=25)


# ============================================================
# PART 7: Lambda Functions — One-Line Functions
# ============================================================
# Lambda is a mini function without a name.
# Good for simple operations, especially with sorted(), map(), filter().

print("\n=== Lambda Functions ===")

# Regular function
def square(x):
    return x ** 2

# Same thing as lambda
square_lambda = lambda x: x ** 2

print(f"square(5) = {square(5)}")
print(f"lambda(5) = {square_lambda(5)}")

# Practical use: sorting with custom key
students = [
    {"name": "Ahmad", "cgpa": 3.5},
    {"name": "Siti", "cgpa": 3.8},
    {"name": "Raj", "cgpa": 3.2},
    {"name": "Mei", "cgpa": 3.9},
]

# Sort by CGPA (highest first)
sorted_students = sorted(students, key=lambda s: s["cgpa"], reverse=True)
print("\nStudents by CGPA (highest first):")
for s in sorted_students:
    print(f"  {s['name']}: {s['cgpa']}")

# With map() — apply function to every item
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"\nDoubled: {doubled}")

# With filter() — keep only items that match
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even only: {evens}")


# ============================================================
# PART 8: Scope — Where Variables Live
# ============================================================
# Variables inside a function are LOCAL — they only exist there.
# Variables outside are GLOBAL — accessible everywhere.

print("\n=== Scope ===")

global_var = "I'm global! 🌍"

def scope_demo():
    local_var = "I'm local! 🏠"
    print(f"  Inside function: {global_var}")   # Can see global
    print(f"  Inside function: {local_var}")    # Can see local

scope_demo()
print(f"  Outside function: {global_var}")     # Can see global
# print(local_var)  ← This would ERROR! local_var doesn't exist here!

# Modifying global variable inside a function (use 'global' keyword)
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(f"  Counter after 3 increments: {counter}")

# PRO TIP: Avoid using 'global' if possible.
# It makes code harder to understand. Better to use parameters and return values!


# ============================================================
# PART 9: Docstrings — Document Your Functions!
# ============================================================
# Triple-quoted strings right after def are docstrings.
# They describe what the function does. Good habit!

print("\n=== Docstrings ===")

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: The calculated BMI value.
    """
    return weight_kg / (height_m ** 2)

# Access the docstring with help() or .__doc__
print(f"BMI function docstring:\n{calculate_bmi.__doc__}")

bmi = calculate_bmi(70, 1.75)
print(f"BMI for 70kg, 1.75m: {bmi:.1f}")


# ============================================================
# 🎉 FUNCTION MASTER!
# ============================================================
# You now know how to write clean, reusable code!
# Next up: Lesson 10 — f-strings and String Formatting!
# We'll learn the art of making text look beautiful.

print("\n✅ Lesson 09 complete! Functions — boleh buat already! 🏗️")
