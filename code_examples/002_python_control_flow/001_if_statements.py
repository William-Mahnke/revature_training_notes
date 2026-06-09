# ═══════════════════════════════════════════════════════
# 1 — IF STATEMENT (by itself)
# The block inside only runs if the condition is True
# Code AFTER the if-statement always runs regardless
# ═══════════════════════════════════════════════════════

age = 20

if age >= 18:
    print("You are an adult.")      # runs — condition is True

print("This always runs.")          # always runs — outside the if block


# ── What happens when the condition is False ───────────

age = 15

if age >= 18:
    print("You are an adult.")      # skipped — condition is False

print("This always runs.")          # always runs — outside the if block


# ── Multiple if statements (each evaluated independently)
score = 85

if score >= 70:
    print("You passed.")            # runs

if score >= 80:
    print("You got a B.")           # runs — each if is checked separately

if score >= 90:
    print("You got an A.")          # skipped — condition is False

print("Evaluation complete.")       # always runs


# ═══════════════════════════════════════════════════════
# 2 — IF-ELSE STATEMENT
# The 'else' block runs when the if condition is False
# One or the other always runs — never both, never neither
# ═══════════════════════════════════════════════════════

age = 20

if age >= 18:
    print("You are an adult.")      # runs — condition is True
else:
    print("You are a minor.")       # skipped


# ── Condition is False ─────────────────────────────────

age = 15

if age >= 18:
    print("You are an adult.")      # skipped — condition is False
else:
    print("You are a minor.")       # runs


# ── Real world example ─────────────────────────────────

is_logged_in = False

if is_logged_in:
    print("Welcome back!")          # skipped
else:
    print("Please log in.")         # runs

print("Page loaded.")               # always runs


# ═══════════════════════════════════════════════════════
# 3 — IF-ELIF-ELSE STATEMENT
# Use elif to check multiple conditions in sequence
# Python stops checking as soon as one condition is True
# The else block is a catch-all if nothing matched
# ═══════════════════════════════════════════════════════

score = 85

if score >= 90:
    print("Grade: A")               # skipped — 85 is not >= 90
elif score >= 80:
    print("Grade: B")               # runs — 85 is >= 80, stops here
elif score >= 70:
    print("Grade: C")               # skipped — already matched above
elif score >= 60:
    print("Grade: D")               # skipped — already matched above
else:
    print("Grade: F")               # skipped — already matched above

print("Grading complete.")          # always runs


# ── Why order matters ──────────────────────────────────
# Python stops at the FIRST True condition
# so always order from most specific to least specific

score = 95

# Wrong order — will print "You passed" instead of "Perfect score"
if score >= 60:
    print("You passed.")            # matches first and stops here
elif score == 100:
    print("Perfect score!")         # never reached

# Correct order — most specific condition first
if score == 100:
    print("Perfect score!")         # skipped — 95 is not 100
elif score >= 90:
    print("Excellent!")             # matches here
elif score >= 60:
    print("You passed.")            # skipped — already matched above


# ── Real world example ─────────────────────────────────
emp_title = "Manager"

if emp_title == "Director":
    access_level = "Full Access"
elif emp_title == "Manager":
    access_level = "Elevated Access"
elif emp_title == "Developer":
    access_level = "Standard Access"
else:
    access_level = "Read Only"      # catch-all for any unrecognized title

print(f"{emp_title} → {access_level}")     # Manager → Elevated Access
