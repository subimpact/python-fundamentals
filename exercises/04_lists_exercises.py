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


print("🏃 Check: python solutions/04_lists_solutions.py")
