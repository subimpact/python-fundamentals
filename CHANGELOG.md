# 📜 Changelog

All notable changes to this project will be documented in this file.

---

## [1.2.0] - 2026-08-08
### Added
- **Deeper automated checkers** for Exercises 07, 08, and 10:
  - Exercise 07 now tests `fizzbuzz()` and `login()` functions against multiple cases (not just one variable)
  - Exercise 08 went from 2 checks to 8 checks — every loop exercise is now verifiable
  - Exercise 10 now checks formatted price, population, percent, and table output
- **CONTRIBUTING.md**: guidelines for beginner-friendly contributions
- **README badges** (Python version, license, lesson/exercise counts)
- **README section** on optional PEP-8 checking with `black` and `flake8`
- **Commented `requests` demo** in Lesson 13 (the dependency was already in `requirements.txt`)

### Fixed
- **EXPECTED_OUTPUTS.md completely regenerated** from actual lesson runs. The old file had drifted — Lessons 01-03 showed outputs the files no longer produce (e.g. Lesson 01 claimed `x_str = 10` when the file actually prints `'30' converted to int: 30`). This was the #1 source of beginner confusion.
- **README project structure** no longer references the removed `C1M1_Ungraded_Lab_1.ipynb` notebook
- **README lesson table** — Lesson 11 correctly lists CSV (not JSON); JSON lives in Lesson 13
- **Exercise 10 hint** said `87.3%` but `0.8725` formats to `87.2%` — corrected
- **Lesson 08 solution** times-table alignment now matches the exercise's expected format

### Changed
- Solutions 07/08/10 now define the same variables the checkers verify (so running a solution file always passes)

---

## [1.1.0] - 2026-05-26
### Added
- **Automated Verification Checkers**: Added local assertion-based validation blocks to the bottom of all 10 exercise files. When run, these scripts provide instant, humorous Malaysian English feedback to help students correct errors instead of showing scary raw tracebacks.
- **Virtual Environment Support**: Created `requirements.txt` listing dependency requirements and added step-by-step instructions in the `README.md` on how to create, activate, and use a Python `venv` on Windows, macOS, and Linux.
- **Expected Outputs Documentation**: Created `EXPECTED_OUTPUTS.md` with snippets of the exact terminal logs for the lessons so students can verify their local script runs.
- **Changelog tracking**: Added this file (`CHANGELOG.md`) to follow repository best practices.

### Changed
- **README.md Upgrades**: Added virtual environment configuration guides, updated recommended workflows, and referenced the new outputs documentation.

---

## [1.0.0] - 2026-05-26
### Added
- **Initial Release**: Complete Malaysian English style Python learning fundamentals repository.
- **Lessons**: 14 standalone, heavily commented lessons from Hello World to Modules & Imports.
- **Exercises**: 10 practice problems with `# TODO` tags.
- **Solutions**: 10 matching answer keys.
- **Reference material**: Preserved original DeepLearning.AI Jupyter notebook `C1M1_Ungraded_Lab_1.ipynb`.
