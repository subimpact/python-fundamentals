"""
  SOLUTIONS 03: Strings ✅
"""
print("Exercise 1:")
text = "I love Python programming"
extracted = text[7:13]
print(f"Extracted: {extracted}")

print("\nExercise 2:")
original = "MALAYSIA"
reversed_str = original[::-1]
print(f"Reversed: {reversed_str}")

print("\nExercise 3:")
messy = "   hELLO, wORLD!   "
clean = messy.strip().title()
# or: clean = messy.strip().capitalize() — but title() capitalizes each word
print(f"Clean: '{clean}'")

print("\nExercise 4:")
sentence = "A cat sat on a mat at Alamanda"
count = sentence.lower().count("a")
print(f"Letter 'a' appears {count} times")

print("\nExercise 5:")
csv_data = "Ahmad,25,Penang,Developer"
fields = csv_data.split(",")
labels = ["Name", "Age", "City", "Job"]
for label, value in zip(labels, fields):
    print(f"  {label}: {value}")

print("\nExercise 6:")
steps = ["Wake up", "Mandi", "Breakfast", "Code", "Sleep"]
result = " → ".join(steps)
print(result)

print("\nExercise 7:")
filename = "my_script.py"
if filename.endswith(".py"):
    print(f"'{filename}' is a Python file!")
elif filename.endswith(".txt"):
    print(f"'{filename}' is a text file!")
else:
    print(f"'{filename}' is some other type of file.")

print("\n✅ All exercises solved!")
