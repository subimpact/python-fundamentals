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


print("🏃 Check: python solutions/05_tuples_sets_solutions.py")
