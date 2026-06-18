from pydantic import BaseModel
from typing import Optional


# --- Pydantic Models ---
# Request model — defines the shape of incoming data
class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: int

# Response model — defines the shape of outgoing data
# Inherits all fields from EmployeeCreate and adds 'id'
class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    salary: int

# Partial update model — all fields optional for PATCH operations
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[int] = None
