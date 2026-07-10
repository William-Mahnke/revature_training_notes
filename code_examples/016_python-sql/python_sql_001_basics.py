import psycopg

# Establishing a basic connection and creating a cursor
conn = psycopg.connect("host=localhost dbname=example user=postgres password=secretpass")

# --- Default Cursor: row access by index only ---
# By default, psycopg3 returns rows as plain tuples.
# Columns must be accessed by their positional index.
cursor = conn.cursor()
# This query is the same as 'SELECT * FROM example.employees'
cursor.execute("SELECT emp_id, emp_name, emp_title, emp_salary FROM examples.employees")

row = cursor.fetchone()
print("**** "*5)
print("::: FETCH BY TUPLE INDEX :::")
print("**** "*5)
print(row[0])    # Access by index — emp_id  # pyright: ignore[reportOptionalSubscript]
print(row[1])    # Access by index — emp_name # pyright: ignore[reportOptionalSubscript]
print(row[2])    # Access by index — emp_title # pyright: ignore[reportOptionalSubscript]
print(row[3])    # Access by index — emp_salary # pyright: ignore[reportOptionalSubscript]

# --- DictCursor: row access by column name ---
# Passing row_factory=dict_row to conn.cursor() changes the row type,
# allowing columns to be accessed by name rather than index.
# This is the preferred approach for readability and maintainability.
from psycopg.rows import dict_row
print("**** "*5)
print("::: FETCH BY COLUMN NAME (dict_row) :::")
print("**** "*5)
cursor2 = conn.cursor(row_factory=dict_row)
cursor2.execute("SELECT * FROM examples.employees")

row2 = cursor2.fetchone()
print(row2["emp_id"])      # Access by column name # pyright: ignore[reportOptionalSubscript]
print(row2["emp_name"]) # pyright: ignore[reportOptionalSubscript]
print(row2["emp_title"]) # pyright: ignore[reportOptionalSubscript]
print(row2["emp_salary"]) # pyright: ignore[reportOptionalSubscript]

# # Always close your cursor and connection when done
# # (We'll see a better way to handle this with context managers)
cursor.close()
cursor2.close()
conn.close()