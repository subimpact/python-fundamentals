"""
  SOLUTIONS 09: Functions ✅
"""
print("Exercise 1:")
def greet(name):
    return f"Hello, {name}! Apa khabar?"
print(greet("Ahmad"))
print(greet("Siti"))

print("\nExercise 2:")
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

bmi, cat = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.1f} ({cat})")

print("\nExercise 3:")
def make_drink(drink="teh tarik", ice=True):
    ice_text = "with ice" if ice else "no ice"
    return f"One {drink}, {ice_text}!"
print(make_drink())
print(make_drink("kopi", False))
print(make_drink("milo"))

print("\nExercise 4:")
def order_food(*items):
    print(f"  Total items: {len(items)}")
    for i, item in enumerate(items, 1):
        print(f"    {i}. {item}")
order_food("nasi lemak", "roti canai", "teh tarik")

print("\nExercise 5:")
def list_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers), sum(numbers)

minimum, maximum, average, total = list_stats([10, 20, 30, 40, 50])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}, Sum: {total}")

print("\nExercise 6:")
people = [
    {"name": "Siti", "age": 28},
    {"name": "Ahmad", "age": 25},
    {"name": "Raj", "age": 30},
    {"name": "Mei", "age": 22},
]
sorted_people = sorted(people, key=lambda p: p["name"])
for p in sorted_people:
    print(f"  {p['name']} (age {p['age']})")

print("\n✅ All exercises solved!")
