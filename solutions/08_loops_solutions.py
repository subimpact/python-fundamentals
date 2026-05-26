"""
  SOLUTIONS 08: Loops ✅
"""
print("Exercise 1:")
for i in range(10, 0, -1):
    print(f"  {i}...")
print("  Blast off! 🚀")

print("\nExercise 2:")
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"Sum: {total}")

print("\nExercise 3:")
states = ["Penang", "Selangor", "Johor", "Sabah", "Sarawak", "Perak"]
for num, state in enumerate(states, 1):
    print(f"  {num}. {state}")

print("\nExercise 4:")
names = ["Ahmad", "Siti", "Raj", "Mei"]
scores = [85, 92, 78, 95]
for name, score in zip(names, scores):
    print(f"  {name} scored {score}")

print("\nExercise 5:")
numbers = [2, 5, 11, 14, 18, 21, 28, 42, 50]
for num in numbers:
    if num % 3 == 0 and num % 7 == 0:
        print(f"Found: {num}")
        break

print("\nExercise 6:")
print("Odd numbers 1-20:", end=" ")
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

print("\nExercise 7:")
for i in range(1, 13):
    print(f"  7 x {i:>2} = {7*i:>3}")

print("\n✅ All exercises solved!")
