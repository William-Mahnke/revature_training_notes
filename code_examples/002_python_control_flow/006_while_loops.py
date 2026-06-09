# ═══════════════════════════════════════════════════════
# 1 — WHAT IS A WHILE LOOP?
# A while loop repeats as long as its condition is True
# It checks the condition BEFORE each iteration
# ═══════════════════════════════════════════════════════

# ── Simple count up ────────────────────────────────────

count = 1

while count <= 5:
    print(count)
    count += 1              # always update the variable
                            # or the loop runs forever

# 1
# 2
# 3
# 4
# 5

# ── Simple count down ─────────────────────────────────

count = 5

while count >= 1:
    print(count)
    count -= 1

# 5
# 4
# 3
# 2
# 1

# ── What happens when the condition starts False ───────
# The loop body never executes at all

count = 10

while count <= 5:           # False immediately — count is already 10
    print(count)            # never runs
    count += 1

print("Loop skipped.")      # runs immediately

# Loop skipped.

# ═══════════════════════════════════════════════════════
# 2 — WHILE LOOP WITH IF STATEMENTS
# ═══════════════════════════════════════════════════════

# ── Label each number as even or odd ──────────────────

count = 1

while count <= 10:
    if count % 2 == 0:
        print(f"{count} — Even")
    else:
        print(f"{count} — Odd")
    count += 1

# 1 — Odd
# 2 — Even
# 3 — Odd
# 4 — Even
# 5 — Odd
# 6 — Even
# 7 — Odd
# 8 — Even
# 9 — Odd
# 10 — Even


# ═══════════════════════════════════════════════════════
# 3 — WHILE LOOP WITH break
# break exits the loop immediately when a
# condition is met, even if the while condition
# is still True
# ═══════════════════════════════════════════════════════

# ── Stop counting when a target is reached ────────────

count = 1

while count <= 10:
    if count == 6:
        print("Reached 6 — stopping.")
        break                           # exits loop immediately
    print(count)
    count += 1

# 1
# 2
# 3
# 4
# 5
# Reached 6 — stopping.               ← never printed 6, 7, 8, 9, 10


# ── Search a list and stop when found ─────────────────

employees = ["Joseph", "Alice", "Bob", "Carol"]
target    = "Bob"
index     = 0

while index < len(employees):
    if employees[index] == target:
        print(f"Found {target} at position {index}!")
        break
    print(f"Checking {employees[index]}...")
    index += 1

# Checking Joseph...
# Checking Alice...
# Found Bob at position 2!


# ═══════════════════════════════════════════════════════
# 4 — WHILE LOOP WITH continue
# continue skips the rest of the current iteration
# and jumps back to the while condition check
# ═══════════════════════════════════════════════════════

# ── Skip a specific number ────────────────────────────

count = 0

while count < 8:
    count += 1              # increment BEFORE continue
                            # or count never updates and loops forever
    if count == 4:
        continue            # skip 4
    print(count)

# 1
# 2
# 3
#                           ← 4 was skipped
# 5
# 6
# 7
# 8


# ── Skip negative values in a list ────────────────────

values = [10, -3, 25, -8, 14, -1, 30]
index  = 0

while index < len(values):
    value  = values[index]
    index += 1

    if value < 0:
        continue            # skip negatives
    print(f"Processing: {value}")

# Processing: 10
# Processing: 25
# Processing: 14
# Processing: 30