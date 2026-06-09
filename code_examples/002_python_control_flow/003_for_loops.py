# ═══════════════════════════════════════════════════════
# 1 — INTRODUCTION: WHAT IS A FOR LOOP?
# A for loop iterates over a sequence, executing the
# indented block once for each item in the sequence
# ═══════════════════════════════════════════════════════

# For-loops repeat operations for each item in an iterable (collections of data)
scores = [85, 92, 78, 90, 88] # this is a list

for score in scores:
    print(score)
# 85
# 92
# 78
# 90
# 88

# ── Looping over a string ──────────────────────────────
# Strings are an iterable sequence of characters
word = "Hello"
for character in word:
    print(character)
# H
# e
# l
# l
# o


# ── Node: Code AFTER the loop always runs ───────────────────
for character in word:
    print(character)
print("Loop finished.")             # always runs after the loop completes

# ═══════════════════════════════════════════════════════
# 2 — LOOPING OVER A LIST
# Lists are the most common collection used with for loops
# ═══════════════════════════════════════════════════════
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry
# mango

# ═══════════════════════════════════════════════════════
# 3 — LOOPING OVER A TUPLE
# Tuples work the same as lists in a for loop
# ═══════════════════════════════════════════════════════

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

for day in days:
    print(day)

# Monday
# Tuesday
# Wednesday
# Thursday
# Friday


# ═══════════════════════════════════════════════════════
# 4 — LOOPING OVER A DICTIONARY
# By default iterates over keys
# Use .values() for values, .items() for both
# ═══════════════════════════════════════════════════════
employee = {
    "id"        : 100,
    "name"      : "Joseph",
    "title"     : "Developer",
    "department": "Engineering"
}

# ── Keys only (default) ────────────────────────────────
for key in employee:
    print(key)
# id
# name
# title
# department

# ── Values only ────────────────────────────────────────
for value in employee.values():
    print(value)
# 100
# Joseph
# Developer
# Engineering

# ── Keys and values together ───────────────────────────
for key, value in employee.items():
    print(f"{key:<12}: {value}")
# id          : 100
# name        : Joseph
# title       : Developer
# department  : Engineering


# ═══════════════════════════════════════════════════════
# 5 — LOOPING OVER A LIST OF DICTIONARIES
# Very common pattern for working with records
# ═══════════════════════════════════════════════════════
employees = [
    {"id": 100, "name": "Joseph", "title": "Developer"},
    {"id": 101, "name": "Alice",  "title": "Manager"},
    {"id": 102, "name": "Bob",    "title": "Intern"},
]

for emp in employees:
    print(f"ID: {emp['id']}  Name: {emp['name']:<10}  Title: {emp['title']}")

# ID: 100  Name: Joseph      Title: Developer
# ID: 101  Name: Alice       Title: Manager
# ID: 102  Name: Bob         Title: Intern


# ═══════════════════════════════════════════════════════
# 6 — FOR LOOP WITH IF-ELSE
# Adding logic inside a loop to act on each item
# ═══════════════════════════════════════════════════════

# ── Filter passing and failing scores ─────────────────
scores = [85, 92, 55, 78, 40, 90, 63]

for score in scores:
    if score >= 70:
        print(f"{score} — Pass")
    else:
        print(f"{score} — Fail")

# 85 — Pass
# 92 — Pass
# 55 — Fail
# 78 — Pass
# 40 — Fail
# 90 — Pass
# 63 — Fail


# ── Assign access levels to employees ─────────────────

employees = [
    {"name": "Joseph", "title": "Developer"},
    {"name": "Alice",  "title": "Manager"},
    {"name": "Bob",    "title": "Intern"},
    {"name": "Carol",  "title": "Director"},
]

for emp in employees:
    if emp["title"] == "Director":
        access = "Full Access"
    elif emp["title"] == "Manager":
        access = "Elevated Access"
    elif emp["title"] == "Developer":
        access = "Standard Access"
    else:
        access = "Limited Access"

    print(f"{emp['name']:<10} ({emp['title']:<10}) → {access}")

# Joseph     (Developer ) → Standard Access
# Alice      (Manager   ) → Elevated Access
# Bob        (Intern    ) → Limited Access
# Carol      (Director  ) → Full Access


# ── Separate a list into two groups ───────────────────

numbers    = [3, 18, 7, 24, 11, 6, 15, 9, 20]
evens      = []
odds       = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

print(f"Evens : {evens}")       # Evens : [18, 24, 6, 20]
print(f"Odds  : {odds}")        # Odds  : [3, 7, 11, 15, 9]