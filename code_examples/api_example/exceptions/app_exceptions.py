# -------------------------------------------------------
# Custom Exceptions
# -------------------------------------------------------

# Custom exception classes carry domain-specific context.
# They are plain Python classes — no FastAPI-specific logic here.
# Exception handlers in app.py intercept these and return
# a consistent JSON error envelope to the client.

class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id: int):
        self.employee_id = employee_id
        self.message = f"Employee with ID {employee_id} not found"

class InvalidDepartmentException(Exception):
    def __init__(self, department: str):
        self.department = department
        self.message = f"'{department}' is not a valid department"

class InvalidAPIKeyException(Exception):
    def __init__(self):
        self.message = "Invalid or missing API key"
