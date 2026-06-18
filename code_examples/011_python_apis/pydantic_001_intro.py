from pydantic import BaseModel, ValidationError
from typing import Optional # Optional indicates that the variable might have a type, or be a None type

# --- Define a basic Pydantic model using BaseModel superclass ---
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float
    manager: Optional[str] = None  # Optional field with a default of None

# --- Valid instantiation ---

alice = Employee(id=1, name="Alice Johnson", department="Engineering", salary=60000)
print(alice)
# id=1 name='Alice Johnson' department='Engineering' salary=60000.0 manager=None

# --- Type coercion ---
# Pydantic coerces compatible types where possible
# Here, id is passed as a string "2" — Pydantic converts it to int 2
bob = Employee(id="2", name="Bob Smith", department="Engineering", salary=55000)
print(bob.id)        # 2
print(type(bob.id))  # <class 'int'>

# --- ValidationError ---
# Raised when data cannot be coerced or is missing entirely
try:
    invalid = Employee(id="one", name="Carol", department="Executive", salary=95000)
except ValidationError as e:
    print(e)
    # 1 validation error for Employee
    # id
    #   Input should be a valid integer, unable to parse string as an integer

# --- Missing required field ---
try:
    missing_field = Employee(id=3, department="Executive", salary=95000)
except ValidationError as e:
    print(e)
    # 1 validation error for Employee
    # name
    #   Field required

# --- model_dump() --- serialises the model to a plain Python dictionary
print(alice.model_dump())
# {'id': 1, 'name': 'Alice Johnson', 'department': 'Engineering', 'salary': 60000.0, 'manager': None}

# --- model_dump_json() --- serialises the model directly to a JSON string
print(alice.model_dump_json())
# {"id":1,"name":"Alice Johnson","department":"Engineering","salary":60000.0,"manager":null}

# --- Accessing fields ---
print(alice.name)        # Alice Johnson
print(alice.salary)      # 60000.0