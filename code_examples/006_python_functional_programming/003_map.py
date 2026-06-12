# ═══════════════════════════════════════════════════════
# map(), filter() and reduce() are utility functions used
# to perform operations against an iterable and return
# an object with processed data
# map()    — applies a function to every item
# filter() — keeps only items where a function is True
# reduce() — cumulatively combines all items into one value
#
# map() and filter() are built-in
# reduce() must be imported from functools
# ═══════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════
# 1 — map()
# Applies a function to EVERY item in an iterable
# Returns a map object (lazy — computed on demand)
# Syntax: map(function, iterable)
# ═══════════════════════════════════════════════════════

# ── Simple example — square every number ───────────────
numbers = [1, 2, 3, 4, 5]

def square_num(num):
    return num ** 2

squared = list(map(square_num, numbers))
print(squared)                         # [1, 4, 9, 16, 25]

# It is common to use a lambda instead of defining a function:
squared_lambda = list(map(lambda x: x ** 2, numbers))
print(squared_lambda)                  # [1, 4, 9, 16, 25]

# ── Uppercase every name ───────────────────────────────
names = ["joseph", "alice", "bob", "carol"]

uppercased = list(map(lambda name: name.upper(), names))
print(uppercased)               # ['JOSEPH', 'ALICE', 'BOB', 'CAROL']

# ── Apply a pay raise to every salary ─────────────────
salaries  = [62000, 88000, 95000, 102000]

raised    = list(map(lambda s: s * 1.10, salaries))
print(raised)                   # [68200.0, 96800.0, 104500.0, 112200.0]

# ── map() with a regular function ─────────────────────
def apply_curve(score):
    return min(score + 5, 100)  # add 5 points, cap at 100

scores  = [85, 40, 92, 55, 97]
curved  = list(map(apply_curve, scores))
print(curved)                   # [90, 45, 97, 60, 100]

# ── map() over two iterables ───────────────────────────
# map() can accept multiple iterables — the function
# receives one item from each iterable per call

base_salaries = [60000, 85000, 92000, 65000, 76000]
bonuses       = [5000,  10000, 8000]

total_comp = list(map(lambda sal, bonus: sal + bonus, base_salaries, bonuses))
print(total_comp)               # [65000, 95000, 100000] - stop when the end of the shorter is reached





# ═══════════════════════════════════════════════════════
# 2 — map() COMPREHENSIONS/GENERATORS
#
# For map() (and filter()), comprehensions and generator
# expressions are almost always the preferred approach
# in modern Python. They are:
# - More readable
# - More Pythonic
# - Equally or more performant
# - Support complex logic more naturally
# ═══════════════════════════════════════════════════════

scores    = [85, 40, 92, 55, 78, 90, 60, 73, 45]
employees = [
    {"name": "Joseph", "dept": "Engineering", "salary": 95000},
    {"name": "Alice",  "dept": "HR",          "salary": 88000},
    {"name": "Bob",    "dept": "Engineering", "salary": 62000},
    {"name": "Carol",  "dept": "Engineering", "salary": 102000},
    {"name": "Dave",   "dept": "HR",          "salary": 71000},
]

# ── map() vs list comprehension ────────────────────────

# map()
squared_map  = list(map(lambda x: x ** 2, scores))

# list comprehension — cleaner and more readable
squared_comp = [x ** 2 for x in scores]

print(squared_map)              # [7225, 1600, 8464, 3025, 6084, 8100, 3600, 5329, 2025]
print(squared_comp)             # [7225, 1600, 8464, 3025, 6084, 8100, 3600, 5329, 2025]


# ── map() vs generator expression ─────────────────────
# When feeding directly into sum(), max(), etc.
# a generator expression is cleaner than map()

salaries     = [e["salary"] for e in employees]

# map() approach
total_map    = sum(map(lambda e: e["salary"], employees))

# generator expression — more natural
total_gen    = sum(e["salary"] for e in employees)

print(total_map)                # 418000
print(total_gen)                # 418000

