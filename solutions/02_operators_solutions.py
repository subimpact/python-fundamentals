import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  SOLUTIONS 02: Operators ✅
"""
print("Exercise 1:")
print(f"a) 17 // 3 = {17 // 3}")
print(f"b) 17 % 3 = {17 % 3}")
print(f"c) 2 ** 5 = {2 ** 5}")
print(f"d) 10 / 3 = {10 / 3}")
print(f"e) True + True + False = {True + True + False}")

print("\nExercise 2:")
number = 24
is_even_and_big = (number % 2 == 0) and (number > 10)
print(f"{number} is even and > 10: {is_even_and_big}")

print("\nExercise 3:")
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius:.1f}°C")

print("\nExercise 4:")
fruits = ["rambutan", "mangosteen", "durian", "papaya"]
has_durian = "durian" in fruits
print(f"Has durian? {has_durian}")

print("\nExercise 5:")
print(f"a) 2 + 3 * 4 - 1 = {2 + 3 * 4 - 1}")     # 13
print(f"b) (2 + 3) * (4 - 1) = {(2 + 3) * (4 - 1)}")  # 15
print(f"c) 10 > 5 and 3 < 1 = {10 > 5 and 3 < 1}")   # False
print(f"d) not (5 > 3 and 2 > 4) = {not (5 > 3 and 2 > 4)}")  # True

print("\n✅ All exercises solved!")
