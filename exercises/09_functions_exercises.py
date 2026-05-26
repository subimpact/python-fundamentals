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


print("🏃 Check: python solutions/09_functions_solutions.py")
