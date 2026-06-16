import pandas as pd

# --- Basic read and write ---
# Write a DataFrame to JSON in records format
# Note: We could have read from csv/parquet/other datatype. The 
# DF is used as a common structure to write to any supported file type
csv_df = pd.read_csv("sales_data.csv")
csv_df.to_json("sales_data.json", orient="records", indent=2)

# Read a JSON file in "records" format (most common from APIs)
# [{"product_id": "PRD-054", "department": "Electronics", ...}, {...}]
print(" === " * 4)
print(" JSON DataFrame ")
print(" === " * 4)
df = pd.read_json("sales_data.json", orient="records")
print(df.head())

# Common orient options
df.to_json("cols.json", orient="columns")   # {col: {index: value}}
df.to_json("index.json", orient="index")    # {index: {col: value}}

# --- Newline-delimited JSON (NDJSON) ---
# Write as NDJSON
print(" === " * 4)
print(" NDJSON ")
print(" === " * 4)
df.to_json("sales_log.ndjson", orient="records", lines=True) # line='True' creates the newline delimited JSON

# Each line is a separate JSON object — common in logs and event streams
# {"product_id": "PRD-054", "quantity": 3}
# {"product_id": "PRD-056", "quantity": 4}
df_ndjson = pd.read_json("sales_log.ndjson", lines=True)
print(df_ndjson.head())

# --- Handling nested JSON with json_normalize ---
# Simulated API response with nested structure
api_response = [
    {
        "order_ref": "ORD-001",
        "sale_date": "2024-01-05",
        "sales_office": "Colorado North",
        "product": {
            "product_id": "PRD-054",
            "name": "Wireless Mouse",
            "department": "Electronics"
        },
        "quantity": 3,
        "unit_price": 29.99
    },
    {
        "order_ref": "ORD-002",
        "sale_date": "2024-01-07",
        "sales_office": "Colorado East",
        "product": {
            "product_id": "PRD-021",
            "name": "Ceramic Plant Pot",
            "department": "Home & Garden"
        },
        "quantity": 5,
        "unit_price": 14.99
    }
]

# Without normalisation — "product" column contains dicts
print(" === " * 4)
print(" API Response JSON [RAW] ")
print(" === " * 4)
api_df_raw = pd.DataFrame(api_response)
api_df_raw.to_json("api_data_raw.json", orient="records")

# With json_normalize — nested keys are flattened with dot notation
print(" === " * 4)
print(" API Response JSON [NORMALIZED] ")
print(" === " * 4)
api_df_normalised = pd.json_normalize(api_response)
api_df_normalised.to_json("api_data_normalized.json", orient="records")
# ['order_ref', 'sale_date', 'sales_office', 'quantity',
#  'unit_price', 'product.product_id', 'product.name', 'product.department']

# Rename flattened columns for cleanliness
api_df_normalised = api_df_normalised.rename(columns={
    "product.product_id": "product_id",
    "product.name": "item_name",
    "product.department": "department"
})
print(api_df_normalised.head())


# ***** ***** ***** ***** ***** ***** ***** *****
# The following is a general structure for 
# Reading JSON directly from an API response
# ***** ***** ***** ***** ***** ***** ***** *****
# import requests                               # library import
# url = "https://api.example.com/sales"         # API endpoint to call
# response = requests.get(url)                  # Call API via library function
# json_data = response.json()                   # Get JSOn Response content
# df_api = pd.json_normalize(json_data)         # Normalize json -> Generate data frame
# print(df_api.shape)                           # process data
