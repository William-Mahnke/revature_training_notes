# ================================================
# This example brings together many of the ideas
# we have covered, and adds some extra, good
# practice tools such as:
#   - Pagination
#   - Custom exceptions
#   - Logging
#   - API Key Authentication
#   - Cookies (set on successful authentication)
#   - Non-JSON responses (CSV file download)
#
# Review this code to better understand valid
# architecture for a REST API in Python using FastAPI
#
# Project structure:
#   root/
#   ├── app.py
#   ├── exceptions/app_exceptions.py
#   ├── models/employee_models.py
#   ├── util/app_util.py
#   └── assets/employee_data.csv
# ================================================
import logging
from fastapi import FastAPI, Depends
from fastapi.requests import Request
from fastapi.responses import JSONResponse, FileResponse
from fastapi.security import APIKeyHeader
from starlette import status
from typing import Optional
from fastapi.responses import JSONResponse as _JSONResponse
# Import our models
from models.employee_models import EmployeeCreate, EmployeeResponse

# Import our exceptions
from exceptions.app_exceptions import (
    EmployeeNotFoundException,
    InvalidDepartmentException,
    InvalidAPIKeyException
)

# Import our constants
from util.app_util import VALID_DEPARTMENTS, VALID_API_KEY

# -------------------------------------------------------
# Logging Setup
# -------------------------------------------------------

# basicConfig sets up the root logger with a format and level.
# Every log message will include the timestamp, log level, and message text.
# Level INFO means INFO, WARNING, and ERROR messages are all captured.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# getLogger(__name__) creates a logger named after this module.
# Using __name__ is best practice — it makes it easy to identify
# which module produced a log entry in larger applications.
logger = logging.getLogger(__name__)

# -------------------------------------------------------
# App Instance
# -------------------------------------------------------

app = FastAPI(title="Employee API", version="1.0.0")

# -------------------------------------------------------
# In-memory data store
# -------------------------------------------------------

employees_db = [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering", "salary": 60000},
    {"id": 2, "name": "Bob Smith",     "department": "Engineering", "salary": 55000},
    {"id": 3, "name": "Carol White",   "department": "Executive",   "salary": 95000},
    {"id": 4, "name": "David Green",   "department": "Marketing",   "salary": 48000},
    {"id": 5, "name": "Emma Davis",    "department": "Finance",     "salary": 52000},
]

# -------------------------------------------------------
# API Key Authentication
# -------------------------------------------------------

# APIKeyHeader extracts the value of the "X-Api-Key" header from incoming requests.
# auto_error=False means FastAPI will not raise automatically if the header is
# missing — we handle the missing/invalid case ourselves in verify_api_key()
# so we can raise our own custom exception and set the cookie on success.
api_key_header = APIKeyHeader(name="X-Api-Key", auto_error=False)

def verify_api_key(request: Request, api_key: str = Depends(api_key_header)) -> str:
    # If the header is missing or the key is wrong, raise our custom exception.
    # The registered handler below converts this into a structured 403 response.
    if not api_key or api_key != VALID_API_KEY:
        logger.warning(f"Failed API key attempt — path: {request.url.path}")
        raise InvalidAPIKeyException()

    logger.info(f"API key validated — path: {request.url.path}")
    return api_key

# -------------------------------------------------------
# Custom Exception Handlers
# -------------------------------------------------------

# Registered with @app.exception_handler() — intercepts the named exception
# type anywhere it is raised in the application and returns a consistent
# JSON response in a standard error envelope.
@app.exception_handler(EmployeeNotFoundException)
async def employee_not_found_handler(request: Request, exc: EmployeeNotFoundException):
    logger.warning(f"Employee not found — ID: {exc.employee_id}")
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": {
                "code": status.HTTP_404_NOT_FOUND,
                "type": "EmployeeNotFound",
                "message": exc.message
            }
        }
    )

@app.exception_handler(InvalidDepartmentException)
async def invalid_department_handler(request: Request, exc: InvalidDepartmentException):
    logger.warning(f"Invalid department supplied — department: '{exc.department}'")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": {
                "code": status.HTTP_400_BAD_REQUEST,
                "type": "InvalidDepartment",
                "message": exc.message
            }
        }
    )

@app.exception_handler(InvalidAPIKeyException)
async def invalid_api_key_handler(request: Request, exc: InvalidAPIKeyException):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "error": {
                "code": status.HTTP_403_FORBIDDEN,
                "type": "InvalidAPIKey",
                "message": exc.message
            }
        }
    )

# -------------------------------------------------------
# Helper function
# -------------------------------------------------------
def find_employee(employee_id: int) -> dict:
    for employee in employees_db:
        if employee["id"] == employee_id:
            return employee
    raise EmployeeNotFoundException(employee_id)

