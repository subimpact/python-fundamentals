"""
=============================================================
  LESSON 12: Error Handling ⚠️
  When things go wrong — handle it gracefully!
=============================================================

Errors happen. Users type letters when you expect numbers.
Files go missing. Internet drops. Dividing by zero.
It's not about avoiding errors — it's about handling them!

Like driving in KL: you know traffic jams WILL happen,
so you plan alternative routes. Same concept!

This lesson covers:
  - Types of errors (syntax vs runtime)
  - try / except
  - Catching specific exceptions
  - else and finally
  - Raising your own exceptions
  - Custom exceptions
  - Common exception types
=============================================================
"""

# ============================================================
# PART 1: Types of Errors
# ============================================================
# Two main types:
# 1. Syntax Errors — code is written wrongly (caught before running)
#    Example: print("hello"  ← missing closing bracket
#
# 2. Exceptions (Runtime Errors) — code is correct but something
#    goes wrong during execution. These we can handle!

print("=== Common Exceptions ===")

# Here are some common ones (DON'T uncomment — they'll crash!):

# ZeroDivisionError
# result = 10 / 0

# TypeError
# result = "hello" + 5

# ValueError
# result = int("abc")

# IndexError
# my_list = [1, 2, 3]
# print(my_list[10])

# KeyError
# my_dict = {"name": "Ahmad"}
# print(my_dict["age"])

# FileNotFoundError
# with open("takde_file.txt") as f: f.read()

# NameError
# print(undefined_variable)

print("(See the comments in the code for examples of each!)")


# ============================================================
# PART 2: try / except — The Safety Net
# ============================================================
# Wrap risky code in 'try', handle the error in 'except'.

print("\n=== try / except ===")

# Without error handling — program CRASHES:
# result = 10 / 0  ← ZeroDivisionError!

# With error handling — program continues:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Cannot divide by zero lah!")

print("Program still running! No crash! 😎")

# Another example
try:
    number = int("hello")
except ValueError:
    print("❌ 'hello' is not a number! Cannot convert!")


# ============================================================
# PART 3: Catching Specific Exceptions
# ============================================================
# Always try to catch SPECIFIC exceptions, not just any error.

print("\n=== Specific Exceptions ===")

def safe_divide(a, b):
    """Divide a by b with error handling."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  ❌ Cannot divide {a} by zero!")
        return None
    except TypeError:
        print(f"  ❌ Invalid types: {type(a).__name__} / {type(b).__name__}")
        return None
    else:
        print(f"  ✅ {a} / {b} = {result}")
        return result

safe_divide(10, 3)
safe_divide(10, 0)
safe_divide(10, "abc")

# Catching multiple exception types in one line
try:
    value = int("not_a_number")
except (ValueError, TypeError) as e:
    print(f"\n  Caught error: {type(e).__name__}: {e}")


# ============================================================
# PART 4: The Full try/except/else/finally
# ============================================================
# try:      code that might fail
# except:   runs if error occurs
# else:     runs if NO error occurred
# finally:  ALWAYS runs (cleanup code)

print("\n=== try / except / else / finally ===")

def read_number_from_string(text):
    """Try to convert text to a number."""
    try:
        number = float(text)
    except ValueError:
        print(f"  ❌ '{text}' is not a valid number!")
    else:
        # Only runs if try succeeded (no exception)
        print(f"  ✅ Successfully converted '{text}' to {number}")
    finally:
        # ALWAYS runs — good for cleanup
        print(f"  📋 Finished processing '{text}'")
    print()

read_number_from_string("3.14")
read_number_from_string("hello")
read_number_from_string("42")


# ============================================================
# PART 5: Catching All Exceptions (Use Carefully!)
# ============================================================
# You CAN catch all exceptions with bare 'except' or 'except Exception',
# but be CAREFUL — it can hide bugs!

print("=== Catching All Exceptions ===")

# Acceptable way — catch Exception (not bare except)
try:
    # Some risky operation
    x = 1 / 0
except Exception as e:
    print(f"  Caught: {type(e).__name__}: {e}")

# DON'T DO THIS (bare except catches EVERYTHING, even Ctrl+C):
# try:
#     something()
# except:  ← BAD! Too broad!
#     pass

# PRO TIP: Catch specific exceptions first, broad ones last:
# try:
#     risky_code()
# except ValueError:
#     handle_value_error()
# except TypeError:
#     handle_type_error()
# except Exception as e:
#     handle_everything_else(e)


# ============================================================
# PART 6: Raising Exceptions
# ============================================================
# You can create your own errors with 'raise'!
# Like a bouncer at a club — "Sorry boss, you cannot enter."

print("\n=== Raising Exceptions ===")

def validate_age(age):
    """Validate that age is reasonable."""
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be a number, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative! Got {age}")
    if age > 150:
        raise ValueError(f"Age {age}? Are you a vampire or what?")
    return True

# Test with valid age
try:
    validate_age(25)
    print("  ✅ Age 25 is valid!")
except (TypeError, ValueError) as e:
    print(f"  ❌ {e}")

# Test with negative age
try:
    validate_age(-5)
except (TypeError, ValueError) as e:
    print(f"  ❌ {e}")

# Test with impossible age
try:
    validate_age(999)
except (TypeError, ValueError) as e:
    print(f"  ❌ {e}")

# Test with wrong type
try:
    validate_age("twenty")
except (TypeError, ValueError) as e:
    print(f"  ❌ {e}")


# ============================================================
# PART 7: Custom Exceptions
# ============================================================
# You can create your own exception classes!
# Just inherit from Exception.

print("\n=== Custom Exceptions ===")

class InsufficientBalanceError(Exception):
    """Raised when account balance is too low."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw RM{amount:.2f}. "
            f"Balance is only RM{balance:.2f}. "
            f"Short by RM{amount - balance:.2f}!"
        )

