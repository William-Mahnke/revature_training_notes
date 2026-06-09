# ═══════════════════════════════════════════════════════
# WHAT IS A DICTIONARY?
# A dictionary is an ordered collection of KEY:VALUE pairs
# Keys must be unique and immutable
# Values can be any data type
# Defined using curly braces {}
# ═══════════════════════════════════════════════════════
# 1 — SIMPLE DICTIONARY CREATION
# ═══════════════════════════════════════════════════════

# ── Empty dictionary ───────────────────────────────────
empty_dict = {}

# ── Basic dictionary ───────────────────────────────────
employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer",
    "is_active" : True
}

print(employee)
# {'emp_id': 100, 'emp_name': 'Joseph', 'emp_title': 'Developer', 'is_active': True}

print(type(employee))           # <class 'dict'>

# ── Using dict() constructor ───────────────────────────
employee = dict(emp_id=100, emp_name="Joseph", emp_title="Developer")
print(employee)
# {'emp_id': 100, 'emp_name': 'Joseph', 'emp_title': 'Developer'}


# ═══════════════════════════════════════════════════════
# 2 — VALID KEY TYPES
# Keys must be IMMUTABLE — strings, integers, floats,
# booleans, and tuples are all valid keys
# Lists and dictionaries are NOT valid keys
# ═══════════════════════════════════════════════════════

valid_keys = {
    "name"          : "string key",        # str
    100             : "integer key",        # int
    3.14            : "float key",          # float
    True            : "boolean key",        # bool
    (1, 2)          : "tuple key",          # tuple
}

print(valid_keys["name"])       # string key
print(valid_keys[100])          # integer key
print(valid_keys[3.14])         # float key
print(valid_keys[True])         # boolean key
print(valid_keys[(1, 2)])       # tuple key

# ── Invalid key types ──────────────────────────────────
# {[1, 2]: "list key"}          # TypeError — lists are mutable, not hashable
# {{"a": 1}: "dict key"}        # TypeError — dicts are mutable, not hashable


# ═══════════════════════════════════════════════════════
# 3 — GETTING VALUES — SQUARE BRACKETS vs get()
# ═══════════════════════════════════════════════════════

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer"
}

# ── Square brackets [] ─────────────────────────────────
# Retrieves the value directly
# Raises a KeyError if the key does not exist

print(employee["emp_name"])     # Joseph
print(employee["emp_title"])    # Developer

# print(employee["salary"])     # KeyError — key does not exist


# ── get() method ───────────────────────────────────────
# Retrieves the value safely
# Returns None if the key does not exist — no error

print(employee.get("emp_name")) # Joseph
print(employee.get("salary"))   # None  ← no error, just None


# ── get(key, default) ──────────────────────────────────
# Returns a default value if the key does not exist
# Much safer than square brackets for optional fields

print(employee.get("salary",    0))             # 0        ← key missing, default returned
print(employee.get("emp_name",  "Unknown"))     # Joseph   ← key exists, default ignored
print(employee.get("dept",      "Unassigned"))  # Unassigned ← key missing, default returned

# ── When to use each ───────────────────────────────────
# []     → use when the key MUST exist — raises error if not found
# get()  → use when the key MAY or MAY NOT exist — safe either way


# ═══════════════════════════════════════════════════════
# 4 — DICTIONARY METHODS
# ═══════════════════════════════════════════════════════

# ── keys() ─────────────────────────────────────────────
# Returns a view of all KEYS in the dictionary

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer",
    "dept"      : "Engineering"
}

print(employee.keys())
# dict_keys(['emp_id', 'emp_name', 'emp_title', 'dept'])

# ── Looping over keys ──────────────────────────────────
for key in employee.keys():
    print(key)

# emp_id
# emp_name
# emp_title
# dept


# ── values() ───────────────────────────────────────────
# Returns a view of all VALUES in the dictionary

print(employee.values())
# dict_values([100, 'Joseph', 'Developer', 'Engineering'])

# ── Looping over values ────────────────────────────────
for value in employee.values():
    print(value)

# 100
# Joseph
# Developer
# Engineering


# ── items() ────────────────────────────────────────────
# Returns a view of all KEY:VALUE pairs as tuples
# Most commonly used for looping over a dictionary

print(employee.items())
# dict_items([('emp_id', 100), ('emp_name', 'Joseph'), ...])

# ── Looping over key value pairs ───────────────────────
for key, value in employee.items():
    print(f"{key:<12} : {value}")

# emp_id       : 100
# emp_name     : Joseph
# emp_title    : Developer
# dept         : Engineering


# ── update() ───────────────────────────────────────────
# Merges another dictionary into the current one
# Overwrites existing keys, adds new ones
# Modifies the original dictionary in place

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer"
}

updates = {
    "emp_title" : "Senior Developer",   # existing key — will be overwritten
    "dept"      : "Engineering",        # new key — will be added
    "salary"    : 95000                 # new key — will be added
}

employee.update(updates)
print(employee)
# {'emp_id': 100, 'emp_name': 'Joseph', 'emp_title': 'Senior Developer',
#  'dept': 'Engineering', 'salary': 95000}

# ── update() with keyword arguments ───────────────────
employee.update(salary=100000, is_active=True)
print(employee.get("salary"))   # 100000
print(employee.get("is_active"))# True


# ── popitem() ──────────────────────────────────────────
# Removes and RETURNS the LAST inserted key:value
# pair as a tuple
# Raises KeyError if the dictionary is empty

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer",
    "dept"      : "Engineering"
}

last_item = employee.popitem()
print(last_item)                # ('dept', 'Engineering') ← last item removed
print(employee)
# {'emp_id': 100, 'emp_name': 'Joseph', 'emp_title': 'Developer'}

last_item = employee.popitem()
print(last_item)                # ('emp_title', 'Developer')


# ── setdefault() ───────────────────────────────────────
# Returns the value for a key if it exists
# If the key does NOT exist, inserts it with
# the given default value and returns that value
# Useful for safely initializing keys

employee = {
    "emp_id"    : 100,
    "emp_name"  : "Joseph",
    "emp_title" : "Developer"
}

# ── Key exists — returns existing value, no changes ────
result = employee.setdefault("emp_name", "Unknown")
print(result)                   # Joseph  ← existing value returned
print(employee["emp_name"])     # Joseph  ← unchanged

# ── Key does not exist — inserts and returns default ───
result = employee.setdefault("dept", "Unassigned")
print(result)                   # Unassigned  ← default inserted and returned
print(employee["dept"])         # Unassigned  ← key now exists in the dict

print(employee)
# {'emp_id': 100, 'emp_name': 'Joseph', 'emp_title': 'Developer', 'dept': 'Unassigned'}