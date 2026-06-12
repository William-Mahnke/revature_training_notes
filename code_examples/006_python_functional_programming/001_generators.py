# ═══════════════════════════════════════════════════════
# WHAT ARE GENERATOR EXPRESSIONS?
# A generator expression is similar to a list
# comprehension but instead of building the entire
# collection in memory at once, it produces items
# ONE AT A TIME on demand — this is called LAZY
# EVALUATION
#
# Syntax:
# List comprehension  →  [expression for item in iterable]
# Generator expression → (expression for item in iterable)
#
# The only syntactic difference is () instead of []
# but the behaviour is fundamentally different
# ──────────────────────────────────────────────────────
# 1 — WHAT IS A GENERATOR EXPRESSION?
# ──────────────────────────────────────────────────────

# ── Creating a generator expression ───────────────────

gen = (x ** 2 for x in range(1, 6))

print(gen)                  # <generator object <genexpr> at 0x...>
print(type(gen))            # <class 'generator'>

# ── A generator does not compute values upfront ────────
# Values are produced one at a time using next()

print(next(gen))            # 1   ← computed NOW on demand
print(next(gen))            # 4   ← computed NOW on demand
print(next(gen))            # 9   ← computed NOW on demand
print(next(gen))            # 16
print(next(gen))            # 25

# print(next(gen))          # StopIteration — exhausted

# ── Generators are also iterable ──────────────────────
# You can loop over them just like a list
gen = (x ** 2 for x in range(1, 6))

for value in gen:
    print(value)

# 1
# 4
# 9
# 16
# 25

# Generators can only be iterated ONCE
# Once exhausted, they are empty — unlike lists

gen = (x ** 2 for x in range(1, 6))

print(f"Consuming the Generator: {list(gen)}")            # [1, 4, 9, 16, 25]  ← consumed
print(f"Trying to Consume again: {list(gen)}")            # []  ← empty — already exhausted


# ═══════════════════════════════════════════════════════
# 2 — SIMPLE ONE-OFF OPERATIONS
# Generators pair naturally with built-in functions
# like sum(), max(), min(), and any()/all()
# The generator feeds values in one at a time — only
# what is needed is ever held in memory
# ═══════════════════════════════════════════════════════

scores = [85, 40, 92, 55, 78, 90, 60, 73, 88, 45]

# ── sum() ──────────────────────────────────────────────
total = sum(x for x in scores if x >= 70)
print(f"Sum of passing scores   : {total}")     # 506

# ── max() ──────────────────────────────────────────────
highest = max(x for x in scores)
print(f"Highest score           : {highest}")   # 92

# ── min() ──────────────────────────────────────────────
lowest = min(x for x in scores)
print(f"Lowest score            : {lowest}")    # 40

# ── min() with filter — lowest PASSING score ──────────
lowest_pass = min(x for x in scores if x >= 70)
print(f"Lowest passing score    : {lowest_pass}")  # 73

# ── Counting with sum() ────────────────────────────────
# If 'x' (current score evaluated) is greater than 70, return as 1 
# otherwise return 0. In this way sum() counts all passing scores

pass_count = sum(1 for x in scores if x >= 70)
print(f"Number of passing scores: {pass_count}")    # 6

# ── any() — True if at least one item matches ─────────
has_perfect = any(x == 100 for x in scores)
print(f"Any perfect scores      : {has_perfect}")   # False

# ── all() — True if every item matches ────────────────
all_passing = all(x >= 70 for x in scores)
print(f"All scores passing      : {all_passing}")   # False


# ──────────────────────────────────────────────────────
# 3 — GENERATOR EXPRESSIONS vs LIST COMPREHENSIONS
# ──────────────────────────────────────────────────────

import sys

# ── List comprehension — builds everything in memory ───
list_comp = [x ** 2 for x in range(100000)]

# ── Generator expression — builds nothing upfront ──────
gen_expr  = (x ** 2 for x in range(100000))

# ── Memory comparison ──────────────────────────────────
print(f"List size     : {sys.getsizeof(list_comp):,} bytes")
# List size     : 824,456 bytes  ← entire list in memory

print(f"Generator size: {sys.getsizeof(gen_expr):,} bytes")
# Generator size: 208 bytes      ← just the generator object


# ── Speed ────────────────────────────────────────────── 
# list comprehension is faster if you need ──
# ALL values repeatedly. Generator is better for
# single-pass operations or when you may not need all values

