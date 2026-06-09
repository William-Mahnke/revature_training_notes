# ═══════════════════════════════════════════════════════
# 1 — WHAT ARE break AND continue?
#
# break    — exits the loop immediately and completely
# continue — skips the rest of the current iteration
#            and moves to the next one
# ═══════════════════════════════════════════════════════

# ── break — stops the loop entirely ───────────────────

for i in range(1, 6):
    if i == 3:
        break                   # exits the loop when i == 3
    print(i)

print("Loop ended.")

# 1
# 2
# Loop ended.                   ← loop stopped at 3, never reached 4 or 5


# ── continue — skips current iteration ────────────────
for i in range(1, 6):
    if i == 3:
        continue                # skips the rest of this iteration when i == 3
    print(i)

print("Loop ended.")

# 1
# 2
#                               ← 3 was skipped
# 4
# 5
# Loop ended.                   ← loop still completed fully


# ═══════════════════════════════════════════════════════
# 2 — break AND continue WITH LISTS
# ═══════════════════════════════════════════════════════

# ── break — stop searching once item is found ─────────

employees = ["Joseph", "Alice", "Bob", "Carol", "Dave"]
search    = "Bob"

for emp in employees:
    if emp == search:
        print(f"Found {search}!")
        break                   # no need to keep searching
    print(f"Checking {emp}...")

# Checking Joseph...
# Checking Alice...
# Found Bob!                    ← stopped here, Carol and Dave never checked


# ── continue — skip certain items ─────────────────────

scores = [85, -1, 92, -1, 78, 55, -1, 90]
# -1 represents a missing score

for score in scores:
    if score == -1:
        continue                # skip missing scores
    print(f"Score: {score}")

# Score: 85
# Score: 92                     ← -1 entries were skipped
# Score: 78
# Score: 55
# Score: 90


# ═══════════════════════════════════════════════════════
# 3 — break AND continue WITH IF-ELSE
# ═══════════════════════════════════════════════════════

# ── continue — skip failed scores, process passed ones ─

scores = [85, 40, 92, 55, 78, 90]

print("Passed Scores:")
for score in scores:
    if score < 70:
        continue                # skip failures
    else:
        print(f"  {score}")

# Passed Scores:
#   85
#   92
#   78
#   90


# ── break — stop processing if a critical value found ──

scores = [85, 92, 78, -999, 90, 55]
# -999 represents corrupted data

print("Processing scores:")
for score in scores:
    if score == -999:
        print("Corrupted data found — stopping.")
        break
    else:
        print(f"  Processing score: {score}")

# Processing scores:
#   Processing score: 85
#   Processing score: 92
#   Processing score: 78

# ═══════════════════════════════════════════════════════
# 4 — break AND continue WITH MATCH STATEMENTS
# ═══════════════════════════════════════════════════════

# ── continue — skip certain order statuses ────────────

orders = ["shipped", "cancelled", "delivered", "pending", "cancelled", "shipped"]

print("Active Orders:")
for order in orders:
    match order:
        case "cancelled":
            continue            # skip cancelled orders
        case "delivered":
            continue            # skip already delivered orders
        case _:
            print(f"{order.capitalize()}")

# Active Orders:
#   Shipped
#   Pending
#   Shipped


# ── break — stop processing on a critical status ───────

orders = ["shipped", "pending", "error", "delivered", "shipped"]

print("Processing Orders:")
for order in orders:
    match order:
        case "error":
            print("Error detected — halting all processing.")
            break
        case "shipped":
            print(f"Order is on its way.")
        case "pending":
            print(f"Order is pending.")
        case "delivered":
            print(f"Order delivered.")

# Processing Orders:
# Order is on its way.
# Order is pending.
# Error detected — halting all processing.