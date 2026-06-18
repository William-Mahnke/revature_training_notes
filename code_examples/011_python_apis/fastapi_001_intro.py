# Install dependencies (run in terminal):
# 1. create a virtual environment (python -m vevn env_name)
# 2. activate the virtual environment (env_name\Scripts\activate)
# 3. install fast api (pip install fastapi uvicorn)
from fastapi import FastAPI

# Create the FastAPI application instance
app = FastAPI(
    title="Employee API",
    description="A simple API for managing employee records.",
    version="1.0.0"
)

# A basic (synchronous) route to confirm the app is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee API"}

# Run the application with uvicorn (run in terminal):
# uvicorn <name_of_file>:app --reload
#
# For this file, the command is:
# uvicorn fastapi_001_intro:app --reload
#
# typically this should be one of the following: 
# uvicorn main:app       # file is main.py
# uvicorn app:app        # file is app.py
# uvicorn server:app     # file is server.py
#
# --reload flag watches for file changes and restarts automatically
#
# Once running, visit:
#   http://127.0.0.1:8000       → root endpoint
#   http://127.0.0.1:8000/docs  → Swagger UI (interactive documentation)
#   http://127.0.0.1:8000/redoc → ReDoc (alternative documentation view)

# --- Asynchronous Route ---

# async def allows FastAPI to handle other requests while this one is awaiting I/O
@app.get("/status")
async def get_status():
    return {"status": "running", "version": "1.0.0"}

# --- Routes with basic metadata ---

# tags group routes together in the Swagger UI documentation
@app.get("/employees", tags=["Employees"])
def get_employees():
    return {"employees": []}

@app.post("/employees", tags=["Employees"])
def create_employee():
    return {"message": "Employee created"}