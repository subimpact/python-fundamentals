# 🐍 Python Fundamentals

**Learn Python from zero to hero — Malaysian style! 🇲🇾**

A complete, beginner-friendly Python learning guide with hands-on lessons, exercises, and solutions. Written in fun Malaysian English so you won't fall asleep reading code. Confirm shiok one!

---

## 📋 Table of Contents

### Lessons
Each lesson is a standalone `.py` file you can read and run. No Jupyter needed!

| # | Lesson | Topics |
|---|--------|--------|
| 00 | [Hello Python!](lessons/00_hello_python.py) | print(), comments, running Python |
| 01 | [Variables & Types](lessons/01_variables_and_types.py) | int, float, str, bool, type(), casting |
| 02 | [Operators](lessons/02_operators.py) | Arithmetic, comparison, logical, assignment |
| 03 | [Strings](lessons/03_strings.py) | Methods, slicing, concatenation, formatting |
| 04 | [Lists](lessons/04_lists.py) | Creating, modifying, list comprehensions |
| 05 | [Tuples & Sets](lessons/05_tuples_and_sets.py) | Immutability, unpacking, set operations |
| 06 | [Dictionaries](lessons/06_dictionaries.py) | Key-value pairs, .items(), comprehensions |
| 07 | [Control Flow](lessons/07_control_flow.py) | if/elif/else, ternary, truthy/falsy, match |
| 08 | [Loops](lessons/08_loops.py) | for, while, break, continue, enumerate, zip |
| 09 | [Functions](lessons/09_functions.py) | def, return, *args, **kwargs, lambda, scope |
| 10 | [f-strings & Formatting](lessons/10_fstrings_and_formatting.py) | f-strings, .format(), .join(), alignment |
| 11 | [File I/O](lessons/11_file_io.py) | Reading, writing, appending, CSV, JSON |
| 12 | [Error Handling](lessons/12_error_handling.py) | try/except, raising, custom exceptions |
| 13 | [Modules & Imports](lessons/13_modules_and_imports.py) | Standard library, pip, creating modules |

### Exercises & Solutions
Practice what you've learned! Each exercise has `# TODO` markers for you to fill in.

| # | Exercise | Solution |
|---|----------|----------|
| 01 | [Variables](exercises/01_variables_exercises.py) | [Solutions](solutions/01_variables_solutions.py) |
| 02 | [Operators](exercises/02_operators_exercises.py) | [Solutions](solutions/02_operators_solutions.py) |
| 03 | [Strings](exercises/03_strings_exercises.py) | [Solutions](solutions/03_strings_solutions.py) |
| 04 | [Lists](exercises/04_lists_exercises.py) | [Solutions](solutions/04_lists_solutions.py) |
| 05 | [Tuples & Sets](exercises/05_tuples_sets_exercises.py) | [Solutions](solutions/05_tuples_sets_solutions.py) |
| 06 | [Dictionaries](exercises/06_dictionaries_exercises.py) | [Solutions](solutions/06_dictionaries_solutions.py) |
| 07 | [Control Flow](exercises/07_control_flow_exercises.py) | [Solutions](solutions/07_control_flow_solutions.py) |
| 08 | [Loops](exercises/08_loops_exercises.py) | [Solutions](solutions/08_loops_solutions.py) |
| 09 | [Functions](exercises/09_functions_exercises.py) | [Solutions](solutions/09_functions_solutions.py) |
| 10 | [f-strings](exercises/10_fstrings_exercises.py) | [Solutions](solutions/10_fstrings_solutions.py) |

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+** — [Download here](https://www.python.org/downloads/)
  - ⚠️ During installation, make sure to check **"Add Python to PATH"**!

### How to Use

1. **Clone this repo:**
   ```bash
   git clone https://github.com/subimpact/python-fundamentals.git
   cd python-fundamentals
   ```

2. **Set up a Virtual Environment (venv) — *Sangat Recommended!* 🛡️**
   To avoid polluting your global system packages, create and activate a Python virtual environment:
   
   * **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **Windows (Command Prompt):**
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   * **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Read and run lessons in order:**
   ```bash
   python lessons/00_hello_python.py
   python lessons/01_variables_and_types.py
   # ... and so on
   ```
   *(Need to verify if your console output matches what it should? Check [EXPECTED_OUTPUTS.md](EXPECTED_OUTPUTS.md)!)*

5. **Try the exercises:**
   ```bash
   # Open the exercise file, fill in the TODOs
   # Then run it. There are built-in Malaysian checkers to guide you!
   python exercises/01_variables_exercises.py

   # Check the solutions when you're done:
   python solutions/01_variables_solutions.py
   ```

### Recommended Workflow
1. 📖 Read the lesson file (it's heavily commented — just read it like a book!)
2. ▶️ Run the lesson and verify your output matches [EXPECTED_OUTPUTS.md](EXPECTED_OUTPUTS.md)
3. 🧪 Try modifying the code to experiment
4. ✏️ Do the matching exercise and run it to trigger the automated checker
5. ✅ Check the solution
6. ➡️ Move to the next lesson

### ⏱️ Estimated Playthrough Duration
For absolute beginners, here is a realistic guide on how long it takes to finish this course:
* **Per Topic (Lesson + Exercise + Solution)**: **~30 to 45 minutes**
  * *15-20 mins*: Read the lesson file, run it, and experiment.
  * *15-25 mins*: Code the exercise, debug with the checker, and review the solution.
* **Full Repository Playthrough**: **6 to 8 hours** of total hands-on learning.

**📅 Recommended Learning Paths:**
* **The "Teh Tarik" Weekend Sprint ☕**: Dedicate 3-4 hours on Saturday and Sunday. You'll be coding comfortably by Sunday night!
* **The Self-Paced Mamak Plan 🍛**: Do 2 topics a day (approx. 1 hour total). You'll finish everything in exactly one week, confirm steady!

---

## 🎯 Who Is This For?

- **Absolute beginners** who have never coded before
- **Students** starting a CS or data science course
- **Developers** from other languages picking up Python
- **Anyone** who wants a fun, easy-to-follow Python refresher

---

## 📁 Project Structure

```
python-fundamentals/
├── README.md              ← You are here!
├── LICENSE                ← MIT License
├── .gitignore             ← Git ignore rules
├── C1M1_Ungraded_Lab_1.ipynb  ← Original notebook reference
├── lessons/               ← 14 lesson files (read + run these!)
│   ├── 00_hello_python.py
│   ├── 01_variables_and_types.py
│   ├── ...
│   └── 13_modules_and_imports.py
├── exercises/             ← Practice problems (fill in the TODOs!)
│   ├── 01_variables_exercises.py
│   ├── ...
│   └── 10_fstrings_exercises.py
└── solutions/             ← Answers for exercises
    ├── 01_variables_solutions.py
    ├── ...
    └── 10_fstrings_solutions.py
```

---

## 🤝 Contributing

Found a typo? Have a better example? Want to add more exercises?

1. Fork this repo
2. Create a branch: `git checkout -b my-improvement`
3. Make your changes
4. Submit a pull request

All contributions are welcome!

---

## 📜 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- Original content inspired by DeepLearning.AI's Python refresher lab
- Written with love from Malaysia 🇲🇾
- Powered by nasi lemak and teh tarik ☕

---

**Happy coding! Jom belajar Python! 🐍🚀**
