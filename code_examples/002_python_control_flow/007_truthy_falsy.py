# ═══════════════════════════════════════════════════════
# WHAT ARE TRUTHY AND FALSY VALUES?
# In Python, every value has an inherent Boolean value
# You can check it using bool() or just use the value
# directly in an if statement
# ═══════════════════════════════════════════════════════

# ── FALSY VALUES ───────────────────────────────────────
# These are ALL the falsy values in Python

print(bool(0))          # False — zero integer
print(bool(0.0))        # False — zero float
print(bool(""))         # False — empty string
print(bool([]))         # False — empty list
print(bool({}))         # False — empty dictionary
print(bool(()))         # False — empty tuple
print(bool(set()))      # False — empty set
print(bool(None))       # False — None


# ── TRUTHY VALUES ──────────────────────────────────────
# Anything that is NOT falsy is truthy

print(bool(1))          # True  — any non-zero integer
print(bool(-1))         # True  — negative numbers too
print(bool(0.1))        # True  — any non-zero float
print(bool("hello"))    # True  — any non-empty string
print(bool(" "))        # True  — even a space is truthy
print(bool([0]))        # True  — a list with items, even if the item is 0
print(bool({"a": 1}))   # True  — a dictionary with entries
print(bool((1, 2)))     # True  — a tuple with items


# ═══════════════════════════════════════════════════════
# USING TRUTHY / FALSY IN IF STATEMENTS
# You don't need == True or == False — Python evaluates
# the value directly
# ═══════════════════════════════════════════════════════

# ── Checking a string ─────────────────────────────────

def greet(name):
    if name:                            # truthy — name has a value
        print(f"Hello, {name}!")
    else:
        print("No name provided.")

greet("Joseph")
# Hello, Joseph!
greet("")
# No name provided

# ── Checking a list ───────────────────────────────────

def count_employees(emp_list):
    if emp_list:                       # truthy — list has items
        print(f"{len(emp_list)} employees found.")
    else:
        print("No employees found.")

count_employees( ["Joseph", "Alice", "Bob"] )
# 3 employees found.
count_employees( [] )
# No employees found.