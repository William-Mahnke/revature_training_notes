# ═══════════════════════════════════════════════════════
# WHAT ARE COMPREHENSIONS?
# Comprehensions are a concise, readable way to create
# new collections from existing iterables in one line
# Python supports comprehensions for:
# Lists [], Sets {}, and Dictionaries {key: value}
# ═══════════════════════════════════════════════════════
# LIST COMPREHENSIONS
# Syntax: [expression for item in iterable]
#         [expression for item in iterable if condition]
# ═══════════════════════════════════════════════════════

# ── Generate squares from 0 to 10 ─────────────────────
# For each x in range(0, 11), compute x ** 2
squares = [x ** 2 for x in range(0, 11)]
print(f"original iterable{list(range(0,11))}")
print(f"returns from list comprehension: {squares}")

# ── Filter with a condition ────────────────────────────
# Only include x ** 2 where x is even (x % 2 == 0)
even_squares = [x ** 2 for x in range(0, 11) if x % 2 == 0]

print("squares :", squares)
# squares : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("even squares :", even_squares)
# even squares : [0, 4, 16, 36, 64, 100]

# ── copy() creates a new independent list ─────────────
# Changes to squares_copy will NOT affect squares
squares_copy = squares.copy()
print("squares_copy : ", squares_copy)


# ── Capitalize each name in the list ──────────────────
# For each name in names, call name.capitalize()
names        = ["amy", "bob", "cathy", "dillon", "edward"]
capitalized  = [name.capitalize() for name in names]
print("capitalized  : ", capitalized)
# capitalized  :  ['Amy', 'Bob', 'Cathy', 'Dillon', 'Edward']


# ── Without comprehension (equivalent) ────────────────
# This is what the list comprehension above replaces
capitalized = []
for name in names:
    capitalized.append(name.capitalize())


# ═══════════════════════════════════════════════════════
# SET COMPREHENSIONS
# Syntax: {expression for item in iterable}
# Same as list comprehension but uses {} and
# automatically removes duplicates
# ═══════════════════════════════════════════════════════

# ── Get the unique lengths of each name ───────────────
# "amy"=3, "bob"=3, "cathy"=5, "dillon"=6, "edward"=6
# Duplicates (3 and 6) are removed automatically
unique_lengths = {len(name) for name in names}
print("unique_lengths : ", unique_lengths)
# unique_lengths :  {3, 5, 6}  ← only unique values, order may vary


# ═══════════════════════════════════════════════════════
# DICT COMPREHENSIONS
# Syntax: {key_expression : value_expression for item in iterable}
# ═══════════════════════════════════════════════════════

# ── Map each name to its character length ─────────────
# Creates a dictionary where name is the key
# and len(name) is the value
length_map = {name: len(name) for name in names}
print("length_map : ", length_map)
# length_map :  {'amy': 3, 'bob': 3, 'cathy': 5, 'dillon': 6, 'edward': 6}


# ═══════════════════════════════════════════════════════
# BUILDING ON THE ABOVE — MORE EXAMPLES
# ═══════════════════════════════════════════════════════

# ── List comprehension with if-else ───────────────────
# You can include an if-else directly in the expression
# Syntax: [value_if_true if condition else value_if_false for item in iterable]

scores  = [85, 40, 92, 55, 78, 90, 60]

results = ["Pass" if score >= 70 else "Fail" for score in scores]
print("results : ", results)
# results :  ['Pass', 'Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Fail']


# ── List comprehension over a list of strings ─────────
# Filter names that are longer than 3 characters
long_names = [name for name in names if len(name) > 3]
print("long_names : ", long_names)
# long_names :  ['cathy', 'dillon', 'edward']


# ── Dict comprehension with a condition ───────────────
# Only include employees with a score of 70 or above
employee_scores = {
    "Joseph" : 85,
    "Andy"  : 40,
    "Brittany": 92,
    "Carol" : 55,
    "Diana" : 78
}

passing = {name: score for name, score in employee_scores.items() if score >= 70}
print("passing : ", passing)
# passing :  {'Joseph': 85, 'Brittany': 92, 'Diana': 78}


# ── Dict comprehension to transform values ────────────
# Convert all scores to a letter grade

def get_grade(score):
    if score >= 90: 
        return "A"
    elif score >= 80: 
        return "B"
    elif score >= 70: 
        return "C"
    elif score >= 60: 
        return "D"
    else: 
        return "F"

grades = {name: get_grade(score) for name, score in employee_scores.items()}
print("grades : ", grades)
# grades :  {'Joseph': 'B', 'Andy': 'F', 'Brittany': 'A', 'Carol': 'F', 'Diana': 'C'}


# ── Nested list comprehension ─────────────────────────
# Flatten a 2D list (list of lists) into a single list
# Outer loop iterates over each row
# Inner loop iterates over each item in the row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [item for row in matrix for item in row]
print("flat : ", flat)
# flat :  [1, 2, 3, 4, 5, 6, 7, 8, 9]