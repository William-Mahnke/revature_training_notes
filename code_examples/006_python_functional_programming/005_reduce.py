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
from functools import reduce

# ═══════════════════════════════════════════════════════
# 3 — reduce()
# Cumulatively applies a function to all items,
# reducing the entire iterable to a SINGLE value
# Must be imported from functools
# Syntax: reduce(function, iterable)
# ═══════════════════════════════════════════════════════

numbers = [1, 2, 3, 4, 5]

# ── Sum all numbers ────────────────────────────────────
# Step 1: f(1, 2) = 3
# Step 2: f(3, 3) = 6
# Step 3: f(6, 4) = 10
# Step 4: f(10,5) = 15

total = reduce(lambda a, b: a + b, numbers)
print(total)                    # 15

# ── Multiply all numbers ───────────────────────────────
# Step 1: f(1, 2) = 2
# Step 2: f(2, 3) = 6
# Step 3: f(6, 4) = 24
# Step 4: f(24,5) = 120

product = reduce(lambda a, b: a * b, numbers)
print(product)                  # 120

# ── Find the maximum value ────────────────────────────
# Step 1: f(1, 2) = 2
# Step 2: f(2, 3) = 3
# Step 3: f(3, 4) = 4
# Step 4: f(4, 5) = 5

maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(maximum)                  # 5

# ── Concatenate a list of strings ─────────────────────
words     = ["Python", "is", "fun", "to", "learn"]

sentence  = reduce(lambda a, b: a + " " + b, words)
print(sentence)                 # Python is fun to learn

# ── reduce() with an initial value ────────────────────
# An optional third argument sets the starting value
# This is useful when the accumulator needs a head start

salaries  = [95000, 88000, 62000, 102000, 71000]

# Starting from 0, add each salary to the running total
total     = reduce(lambda acc, salary: acc + salary, salaries, 0)
print(f"Total payroll: ${total:,}")     # Total payroll: $418,000

# ── reduce() to find the highest-paid employee ─────────
employees = [
    {"name": "Joseph", "salary": 95000},
    {"name": "Alice",  "salary": 88000},
    {"name": "Carol",  "salary": 102000},
    {"name": "Bob",    "salary": 62000},
]

top_earner = reduce(
    lambda a, b: a if a["salary"] > b["salary"] else b,
    employees
)
print(f"Top earner: {top_earner['name']} — ${top_earner['salary']:,}")
# Top earner: Carol — $102,000


# ── reduce() has NO comprehension equivalent ──────────
# This is where reduce() stays the right tool —
# there is no clean comprehension syntax for
# cumulative operations across all items

salaries = [95000, 88000, 62000, 102000, 71000]

# reduce() — the right tool for cumulative operations
total    = reduce(lambda acc, s: acc + s, salaries, 0)
print(f"Total : ${total:,}")            # Total : $418,000

product  = reduce(lambda acc, s: acc * s, [1, 2, 3, 4, 5])
print(f"Product: {product}")            # Product: 120

# Note: some built-in functions CAN replace reduce
# i.e. reduce() might be too complex to use instead of 
# leveraging built-in functionality.
# For summing - sum() replaces reduce() for simple totals

total_sum = sum(salaries)
print(f"Total : ${total_sum:,}")        # Total : $418,000

# reduce() shines when the operation is more complex
# and no built-in tool covers it — like the highest-paid
# employee example above, or building a nested result