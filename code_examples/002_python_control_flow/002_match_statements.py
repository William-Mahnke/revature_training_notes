# ═══════════════════════════════════════════════════════
# 1 — SIMPLE MATCH STATEMENT
# Matches a value against a series of patterns
# ═══════════════════════════════════════════════════════
# ── Matching integers ──────────────────────────────────
number = 3
match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")                      # matches here


day = "Monday"
match day:
    case "Monday":
        print("Start of the work week.")    # matches here
    case "Friday":
        print("End of the work week.")
    case "Saturday" | "Sunday":             # | means OR — matches either value
        print("It's the weekend!")
    case _:                                 # _ is the wildcard — matches anything
        print("It's a weekday.")

letter = 'e'
match letter:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print("Your letter is a vowel")
    case 'y':
        print("Your letter is sometimes a vowel")
    case _:
        print("Your letter is a consonant")

# ═══════════════════════════════════════════════════════
# 2 — IF-ELIF-ELSE vs MATCH STATEMENT
# Both produce identical results — match is cleaner
# when comparing one variable against many values
# ═══════════════════════════════════════════════════════

emp_title = "Manager"

# ── Using if-elif-else ─────────────────────────────────
if emp_title == "Director":
    access_level = "Full Access"
elif emp_title == "Manager":
    access_level = "Elevated Access"
elif emp_title == "Developer":
    access_level = "Standard Access"
elif emp_title == "Intern":
    access_level = "Limited Access"
else:
    access_level = "Read Only"

print(f"{emp_title} → {access_level}")      # Manager → Elevated Access


# ── Using match statement (same result, cleaner code) ──
match emp_title:
    case "Director":
        access_level = "Full Access"
    case "Manager":
        access_level = "Elevated Access"    # matches here
    case "Developer":
        access_level = "Standard Access"
    case "Intern":
        access_level = "Limited Access"
    case _:
        access_level = "Read Only"

print(f"{emp_title} → {access_level}")      # Manager → Elevated Access


# ═══════════════════════════════════════════════════════
# 3 — REAL WORLD EXAMPLE
# A simple restaurant order menu
# ═══════════════════════════════════════════════════════
def place_order(item):
    match item:
        case "burger":
            price = 8.99
            prep   = "10 minutes"
        case "pizza":
            price = 12.99
            prep   = "20 minutes"
        case "salad":
            price = 6.99
            prep   = "5 minutes"
        case "soda":
            price = 1.99
            prep   = "1 minute"
        case _:
            print(f"Sorry, '{item}' is not on the menu.")
            return

    print(f"Order  : {item.capitalize()}")
    print(f"Price  : ${price:.2f}")
    print(f"Ready in {prep}")
    print("─" * 30)


# ── Place some orders ──────────────────────────────────
place_order("burger")
place_order("soda")
place_order("hotdog")       # not on the menu
