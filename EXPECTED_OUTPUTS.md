# 📋 Expected Outputs Reference

This document lists the expected terminal outputs when running the lesson files. Use this to verify that everything is running correctly on your computer!

---

## Lesson 00: Hello Python!
**Command:** `python lessons/00_hello_python.py`
```text
Hello, World!
Selamat datang ke Python!
42
3.14
True
My name is Python and I am 30 years old
Nasi + Lemak + Ayam
Loading...Done!

--- Python as a Calculator ---
2 + 3 = 5
10 - 4 = 6
5 * 6 = 30
15 / 4 = 3.75
15 // 4 = 3
15 % 4 = 3
2 ** 10 = 1024

✅ Lesson 00 complete! You're on your way, boss! 🎉
```

---

## Lesson 01: Variables & Types
**Command:** `python lessons/01_variables_and_types.py`
```text
=== Variables ===
My name is Ahmad
I am 25 years old
My height is 1.75 meters
Am I a student? True

=== Type Checking ===
Type of name: <class 'str'>
Type of age: <class 'int'>
Type of height: <class 'float'>
Type of is_student: <class 'bool'>

=== Dynamic Typing ===
x is 42 (type: <class 'int'>)
x is now durian (type: <class 'str'>)

=== Type Casting ===
x_str = 10 (type: <class 'str'>)
x_int = 10 (type: <class 'int'>)
y_float = 25.0 (type: <class 'float'>)
z_int = 3 (type: <class 'int'>)

=== Boolean Truthiness ===
bool(1) -> True
bool(0) -> False
bool("hello") -> True
bool("") -> False

✅ Lesson 01 complete! Variables are in the bag! 🎒
```

---

## Lesson 02: Operators
**Command:** `python lessons/02_operators.py`
```text
=== Arithmetic Operators ===
a = 15, b = 4
a + b  = 19
a - b  = 11
a * b  = 60
a / b  = 3.75
a // b = 3
a % b  = 3
a ** b = 50625

=== Comparison Operators ===
a = 15, b = 4
a > b  -> True
a < b  -> False
a == b -> False
a != b -> True
a >= 15 -> True
a <= 10 -> False

=== Logical Operators ===
True and False -> False
True or False  -> True
not True       -> False
(a > 10) and (b < 5) -> True

=== Assignment Operators ===
Initial x = 10
After x += 5: 15
After x *= 2: 30
After x /= 10: 3.0

=== Membership Operators ===
'nasi' in 'nasi lemak'? True
'roti' in 'nasi lemak'? False
'teh' not in 'milo dinosaur'? True

✅ Lesson 02 complete! Operators? Done deal weh! ⚡
```

---

## Lesson 03: Strings
**Command:** `python lessons/03_strings.py`
```text
=== Creating & Concatenating Strings ===
Single quotes: Hello
Double quotes: World
Triple quotes: Multi-line string
Hello World!
Nasi Lemak RM 5.50

=== String Length ===
Length of 'Roti Canai' is 10 characters

=== String Indexing ===
Text: durian
First letter [0]: d
Last letter [-1]: n
Third letter [2]: r

=== String Slicing ===
Text: Kuala Lumpur
First 5 characters [:5]: Kuala
Last 6 characters [-6:]: Lumpur
Slicing [3:8]: la Lu
Reversed: rupmuL alauK

=== String Methods ===
Original:   kuala lumpur
Uppercase:  KUALA LUMPUR
Titlecase:  Kuala Lumpur
Original stays same: kuala lumpur
'  clean me  ' strip() -> 'clean me'
'nasi lemak' replace('nasi', 'roti') -> 'roti lemak'
'teh,tarik,kurang,manis' split(',') -> ['teh', 'tarik', 'kurang', 'manis']
'Ahmad' starts with 'Ah'? True
'Ahmad' ends with 'mad'? True
Is '123' numeric? True
Is 'abc' numeric? False

✅ Lesson 03 complete! Strings are super senang! 🧶
```

---

## Lesson 04: Lists
**Command:** `python lessons/04_lists.py`
```text
=== Creating Lists ===
Mamak order: ['roti canai', 'teh tarik', 'maggi goreng']
Prices: [2.5, 1.8, 7.0]
Mixed list: ['Ahmad', 25, True, 3.14, None]
Empty list: []

=== Accessing Elements ===
List: ['durian', 'rambutan', 'mangosteen', 'jackfruit', 'papaya']
First item (index 0): durian
Last item (index -1): papaya
Third item (index 2): mangosteen

Slice [1:3]: ['rambutan', 'mangosteen']
Slice [:3]:  ['durian', 'rambutan', 'mangosteen']
Slice [2:]:  ['mangosteen', 'jackfruit', 'papaya']
Reversed:    ['papaya', 'jackfruit', 'mangosteen', 'rambutan', 'durian']

=== Modifying Lists ===
Original list: ['RAG', 'is', 'awesome']
After append('!'): ['RAG', 'is', 'awesome', '!']
After remove('awesome'): ['RAG', 'is', '!']
After insert(2, 'very cool'): ['RAG', 'is', 'very cool', '!']
After pop(): ['RAG', 'is', 'very cool'] (popped item: '!')
After pop(0): ['is', 'very cool'] (popped item: 'RAG')
After l1[0] = 'Python': ['Python', 'very cool']
After extend(['is', 'great']): ['Python', 'very cool', 'is', 'great']
After clear(): []

=== Return Values (Common Gotcha!) ===
Return value of .append(): None
But the list IS modified: ['nasi', 'lemak', 'ayam']

=== List Comprehensions ===
Squares (0-9): [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Squares (loop): [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Even squares:   [0, 4, 16, 36, 64]
Even sq (loop): [0, 4, 16, 36, 64]

--- More List Comprehension Examples ---
Uppercase: ['NASI LEMAK', 'ROTI CANAI', 'CHAR KUEY TEOW']
Foods starting with 'r': ['roti canai']
Lengths: [10, 10, 14]

=== Nested Lists ===
Grid: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Row 0: [1, 2, 3]
Element at [1][2]: 6

=== Useful Functions ===
List: [42, 7, 15, 3, 99, 23]
Length:  6
Min:     3
Max:     99
Sum:     189
Sorted:  [3, 7, 15, 23, 42, 99]
Reverse sorted: [99, 42, 23, 15, 7, 3]
After .sort(): [3, 7, 15, 23, 42, 99]
After .reverse(): [99, 42, 23, 15, 7, 3]
Index of 42: 1

['a', 'b', 'a', 'c', 'a', 'b'].count('a') → 3
'a' in ['a', 'b', 'a', 'c', 'a', 'b']? True

=== Copying Lists ===
Original after modifying reference: [1, 2, 3, 999]
Real copy (unaffected): [1, 2, 3]

✅ Lesson 04 complete! Lists? No problem lah! 📋
```

---

*(For lessons 05 through 13, running the files will output the same style of sectioned logs. Make sure you see the green checkmarks at the end of each run!)*
