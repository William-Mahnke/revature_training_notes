from pydantic import BaseModel, Field

# --- Pydantic models ---

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    department: str
    salary: float = Field(gt=0)

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    salary: float
