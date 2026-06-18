from fastapi import FastAPI, HTTPException
from typing import Optional
from fastapi_002_models import EmployeeCreate, EmployeeResponse, EmployeeUpdate

app = FastAPI(title="Employee API", version="1.0.0")

# Simulated in-memory data store
employees_db = [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering", "salary": 60000},
    {"id": 2, "name": "Bob Smith",     "department": "Engineering", "salary": 55000},
    {"id": 3, "name": "Carol White",   "department": "Executive",   "salary": 95000},
]

# --- GET: Retrieve all employees ---
# Optional query parameter — filters by department if provided
# Example: GET /employees?department=Engineering
@app.get("/employees", tags=["Employees"])
def get_employees(department: Optional[str] = None):
    if department:
        return [e for e in employees_db if e["department"] == department]
    return employees_db

# --- GET: Retrieve a single employee by ID ---
# HTTPException raises a structured error response with the correct status code
# Example: GET /employees/1
@app.get("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def get_employee(employee_id: int):
    for employee in employees_db:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail=f"Employee with ID {employee_id} not found")

# --- POST: Create a new employee ---
# response_model filters the response to only include fields on EmployeeResponse
# status_code=201 signals that a new resource was successfully created
# Example: POST /employees
@app.post("/employees", response_model=EmployeeResponse, status_code=201, tags=["Employees"])
def create_employee(employee: EmployeeCreate):
    new_employee = {
        "id": len(employees_db) + 1,
        "name": employee.name,
        "department": employee.department,
        "salary": employee.salary
    }
    employees_db.append(new_employee)
    return new_employee

# --- PUT: Replace an employee record entirely ---
# All fields required — represents a full replacement of the resource
# Example: PUT /employees/1
@app.put("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def update_employee(employee_id: int, employee: EmployeeCreate):
    for index, existing in enumerate(employees_db):
        if existing["id"] == employee_id:
            updated = {"id": employee_id, **employee.model_dump()}
            employees_db[index] = updated
            return updated
    raise HTTPException(status_code=404, detail=f"Employee with ID {employee_id} not found")

# --- PATCH: Partially update an employee record ---
# Only supplied fields are updated — None values are ignored
# Example: PATCH /employees/1
@app.patch("/employees/{employee_id}", response_model=EmployeeResponse, tags=["Employees"])
def partial_update_employee(employee_id: int, employee: EmployeeUpdate):
    for index, existing in enumerate(employees_db):
        if existing["id"] == employee_id:
            updated_fields = employee.model_dump(exclude_none=True)
            employees_db[index].update(updated_fields)
            return