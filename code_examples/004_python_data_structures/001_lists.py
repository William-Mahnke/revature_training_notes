# ═══════════════════════════════════════════════════════
# 1 — SIMPLE LIST CREATION
# A list is an ordered, mutable collection of items
# Defined using square brackets []
# ═══════════════════════════════════════════════════════

# ── Empty list ─────────────────────────────────────────
empty_list = []

# ── List of strings ────────────────────────────────────
fruits = ["apple", "banana", "cherry", "mango"]

# ── List of integers ───────────────────────────────────
scores = [85, 92, 78, 90, 88]

# ── List of floats ─────────────────────────────────────
prices = [9.99, 14.99, 4.99, 24.99]

print(fruits)                   # ['apple', 'banana', 'cherry', 'mango']
print(scores)                   # [85, 92, 78, 90, 88]
print(prices)                   # [9.99, 14.99, 4.99, 24.99]


# ═══════════════════════════════════════════════════════
# 2 — MIXED TYPES IN A LIST
# Python lists can hold any combination of data types
# in the same list
# ═══════════════════════════════════════════════════════

mixed = ["Joseph", 100, 3.14, True, None]

print(mixed)                    # ['Joseph', 100, 3.14, True, None]
print(type(mixed[0]))           # <class 'str'>
print(type(mixed[1]))           # <class 'int'>
print(type(mixed[2]))           # <class 'float'>
print(type(mixed[3]))           # <class 'bool'>
print(type(mixed[4]))           # <class 'NoneType'>


# ═══════════════════════════════════════════════════════
# 3 — ACCESSING ELEMENTS BY INDEX
# Lists are zero-indexed — the first element is at index 0
# Negative indexes count backwards from the end
# ═══════════════════════════════════════════════════════

employees = ["Joseph", "Alice", "Bob", "Carol", "Dave"]

# ── Positive indexing ──────────────────────────────────
print(employees[0])             # Joseph  ← first element
print(employees[1])             # Alice
print(employees[2])             # Bob
print(employees[3])             # Carol
print(employees[4])             # Dave    ← last element

# ── Negative indexing — counts from the end ────────────
print(employees[-1])            # Dave    ← last element
print(employees[-2])            # Carol
print(employees[-3])            # Bob
print(employees[-4])            # Alice
print(employees[-5])            # Joseph  ← first element

# ── Finding the index of an element ───────────────────
print(employees.index("Bob"))   # 2  ← returns the index of the first match

# ── Checking if an element exists ─────────────────────
print("Alice" in employees)     # True
print("Zara"  in employees)     # False

# ── Accessing out of range ─────────────────────────────
# print(employees[10])          # IndexError — index out of range


# ═══════════════════════════════════════════════════════
# 4 — LIST SLICING
# Extract a portion of a list using [start:stop:step]
# start — index to begin at (inclusive)
# stop  — index to stop at  (exclusive)
# step  — how many to jump  (optional, default is 1)
# ═══════════════════════════════════════════════════════

employees = ["Joseph", "Alice", "Bob", "Carol", "Dave"]

# ── Basic slicing ──────────────────────────────────────
print(employees[1:4])           # ['Alice', 'Bob', 'Carol']  ← index 1 up to (not including) 4
print(employees[0:3])           # ['Joseph', 'Alice', 'Bob']

# ── Omitting start or stop ─────────────────────────────
print(employees[:3])            # ['Joseph', 'Alice', 'Bob']     ← from beginning to index 3
print(employees[2:])            # ['Bob', 'Carol', 'Dave']       ← from index 2 to end
print(employees[:])             # ['Joseph', 'Alice', 'Bob', 'Carol', 'Dave'] ← full copy

# ── Using a step ──────────────────────────────────────
print(employees[::2])           # ['Joseph', 'Bob', 'Dave']  ← every 2nd element
print(employees[1::2])          # ['Alice', 'Carol']         ← every 2nd starting from index 1

