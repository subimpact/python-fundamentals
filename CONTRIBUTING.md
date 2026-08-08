# 🤝 Contributing to Python Fundamentals

First of all — terima kasih (thank you) for wanting to help! This repo is built for absolute beginners, so every contribution should make learning *easier*, not more impressive.

## What we're looking for

- **Typo fixes** — in code comments, README, or lesson docs
- **Better examples** — a clearer analogy, a funnier Malaysian reference
- **New exercises** — especially ones that test a common beginner trap
- **Checker improvements** — catch more mistakes with friendlier messages
- **Bug reports** — if a lesson crashes on your machine, that's a bug

## Guidelines (keep it beginner-friendly!)

- **No clever one-liners.** If a simple `for` loop is clearer, use the loop.
- **Explain the *why*** in comments, not just the *what*.
- **Don't introduce concepts before their lesson.** Lesson 03 shouldn't use list comprehensions — those come in Lesson 04.
- **Malaysian English is welcome** in comments and messages (it's the repo's soul!), but keep code identifiers in plain English.
- **Solutions must pass the exercise checker.** Run the exercise file after editing its solution to confirm zero ❌.
- **Update EXPECTED_OUTPUTS.md** if you change what a lesson prints.

## How to contribute

1. **Fork** this repo
2. **Create a branch:** `git checkout -b my-improvement`
3. **Make your changes**
4. **Test your changes:**
   ```bash
   # Lessons must all run clean:
   for f in lessons/*.py; do python3 "$f" || echo "FAIL: $f"; done
   # Solutions must pass their checkers:
   for f in solutions/*.py; do python3 "$f" || echo "FAIL: $f"; done
   ```
5. **Commit** with a clear message: `fix: clarify slicing explanation in lesson 03`
6. **Push and open a pull request**

## Code style

- Follow [PEP-8](https://peps.python.org/pep-0008/) (the repo includes `black` and `flake8` for checking)
- Use snake_case for variables and functions
- Match the existing comment style (`# ===== SECTION =====` headers)

## Questions?

Open an [issue](https://github.com/subimpact/python-fundamentals/issues) — we're friendly, we promise. No question is too basic!

**Jom contribute! 🇲🇾🐍**
