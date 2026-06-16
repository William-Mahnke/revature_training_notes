import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Introducing a product catalogue reference table ---

# In a real pipeline this would be read from a database or file
# Here we construct it directly to illustrate the merge pattern
product_catalogue = pd.DataFrame({
    "product_id":   ["PRD-054", "PRD-055", "PRD-056", "PRD-058", "PRD-061",
                     "PRD-021", "PRD-023", "PRD-025", "PRD-028", "PRD-031",
                     "PRD-087", "PRD-091", "PRD-093",
                     "PRD-142", "PRD-147", "PRD-149", "PRD-119"],
    "supplier":     ["TechSource", "TechSource", "TechSource", "TechSource", "TechSource",
                     "GreenGoods", "GreenGoods", "GreenGoods", "GreenGoods", "GreenGoods",
                     "StyleCo", "StyleCo", "StyleCo",
                     "OfficeBase", "OfficeBase", "OfficeBase", "OfficeBase"],
    "weight_kg":    [0.2, 0.5, 0.1, 0.4, 0.3,
                     1.2, 2.5, 0.8, 0.3, 1.1,
                     0.6, 1.4, 0.9,
                     0.4, 1.2, 0.1, 0.8]
})

# --- inner join (default) ---
print(" === " * 4)
print(" Joins (inner - Default) ")
print(" === " * 4)
# Only rows with a matching product_id in both DataFrames are kept
df_inner = pd.merge(df, product_catalogue, on="product_id")
print(df_inner.shape)           # (50, 10) — all sales rows matched
print(df_inner.columns.tolist())
# ['product_id', 'sale_date', 'state', 'sales_office', 'department',
#  'item_name', 'quantity', 'unit_price', 'supplier', 'weight_kg']

# --- left join ---
print(" === " * 4)
print(" Joins (left) ")
print(" === " * 4)
# All rows from df are kept; nulls introduced where no catalogue match exists
df_left = pd.merge(df, product_catalogue, on="product_id", how="left")
print(df_left)
print(df_left["supplier"].isnull().sum())  # 0 if all product_ids matched

# --- right join ---
print(" === " * 4)
print(" Joins (right) ")
print(" === " * 4)
# All rows from product_catalogue are kept; nulls introduced where no catalogue match exists
df_right = pd.merge(df, product_catalogue, on="product_id", how="right")
print(df_right)
print(df_right["sales_office"].isnull().sum()) # 0 if all products are sold in some sales office

# --- Joining on columns with different names ---
print(" === " * 4)
print(" Joins With different column names ")
print(" === " * 4)
# Simulate a reference table where the key column has a different name
region_info = pd.DataFrame({
    "office_name": ["Colorado North", "Colorado East", "Colorado South",
                    "Colorado West", "California North", "California South",
                    "Arizona", "Nevada"],
    "region_manager": ["Alice Brown", "Alice Brown", "Alice Brown", "Alice Brown",
                       "James Lee",  "James Lee",
                       "Sara Patel", "Sara Patel"]
})

df_with_manager = pd.merge(
    df, region_info,
    left_on="sales_office",  # key column name in left DataFrame
    right_on="office_name",  # key column name in right DataFrame
    how="left"
)
print(df_with_manager[["sales_office", "office_name", "region_manager"]].head())
# office_name is now a redundant column — drop it
df_with_manager = df_with_manager.drop(columns=["office_name"])
print(f"After Dropping office_name:\n {df_with_manager.head()}")

# --- concat: stacking rows vertically ---
print(" === " * 4)
print(" Concat (Stacking rows) ")
print(" === " * 4)
# When Concating DataFrames with mismatched columns - you will get NaN for null values
mismatched = pd.concat(
    [df, product_catalogue],
    ignore_index=True  # reset index — without this, index values are duplicated
)
print(mismatched)

# Simulate data arriving as separate DataFrames per state
colorado_df   = df[df["state"] == "Colorado"]
california_df = df[df["state"] == "California"]
arizona_df    = df[df["state"] == "Arizona"]
nevada_df     = df[df["state"] == "Nevada"]
print(f":::Colorado Sales:::")
print(colorado_df.head(2))
print(f":::California Sales:::")
print(california_df.head(2))
print(f":::Arizona Sales:::")
print(arizona_df.head(2))
print(f":::Nevada Sales:::")
print(nevada_df.head(2))
# Stack all four back into a single DataFrame
combined_sales = pd.concat(
    [colorado_df, california_df, arizona_df, nevada_df],
    ignore_index=True  # reset index — without this, index values are duplicated
)
print(":::All Sales:::")
print(combined_sales.head())
print(combined_sales.tail())

# --- concat: stacking columns horizontally ---
print(" === " * 4)
print(" Concat (Stacking Columns) ")
print(" === " * 4)
# Add the supplier and weight columns from the catalogue alongside the sales data
df_cols = pd.concat([df, product_catalogue[["supplier", "weight_kg"]]], axis=1)
print(df_cols.head())
print(df_cols.tail())
# Note: horizontal concat aligns on index — only reliable when both DataFrames
# share the same index. Use merge() when joining on a key column is needed.