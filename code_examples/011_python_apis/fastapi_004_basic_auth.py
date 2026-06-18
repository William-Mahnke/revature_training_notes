import secrets
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

app = FastAPI(title="Employee API", version="1.0.0")

# HTTPBasic reads the Authorization header, decodes the Base64 credentials,
# and injects them as an HTTPBasicCredentials object (with .username and .password).
# FastAPI adds a padlock icon in Swagger UI (/docs) for any route that uses this —
# clicking it opens a username/password prompt so you can test without
# constructing the Authorization header manually.
security = HTTPBasic()

# Simulated user store — in production this would be a database
# lookup with properly hashed passwords (e.g. using bcrypt).
USERS = {
    "alice": "password123",
    "bob":   "securepass"
}

# -------------------------------------------------------
# The wrong way — using == for credential comparison
# -------------------------------------------------------

# Depends() - Built-in FastAPI function for injecting dependencies
def get_current_user_unsafe(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    stored_password = USERS.get(credentials.username)

    # This works correctly in terms of logic — but == short-circuits,
    # meaning it stops comparing at the first character that differs.
    # An attacker measuring response times across thousands of requests
    # can exploit this to guess the password character by character.
    if stored_password is None or credentials.password != stored_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentials.username

# -------------------------------------------------------
# The correct way — using secrets.compare_digest()
# -------------------------------------------------------

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    stored_password = USERS.get(credentials.username, "")
    # If the username does not exist, .get() returns "" so that
    # compare_digest still runs — this prevents an attacker from
    # detecting valid usernames by observing faster rejection times.

    # secrets.compare_digest() always takes the same time regardless
    # of where the two strings differ — timing measurement is useless.
    # encode("utf-8") is required because compare_digest expects bytes.
    password_correct = secrets.compare_digest(
        credentials.password.encode("utf-8"),
        stored_password.encode("utf-8")
    )

    if not password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"}
        )

    return credentials.username

# -------------------------------------------------------
# Protected routes
# -------------------------------------------------------

# Depends(get_current_user) runs the authentication dependency first.
# If credentials are invalid it raises 401 and the handler never runs.
# If credentials are valid the authenticated username is injected.
@app.get("/employees/me", tags=["Auth"])
def get_my_profile(username: str = Depends(get_current_user)):
    return {
        "username": username,
        "message": f"Hello {username}, you are authenticated."
    }

@app.get("/employees", tags=["Auth"])
def get_employees(username: str = Depends(get_current_user)):
    return {"employees": [], "requested_by": username}

# Unprotected route — no Depends() on get_current_user,
# so no credentials are required to reach this endpoint.
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Employee API"}