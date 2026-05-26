"""
=============================================================
  LESSON 11: File I/O 📁
  Reading and writing files — like a digital filing cabinet!
=============================================================

Your programs so far only work with data in memory — once the
program ends, everything disappears! Like writing on a whiteboard
and someone erases it. Sedih (sad)!

File I/O lets you SAVE data to files and READ data back.
Now your work can persist! Macam simpan (save) in Tupperware!

This lesson covers:
  - Opening and closing files
  - The 'with' statement (best practice!)
  - Reading files (read, readline, readlines)
  - Writing files (write, writelines)
  - Appending to files
  - Working with file paths
  - Reading/writing CSV-like data

NOTE: This lesson creates temporary files in a 'temp_files' folder.
      They'll be created automatically when you run this lesson.
=============================================================
"""

import os

# Create a temp directory for our file examples
TEMP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "temp_files")
os.makedirs(TEMP_DIR, exist_ok=True)

# ============================================================
# PART 1: Writing to a File
# ============================================================
# Use open() with mode 'w' to write.
# IMPORTANT: 'w' mode OVERWRITES the file! Everything gone!

print("=== Writing Files ===")

# The old way (don't do this):
# file = open("myfile.txt", "w")
# file.write("hello")
# file.close()  ← Must remember to close! If error happens before this, file stays open!

# The CORRECT way: use 'with' statement!
# It automatically closes the file, even if an error occurs.
# Like having a safety net — confirm selamat (safe)!

filepath = os.path.join(TEMP_DIR, "my_first_file.txt")
with open(filepath, "w", encoding="utf-8") as file:
    file.write("Hello from Python!\n")
    file.write("This is my first file.\n")
    file.write("Selamat datang!\n")

print(f"✅ File written to: {filepath}")


# ============================================================
# PART 2: Reading a File
# ============================================================

print("\n=== Reading Files ===")

# Method 1: .read() — read ENTIRE file as one string
with open(filepath, "r", encoding="utf-8") as file:
    content = file.read()
print("--- .read() (entire file) ---")
print(content)

# Method 2: .readline() — read ONE line at a time
with open(filepath, "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
print("--- .readline() ---")
print(f"Line 1: {line1.strip()}")  # .strip() removes the \n
print(f"Line 2: {line2.strip()}")

# Method 3: .readlines() — read ALL lines into a list
with open(filepath, "r", encoding="utf-8") as file:
    lines = file.readlines()
print(f"--- .readlines() → list ---")
print(f"Lines: {lines}")

# Method 4 (BEST): Loop through the file directly
print("--- Looping through file ---")
with open(filepath, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"  Line {line_number}: {line.strip()}")


# ============================================================
# PART 3: File Modes
# ============================================================
# 'r'  — Read (default). File must exist!
# 'w'  — Write. Creates new or OVERWRITES existing!
# 'a'  — Append. Adds to end of file.
# 'x'  — Create. Error if file already exists.
# 'r+' — Read and Write.
# 'b'  — Binary mode (add to above: 'rb', 'wb').

print("\n=== File Modes ===")

# Append mode — adds to end without erasing
append_file = os.path.join(TEMP_DIR, "log.txt")

# First write
with open(append_file, "w", encoding="utf-8") as file:
    file.write("[2024-01-01] Server started\n")

# Append more
with open(append_file, "a", encoding="utf-8") as file:
    file.write("[2024-01-01] User logged in\n")
    file.write("[2024-01-01] User ordered nasi lemak\n")

# Read it back
with open(append_file, "r", encoding="utf-8") as file:
    print(file.read())


# ============================================================
# PART 4: Writing Multiple Lines
# ============================================================

print("=== Writing Multiple Lines ===")

# Using .writelines() — writes a list of strings
# NOTE: .writelines() does NOT add \n automatically!
mamak_menu = [
    "Nasi Lemak - RM5.50\n",
    "Roti Canai - RM2.50\n",
    "Teh Tarik  - RM1.80\n",
    "Maggi Goreng - RM7.00\n",
]

menu_file = os.path.join(TEMP_DIR, "menu.txt")
with open(menu_file, "w", encoding="utf-8") as file:
    file.write("=== MAMAK MENU ===\n")
    file.writelines(mamak_menu)
    file.write("==================\n")

with open(menu_file, "r", encoding="utf-8") as file:
    print(file.read())


# ============================================================
# PART 5: Working with CSV-like Data
# ============================================================
# CSV = Comma Separated Values. Super common file format!

print("=== CSV-like Data ===")

# Writing CSV data
csv_file = os.path.join(TEMP_DIR, "students.csv")
students = [
    ["Name", "Age", "Course", "CGPA"],
    ["Ahmad", "20", "Computer Science", "3.5"],
    ["Siti", "21", "Engineering", "3.8"],
    ["Raj", "19", "Business", "3.2"],
    ["Mei Ling", "22", "Medicine", "3.9"],
]

with open(csv_file, "w", encoding="utf-8") as file:
    for row in students:
        file.write(",".join(row) + "\n")
print(f"✅ CSV written to: {csv_file}")

# Reading CSV data back
print("\nReading CSV:")
with open(csv_file, "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(",")
        print(f"  {parts}")

# For real CSV work, use the csv module:
# import csv
# with open('file.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# ============================================================
# PART 6: Checking if File Exists
# ============================================================
# Before reading a file, you might want to check if it exists!

print("\n=== Checking Files ===")

print(f"menu.txt exists? {os.path.exists(menu_file)}")
print(f"ghost.txt exists? {os.path.exists('ghost.txt')}")
print(f"Is file? {os.path.isfile(menu_file)}")
print(f"Is directory? {os.path.isdir(TEMP_DIR)}")
print(f"File size: {os.path.getsize(menu_file)} bytes")


# ============================================================
# PART 7: Error Handling with Files
# ============================================================
# Always handle the case where the file might not exist!

print("\n=== Error Handling ===")

try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ File not found! (Don't worry, this was expected)")
except PermissionError:
    print("❌ No permission to read this file!")


# ============================================================
# PART 8: Practical Example — Simple Data Logger
# ============================================================

print("\n=== Practical Example: Data Logger ===")

log_file = os.path.join(TEMP_DIR, "order_log.txt")

def log_order(customer, items):
    """Log an order to file."""
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"Customer: {customer}\n")
        for item in items:
            file.write(f"  - {item}\n")
        file.write("---\n")

# Clear previous log
with open(log_file, "w", encoding="utf-8") as file:
    file.write("=== ORDER LOG ===\n\n")

# Log some orders
log_order("Ahmad", ["Nasi Lemak", "Teh Tarik"])
log_order("Siti", ["Roti Canai", "Milo Dinosaur"])
log_order("Raj", ["Thosai", "Coffee"])

# Read the log
with open(log_file, "r", encoding="utf-8") as file:
    print(file.read())

print(f"📂 All temp files are in: {TEMP_DIR}")
print("   Feel free to check them out!")


# ============================================================
# 🎉 FILE I/O — DONE!
# ============================================================
# Now your programs can save and load data!
# Next up: Lesson 12 — Error Handling!
# We'll learn how to handle mistakes gracefully.

print("\n✅ Lesson 11 complete! File I/O — boleh save data! 📁")
