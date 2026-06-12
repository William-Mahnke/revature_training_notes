
# ═══════════════════════════════════════════════════════
# CUSTOM EXCEPTIONS
# You can create your own exception classes by inheriting
# from Exception (or any built-in exception class)
# Custom exceptions make your error handling more
# descriptive and specific to your application
# ═══════════════════════════════════════════════════════

# ── Defining custom exceptions ─────────────────────────
class InvalidAgeError(Exception):
    """Raised when an age value is outside the accepted range."""
    pass

class InvalidSalaryError(Exception):
    """Raised when a salary value is negative."""
    pass

class DuplicateEmployeeError(Exception):
    """Raised when attempting to add an employee that already exists."""
    pass


# ── Raising a custom exception with 'raise' ────────────
# 'raise' manually triggers an exception
def set_age(age):
    if age < 18 or age > 100:
        raise InvalidAgeError(f"Age {age} is not valid. Must be between 18 and 100.")
    print(f"Age set to {age}")

try:
    set_age(15)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
    # InvalidAgeError: Age 15 is not valid. Must be between 18 and 100.

try:
    set_age(30)                     # valid — no exception raised
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
# Age set to 30


# ── Using multiple custom exceptions together ──────────

existing_employees = ["Joseph", "Alice", "Bob"]

def add_employee(name, salary):
    if name in existing_employees:
        raise DuplicateEmployeeError(f"'{name}' already exists.")
    if salary < 0:
        raise InvalidSalaryError(f"Salary cannot be negative. Got: {salary}")
    existing_employees.append(name)
    print(f"✔ Employee '{name}' added with salary ${salary:,.2f}")

# ── Valid employee ─────────────────────────────────────
try:
    add_employee("Carol", 55000)
except DuplicateEmployeeError as e:
    print(f"DuplicateEmployeeError: {e}")
except InvalidSalaryError as e:
    print(f"InvalidSalaryError: {e}")
# ✔ Employee 'Carol' added with salary $55,000.00

# ── Duplicate employee ─────────────────────────────────
try:
    add_employee("Joseph", 60000)
except DuplicateEmployeeError as e:
    print(f"DuplicateEmployeeError: {e}")
except InvalidSalaryError as e:
    print(f"InvalidSalaryError: {e}")
# DuplicateEmployeeError: 'Joseph' already exists.

# ── Invalid salary ─────────────────────────────────────
try:
    add_employee("Dave", -500)
except DuplicateEmployeeError as e:
    print(f"DuplicateEmployeeError: {e}")
except InvalidSalaryError as e:
    print(f"InvalidSalaryError: {e}")
# InvalidSalaryError: Salary cannot be negative. Got: -500


# ── Custom exception with extra attributes ─────────────
# You can override __init__ to store additional context

class InvalidSalaryError(Exception):
    """Raised when a salary value is invalid."""

    def __init__(self, salary, message="Salary must be a positive number."):
        self.salary  = salary
        self.message = message
        super().__init__(f"{message} Got: {salary}")

try:
    raise InvalidSalaryError(-500)
except InvalidSalaryError as e:
    print(f"Error    : {e}")
    print(f"Bad value: {e.salary}")

# Error    : Salary must be a positive number. Got: -500
# Bad value: -500