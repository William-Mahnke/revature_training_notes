import pandas as pd

# --- Basic read ---
df = pd.read_csv("sales_data.csv")
print("*** Head - No arg ***")
print(df.head())    # display first 5 rows

print("*** Head (3) ***")
print(df.head(3))   # display first 3 (argument provided)

print("*** Tail (7) ***")
print(df.tail(7))   # display last n rows (based on int argument provided)

print(df.shape)   # (50, 8)
print(df.dtypes)

# --- Useful read_csv parameters ---
# Parse sale_date as a datetime on load (saves a conversion step later)
print(" === " * 4)
print(" Sales_data Dtype ")
print(" === " * 4)
df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])
print(df["sale_date"].dtype)  # datetime64[ns]

# Load only the columns you need
print(" === " * 4)
print(" usecols ")
print(" === " * 4)
df_slim = pd.read_csv(
    "sales_data.csv",
    usecols=["product_id", "department", "item_name", "quantity", "unit_price"]
)
print(df_slim.columns.tolist())

# Force a column to a specific dtype on load
df = pd.read_csv("sales_data.csv", dtype={"quantity": "int32"}) # Convert to smaller datatype if you need to save on memory

# Treat additional strings as null values
df = pd.read_csv("sales_data.csv", na_values=["N/A", "unknown", "-", ""])

# Inspect just the first 10 rows of a large file without loading it all
df_preview = pd.read_csv("sales_data.csv", nrows=10)
print(" === " * 4)
print(" Only load 10 rows ")
print(" === " * 4)
print(df_preview)

# Skip the first 2 data rows after the header
df_skipped = pd.read_csv("sales_data.csv", skiprows=[1, 2])

# --- Writing to CSV ---

# Basic write — always pass index=False unless your index is meaningful data
# df.to_csv("path-to-file", index=False)
df.to_csv("sales_data_indexed.csv")

# Write a filtered subset to a new file
colorado_df = df[df["state"] == "Colorado"]
print(" === " * 4)
print(" Filtered DataFrame [colorado_df] ")
print(" === " * 4)
print(colorado_df)
colorado_df.to_csv("sales_colorado.csv", index=False)

# --- Handling large files with chunksize ---
# Process a large CSV in chunks of 1000 rows at a time
chunk_iter = pd.read_csv("sales_data.csv", chunksize=1000) # Our csv is not big enough to take advantage of this...

results = []
for chunk in chunk_iter:
    # Perform an operation on each chunk — here, filter for Electronics
    electronics_chunk = chunk[chunk["department"] == "Electronics"]
    results.append(electronics_chunk)

# Combine all processed chunks into a single DataFrame
print(" === " * 4)
print(" Concat DataFrame (electronics_df) ")
print(" === " * 4)
electronics_df = pd.concat(results)
print(electronics_df)
print(electronics_df.shape)