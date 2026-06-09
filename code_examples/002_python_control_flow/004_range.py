# ═══════════════════════════════════════════════════════
# 1 — WHAT IS range()?
# range() generates a sequence of numbers
# It takes up to 3 arguments: start, stop, step
# ═══════════════════════════════════════════════════════

# ── range(stop) ────────────────────────────────────────
# Starts at 0 by default, stops BEFORE the stop value

print ( range(5) )

print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(10)))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── range(start, stop) ─────────────────────────────────
# Starts at 'start', stops BEFORE 'stop'

print(list(range(1, 6)))        # [1, 2, 3, 4, 5]
print(list(range(5, 11)))       # [5, 6, 7, 8, 9, 10]

# ── range(start, stop, step) ───────────────────────────
# 'step' controls the increment between each number

print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]      — evens
print(list(range(1, 10, 2)))    # [1, 3, 5, 7, 9]      — odds
print(list(range(0, 11, 5)))    # [0, 5, 10]            — fives
print(list(range(10, 0, -1)))   # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] — countdown


# ═══════════════════════════════════════════════════════
# 2 — SIMPLE FOR LOOP WITH range()
# ═══════════════════════════════════════════════════════

# ── Count up from 0 to 4 ─────────────────────────────────
for i in range(5):
    print(i)

# 0
# 1
# 2
# 3
# 4

# ── Count down from 5 to 1 ─────────────────────────────────────────
for i in range(5, 0, -1):
    print(i)

# 5
# 4
# 3
# 2
# 1

# ═══════════════════════════════════════════════════════
# 3 — USING range() WITH IF-ELSE LOGIC
# ═══════════════════════════════════════════════════════

# ── Print even and odd numbers from 1 to 10 ───────────
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} — Even")
    else:
        print(f"{i} — Odd")

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


# ── Assign a grade to each score in a list ────────────
scores = [92, 85, 55, 78, 40, 90]

for i in range(len(scores)):
    score = scores[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Score {i + 1}: {score}  →  Grade: {grade}")

# Score 1: 92  →  Grade: A
# Score 2: 85  →  Grade: B
# Score 3: 55  →  Grade: F
# Score 4: 78  →  Grade: C
# Score 5: 40  →  Grade: F
# Score 6: 90  →  Grade: A


# ═══════════════════════════════════════════════════════
# 4 — BUILDING A MULTIPLICATION TABLE
# Nested for loops with range()
# The inner loop runs fully for each iteration
# of the outer loop
# ═══════════════════════════════════════════════════════

table_num = 5

print(f"Multiplication Table for {table_num}:")
print("─" * 30)

for i in range(1, 11):
    result = table_num * i
    print(f"  {table_num} x {i:<3} = {result}")

# Multiplication Table for 5:
# ──────────────────────────────
#   5 x 1   = 5
#   5 x 2   = 10
#   5 x 3   = 15
#   5 x 4   = 20
#   5 x 5   = 25
#   5 x 6   = 30
#   5 x 7   = 35
#   5 x 8   = 40
#   5 x 9   = 45
#   5 x 10  = 50