# ── Negative step — reverses the list ─────────────────
print(employees[::-1])          # ['Dave', 'Carol', 'Bob', 'Alice', 'Joseph']


# ═══════════════════════════════════════════════════════
# 5 — NESTED LISTS
# A list can contain other lists as elements
# Access nested elements by chaining index brackets
# ═══════════════════════════════════════════════════════

departments = [
    ["Joseph", "Alice", "Bob"],         # index 0 — Engineering
    ["Carol", "Dave"],                  # index 1 — HR
    ["Eve", "Frank", "Grace", "Hank"]   # index 2 — Sales
]

# ── Accessing a nested list ────────────────────────────
print(departments[0])           # ['Joseph', 'Alice', 'Bob']
print(departments[1])           # ['Carol', 'Dave']

# ── Accessing an element inside a nested list ──────────
print(departments[0][0])        # Joseph  ← first item in first list
print(departments[0][2])        # Bob     ← third item in first list
print(departments[2][1])        # Frank   ← second item in third list
print(departments[1][-1])       # Dave    ← last item in second list

# ── Looping through a nested list ─────────────────────
labels = ["Engineering", "HR", "Sales"]

for i in range(len(departments)):
    print(f"{labels[i]}:")
    for employee in departments[i]:
        print(f"  - {employee}")

# Engineering:
#   - Joseph
#   - Alice
#   - Bob
# HR:
#   - Carol
#   - Dave
# Sales:
#   - Eve
#   - Frank
#   - Grace
#   - Hank


# ═══════════════════════════════════════════════════════
# 6 — COMMON LIST METHODS
# ═══════════════════════════════════════════════════════

# ── append() ───────────────────────────────────────────
# Adds a single item to the END of the list

employees = ["Joseph", "Alice", "Bob"]

employees.append("Carol")
print(employees)                # ['Joseph', 'Alice', 'Bob', 'Carol']


# ── insert() ───────────────────────────────────────────
# Inserts an item at a SPECIFIC index
# insert(index, value)

employees.insert(1, "Zara")     # insert "Zara" at index 1
print(employees)                # ['Joseph', 'Zara', 'Alice', 'Bob', 'Carol']


# ── remove() ───────────────────────────────────────────
# Removes the FIRST occurrence of a value
# Raises ValueError if the value is not found

employees.remove("Zara")
print(employees)                # ['Joseph', 'Alice', 'Bob', 'Carol']

# employees.remove("Dave")      # ValueError — Dave is not in the list


# ── pop() ──────────────────────────────────────────────
# Removes and RETURNS an item by index
# Defaults to the last item if no index is given

employees = ["Joseph", "Alice", "Bob", "Carol"]

popped = employees.pop()        # removes and returns last item
print(popped)                   # Carol
print(employees)                # ['Joseph', 'Alice', 'Bob']

popped = employees.pop(1)       # removes and returns item at index 1
print(popped)                   # Alice
print(employees)                # ['Joseph', 'Bob']


# ── sort() ─────────────────────────────────────────────
# Sorts the list IN PLACE — modifies the original list
# Default is ascending order
# Use reverse=True for descending

scores = [85, 92, 78, 90, 55, 88]

scores.sort()
print(scores)                   # [55, 78, 85, 88, 90, 92]  ← ascending

scores.sort(reverse=True)
print(scores)                   # [92, 90, 88, 85, 78, 55]  ← descending

employees = ["Joseph", "Alice", "Bob", "Carol"]

employees.sort()
print(employees)                # ['Alice', 'Bob', 'Carol', 'Joseph']  ← alphabetical


# ── reverse() ──────────────────────────────────────────
# Reverses the list IN PLACE — does NOT sort,
# just flips the current order

employees = ["Joseph", "Alice", "Bob", "Carol"]

employees.reverse()
print(employees)                # ['Carol', 'Bob', 'Alice', 'Joseph']

scores = [85, 92, 78, 90, 55]

scores.reverse()
print(scores)                   # [55, 90, 78, 92, 85]  ← just flipped, not sorted