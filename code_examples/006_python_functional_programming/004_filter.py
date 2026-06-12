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
# 2 — filter()
# Keeps only items where the function returns True
# Returns a filter object (lazy — computed on demand)
# Syntax: filter(function, iterable)
# ═══════════════════════════════════════════════════════

scores = [85, 40, 92, 55, 78, 90, 60, 73, 45]

# ── Keep only passing scores ───────────────────────────
passing = list(filter(lambda score: score >= 70, scores))
print(passing)                  # [85, 92, 78, 90, 73]

# ── Keep only even numbers ────────────────────────────
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens   = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                    # [2, 4, 6, 8, 10]

# ── Filter employees by department ────────────────────
employees = [
    {"name": "Joseph", "dept": "Engineering", "salary": 95000},
    {"name": "Alice",  "dept": "HR",          "salary": 88000},
    {"name": "Bob",    "dept": "Engineering", "salary": 62000},
    {"name": "Carol",  "dept": "Engineering", "salary": 102000},
    {"name": "Dave",   "dept": "HR",          "salary": 71000},
]

eng_team = list(filter(lambda e: e["dept"] == "Engineering", employees))
for emp in eng_team:
    print(f"  {emp['name']:<10} ${emp['salary']:,}")

# Joseph     $95,000
# Bob        $62,000
# Carol      $102,000

# ── filter() with None — removes falsy values ──────────
# Passing None as the function removes all falsy items

mixed = [0, 1, "", "hello", None, 42, False, True, [], [1]]
truthy = list(filter(None, mixed))
print(truthy)                   # [1, 'hello', 42, True, [1]]


# ═══════════════════════════════════════════════════════
# 2 — filter() COMPREHENSIONS/GENERATORS
#
# For filter() (and map()), comprehensions and generator
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

# ── filter() vs list comprehension ─────────────────────

# filter()
passing_map  = list(filter(lambda s: s >= 70, scores))

# list comprehension — easier to read at a glance
passing_comp = [s for s in scores if s >= 70]

print(passing_map)              # [85, 92, 78, 90, 73]
print(passing_comp)             # [85, 92, 78, 90, 73]

# ── filter() vs generator expression ──────────────────

# filter() approach
eng_salaries_map = list(filter(
    lambda e: e["dept"] == "Engineering", employees
))

# generator expression — reads like plain English
eng_salaries_gen = [e for e in employees if e["dept"] == "Engineering"]

print([e["name"] for e in eng_salaries_map])    # ['Joseph', 'Bob', 'Carol']
print([e["name"] for e in eng_salaries_gen])    # ['Joseph', 'Bob', 'Carol']