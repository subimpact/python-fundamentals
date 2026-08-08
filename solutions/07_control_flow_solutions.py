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
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

for i in range(1, 21):
    print(fizzbuzz(i), end=" ")
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
def login(username, password):
    if username == "admin" and password == "python123":
        return "success"
    elif username == "admin":
        return "wrong password"
    else:
        return "unknown user"

username = "admin"
password = "python123"
print(login(username, password))

print("\n✅ All exercises solved!")
