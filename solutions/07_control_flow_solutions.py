import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  SOLUTIONS 07: Control Flow ✅
"""
print("Exercise 1:")
score = 75
if score >= 80:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 40:
    grade = "C"
elif score >= 20:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} → Grade: {grade}")

print("\nExercise 2: FizzBuzz")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

print("\nExercise 3:")
temperature = 35
drink = "teh tarik" if temperature > 30 else "milo ais"
print(f"At {temperature}°C, I'll have: {drink}")

print("\nExercise 4:")
year = 2024
is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
print(f"{year} is a leap year: {is_leap}")

print("\nExercise 5:")
username = "admin"
password = "python123"
if username == "admin" and password == "python123":
    print("✅ Login successful! Welcome, admin!")
elif username == "admin":
    print("❌ Wrong password!")
else:
    print("❌ Username not found!")

print("\n✅ All exercises solved!")