# -------------------------------------------------------
# Authentication Route
# -------------------------------------------------------
# POST /auth — validates the API key and sets a session cookie on success.
# This is the entry point for clients — they call this first, receive a cookie,
# and the browser/client then includes that cookie on subsequent requests.
# The cookie is used here as a lightweight session marker alongside the key.
@app.post("/auth", tags=["Auth"])
def authenticate(request: Request, response: JSONResponse = None, api_key: str = Depends(verify_api_key) ):
    logger.info("Authentication successful — session cookie issued")

    # Build the response manually so we can attach the cookie to it.
    # We set the cookie here rather than in verify_api_key because
    # only a Response object can set cookies, not a plain dependency.
    resp = _JSONResponse(
        content={"message": "Authenticated successfully. Session cookie set."},
        status_code=status.HTTP_200_OK
    )

    # Set the session cookie on the response.
    # httponly=True  — JavaScript cannot read this cookie (XSS protection).
    # max_age=3600   — cookie expires after 1 hour.
    # samesite="lax" — not sent on cross-site requests (CSRF protection).
    resp.set_cookie(
        key="session",
        value="authenticated",
        httponly=True,
        max_age=3600,
        samesite="lax"
    )
    return resp

# -------------------------------------------------------
# Cookie validation helper
# -------------------------------------------------------

def require_session(request: Request):
    # Reads the session cookie set by POST /auth.
    # Any route that depends on this will be blocked if the
    # cookie is absent — the client must authenticate first.
    session = request.cookies.get("session")
    if not session or session != "authenticated":
        logger.warning(f"Request without valid session cookie — path: {request.url.path}")
        raise InvalidAPIKeyException()

# -------------------------------------------------------
# Routes
# -------------------------------------------------------
# --- GET: Retrieve all employees with pagination ---
# Requires a valid session cookie (set via POST /auth).
# skip and limit are plain function arguments — FastAPI treats
# them as query parameters automatically.
# Example: GET /employees?skip=0&limit=3
# Example: GET /employees?department=Engineering&skip=0&limit=10
@app.get(
    "/employees",
    response_model=list[EmployeeResponse],
    status_code=status.HTTP_200_OK,
    tags=["Employees"]
)
def get_employees(request: Request, department: Optional[str] = None, skip: int  = 0, limit: int = 5, _session = Depends(require_session)):
    logger.info(f"GET /employees — department: {department}, skip: {skip}, limit: {limit}")

    if department and department not in VALID_DEPARTMENTS:
        raise InvalidDepartmentException(department)

    results = employees_db
    if department:
        results = [e for e in results if e["department"] == department]

    # Apply pagination — slice the results list using skip and limit
    return results[skip: skip + limit]

# --- GET: Retrieve a single employee by ID ---
# Raises EmployeeNotFoundException if not found — handled by the registered handler.
@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
    tags=["Employees"]
)
def get_employee(employee_id: int, _session = Depends(require_session)):
    logger.info(f"GET /employees/{employee_id}")
    return find_employee(employee_id)

# --- POST: Create a new employee ---
@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Employees"]
)
def create_employee(employee: EmployeeCreate, _session = Depends(require_session) ):
    if employee.department not in VALID_DEPARTMENTS:
        raise InvalidDepartmentException(employee.department)

    new_employee = {
        "id": len(employees_db) + 1,
        **employee.model_dump()
    }
    employees_db.append(new_employee)
    logger.info(f"POST /employees — created employee ID: {new_employee['id']} ({new_employee['name']})")
    return new_employee

# --- DELETE: Remove an employee ---
@app.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Employees"]
)
def delete_employee(
    employee_id: int,
    _session = Depends(require_session)
):
    for index, employee in enumerate(employees_db):
        if employee["id"] == employee_id:
            employees_db.pop(index)
            logger.info(f"DELETE /employees/{employee_id} — employee removed")
            return
    raise EmployeeNotFoundException(employee_id)

# --- GET: Download employee data as a CSV file ---
# Returns the CSV from the assets directory as a file download.
# Does not require authentication — treated as a public data export.
@app.get(
    "/employees/export/csv",
    tags=["Employees"]
)
def download_employee_csv():
    logger.info("GET /employees/export/csv — CSV download requested")

    # FileResponse streams the file from disk directly to the client.
    # media_type="text/csv" ensures the client handles the content correctly.
    # Content-Disposition: attachment tells the browser to download the
    # file rather than attempting to display it inline.
    return FileResponse(
        path="assets/employee_data.csv",
        filename="employee_data.csv",
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=employee_data.csv"}
    )
