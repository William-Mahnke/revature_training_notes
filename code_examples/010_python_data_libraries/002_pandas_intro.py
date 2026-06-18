import pandas as pd

# pandas exposes its core data structures at the top level
# A Series is a one-dimensional labelled array
print(" === " * 4)
print(" Series ")
print(" === " * 4)
sales_figures = pd.Series([1200, 850, 1540, 990, 1375])
print(sales_figures)
# 0    1200
# 1     850
# 2    1540
# 3     990
# 4    1375
# dtype: int64


# A DataFrame is a two-dimensional labelled table — like a spreadsheet or SQL table
data = {
    "product": ["Wireless Mouse", "USB-C Hub", "Bluetooth Speaker"],
    "department": ["Electronics", "Electronics", "Electronics"],
    "unit_price": [29.99, 44.99, 89.99]
}

print(" === " * 4)
print(" Data Frame ")
print(" === " * 4)
df = pd.DataFrame(data)
print(df)
#              product   department  unit_price
# 0     Wireless Mouse  Electronics       29.99
# 1          USB-C Hub  Electronics       44.99
# 2  Bluetooth Speaker  Electronics       89.99

print(" === " * 4)
print(" Data Frame Properties ")
print(" === " * 4)
# Inspecting basic properties of a DataFrame
print(df.shape)    # (3, 3) — rows, columns
print(df.columns)  # Index(['product', 'department', 'unit_price'], dtype='object')
print(df.dtypes)   # column data types


# Pandas is incredibly useful when we generate dataframes from a datasource
df = pd.read_csv("sales_data.csv")

# --- Series ---
print(" === " * 4)
print(" Series [sales_data.csv] ")
print(" === " * 4)
# Selecting a single column returns a Series
prices = df["unit_price"]
print(type(prices))   # <class 'pandas.core.series.Series'>
print(prices.head())

# A Series has both values and an index
print(prices.values)  # The underlying NumPy array
print(prices.index)   # The row labels (default: RangeIndex 0, 1, 2, ...)

# --- DataFrame basics ---

print(" === " * 4)
print(" DataFrame [sales_data.csv] ")
print(" === " * 4)
# Selecting multiple columns returns a DataFrame
subset = df[["department", "item_name", "unit_price"]]
print(type(subset))   # <class 'pandas.core.frame.DataFrame'>
print(subset.head())

# Each column has a dtype
print(df.dtypes)
# product_id      object
# sale_date       object
# state           object
# sales_office    object
# department      object
# item_name       object
# quantity         int64
# unit_price      float64

# # --- Indexing with .loc and .iloc ---

# print(" === " * 4)
# print(" Indexing ( iloc[] ) ")
# print(" === " * 4)
# # .iloc — position based (like a list index)
# print(df.iloc[0])        # First row
# print(df.iloc[0:3])      # First three rows
# print(df.iloc[0, 2])     # Row 0, column 2 (state)

# print(" === " * 4)
# print(" Indexing ( loc[] ) ")
# print(" === " * 4)
# # .loc — label based (uses the actual index label)
# print(df.loc[0])         # Row with index label 0
# print(df.loc[0:2])       # Rows with index labels 0 through 2 (inclusive)
# print(df.loc[0, "state"])  # Row 0, column "state"

# print(" === " * 4)
# print(" Setting a meaningful index ")
# print(" === " * 4)
# # Setting a meaningful index
# df_indexed = df.set_index("product_id")
# print(df_indexed.loc["PRD-054"])  # All rows for product PRD-054

# # --- Boolean masking ---

# print(" === " * 4)
# print(" Boolean Masking (filtering) ")
# print(" === " * 4)
# # Single condition — Colorado sales only
# colorado_mask = df["state"] == "Colorado"
# colorado_sales = df[colorado_mask]
# print(colorado_sales.shape)  # (approx 25 rows, 8 columns)

# # Combine conditions with & and |
# electronics_colorado = df[
#     (df["state"] == "Colorado") &
#     (df["department"] == "Electronics")
# ]
# print(electronics_colorado[["item_name", "quantity", "unit_price"]])

# # Filter rows where unit_price is above 50
# premium = df[df["unit_price"] > 50]
# print(premium["item_name"].unique())