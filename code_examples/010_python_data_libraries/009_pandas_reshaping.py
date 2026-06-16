import pandas as pd

# --- pivot: simple example ---

# pivot() requires unique combinations of index and columns values
print(" === " * 4)
print(" Simple Dataset ")
print(" === " * 4)

# Creation of a small dataset with no duplicates form demonstration purposes
data = {
    "product":    ["Wireless Mouse", "Wireless Mouse", "USB-C Hub", "USB-C Hub"],
    "state":      ["Colorado",       "California",     "Colorado",  "California"],
    "unit_price": [24.99,            29.99,            44.99,       47.99]
}

df_simple = pd.DataFrame(data)
print(df_simple)
#          product       state  unit_price
# 0  Wireless Mouse    Colorado       24.99
# 1  Wireless Mouse  California       29.99
# 2       USB-C Hub    Colorado       44.99
# 3       USB-C Hub  California       47.99

# Reshape so each product is a row and each state becomes a column
print(" === " * 4)
print(" Pivot (Long->Wide) ")
print(" === " * 4)
pivoted = df_simple.pivot(
    index="product",    # unique row identifier
    columns="state",    # unique values become column headers
    values="unit_price" # values to populate the cells
)
print(pivoted)
# state           California  Colorado
# product
# USB-C Hub            47.99     44.99
# Wireless Mouse       29.99     24.99

# If a duplicate combination exists, pivot() raises a ValueError
# Use pivot_table() with an aggfunc to handle that situation instead


# --- pivot_table: long to wide with aggregation ---
print(" === " * 4)
print(" Pivot Table (Long->Wide with Aggregation) ")
print(" === " * 4)
# Read our data
df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# Add a month column to support reshaping examples
df["month"] = df["sale_date"].dt.to_period("M").astype(str)
print(df.head())

print(" === " * 4)
print(" Pivot Table (Long->Wide) ")
print(" === " * 4)
# Total quantity sold per department per month
pivot = df.pivot_table(
    index="department",
    columns="month",
    values="quantity",
    aggfunc="sum",
    fill_value=0       # fill missing combinations with 0 rather than NaN
)
print(pivot)
#                  month  2024-01  2024-02  2024-03  2024-04
# department
# Clothing                     8       16       11        3
# Electronics                 12       12       14        5
# Home & Garden               13       16       13       12
# Stationery                  10       18       17        3

# Add row and column totals
print(" === " * 4)
print(" Pivot Table with Margins ")
print(" === " * 4)
pivot_with_margins = df.pivot_table(
    index="department",
    columns="month",
    values="quantity",
    aggfunc="sum",
    fill_value=0,
    margins=True,      # adds an "All" row and column
    margins_name="Total"
)
print(pivot_with_margins)

print(" === " * 4)
print(" Melt (Wide->Long) ")
print(" === " * 4)
# --- melt: wide to long ---
print(pivot.info()) # Notice that 'department' is not a column anymore
# Reverse the pivot — collapse month columns back into rows
pivot_reset = pivot.reset_index()

melted = pivot_reset.melt(
    id_vars="department",        # columns to keep as identifiers
    var_name="month",            # name for the new column holding former column headers
    value_name="total_quantity"  # name for the new column holding values
)
print(f"Melt [Index Reset]:\n {melted.sort_values(["department", "month"]).head(8)}")
#       department    month  total_quantity
# 0       Clothing  2024-01               8
# 4       Clothing  2024-02              16
# 8       Clothing  2024-03              11
# 12      Clothing  2024-04               3
# 1    Electronics  2024-01              12

# --- stack and unstack ---
print(" === " * 4)
print(" Stack ")
print(" === " * 4)
# stack: move column labels into the row index
stacked = pivot.stack()
print(type(stacked))   # pandas Series with a MultiIndex
print(stacked.head(8))

print(" === " * 4)
print(" UnStack ")
print(" === " * 4)
# unstack: move a level of the row index back into columns — inverse of stack
unstacked = stacked.unstack()
print(unstacked.equals(pivot))  # True — round trip preserves the data

# --- transpose ---
print(" === " * 4)
print(" Transpose ")
print(" === " * 4)
# Flip rows and columns — useful for display or when a tool expects a different orientation
print(pivot.transpose())
# department  Clothing  Electronics  Home & Garden  Stationery
# month
# 2024-01            8           12             13          10
# 2024-02           11           10             10          18
# 2024-03           11           14             13          17
# 2024-04            3            5             12           3
