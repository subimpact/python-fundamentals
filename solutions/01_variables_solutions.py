import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  SOLUTIONS 01: Variables and Data Types ✅
"""

# Exercise 1
my_name = "Ahmad"
my_age = 25
my_height = 1.75
is_student = True
print(f"Name: {my_name}, Age: {my_age}, Height: {my_height}m, Student: {is_student}")

# Exercise 2
mystery_a = 42
mystery_b = "hello"
mystery_c = 3.14
mystery_d = True
mystery_e = None
print(f"\n{mystery_a} is type: {type(mystery_a).__name__}")
print(f"{mystery_b} is type: {type(mystery_b).__name__}")
print(f"{mystery_c} is type: {type(mystery_c).__name__}")
print(f"{mystery_d} is type: {type(mystery_d).__name__}")
print(f"{mystery_e} is type: {type(mystery_e).__name__}")

# Exercise 3
print(f"\nint('100') = {int('100')}")
print(f"float(25) = {float(25)}")
print(f"int(3.99) = {int(3.99)}  ← Truncates, doesn't round!")
print(f"bool(0) = {bool(0)}  ← Zero is False!")
print(f"bool('') = {bool('')}  ← Empty string is False!")

# Exercise 4
x = "Nasi Lemak"
y = "Roti Canai"
x, y = y, x  # Python's tuple swap — one line!
print(f"\nAfter swap: x = {x}, y = {y}")

# Exercise 5
city, country, population = "Kuala Lumpur", "Malaysia", 32000000
print(f"\n{city}, {country} - Population: {population:,}")

print("\n✅ All exercises solved!")
