from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory data store
employees_db = [
    {"id": 1, "name": "Alice Johnson", "department": "Engineering", "salary": 60000},
    {"id": 2, "name": "Bob Smith",     "department": "Engineering", "salary": 55000},
    {"id": 3, "name": "Carol White",   "department": "Executive",   "salary": 95000},
]

def find_employee(employee_id):
    for employee in employees_db:
        if employee["id"] == employee_id:
            return employee
    abort(404, description=f"Employee with ID {employee_id} not found")

# --- GET: Retrieve all employees ---
# Query parameter accessed via request.args
@app.route("/employees", methods=["GET"])
def get_employees():
    department = request.args.get("department")
    if department:
        return jsonify([e for e in employees_db if e["department"] == department])
    return jsonify(employees_db)

# --- GET: Retrieve a single employee ---
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    return jsonify(find_employee(employee_id))

# --- POST: Create a new employee ---
# Request body accessed via request.json — no automatic validation
@app.route("/employees", methods=["POST"])
def create_employee():
    data = request.json
    if not data or not all(k in data for k in ("name", "department", "salary")):
        abort(400, description="Missing required fields: name, department, salary")
    new_employee = {
        "id": len(employees_db) + 1,
        "name": data["name"],
        "department": data["department"],
        "salary": data["salary"]
    }
    employees_db.append(new_employee)
    return jsonify(new_employee), 201

# --- PUT: Replace an employee record entirely ---
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    employee = find_employee(employee_id)
    data = request.json
    if not data or not all(k in data for k in ("name", "department", "salary")):
        abort(400, description="Missing required fields: name, department, salary")
    employee.update({"name": data["name"], "department": data["department"], "salary": data["salary"]})
    return jsonify(employee)

# --- PATCH: Partially update an employee ---
@app.route("/employees/<int:employee_id>", methods=["PATCH"])
def partial_update_employee(employee_id):
    employee = find_employee(employee_id)
    data = request.json
    for field in ("name", "department", "salary"):
        if field in data:
            employee[field] = data[field]
    return jsonify(employee)

# --- DELETE: Remove an employee ---
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    for index, employee in enumerate(employees_db):
        if employee["id"] == employee_id:
            employees_db.pop(index)
            return "", 204
    abort(404, description=f"Employee with ID {employee_id} not found")

if __name__ == "__main__":
    app.run(debug=True)