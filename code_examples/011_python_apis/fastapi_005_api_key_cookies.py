from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.security import APIKeyHeader, APIKeyQuery
from starlette import status

app = FastAPI(title="Employee API", version="1.0.0")

# -------------------------------------------------------
# API Key Authentication
# -------------------------------------------------------

VALID_API_KEY = "super-secret-employee-key-2026"

# RECOMMENDED — APIKeyHeader extracts the key from a named request header.
# Headers are not stored in server logs or browser history, keeping the key private.
# auto_error=True means FastAPI raises 403 automatically if the header is absent.
# To test in Swagger UI: click the padlock icon and enter the key there.
# To test manually: include the header "X-Api-Key: super-secret-employee-key-2025"
api_key_header = APIKeyHeader(name="X-Api-Key", auto_error=True)

# DISCOURAGED — APIKeyQuery extracts the key from a URL query parameter.
# Example request: GET /reports?api_key=super-secret-employee-key-2025
# The full URL (including the key) may be written to server logs, stored in browser
# history, and captured by proxies — the key is far more likely to be exposed.
# Shown here for awareness only — avoid this pattern in production.
api_key_query = APIKeyQuery(name="api_key", auto_error=False)

# --- Recommended: header-based API key dependency ---
def verify_api_key_header(api_key: str = Depends(api_key_header)) -> str:
    if api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )
    return api_key

# --- Discouraged: query parameter API key dependency ---
# Included for awareness — do not use this pattern in new APIs.
# auto_error=False means a missing key returns None rather than raising
# immediately, so we handle the invalid/missing case ourselves.
def verify_api_key_query(api_key: str = Depends(api_key_query)) -> str:
    if not api_key or api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing API key"
        )
    return api_key

# Protected via header — the recommended approach
@app.get("/employees", tags=["API Key Auth"])
def get_employees(api_key: str = Depends(verify_api_key_header)):
    return {"employees": [], "authenticated_via": "header"}

# Protected via query parameter — shown for awareness, not recommended
# Example: GET /reports?api_key=super-secret-employee-key-2025
@app.get("/reports", tags=["API Key Auth"])
def get_reports(api_key: str = Depends(verify_api_key_query)):
    return {"reports": [], "authenticated_via": "query_param — avoid in production"}

# -------------------------------------------------------
# Cookies & Sessions
# -------------------------------------------------------

# Simulated session store — in production this would be a database
# or Redis instance storing session data server-side.
SESSIONS: dict = {}

# --- Set a cookie (login) ---
# The Response object is injected by FastAPI — adding it as a parameter
# does not change the route's return value; FastAPI handles it separately.
@app.post("/login", tags=["Cookies"])
def login(response: Response, username: str, password: str):
    # Simplified credential check — replace with real validation in production
    if username == "alice" and password == "password123":
        session_token = f"session-{username}-token-abc123"

        # Store session data server-side keyed by the token.
        # The cookie only holds the token — not the session data itself.
        # This means sensitive data never travels to the client.
        SESSIONS[session_token] = {"username": username, "role": "admin"}

        # Set the session cookie on the response.
        # httponly=True  — JavaScript cannot read this cookie (XSS protection).
        # max_age=15   — cookie expires after 15 seconds (typically something like 3600 seconds - 1 hour is used).
        # samesite="lax" — cookie is not sent on cross-site requests (CSRF protection).
        response.set_cookie(
            key="session_token",
            value=session_token,
            httponly=True,
            max_age=15,
            samesite="lax"
        )
        return {"message": f"Welcome {username}, session started."}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )

# --- Read a cookie (access a protected page) ---
# The Request object gives access to all incoming cookies via request.cookies.
@app.get("/dashboard", tags=["Cookies"])
def dashboard(request: Request):
    # Retrieve the session token from the incoming cookies
    session_token = request.cookies.get("session_token")

    if not session_token or session_token not in SESSIONS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No valid session found — please log in"
        )

    # Look up the session data server-side using the token as the key
    session_data = SESSIONS[session_token]
    return {
        "message": f"Welcome back {session_data['username']}",
        "role": session_data["role"]
    }

# --- Clear a cookie (logout) ---
# delete_cookie() sets the cookie's max_age to 0, expiring it immediately
# on the client side. We also remove the session from the server-side store.
@app.post("/logout", tags=["Cookies"])
def logout(request: Request, response: Response):
    session_token = request.cookies.get("session_token")

    # Remove the session from the server-side store if it exists
    if session_token and session_token in SESSIONS:
        del SESSIONS[session_token]

    # Expire the cookie on the client side
    response.delete_cookie(key="session_token")
    return {"message": "Logged out successfully"}