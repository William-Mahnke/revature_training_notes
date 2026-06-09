# ─────────────────────────────────────────
# 0. VARIABLES
# Variables are named references to data
# ─────────────────────────────────────────
my_var = "some value"
print("My variable: " + my_var)

# Variables in python are "dynamically typed" - the type can change
my_var = 123
print(f"My variable: {my_var}")

# ─────────────────────────────────────────
# 1. INTEGER (int)
# Whole numbers, positive or negative
# ─────────────────────────────────────────
age = 25
temperature = -10
print(type(age))          # <class 'int'>

# ─────────────────────────────────────────
# 2. FLOAT (float)
# Decimal numbers, positive or negative
# ─────────────────────────────────────────
price = 19.99
gravity = -9.8
print(type(price))        # <class 'float'>

# ─────────────────────────────────────────
# 3. STRING (str)
# Text, wrapped in single or double quotes
# ─────────────────────────────────────────
name = "Joseph"
greeting = 'Hello, World!'
print(type(name))         # <class 'str'>

# ─────────────────────────────────────────
# 4. BOOLEAN (bool)
# True or False only
# ─────────────────────────────────────────
is_active = True
is_deleted = False
print(type(is_active))    # <class 'bool'>

# ─────────────────────────────────────────
# 5. NONE (NoneType)
# Represents the absence of a value
# ─────────────────────────────────────────
middle_name = None
print(type(middle_name))  # <class 'NoneType'>


value = 5
print(type(value))
print(type(str(value)))