"""
  SOLUTIONS 04: Lists ✅
"""
print("Exercise 1:")
foods = ["nasi lemak", "roti canai", "satay", "rendang", "char kuey teow"]
foods.append("cendol")
foods.insert(2, "laksa")
foods.pop(0)
print(f"Final list: {foods}")
print(f"Length: {len(foods)}")

print("\nExercise 2:")
cubes = [x**3 for x in range(1, 11)]
print(f"Cubes: {cubes}")

print("\nExercise 3:")
words = ["nasi", "roti", "maggi", "teh", "milo", "laksa", "satay", "cendol"]
long_words = [w for w in words if len(w) > 4]
print(f"Long words: {long_words}")

print("\nExercise 4:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = sorted(list(set(numbers)))
print(f"Unique: {unique}")

print("\nExercise 5:")
menu = [("nasi lemak", 5.50), ("roti canai", 2.50), ("teh tarik", 1.80), ("laksa", 8.00)]
sorted_menu = sorted(menu, key=lambda x: x[1])
for item, price in sorted_menu:
    print(f"  {item}: RM{price}")

print("\nExercise 6:")
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [item for sublist in nested for item in sublist]
print(f"Flat: {flat}")

print("\n✅ All exercises solved!")
