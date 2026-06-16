import pandas as pd

# parse_dates automatically changes the indicated columns to an appropriate dtype on load
df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Inspecting nulls ---
print(" === " * 4)
print(" Inspecting Nulls ")
print(" === " * 4)
print(df.isnull().sum())
# state          2
# unit_price     5

# View the rows where state is null
print(df[df["state"].isnull()])
# Both rows have a valid sales_office we can use to infer state

# --- Filling nulls ---
print(" === " * 4)
print(" Filling Nulls ")
print(" === " * 4)
# Fill missing state values by mapping from sales_office
# Every sales_office maps to exactly one state — reliable inference
office_to_state = {
    "California North": "California",
    "California South": "California",
    "Arizona":          "Arizona",
    "Nevada":           "Nevada",
    "Colorado North":   "Colorado",
    "Colorado South":   "Colorado",
    "Colorado East":    "Colorado",
    "Colorado West":    "Colorado"
}
# Set each state, where the state is na (fillna) to the corresponding value from the 'office_to_state' dict created above
df["state"] = df["state"].fillna(df["sales_office"].map(office_to_state))
print(f"Remianing Null States: {df["state"].isnull().sum()}")  # 0 — all state nulls resolved

# Fill missing unit_price by matching on product_id
# Use the median price per product_id to fill gaps
median_prices = df.groupby("product_id")["unit_price"].transform("median")
df["unit_price"] = df["unit_price"].fillna(median_prices)
print(f"Remianing null prices: {df["unit_price"].isnull().sum()}")  # 0 — all unit_price nulls resolved

# --- Dropping nulls (use deliberately) ---
print(" === " * 4)
print(" Dropping Nulls ")
print(" === " * 4)
# Drop rows where a specific column is null — scoped, not global
df_no_null_price = df.dropna(subset=["unit_price"])
print(f"Rows dropped: {len(df) - len(df_no_null_price)}") # Prints 0 because we just filled those nulls above - you could instead drop them for some analysis...

# --- Fixing dtypes ---
print(" === " * 4)
print(" Fixing Datatypes ")
print(" === " * 4)
# sale_date already parsed correctly via parse_dates on load
# If loaded without parse_dates, convert explicitly
df["sale_date"] = pd.to_datetime(df["sale_date"])
print(df["sale_date"].dtype)  # datetime64[ns]

# Convert quantity to a smaller integer type to save memory
df["quantity"] = df["quantity"].astype("int32")

# --- Removing duplicates ---
print(" === " * 4)
print(" Removing Duplicates ")
print(" === " * 4)
print(df.duplicated().sum())  # Check for fully duplicate rows

# Scope to specific columns — flag duplicate product/date combinations
dupes = df.duplicated(subset=["product_id", "sale_date"], keep=False)
print(df[dupes])

df = df.drop_duplicates()

# --- Renaming columns ---
print(" === " * 4)
print(" Renaming Columns ")
print(" === " * 4)
print(f"Before Renaming:\n{df.columns.tolist()}")
df = df.rename(columns={
    "item_name": "product_name",
    "unit_price": "price"
})
print(f"After Renaming:\n{df.columns.tolist()}")

# --- Replacing values ---
print(" === " * 4)
print(" Replacing Values ")
print(" === " * 4)
# Fix a known categorical inconsistency spotted during exploration
df["state"] = df["state"].replace({
    "Colroado": "Colorado",   # typo correction
    "Calif":    "California"  # abbreviation standardisation
})

# --- Dropping columns ---
print(" === " * 4)
print(" Dropping Columns ")
print(" === " * 4)
# Remove a column that is no longer needed
df = df.drop(columns=["sales_office"])

# --- Clipping outliers ---

# Cap unit_price at the 95th percentile rather than dropping outliers entirely
upper_limit = df["price"].quantile(0.95)
df["price"] = df["price"].clip(upper=upper_limit)
print(df["price"].max())  # Now capped at the 95th percentile value

# --- Verify the cleaned DataFrame ---
print(" === " * 4)
print(" Final Verification ")
print(" === " * 4)
df.info()
print(f"null count:\n{df.isnull().sum()}")  # Should be all zeros after cleaning