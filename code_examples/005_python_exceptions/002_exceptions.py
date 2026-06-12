# ═══════════════════════════════════════════════════════
# WHAT ARE EXCEPTIONS?
# An exception is a problem that occurs during the
# execution of a program. When Python encounters an
# error it raises an exception which, if unhandled,
# will crash the program and print a traceback.
#
# Although Python uses 'Error' and Exception 
# interchangeably, keep in mind the term 'Errors' 
# typically refer to issues which are 'unrecoverable' 
# whereas 'Exception' typically refers to 'recoverable'
# issues in your code. You are expected to handle
# exceptions, but not necessarily handle errors
#
# In Python Exceptions are typically named ending
# with 'Error' by convention
#
# Common built-in exceptions:
# ZeroDivisionError — dividing by zero
# ValueError        — wrong value type passed to a function
# TypeError         — wrong data type used in an operation
# IndexError        — accessing an index that doesn't exist
# KeyError          — accessing a dict key that doesn't exist
# FileNotFoundError — trying to open a file that doesn't exist
# ═══════════════════════════════════════════════════════
# 1 — WHAT HAPPENS WITHOUT EXCEPTION HANDLING?
# Python raises an exception and the program crashes
# ═══════════════════════════════════════════════════════

# ── ZeroDivisionError ──────────────────────────────────
# print(10 / 0) # un-comment this line + run to see this exception
# ZeroDivisionError: division by zero

# ── ValueError ─────────────────────────────────────────
# int("hello") # un-comment this line + run to see this exception
# ValueError: invalid literal for int() with base 10: 'hello'

# ── IndexError ─────────────────────────────────────────
names = ["Joseph", "Alice"]
# print(names[10]) # un-comment this line + run to see this exception
# IndexError: list index out of range

# ── KeyError ───────────────────────────────────────────
employee = {"name": "Joseph"}
# print(employee["salary"]) # un-comment this line + run to see this exception
# KeyError: 'salary'

# ── TypeError ──────────────────────────────────────────
# print("Age: " + 25) # un-comment this line + run to see this exception
# TypeError: can only concatenate str (not "int") to str


# ═══════════════════════════════════════════════════════
# 2 — BASIC TRY / EXCEPT BLOCK
# try    — the block of code to attempt
# except — runs if an exception is raised in the try block
# The program does NOT crash — the exception is handled
# ═══════════════════════════════════════════════════════

# ── Handling a single exception ────────────────────────
try:
    result = 10 / 0                 # raises ZeroDivisionError
    print(result)                   # never reached
except ZeroDivisionError:
    print("Cannot divide by zero.") # handled gracefully

print("Program continues.")         # program does not crash


# ── Catching the exception object ─────────────────────
# Use 'as e' to access the exception message

try:
    number = int("hello")           # raises ValueError
except ValueError as e:
    print(f"ValueError caught: {e}")
    # ValueError caught: invalid literal for int() with base 10: 'hello'


# ── Handling multiple specific exceptions ─────────────
# List each exception type you want to handle separately

def divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print("Both values must be numbers.")

divide(10, 2)           # 10 / 2 = 5.0
divide(10, 0)           # Cannot divide by zero.
divide(10, "two")       # Both values must be numbers.


# ── Handling multiple exceptions in one except ─────────
# Use a tuple to catch several exceptions the same way

try:
    names = ["Joseph", "Alice"]
    print(names[10])                # raises IndexError
except (IndexError, KeyError) as e:
    print(f"Access error: {e}")
    # Access error: list index out of range


# ── Catching all exceptions with Exception ─────────────
# Exception is the base class for most built-in exceptions
# Use sparingly — catching everything can hide real bugs

try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred | Class of Error: {type(e)}")
    # <class 'ZeroDivisionError'>

    # A typical error message looks like this:
    print(f"An error occurred: {type(e).__name__} : {e}")
    # An error occurred: ZeroDivisionError — division by zero


# ── try / except / else ────────────────────────────────
# else runs only if NO exception was raised in the try block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Success — result is {result}")  # ✅ runs — no exception was raised

# Success — result is 5.0


# ═══════════════════════════════════════════════════════
# 3 — FINALLY
# The finally block ALWAYS runs — whether an exception
# was raised or not. It is used for cleanup tasks such
# as closing files, releasing resources, or printing
# a final status message
# ═══════════════════════════════════════════════════════

# ── finally always runs ────────────────────────────────
def process_score(score):
    print(f"\nProcessing score: {score}")
    try:
        result = 100 / score
        print(f"Result: {result:.2f}")
    except ZeroDivisionError:
        print("Score cannot be zero.")
    except TypeError:
        print("Score must be a number.")
    finally:
        print("── Processing complete ──")   # always runs

process_score(25)           # runs normally
# Processing score: 25
# Result: 4.00
# ── Processing complete ──

process_score(0)            # raises ZeroDivisionError
# Processing score: 0
# Score cannot be zero.
# ── Processing complete ──

process_score("ten")        # raises TypeError
# Processing score: ten
# Score must be a number.
# ── Processing complete ──


# ── try / except / else / finally together ────────────
def get_employee(employees, index):
    print(f"\nFetching index {index}...")
    try:
        employee = employees[index]
    except IndexError:
        print(f"Index {index} out of bounds of collection.")
    else:
        print(f"Found: {employee}")
    finally:
        print("── Fetch attempt complete ──")   # always runs

staff = ["Joseph", "Alice", "Bob"]

get_employee(staff, 1)      # valid index
get_employee(staff, 10)     # invalid index

# Fetching index 1...
# ✔ Found: Alice
# ── Fetch attempt complete ──

# Fetching index 10...
# out of bounds of collection.
# ── Fetch attempt complete ──

