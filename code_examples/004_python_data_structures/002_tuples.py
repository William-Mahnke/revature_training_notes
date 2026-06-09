# ═══════════════════════════════════════════════════════
# WHAT IS A TUPLE?
# A tuple is an ordered, IMMUTABLE collection of items
# Immutable means once created it cannot be changed —
# no adding, removing, or modifying elements
# ═══════════════════════════════════════════════════════
# 1 — SIMPLE TUPLE CREATION
# ═══════════════════════════════════════════════════════

# ── Using parentheses () ───────────────────────────────
empty_tuple    = ()
fruits         = ("apple", "banana", "cherry")
scores         = (85, 92, 78, 90, 88)
mixed          = ("Joseph", 100, 3.14, True)

print(fruits)                   # ('apple', 'banana', 'cherry')
print(scores)                   # (85, 92, 78, 90, 88)
print(mixed)                    # ('Joseph', 100, 3.14, True)
print(type(fruits))             # <class 'tuple'>

# ── Using tuple() constructor ──────────────────────────
# Converts another iterable (like a list) into a tuple

from_list    = tuple([1, 2, 3, 4, 5])
from_string  = tuple("Hello")

print(from_list)                # (1, 2, 3, 4, 5)
print(from_string)              # ('H', 'e', 'l', 'l', 'o')

# ── Single item tuple ──────────────────────────────────
# A trailing comma is REQUIRED for a single item tuple
# Without it Python treats it as just a value in parentheses

single        = ("Joseph",)     # this is a tuple
not_a_tuple   = ("Joseph")      # this is just a string

print(type(single))             # <class 'tuple'>
print(type(not_a_tuple))        # <class 'str'>

# ── Tuples are immutable ───────────────────────────────
fruits = ("apple", "banana", "cherry")

# fruits[0] = "mango"           # TypeError — tuples cannot be modified


# ═══════════════════════════════════════════════════════
# 2 — TUPLE PACKING
# Packing is when you assign multiple values into
# a single tuple — Python bundles them automatically
# Parentheses are optional when packing
# ═══════════════════════════════════════════════════════

# ── With parentheses ───────────────────────────────────
employee      = ("Joseph", 100, "Developer")
coordinates   = (40.7128, -74.0060)

print(employee)                 # ('Joseph', 100, 'Developer')
print(coordinates)              # (40.7128, -74.006)

# ── Without parentheses — Python still creates a tuple ─
employee      = "Joseph", 100, "Developer"
print(employee)                 # ('Joseph', 100, 'Developer')
print(type(employee))           # <class 'tuple'>


# ═══════════════════════════════════════════════════════
# 3 — TUPLE UNPACKING
# Unpacking assigns each element of a tuple to
# individual variables in a single statement
# The number of variables must match the number
# of elements — unless using *
# ═══════════════════════════════════════════════════════

# ── Basic unpacking ────────────────────────────────────
employee = ("Joseph", 100, "Developer")

emp_name, emp_id, emp_title = employee

print(emp_name)                 # Joseph
print(emp_id)                   # 100
print(emp_title)                # Developer

# ── Unpacking coordinates ──────────────────────────────
coordinates = (40.7128, -74.0060)

latitude, longitude = coordinates

print(f"Latitude  : {latitude}")    # Latitude  : 40.7128
print(f"Longitude : {longitude}")   # Longitude : -74.006

# ── Using * to capture remaining items ────────────────
# The * variable collects everything not explicitly assigned

scores = (92, 85, 78, 66, 55)

first, second, *rest = scores

print(first)                    # 92
print(second)                   # 85
print(rest)                     # [78, 66, 55]  ← captured as a list

first, *middle, last = scores

print(first)                    # 92
print(middle)                   # [85, 78, 66]
print(last)                     # 55

# ── Mismatch raises an error ───────────────────────────
# Recall that employee = ("Joseph", 100, "Developer") 
# emp_name, emp_id = employee   # ValueError: too many values to unpack
# emp_name, emp_id, emp_title, emp_org = employee # ValueError: not enough values to unpack

# ═══════════════════════════════════════════════════════
# 4 — INDEXING, NEGATIVE INDEXING, AND SLICING
# Tuples support all the same indexing and slicing
# as lists — the only difference is you cannot
# modify the result
# ═══════════════════════════════════════════════════════

employees = ("Joseph", "Alice", "Bob", "Carol", "Dave")

# ── Positive indexing ──────────────────────────────────
print(employees[0])             # Joseph  ← first element
print(employees[1])             # Alice
print(employees[4])             # Dave    ← last element

# ── Negative indexing ──────────────────────────────────
print(employees[-1])            # Dave    ← last element
print(employees[-2])            # Carol
print(employees[-5])            # Joseph  ← first element

# ── Slicing ────────────────────────────────────────────
print(employees[1:4])           # ('Alice', 'Bob', 'Carol')
print(employees[:3])            # ('Joseph', 'Alice', 'Bob')
print(employees[2:])            # ('Bob', 'Carol', 'Dave')
print(employees[::2])           # ('Joseph', 'Bob', 'Dave')  ← every 2nd element
print(employees[::-1])          # ('Dave', 'Carol', 'Bob', 'Alice', 'Joseph')


# ═══════════════════════════════════════════════════════
# 5 — USING TUPLES AS DICTIONARY KEYS
# Because tuples are immutable they can be used
# as dictionary keys — lists cannot because they
# are mutable
# ═══════════════════════════════════════════════════════

# ── Coordinates as keys ────────────────────────────────
locations = {
    (40.7128, -74.0060) : "New York City",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298) : "Chicago"
}

print(locations[(40.7128, -74.0060)])   # New York City
print(locations[(41.8781, -87.6298)])   # Chicago

# ── Grid positions as keys ─────────────────────────────
grid = {
    (0, 0): "Start",
    (0, 1): "Empty",
    (1, 0): "Wall",
    (1, 1): "End"
}

print(grid[(0, 0)])             # Start
print(grid[(1, 1)])             # End

# ── Looping over tuple keys ────────────────────────────
for coordinates, city in locations.items():
    lat, lon = coordinates      # unpack the tuple key
    print(f"{city:<20} Lat: {lat}   Lon: {lon}")

# New York City        Lat: 40.7128   Lon: -74.006
# Los Angeles          Lat: 34.0522   Lon: -118.2437
# Chicago              Lat: 41.8781   Lon: -87.6298

# ── Why not a list as a key? ───────────────────────────
# list_key = {[0, 0]: "Start"}  # TypeError — unhashable type: 'list'