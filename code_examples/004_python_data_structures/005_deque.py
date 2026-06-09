# ═══════════════════════════════════════════════════════
# WHAT IS A DEQUE?
# A deque (double-ended queue) is a data structure
# that allows you to efficiently add and remove items
# from BOTH ends — the left and the right
# It is imported from Python's built-in 'collections'
# module
# ═══════════════════════════════════════════════════════
# IMPORT STATEMENT
# Deque is not available by default — it must be
# imported from the collections module before use
# ═══════════════════════════════════════════════════════

from collections import deque


# ═══════════════════════════════════════════════════════
# 1 — SIMPLE DEQUE CREATION
# ═══════════════════════════════════════════════════════

# ── Empty deque ────────────────────────────────────────
empty_deque = deque()
print(empty_deque)              # deque([])
print(type(empty_deque))        # <class 'collections.deque'>

# ── From a list ────────────────────────────────────────
employees   = deque(["Joseph", "Alice", "Bob", "Carol"])
scores      = deque([85, 92, 78, 90])

print(employees)                # deque(['Joseph', 'Alice', 'Bob', 'Carol'])
print(scores)                   # deque([85, 92, 78, 90])

# ── With a maxlen ──────────────────────────────────────
# maxlen limits the size of the deque
# When full, adding a new item automatically removes
# the item from the opposite end

limited = deque([1, 2, 3], maxlen=3)
print(limited)                  # deque([1, 2, 3], maxlen=3)

limited.append(4)               # right side full — removes 1 from the left
print(limited)                  # deque([2, 3, 4], maxlen=3)


# ═══════════════════════════════════════════════════════
# 2 — COMMON DEQUE METHODS
# ═══════════════════════════════════════════════════════

# ── append() ───────────────────────────────────────────
# Adds a single item to the RIGHT end of the deque

employees = deque(["Joseph", "Alice", "Bob"])

employees.append("Carol")
print(employees)                # deque(['Joseph', 'Alice', 'Bob', 'Carol'])

employees.append("Dave")
print(employees)                # deque(['Joseph', 'Alice', 'Bob', 'Carol', 'Dave'])


# ── appendleft() ───────────────────────────────────────
# Adds a single item to the LEFT end of the deque

employees = deque(["Joseph", "Alice", "Bob"])

employees.appendleft("Zara")
print(employees)                # deque(['Zara', 'Joseph', 'Alice', 'Bob'])

employees.appendleft("Eve")
print(employees)                # deque(['Eve', 'Zara', 'Joseph', 'Alice', 'Bob'])


# ── pop() ──────────────────────────────────────────────
# Removes and RETURNS the item from the RIGHT end

employees = deque(["Joseph", "Alice", "Bob", "Carol"])

popped = employees.pop()
print(popped)                   # Carol   ← removed from right
print(employees)                # deque(['Joseph', 'Alice', 'Bob'])

popped = employees.pop()
print(popped)                   # Bob     ← removed from right
print(employees)                # deque(['Joseph', 'Alice'])


# ── popleft() ──────────────────────────────────────────
# Removes and RETURNS the item from the LEFT end

employees = deque(["Joseph", "Alice", "Bob", "Carol"])

popped = employees.popleft()
print(popped)                   # Joseph  ← removed from left
print(employees)                # deque(['Alice', 'Bob', 'Carol'])

popped = employees.popleft()
print(popped)                   # Alice   ← removed from left
print(employees)                # deque(['Bob', 'Carol'])


# ── rotate() ───────────────────────────────────────────
# Rotates the deque by n steps
# Positive n rotates to the RIGHT — items shift right,
# items that fall off the right are added to the left
# Negative n rotates to the LEFT — items shift left,
# items that fall off the left are added to the right

employees = deque(["Joseph", "Alice", "Bob", "Carol", "Dave"])

# ── Rotate right ───────────────────────────────────────
employees.rotate(1)
print(employees)        # deque(['Dave', 'Joseph', 'Alice', 'Bob', 'Carol'])
#                                  ↑ Dave moved from right end to left end

employees.rotate(2)
print(employees)        # deque(['Bob', 'Carol', 'Dave', 'Joseph', 'Alice'])
#                                  ↑ last 2 items wrapped to the front

# ── Rotate left ────────────────────────────────────────
employees = deque(["Joseph", "Alice", "Bob", "Carol", "Dave"])

employees.rotate(-1)
print(employees)        # deque(['Alice', 'Bob', 'Carol', 'Dave', 'Joseph'])
#                                                                    ↑ Joseph moved from left to right

employees.rotate(-2)
print(employees)        # deque(['Carol', 'Dave', 'Joseph', 'Alice', 'Bob'])
#                                                                    ↑ first 2 items wrapped to the end


# ── extend() ───────────────────────────────────────────
# Adds multiple items to the RIGHT end of the deque
# Accepts any iterable (list, tuple, set, etc.)

employees = deque(["Joseph", "Alice"])

employees.extend(["Bob", "Carol", "Dave"])
print(employees)        # deque(['Joseph', 'Alice', 'Bob', 'Carol', 'Dave'])


# ── extendleft() ───────────────────────────────────────
# Adds multiple items to the LEFT end of the deque
# Each item is added one at a time to the left
# so the final order is REVERSED from the input

employees = deque(["Joseph", "Alice"])

employees.extendleft(["Bob", "Carol", "Dave"])
print(employees)        # deque(['Dave', 'Carol', 'Bob', 'Joseph', 'Alice'])
#                                  ↑ reversed — Bob added first, then Carol over it, then Dave

# ── Why is extendleft() reversed? ─────────────────────
# It processes the list one item at a time:
# Step 1: appendleft("Bob")   → deque(['Bob',   'Joseph', 'Alice'])
# Step 2: appendleft("Carol") → deque(['Carol', 'Bob',    'Joseph', 'Alice'])
# Step 3: appendleft("Dave")  → deque(['Dave',  'Carol',  'Bob',    'Joseph', 'Alice'])