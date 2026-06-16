import pandas as pd

# A backend library is required to read and write Parquet
# pyarrow is the recommended default — install with: pip install pyarrow
# fastparquet is an alternative but less commonly used in modern workflows

# --- Writing to Parquet ---
df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

df.to_parquet("sales_data.parquet", index=False)
# Compression is applied automatically (snappy by default)
# Other options: gzip, zstd — trade off between speed and file size

# --- Reading from Parquet ---
df_parquet = pd.read_parquet("sales_data.parquet")
print(df_parquet.dtypes)
# Note: dtypes are restored exactly from the schema — no inference needed
# sale_date will come back as datetime64, quantity as int64
# no re-parsing or dtype correction required after load

# Read only specific columns — unneeded columns are never loaded from disk
# This is one of Parquet's key advantages over CSV at scale
df_slim = pd.read_parquet(
    "sales_data.parquet",
    columns=["department", "item_name", "unit_price"]
)
print(df_slim.head())