"""
  SOLUTIONS 06: Dictionaries ✅
"""
print("Exercise 1:")
menu = {"nasi lemak": 5.50, "roti canai": 2.50, "teh tarik": 1.80, "maggi goreng": 7.00}
for item, price in menu.items():
    print(f"  {item:<15} RM{price:.2f}")

print("\nExercise 2:")
student = {"name": "Ahmad", "age": 20, "course": "CS"}
email = student.get("email", "No email provided")
print(f"Email: {email}")

print("\nExercise 3:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Method 1: Using |  (Python 3.9+)
merged = dict1 | dict2
print(f"Merged (|): {merged}")
# Method 2: Using ** unpacking
merged2 = {**dict1, **dict2}
print(f"Merged (**): {merged2}")
# Method 3: Using .update()
merged3 = dict1.copy()
merged3.update(dict2)
print(f"Merged (update): {merged3}")

print("\nExercise 4:")
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

print("\nExercise 5:")
sentence = "nasi lemak is the best and nasi goreng is also the best"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word counts: {word_count}")

# Bonus: using Counter
from collections import Counter
print(f"With Counter: {dict(Counter(sentence.split()))}")

print("\nExercise 6:")
original = {"Malaysia": "KL", "Singapore": "SG", "Thailand": "BKK"}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

print("\n✅ All exercises solved!")
