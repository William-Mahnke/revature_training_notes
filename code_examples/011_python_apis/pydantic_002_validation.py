from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict
from typing import Optional
from enum import Enum

# --- Enum for department validation ---
class Department(str, Enum):
    ENGINEERING = "Engineering"
    EXECUTIVE   = "Executive"
    MARKETING   = "Marketing"
    FINANCE     = "Finance"

# --- This Model is used as a Nested model (see respective Employee field) ---
class Address(BaseModel):
    street: str
    city: str
    postcode: str = Field(min_length=5, max_length=10)

# --- Main model with Field() constraints and validators ---
class Employee(BaseModel):

    # model_config applies configuration at the class level
    model_config = ConfigDict(str_strip_whitespace=True)

    id: int
    name: str = Field(min_length=2, max_length=100, description="Full name of the employee")
    department: Department  # Enum field — only accepts declared department values
    salary: float = Field(gt=0, description="Annual salary in GBP — must be greater than zero")
    manager: Optional[str] = Field(default=None, description="Name of the employee's line manager")
    address: Optional[Address] = None  # Nested model — validated recursively

    # --- Field validator [See Validation Errors below]---
    # Runs after type validation — value is already a str at this point
    @field_validator("name")
    @classmethod
    def name_must_contain_space(cls, value):
        if " " not in value:
            raise ValueError("Name must include both first and last name")
        return value.title()  # Normalises capitalisation

    # --- Model validator [See Validation Errors below]---
    # Runs after all field validators — has access to the full model
    @model_validator(mode="after")
    def check_executive_salary(self):
        if self.department == Department.EXECUTIVE and self.salary < 80000:
            raise ValueError("Executive employees must have a salary of at least 80,000")
        return self

# --- Valid instantiation ---
alice = Employee(
    id=1,
    name="alice johnson",       # Normalised to "Alice Johnson" by field validator
    department="Engineering",   # Coerced to Department.ENGINEERING
    salary=60000,
    address={
        "street": "12 Baker Street",
        "city": "London",
        "postcode": "W1U 3BH"
    }
)

print(alice.name)                   # Alice Johnson
print(alice.department)             # Department.ENGINEERING
print(alice.address.city)           # London
print(alice.model_dump())

# --- Constraint violation ---

from pydantic import ValidationError


try:
    # The field_validator("name") checks if the name has a space. This doesn't - Raises Error
    invalid = Employee(id=2, name="Bob", department="Engineering", salary=55000)
except ValidationError as e:
    print(e)
    # name
    #   Value error: Name must include both first and last name

# --- Invalid enum value ---
try:
    invalid_dept = Employee(id=3, name="Carol White", department="Accounting", salary=95000)
except ValidationError as e:
    print(e)
    # department
    #   Input should be 'Engineering', 'Executive', 'Marketing' or 'Finance'

# --- Cross-field validator violation ---

try:
    # The model_validator(mode="after") checks if Executive employees have at least 80,000 salary. This does not - raises Error
    low_exec = Employee(id=4, name="David Green", department="Executive", salary=50000)
except ValidationError as e:
    print(e)
    # Value error: Executive employees must have a salary of at least 80,000

# --- model_dump() with nested model ---
carol = Employee(
    id=5,
    name="Carol White",
    department="Executive",
    salary=95000,
    address={"street": "9 Regent Street", "city": "London", "postcode": "SW1Y 4PE"}
)
print(carol.model_dump())
# {
#   'id': 5,
#   'name': 'Carol White',
#   'department': <Department.EXECUTIVE: 'Executive'>,
#   'salary': 95000.0,
#   'manager': None,
#   'address': {'street': '9 Regent Street', 'city': 'London', 'postcode': 'SW1Y 4PE'}
# }