# ═══════════════════════════════════════════════════════
# WHAT IS A SET?
# A set is an unordered collection of UNIQUE items
# Sets automatically remove duplicate values
# Because they are unordered, sets have NO index —
# you cannot access elements by position
# ═══════════════════════════════════════════════════════
# 1 — SIMPLE SET CREATION
# ═══════════════════════════════════════════════════════

# ── Using curly braces {} ──────────────────────────────
fruits = {"apple", "banana", "cherry"}
scores = {85, 92, 78, 90, 88}

print(fruits)                   # {'apple', 'banana', 'cherry'} (order may vary)
print(scores)                   # {88, 90, 92, 78, 85}          (order may vary)
print(type(fruits))             # <class 'set'>

# ── Duplicates are automatically removed ───────────────
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)                  # {1, 2, 3, 4} ← duplicates removed automatically

employees = {"Joseph", "Alice", "Joseph", "Bob", "Alice"}
print(employees)                # {'Joseph', 'Alice', 'Bob'} ← duplicates removed


# ── Using set() constructor ────────────────────────────
# Converts another iterable into a set

from_list   = set([1, 2, 3, 4, 5])
from_string = set("hello")      # each character becomes an element

print(from_list)                # {1, 2, 3, 4, 5}
print(from_string)              # {'h', 'e', 'l', 'o'} ← duplicate 'l' removed


# ═══════════════════════════════════════════════════════
# CREATING AN EMPTY SET — {} vs set()
#
# {} does NOT create an empty set — it creates an
# empty DICTIONARY. Always use set() for an empty set.
# ═══════════════════════════════════════════════════════

empty_dict  = {}                # this is an empty dictionary
empty_set   = set()             # this is an empty set

print(type(empty_dict))         # <class 'dict'>
print(type(empty_set))          # <class 'set'>


# ═══════════════════════════════════════════════════════
# 2 — COMMON SET METHODS
# ═══════════════════════════════════════════════════════

# ── add() ──────────────────────────────────────────────
# Adds a single item to the set
# If the item already exists, nothing happens

employees = {"Joseph", "Alice", "Bob"}

employees.add("Carol")
print(employees)                # {'Joseph', 'Alice', 'Bob', 'Carol'}

employees.add("Alice")          # already exists — no error, no duplicate added
print(employees)                # {'Joseph', 'Alice', 'Bob', 'Carol'}


# ── remove() ───────────────────────────────────────────
# Removes a specific item from the set
# Raises a KeyError if the item does not exist

employees = {"Joseph", "Alice", "Bob", "Carol"}

employees.remove("Bob")
print(employees)                # {'Joseph', 'Alice', 'Carol'}

# employees.remove("Dave")      # KeyError — Dave is not in the set


# ── discard() ──────────────────────────────────────────
# Removes a specific item from the set
# Does NOT raise an error if the item does not exist
# Use discard() when you are not sure if the item exists

employees = {"Joseph", "Alice", "Bob", "Carol"}

employees.discard("Bob")
print(employees)                # {'Joseph', 'Alice', 'Carol'}

employees.discard("Dave")       # no error — Dave simply was not there
print(employees)                # {'Joseph', 'Alice', 'Carol'} ← unchanged

# ── remove() vs discard() ──────────────────────────────
# remove()  → use when the item SHOULD exist — raises an error if not found
# discard() → use when the item MAY or MAY NOT exist — safe either way


# ── difference() ───────────────────────────────────────
# Returns a NEW set with items that are in the first set
# but NOT in the second set
# Does not modify either original set

all_employees       = {"Joseph", "Alice", "Bob", "Carol", "Dave"}
active_employees    = {"Joseph", "Alice", "Carol"}

inactive = all_employees.difference(active_employees)
print(inactive)                 # {'Bob', 'Dave'} ← in all but not in active

# ── The - operator does the same thing ─────────────────
inactive = all_employees - active_employees
print(inactive)                 # {'Bob', 'Dave'}

# ── Original sets are unchanged ────────────────────────
print(all_employees)            # {'Joseph', 'Alice', 'Bob', 'Carol', 'Dave'}
print(active_employees)         # {'Joseph', 'Alice', 'Carol'}


# ── clear() ────────────────────────────────────────────
# Removes ALL items from the set, leaving it empty
# NOTE: clear() also works on lists and dictionaries

employees = {"Joseph", "Alice", "Bob"}

employees.clear()
print(employees)                # set()  ← empty set


# ── copy() ─────────────────────────────────────────────
# Returns a SHALLOW copy of the set — a new independent set
# Changes to the copy do not affect the original
# NOTE: copy() also works on lists and dictionaries

employees       = {"Joseph", "Alice", "Bob"}
employees_copy  = employees.copy()

employees_copy.add("Carol")     # only modifies the copy

print(employees)                # {'Joseph', 'Alice', 'Bob'}       ← original unchanged
print(employees_copy)           # {'Joseph', 'Alice', 'Bob', 'Carol'}

# ── Without copy() — both variables point to same set ──
employees       = {"Joseph", "Alice", "Bob"}
employees_ref   = employees             # NOT a copy — same object in memory

employees_ref.add("Carol")

print(employees)                # {'Joseph', 'Alice', 'Bob', 'Carol'} ← original also changed!
print(employees_ref)            # {'Joseph', 'Alice', 'Bob', 'Carol'}