# ═══════════════════════════════════════════════════════
# SECTION 1 — ARITHMETIC OPERATORS
# Used to perform mathematical operations
# ═══════════════════════════════════════════════════════

a = 10
b = 3

addition        = a + b     # 13  - adds two values
subtraction     = a - b     # 7   - subtracts right from left
multiplication  = a * b     # 30  - multiplies two values
division        = a / b     # 3.333... - always returns a float
floor_division  = a // b    # 3   - divides and rounds DOWN to nearest whole number
modulus         = a % b     # 1   - returns the remainder of division
exponentiation  = a ** b    # 1000 - raises left to the power of right

print(addition)             # 13
print(subtraction)          # 7
print(multiplication)       # 30
print(division)             # 3.3333333333333335
print(floor_division)       # 3
print(modulus)              # 1
print(exponentiation)       # 1000


# ═══════════════════════════════════════════════════════
# SECTION 2 — ASSIGNMENT OPERATORS
# Used to assign or update variable values
# ═══════════════════════════════════════════════════════

x = 10          # basic assignment

x += 5          # same as x = x + 5       → 15
x -= 3          # same as x = x - 3       → 12
x *= 2          # same as x = x * 2       → 24
x /= 4          # same as x = x / 4       → 6.0
x //= 2         # same as x = x // 2      → 3.0
x %= 2          # same as x = x % 2       → 1.0
x **= 3         # same as x = x ** 3      → 1.0

print(x)        # 1.0


# ═══════════════════════════════════════════════════════
# SECTION 3 — COMPARISON OPERATORS
# Compare two values — always return a Boolean (True/False)
# ═══════════════════════════════════════════════════════

a = 10
b = 3

print(a == b)   # False - equal to
print(a != b)   # True  - not equal to
print(a > b)    # True  - greater than
print(a < b)    # False - less than
print(a >= b)   # True  - greater than or equal to
print(a <= b)   # False - less than or equal to


# ═══════════════════════════════════════════════════════
# SECTION 4 — LOGICAL OPERATORS
# Combine multiple conditions — return a Boolean (True/False)
# ═══════════════════════════════════════════════════════

is_employed = True
has_id = True
is_suspended = False

# AND — both conditions must be True
print(is_employed and has_id)           # True
print(is_employed and is_suspended)     # False

# OR — at least one condition must be True
print(is_employed or is_suspended)      # True
print(is_suspended or False)            # False

# NOT — inverts the Boolean value
print(not is_suspended)                 # True
print(not is_employed)                  # False


# ═══════════════════════════════════════════════════════
# SECTION 5 — MEMBERSHIP + IDENTITY OPERATORS
# ═══════════════════════════════════════════════════════

# ── MEMBERSHIP ──────────────────────────────────────────
# 'in' and 'not in' — check if a value exists in a sequence

employees = ["Joseph", "Revature", "Alice"]
name = "Joseph"

print(name in employees)                # True  - name exists in the list
print("Bob" in employees)               # False - Bob is not in the list
print("Bob" not in employees)           # True  - Bob is not in the list
print("J" in name)                      # True  - 'J' exists in the string "Joseph"

# ── IDENTITY ────────────────────────────────────────────
# 'is' and 'is not' — check if two variables point to the SAME object in memory
# (not just equal in value, but literally the same object)

a = [1, 2, 3]
b = a           # b points to the SAME object as a
c = [1, 2, 3]   # c is a NEW object with the same values

print(a is b)           # True  - same object in memory
print(a is c)           # False - different objects, even though values are equal
print(a == c)           # True  - values are equal, but not the same object
print(a is not c)       # True  - confirms they are different objects

# Common identity check — testing for None
middle_name = None
print(middle_name is None)      # True  - recommended way to check for None
print(middle_name is not None)  # False