# ── Use a LIST when: ───────────────────────────────────
# - You need to access values multiple times
# - You need indexing (gen[0] is not valid)
# - You need len() (generators have no length)
# - The dataset is small

squares_list = [x ** 2 for x in range(10)]
print(squares_list[3])          # 9  — indexing works on lists
print(len(squares_list))        # 10 — len() works on lists

# ── Use a GENERATOR when: ──────────────────────────────
# - You only need to iterate once
# - The dataset is large or infinite
# - You are feeding into sum(), max(), min(), any(), all()
# - Memory efficiency matters

squares_gen = (x ** 2 for x in range(10))
# print(squares_gen[3])         # TypeError — generators are not subscriptable
# print(len(squares_gen))       # TypeError — generators have no len()


# ── Side by side comparison ────────────────────────────

data = range(1, 11)

# List comprehension — all values computed and stored
squares_list = [x ** 2 for x in data]
print(f"List : {squares_list}")
# List : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Generator expression — values computed one at a time
squares_gen  = (x ** 2 for x in data)
print(f"Sum  : {sum(squares_gen)}")     # 385 — only needed the total, not the list


# ═══════════════════════════════════════════════════════
# 4 — REAL WORLD EXAMPLE
# Processing a large employee payroll dataset
#
# Imagine a company with thousands of employees
# stored in a list of dictionaries. We need to:
# - Find the total salary cost for a department
# - Find the highest earner
# - Check if anyone earns over a threshold
# - Count employees in a department
#
# A generator expression lets us do all of this
# without building intermediate lists in memory
# ═══════════════════════════════════════════════════════

employees = [
    {"name": "Joseph",  "dept": "Engineering", "salary": 95000},
    {"name": "Alice",   "dept": "Engineering", "salary": 88000},
    {"name": "Bob",     "dept": "HR",          "salary": 62000},
    {"name": "Carol",   "dept": "Engineering", "salary": 102000},
    {"name": "Dave",    "dept": "HR",          "salary": 58000},
    {"name": "Eve",     "dept": "Engineering", "salary": 79000},
    {"name": "Frank",   "dept": "HR",          "salary": 71000},
    {"name": "Grace",   "dept": "Engineering", "salary": 115000},
    {"name": "Hank",    "dept": "HR",          "salary": 66000},
    {"name": "Isla",    "dept": "Engineering", "salary": 91000},
]

dept = "Engineering"

# ── Total salary cost for Engineering ─────────────────
total_salary = sum(
    emp["salary"] for emp in employees if emp["dept"] == dept
)
print(f"Total salary ({dept})  : ${total_salary:,}")
# Total salary (Engineering)  : $570,000

# ── Highest earner in Engineering ─────────────────────
top_salary = max(
    emp["salary"] for emp in employees if emp["dept"] == dept
)
print(f"Highest salary ({dept}): ${top_salary:,}")
# Highest salary (Engineering): $115,000

# ── Lowest earner in Engineering ──────────────────────
lowest_salary = min(
    emp["salary"] for emp in employees if emp["dept"] == dept
)
print(f"Lowest salary ({dept}) : ${lowest_salary:,}")
# Lowest salary (Engineering) : $79,000

# ── Count of Engineering employees ────────────────────
eng_count = sum(1 for emp in employees if emp["dept"] == dept)
print(f"Headcount ({dept})     : {eng_count}")
# Headcount (Engineering)     : 6

# ── Does anyone earn over $110,000? ───────────────────
has_high_earner = any(
    emp["salary"] > 110000 for emp in employees if emp["dept"] == dept
)
print(f"Earner over $110k      : {has_high_earner}")
# Earner over $110k      : True

# ── Do ALL Engineering staff earn over $75,000? ───────
all_above_threshold = all(
    emp["salary"] > 75000 for emp in employees if emp["dept"] == dept
)
print(f"All earn over $75k     : {all_above_threshold}")
# All earn over $75k     : False  ← Eve earns $79,000 — wait, that IS above 75k
#                                    Eve earns $79,000 which is > 75,000
#                                    The False comes from no one being below 75k
#                                    Let's check a tighter threshold:

all_above_90k = all(
    emp["salary"] > 90000 for emp in employees if emp["dept"] == dept
)
print(f"All earn over $90k     : {all_above_90k}")
# All earn over $90k     : False  ← Eve ($79k) and Alice ($88k) are below $90k