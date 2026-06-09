# ═══════════════════════════════════════════════════════
# 1 — LOCAL SCOPE
# Variables defined INSIDE a function
# Only accessible within that function
# ═══════════════════════════════════════════════════════

def greet():
    name = "Joseph"             # local variable — only exists inside greet()
    print(f"Hello, {name}!")

greet()                         # Hello, Joseph!

# print(name)                   # NameError — name only exists inside greet()


# ── Each function has its own local scope ──────────────

def func_one():
    number = 10                 # local to func_one
    print(f"func_one: {number}")

def func_two():
    number = 99                 # local to func_two — completely separate variable
    print(f"func_two: {number}")

func_one()                      # func_one: 10
func_two()                      # func_two: 99


# ═══════════════════════════════════════════════════════
# 2 — GLOBAL SCOPE
# Variables defined OUTSIDE of any function
# Accessible from anywhere in the file
# ═══════════════════════════════════════════════════════

company = "Acme Corp"           # global variable

def print_company():
    print(company)              # can READ a global variable from inside a function

print_company()                 # Acme Corp
print(company)                  # Acme Corp — accessible outside too


# ── Modifying a global variable inside a function ──────
# You must declare it with the 'global' keyword
# otherwise Python creates a new local variable instead

employee_count = 10             # global variable

def add_employee():
    global employee_count       # tells Python to use the global variable
    employee_count += 1         # modifies the global variable

print(employee_count)           # 10
add_employee()
print(employee_count)           # 11  ← global was modified


# ── Without 'global' keyword ───────────────────────────

employee_count = 10

def add_employee_wrong():
    employee_count = 99         # creates a NEW local variable
                                # does NOT modify the global
    print(f"Inside : {employee_count}")

add_employee_wrong()            # Inside : 99
print(f"Outside: {employee_count}")   # Outside: 10 ← global unchanged


# ═══════════════════════════════════════════════════════
# 3 — ENCLOSING SCOPE
# Exists when a function is defined INSIDE another function
# The inner function can access variables from the
# outer function — this is called a 'closure'
# ═══════════════════════════════════════════════════════

def outer_function():
    emp_name = "Joseph"                 # enclosing variable

    def inner_function():
        print(f"Employee: {emp_name}")  # inner can READ enclosing variable

    inner_function()

outer_function()                        # Employee: Joseph


# ── Modifying an enclosing variable ───────────────────
# Use the 'nonlocal' keyword to modify a variable
# from the enclosing scope

def outer_function():
    count = 0                           # enclosing variable

    def inner_function():
        nonlocal count                  # tells Python to use the enclosing variable
        count += 1                      # modifies the enclosing variable
        print(f"Inside inner  : {count}")

    inner_function()
    inner_function()
    print(f"Inside outer  : {count}")   # reflects the changes made in inner

outer_function()

# Inside inner  : 1
# Inside inner  : 2
# Inside outer  : 2


# ── Without 'nonlocal' keyword ─────────────────────────

def outer_function():
    count = 0

    def inner_function():
        count = 99                      # creates a new local variable
                                        # does NOT modify the enclosing count
        print(f"Inside inner  : {count}")

    inner_function()
    print(f"Inside outer  : {count}")   # enclosing count unchanged

outer_function()

# Inside inner  : 99
# Inside outer  : 0                     ← enclosing count unchanged


# ═══════════════════════════════════════════════════════
# 4 — BUILT-IN SCOPE
# Python's built-in functions and keywords
# Always available everywhere without importing
# Examples: print(), input(), len(), type(),
#           int(), str(), float(), bool(), range()
# ═══════════════════════════════════════════════════════

# ── These are all built-in scope — always available ────

numbers = [5, 2, 8, 1, 9, 3]

print(len(numbers))             # 6    — built-in len()
print(type(numbers))            # <class 'list'> — built-in type()
print(min(numbers))             # 1    — built-in min()
print(max(numbers))             # 9    — built-in max()
print(sum(numbers))             # 28   — built-in sum()
print(sorted(numbers))          # [1, 2, 3, 5, 8, 9] — built-in sorted()


# ──  Never name your variables after built-ins ──────
# Doing so overwrites them in your local/global scope

# Wrong — overwrites the built-in len function
len = 10
# print(len([1, 2, 3]))         # TypeError — len is now an integer, not a function

# Fix — use a descriptive name instead
list_length = 10


# ═══════════════════════════════════════════════════════
# PUTTING IT ALL TOGETHER — LEGB IN ACTION
# Python searches scopes in this order:
# Local → Enclosing → Global → Built-in
# ═══════════════════════════════════════════════════════

name = "Global Name"                        # global scope

def outer():
    name = "Enclosing Name"                 # enclosing scope

    def inner():
        name = "Local Name"                 # local scope
        print(f"inner   : {name}")          # Local Name   — found in local first

    def inner_no_local():
        print(f"no local: {name}")          # Enclosing Name — not local, looks up to enclosing

    inner()
    inner_no_local()

def no_enclosing():
    print(f"global  : {name}")              # Global Name  — not local, looks up to global

outer()
no_enclosing()

# inner   : Local Name
# no local: Enclosing Name
# global  : Global Name