"""
  SOLUTIONS 05: Tuples and Sets ✅
"""
print("Exercise 1:")
coordinates = (3.1415, 2.7182, 1.6180)
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

print("\nExercise 2:")
orders = ["teh tarik", "roti canai", "teh tarik", "nasi lemak", "roti canai", "teh tarik"]
unique_orders = set(orders)
print(f"Unique orders: {unique_orders}")
print(f"Count: {len(unique_orders)}")

print("\nExercise 3:")
ali = {"nasi lemak", "teh tarik", "roti canai", "milo"}
abu = {"teh tarik", "maggi goreng", "milo", "bandung"}
both_ordered = ali & abu  # or ali.intersection(abu)
print(f"Both ordered: {both_ordered}")

print("\nExercise 4:")
ali_only = ali - abu  # or ali.difference(abu)
print(f"Ali only: {ali_only}")

print("\nExercise 5:")
a = 100
b = 200
a, b = b, a
print(f"a={a}, b={b}")

print("\n✅ All exercises solved!")
