from fastapi import FastAPI
from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    PlainTextResponse,
)

app = FastAPI(title="Employee API", version="1.0.0")

# -------------------------------------------------------
# FileResponse — serve a static file from disk
# -------------------------------------------------------
@app.get("/employees/logo", tags=["Responses"])
def get_logo():
    # FileResponse streams the file at the given path directly to the client.
    # media_type is inferred from the file extension automatically.
    # filename= sets the Content-Disposition header — the browser will suggest
    # this name if the user saves the file.
    return FileResponse(
        path="assets/logo.jpg",
        filename="revature-logo.jpg",
        media_type="image/jpeg" # image/png for png images
    )

# -------------------------------------------------------
# FileResponse — serve a static CSV file from disk
# -------------------------------------------------------
@app.get("/employees/data/csv", tags=["Responses"])
def download_employee_data():
    # FileResponse serves the CSV file directly from disk.
    # Content-Disposition: attachment forces the browser to download
    # the file rather than attempting to display it inline.
    # media_type="text/csv" ensures the client handles it correctly.
    return FileResponse(
        path="assets/employee_data.csv",
        filename="employee_data.csv",
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=employee_data.csv"}
    )

# -------------------------------------------------------
# HTMLResponse — return dynamically generated HTML
# -------------------------------------------------------
# Simulated employee data — would come from a database in production
employees_db = [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering", "salary": 60000},
    {"id": 2, "name": "Bob Smith",     "department": "Engineering", "salary": 55000},
    {"id": 3, "name": "Carol White",   "department": "Executive",   "salary": 95000},
]

@app.get("/employees/directory", tags=["Responses"], response_class=HTMLResponse)
def employee_directory():
    # HTMLResponse sets Content-Type: text/html automatically.
    # Use this when HTML is built dynamically at runtime from data or logic.
    # For a static .html file saved to disk, FileResponse is more appropriate.
    rows = "".join(
        f"<tr><td>{e['id']}</td><td>{e['name']}</td><td>{e['department']}</td></tr>"
        for e in employees_db
    )
    html = f"""
    <html>
        <head><title>Employee Directory</title></head>
        <body>
            <h1>Employee Directory</h1>
            <table border="1">
                <tr><th>ID</th><th>Name</th><th>Department</th></tr>
                {rows}
            </table>
        </body>
    </html>
    """
    return HTMLResponse(content=html, status_code=200)

# -------------------------------------------------------
# PlainTextResponse — return unformatted plain text
# -------------------------------------------------------
# Simulated application log entries — would be read from a real log file in production
application_logs = [
    "[2025-06-01 08:00:12] INFO     Application started successfully",
    "[2025-06-01 08:01:45] INFO     GET /employees - 200 OK - 12ms",
    "[2025-06-01 08:03:22] INFO     POST /employees - 201 Created - 18ms",
    "[2025-06-01 08:05:10] WARNING  GET /employees/99 - 404 Not Found - 8ms",
    "[2025-06-01 08:07:55] INFO     DELETE /employees/2 - 204 No Content - 14ms",
    "[2025-06-01 08:10:03] ERROR    Database connection timeout — retrying (1/3)",
    "[2025-06-01 08:10:06] ERROR    Database connection timeout — retrying (2/3)",
    "[2025-06-01 08:10:09] INFO     Database connection restored",
    "[2025-06-01 08:15:30] INFO     GET /employees - 200 OK - 11ms",
    "[2025-06-01 08:20:47] WARNING  Slow response detected: POST /employees - 342ms",
]

@app.get("/employees/logs", tags=["Responses"])
def get_application_logs():
    # PlainTextResponse sets Content-Type: text/plain automatically.
    # Useful for returning log output, health check messages, or any
    # response that should be read as raw text rather than parsed as JSON.
    # Note - for this example, the 'application_logs' is a list in this code
    # However, you could read log data from a file/database to return as
    # raw text instead - if you want to return the entire log file - use FileResponse
    return PlainTextResponse(content="\n".join(application_logs))
