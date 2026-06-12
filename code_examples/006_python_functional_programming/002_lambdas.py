# ═══════════════════════════════════════════════════════
# WHAT ARE LAMBDA FUNCTIONS?
# A lambda is a small, anonymous (unnamed) function
# defined in a single line using the 'lambda' keyword
#
# Syntax:
# lambda arguments : expression
#
# Key characteristics:
# - Can take any number of arguments
# - Can only contain a SINGLE expression
# - Always returns the result of that expression
# - Cannot contain statements, loops, or multiple lines
#
# Regular function:          Lambda equivalent:
# def add(a, b):             lambda a, b: a + b
#     return a + b
# ═══════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════
# 1 — BASIC LAMBDA SYNTAX
# ═══════════════════════════════════════════════════════
# ── No arguments ───────────────────────────────────────
greet = lambda: "Hello, World!"
print(greet())                  # Hello, World!

# Equivalent Function:
# def greet():
#     return "Hello, World!"

# ── One argument ───────────────────────────────────────
square = lambda x: x ** 2

# Equivalent Function:
# def square(x):
#     return x ** 2

print(square(5))                # 25
print(square(9))                # 81

# ── Two arguments ──────────────────────────────────────
add = lambda a, b: a + b

# Equivalent Function:
# def add(a, b):
#     return a + b

print(add(3, 7))                # 10

multiply = lambda a, b: a * b
print(multiply(4, 6))           # 24

# ── Three arguments ────────────────────────────────────
full_name = lambda first, last, title: f"{title} {first} {last}"
print(full_name("John", "Smith", "Mr"))   # Mr John Smith

# ── With a condition (ternary expression) ──────────────
# Lambdas support inline if-else (ternary) expressions
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))               # Even
print(is_even(7))               # Odd

is_passing = lambda score: "Pass" if score >= 70 else "Fail"
print(is_passing(85))           # Pass
print(is_passing(55))           # Fail


# ═══════════════════════════════════════════════════════
# 2 — REGULAR FUNCTION vs LAMBDA
# ═══════════════════════════════════════════════════════

# ── Regular function ───────────────────────────────────
def get_discount_regular(price, rate):
    return price - (price * rate)

# ── Lambda equivalent ──────────────────────────────────
get_discount_lambda = lambda price, rate: price - (price * rate)

# ── Both produce identical results ────────────────────
print(get_discount_regular(100, 0.2))   # 80.0
print(get_discount_lambda(100, 0.2))    # 80.0

# ── When to use each ───────────────────────────────────
# Regular function → reusable, complex, multi-line logic
# Lambda           → short, throwaway, single expression


# ═══════════════════════════════════════════════════════
# 3 — LAMBDAS WITH sorted()
# The 'key' parameter of sorted() accepts a function
# that tells Python WHAT to sort by
# Lambdas are the most common way to supply this
# ═══════════════════════════════════════════════════════

employees = [
    {"name": "Carol",  "salary": 102000, "age": 34},
    {"name": "Joseph", "salary": 95000,  "age": 28},
    {"name": "Alice",  "salary": 88000,  "age": 41},
    {"name": "Dave",   "salary": 115000, "age": 36},
    {"name": "Bob",    "salary": 62000,  "age": 25},
]

# ── Sort by salary (ascending) ────────────────────────
by_salary = sorted(employees, key=lambda emp: emp["salary"])
for emp in by_salary:
    print(f"  {emp['name']:<10} ${emp['salary']:,}")

# Bob        $62,000
# Alice      $88,000
# Joseph     $95,000
# Carol      $102,000
# Dave       $115,000

# ── Sort by salary (descending) ────────────────────────
by_salary_desc = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
for emp in by_salary_desc:
    print(f"  {emp['name']:<10} ${emp['salary']:,}")

# Dave       $115,000
# Carol      $102,000
# Joseph     $95,000
# Alice      $88,000
# Bob        $62,000