class InvalidAmountError(Exception):
    """Raised when amount is invalid."""
    pass

def withdraw(balance, amount):
    """Withdraw money with validation."""
    if amount <= 0:
        raise InvalidAmountError("Amount must be positive!")
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

# Test scenarios
account_balance = 100.00

try:
    account_balance = withdraw(account_balance, 30)
    print(f"  ✅ Withdrew RM30. Balance: RM{account_balance:.2f}")

    account_balance = withdraw(account_balance, 50)
    print(f"  ✅ Withdrew RM50. Balance: RM{account_balance:.2f}")

    account_balance = withdraw(account_balance, 100)  # This will fail!
except InsufficientBalanceError as e:
    print(f"  ❌ {e}")
except InvalidAmountError as e:
    print(f"  ❌ {e}")


# ============================================================
# PART 8: Practical Example — Safe User Input
# ============================================================

print("\n=== Practical Example ===")

def get_valid_number(prompt, min_val=None, max_val=None):
    """
    Simulate getting a valid number from user.
    In real code, you'd use input() in a while loop.
    """
    # Simulating some inputs
    test_inputs = ["abc", "-5", "25", "999"]

    for test_input in test_inputs:
        try:
            value = float(test_input)
            if min_val is not None and value < min_val:
                raise ValueError(f"Must be at least {min_val}")
            if max_val is not None and value > max_val:
                raise ValueError(f"Must be at most {max_val}")
            print(f"  ✅ '{test_input}' → Valid: {value}")
        except ValueError as e:
            print(f"  ❌ '{test_input}' → Invalid: {e}")

get_valid_number("Enter age: ", min_val=0, max_val=150)


# ============================================================
# PART 9: Common Exception Types Reference
# ============================================================
# Here's a handy reference of the most common exceptions:
#
# ValueError       — Wrong value (int("abc"))
# TypeError        — Wrong type ("hello" + 5)
# KeyError         — Dict key not found
# IndexError       — List index out of range
# FileNotFoundError — File doesn't exist
# ZeroDivisionError — Dividing by zero
# AttributeError   — Object has no such attribute/method
# ImportError       — Module not found
# NameError        — Variable not defined
# PermissionError  — No permission to access file
# RuntimeError     — General runtime error
# StopIteration    — Iterator exhausted
# OverflowError    — Number too large
# RecursionError   — Too many recursive calls

print("\n(See code comments for the full exception reference table!)")


# ============================================================
# 🎉 ERROR HANDLER PRO!
# ============================================================
# Now your programs can handle errors gracefully!
# No more mysterious crashes — you're in control!
# Next up: Lesson 13 — Modules and Imports!

print("\n✅ Lesson 12 complete! Errors? Bring it on! ⚠️")
