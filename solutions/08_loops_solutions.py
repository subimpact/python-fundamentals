import sys
# Force UTF-8 encoding for Windows terminal emoji support
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

"""
  SOLUTIONS 08: Loops ✅
"""
print("Exercise 1:")
countdown = []
for i in range(10, 0, -1):
    countdown.append(i)
    print(f"  {i}...")
blast_off = "Blast off! 🚀"
print(f"  {blast_off}")

print("\nExercise 2:")
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"Sum: {total}")

print("\nExercise 3:")
states = ["Penang", "Selangor", "Johor", "Sabah", "Sarawak", "Perak"]
numbered = []
for num, state in enumerate(states, 1):
    numbered.append(f"{num}. {state}")
    print(f"  {num}. {state}")

print("\nExercise 4:")
names = ["Ahmad", "Siti", "Raj", "Mei"]
scores = [85, 92, 78, 95]
report = []
for name, score in zip(names, scores):
    report.append(f"{name} scored {score}")
    print(f"  {name} scored {score}")

print("\nExercise 5:")
numbers = [2, 5, 11, 14, 18, 21, 28, 42, 50]
found = None
for num in numbers:
    if num % 3 == 0 and num % 7 == 0:
        found = num
        print(f"Found: {num}")
        break

print("\nExercise 6:")
print("Odd numbers 1-20:", end=" ")
odd_numbers = []
for i in range(1, 21):
    if i % 2 == 0:
        continue
    odd_numbers.append(i)
    print(i, end=" ")
print()

print("\nExercise 7:")
times_table = []
for i in range(1, 13):
    times_table.append(f"7 x {i:>2} = {7*i:>2}")
    print(f"  7 x {i:>2} = {7*i:>2}")

print("\n✅ All exercises solved!")
