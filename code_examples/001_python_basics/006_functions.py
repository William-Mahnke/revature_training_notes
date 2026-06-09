# ═══════════════════════════════════════════════════════
# 1 — SIMPLE HELLO WORLD FUNCTION
# A basic function with no parameters and no return value
# ═══════════════════════════════════════════════════════

def say_hello():
    print("Hello, World!")

say_hello()                     # Hello, World!


# ═══════════════════════════════════════════════════════
# Functions can 'return' data
# ═══════════════════════════════════════════════════════

# ── Returns a String ───────────────────────────────────
def get_greeting():
    return "Hello, World!"

result = get_greeting()
print(result)                   # Hello, World!
print(type(result))             # <class 'str'>

# ── Returns an Integer ─────────────────────────────────
def get_employee_count():
    return 42

count = get_employee_count()    # you can assign a funtion's return value to a variable
print(count)                    # 42
print(type(count))              # <class 'int'>


# ═══════════════════════════════════════════════════════
# Functions can call other functions
# ═══════════════════════════════════════════════════════

def get_first_name():
    return "Joseph"

def get_last_name():
    return "Smith"

def get_full_name():
    first = get_first_name()        # calls get_first_name()
    last  = get_last_name()         # calls get_last_name()
    return f"{first} {last}"

print(get_full_name())          # Joseph Smith


# ═══════════════════════════════════════════════════════
# 4 — FUNCTION THAT TAKES ARGUMENTS
# Parameters are defined in the function signature
# Arguments are the values passed in when calling it
# ═══════════════════════════════════════════════════════

def greet_employee(name, title):
    print(f"Welcome, {title} {name}!")

greet_employee("Joseph", "Developer")      # Welcome, Developer Joseph!
greet_employee("Alice",  "Manager")        # Welcome, Manager Alice!


# ═══════════════════════════════════════════════════════
# 5 — FUNCTION WITH DEFAULT PARAMETERS
# Default values are used when no argument is passed in
# ═══════════════════════════════════════════════════════

def greet_employee(name, title="Employee"):
    print(f"Welcome, {title} {name}!")

greet_employee("Joseph", "Developer")      # Welcome, Developer Joseph!
greet_employee("Alice")                    # Welcome, Employee Alice! (default used)


# ═══════════════════════════════════════════════════════
# *args collects any number of positional arguments
# into a tuple — useful when you don't know how many
# arguments will be passed in
# ═══════════════════════════════════════════════════════

def list_employees(*args):
    print("Employee List:")
    for name in args:
        print(f" - {name}")

list_employees("Joseph")
# Employee List:
#   - Joseph

list_employees("Joseph", "Alice", "Bob", "Carol")
# Employee List:
#   - Joseph
#   - Alice
#   - Bob
#   - Carol

# You can combine these ideas...
def add_all(*nums):
    print(nums)
    return sum(nums)

print( add_all(1, 2, 3, 4, 5) )

# ═══════════════════════════════════════════════════════
# **kwargs collects any number of keyword arguments
# into a dictionary — useful when you want named
# key/value pairs but don't know how many there will be
# ═══════════════════════════════════════════════════════

def create_employee(**kwargs):
    print("New Employee:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

create_employee(id=100, name="Joseph", title="Developer", department="Engineering")
# New Employee:
#   id         : 100
#   name       : Joseph
#   title      : Developer
#   department : Engineering

create_employee(id=101, name="Alice")
# New Employee:
#   id         : 101
#   name       : Alice