# ── Sort by name alphabetically ────────────────────────
by_name = sorted(employees, key=lambda emp: emp["name"])
for emp in by_name:
    print(f"  {emp['name']}")

# Alice
# Bob
# Carol
# Dave
# Joseph

# ── Sort by age ────────────────────────────────────────
by_age = sorted(employees, key=lambda emp: emp["age"])
for emp in by_age:
    print(f"  {emp['name']:<10} Age: {emp['age']}")

# Bob        Age: 25
# Joseph     Age: 28
# Carol      Age: 34
# Dave       Age: 36
# Alice      Age: 41


# ═══════════════════════════════════════════════════════
# 4 — LAMBDAS WITH map()
# map(function, iterable) applies a function to
# every item in an iterable and returns a map object
# Lambdas are a natural fit here
# ═══════════════════════════════════════════════════════

scores = [85, 40, 92, 55, 78, 90, 60]

# ── Apply a curve — add 5 points to every score ────────
curved = list(map(lambda score: score + 5, scores))
print(curved)
# [90, 45, 97, 60, 83, 95, 65]

# ── Convert all names to uppercase ────────────────────
names     = ["joseph", "alice", "bob", "carol"]
uppercased = list(map(lambda name: name.upper(), names))
print(uppercased)
# ['JOSEPH', 'ALICE', 'BOB', 'CAROL']

# ── Format salaries as strings ─────────────────────────
salaries  = [95000, 88000, 102000, 62000]
formatted = list(map(lambda s: f"${s:,}", salaries))
print(formatted)
# ['$95,000', '$88,000', '$102,000', '$62,000']


# ═══════════════════════════════════════════════════════
# 5 — LAMBDAS WITH filter()
# filter(function, iterable) returns only the items
# for which the function returns True
# ═══════════════════════════════════════════════════════

scores    = [85, 40, 92, 55, 78, 90, 60, 73, 88, 45]

# ── Keep only passing scores ───────────────────────────
passing   = list(filter(lambda score: score >= 70, scores))
print(passing)
# [85, 92, 78, 90, 73, 88]

# ── Keep only failing scores ───────────────────────────
failing   = list(filter(lambda score: score < 70, scores))
print(failing)
# [40, 55, 60, 45]

# ── Filter employees by department ────────────────────
employees = [
    {"name": "Joseph", "dept": "Engineering"},
    {"name": "Alice",  "dept": "HR"},
    {"name": "Bob",    "dept": "Engineering"},
    {"name": "Carol",  "dept": "HR"},
    {"name": "Dave",   "dept": "Engineering"},
]

engineering = list(filter(lambda emp: emp["dept"] == "Engineering", employees))
for emp in engineering:
    print(f"  {emp['name']}")

# Joseph
# Bob
# Dave


# ═══════════════════════════════════════════════════════
# 6 — COMBINING map(), filter(), AND sorted()
# These three functions combine naturally with lambdas
# to build clean data transformation pipelines
# ═══════════════════════════════════════════════════════

employees = [
    {"name": "Joseph", "dept": "Engineering", "salary": 95000},
    {"name": "Alice",  "dept": "HR",          "salary": 88000},
    {"name": "Bob",    "dept": "Engineering",  "salary": 62000},
    {"name": "Carol",  "dept": "Engineering",  "salary": 102000},
    {"name": "Dave",   "dept": "HR",           "salary": 71000},
]

# Step 1 — filter: Engineering only
# Step 2 — filter: salary above $80,000
# Step 3 — sorted: by salary descending
# Step 4 — map:    format for display

engineering     = filter(lambda e: e["dept"] == "Engineering", employees)
high_earners    = filter(lambda e: e["salary"] > 80000, engineering)
sorted_earners  = sorted(high_earners, key=lambda e: e["salary"], reverse=True)
formatted       = list(map(lambda e: f"  {e['name']:<10} ${e['salary']:,}", sorted_earners))

print("High Earners in Engineering:")
for line in formatted:
    print(line)

# High Earners in Engineering:
#   Carol      $102,000
#   Joseph     $95,000