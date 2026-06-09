# ═══════════════════════════════════════════════════════
# WHAT IS iter()?
# iter() returns an ITERATOR object from an iterable
# An iterable is anything you can loop over
# An iterator is an object that keeps track of WHERE
# you are in the sequence and returns the NEXT item
# each time next() is called on it
#
# Under the hood, a for loop does this automatically —
# iter() and next() let you do it manually
# ═══════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════
# 1 — ITERATING OVER A LIST
# ═══════════════════════════════════════════════════════

employees = ["Joseph", "Alice", "Bob", "Carol"]

# ── What a for loop does under the hood ───────────────
iterator = iter(employees)          # creates an iterator from the list

print(next(iterator))               # Joseph  ← first call returns first item
print(next(iterator))               # Alice   ← second call returns second item
print(next(iterator))               # Bob
print(next(iterator))               # Carol

# print(next(iterator))             # ❌ StopIteration — no more items

# ── Using a while loop with iter() ────────────────────
iterator = iter(employees)

while True:
    try:
        employee = next(iterator)
        print(employee)
    except StopIteration:
        break                       # StopIteration signals the end of the sequence

# Joseph
# Alice
# Bob
# Carol


# ═══════════════════════════════════════════════════════
# 2 — ITERATING OVER A TUPLE
# ═══════════════════════════════════════════════════════

coordinates = (40.7128, -74.0060, 100.5)    # lat, lon, altitude

iterator = iter(coordinates)

lat      = next(iterator)
lon      = next(iterator)
altitude = next(iterator)

print(f"Latitude  : {lat}")         # Latitude  : 40.7128
print(f"Longitude : {lon}")         # Longitude : -74.006
print(f"Altitude  : {altitude}")    # Altitude  : 100.5


# ═══════════════════════════════════════════════════════
# 3 — ITERATING OVER A STRING
# A string is an iterable of individual characters
# ═══════════════════════════════════════════════════════

name     = "Joseph"
iterator = iter(name)

print(next(iterator))               # J
print(next(iterator))               # o
print(next(iterator))               # s
print(next(iterator))               # e
print(next(iterator))               # p
print(next(iterator))               # h

# ── Collecting characters manually ────────────────────
name     = "Hello"
iterator = iter(name)
result   = []

while True:
    try:
        result.append(next(iterator))
    except StopIteration:
        break

print(result)                       # ['H', 'e', 'l', 'l', 'o']


# ═══════════════════════════════════════════════════════
# 4 — ITERATING OVER A DICTIONARY
# By default iterates over KEYS
# Use .values() or .items() for other views
# ═══════════════════════════════════════════════════════

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer",
    "dept"      : "Engineering"
}

# ── Iterating over keys (default) ─────────────────────
iterator = iter(employee)

print(next(iterator))               # emp_id
print(next(iterator))               # emp_name
print(next(iterator))               # emp_title
print(next(iterator))               # dept

# ── Iterating over values ──────────────────────────────
iterator = iter(employee.values())

print(next(iterator))               # 100
print(next(iterator))               # Joseph

# ── Iterating over items ───────────────────────────────
iterator = iter(employee.items())

print(next(iterator))               # ('emp_id', 100)
print(next(iterator))               # ('emp_name', 'Joseph')


# ═══════════════════════════════════════════════════════
# 5 — CUSTOM ITERABLE: A STACK
#
# A Stack is a LIFO data structure:
# LIFO = Last In, First Out
# The last item added is the first item removed
# Think of it like a stack of plates —
# you add and remove from the TOP
#
# To make a class iterable in Python it must
# implement two special methods:
#
# __iter__() — called by iter(), returns the
#              iterator object (self in this case)
#
# __next__() — called by next(), returns the
#              next item or raises StopIteration
#              when there are no more items
# ═══════════════════════════════════════════════════════

class MyStack:
    """A simple LIFO stack implementation."""

    def __init__(self):
        self._items = []            # internal list to store items

    # ── Stack operations ───────────────────────────────

    def push(self, item):
        """Add an item to the TOP of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the TOP of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the TOP item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

    # ── String representation ──────────────────────────

    def __repr__(self):
        return f"Stack(TOP → {self._items[::-1]})"

    # ── Iteration support ──────────────────────────────

    def __iter__(self):
        """
        Called by iter() — prepares iteration from the TOP.
        Stores the starting index at the top of the stack
        and returns self as the iterator object.
        """
        self._index = len(self._items) - 1  # start at the top
        return self

    def __next__(self):
        """
        Called by next() — returns the next item from
        the top down. Raises StopIteration when all
        items have been visited.
        """
        if self._index < 0:
            raise StopIteration             # signals end of iteration
        item         = self._items[self._index]
        self._index -= 1                    # move down the stack
        return item


# ═══════════════════════════════════════════════════════
# USING THE CUSTOM STACK
# ═══════════════════════════════════════════════════════

# ── Build the stack ────────────────────────────────────
stack = MyStack()

stack.push("Joseph")            # bottom
stack.push("Alice")
stack.push("Bob")
stack.push("Carol")             # top

print(stack)                    # Stack(TOP → ['Carol', 'Bob', 'Alice', 'Joseph'])
print(f"Size    : {stack.size()}")      # Size    : 4
print(f"Top item: {stack.peek()}")      # Top item: Carol


# ── Manually iterate using iter() and next() ──────────
print("\nManual iteration:")
iterator = iter(stack)          # calls __iter__()

print(next(iterator))           # Carol   ← top of stack first
print(next(iterator))           # Bob
print(next(iterator))           # Alice
print(next(iterator))           # Joseph

# print(next(iterator))         # StopIteration — stack exhausted


# ── Iterate using a for loop ───────────────────────────
# A for loop calls iter() and next() automatically

print("\nFor loop iteration (LIFO order):")
for employee in stack:
    print(f"  {employee}")

# Carol    ← top
# Bob
# Alice
# Joseph   ← bottom


# ── Stack operations ───────────────────────────────────
print("\nPopping items:")
print(stack.pop())              # Carol   ← last in, first out
print(stack.pop())              # Bob
print(stack)                    # Stack(TOP → ['Alice', 'Joseph'])