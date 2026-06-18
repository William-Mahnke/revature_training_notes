import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Case standardisation ---
print(" === " * 4)
print(" Case Standardization ")
print(" === " * 4)
# Set columns to lowers - case insensitive
df["department"] = df["department"].str.lower()
print(df["department"].unique())
# ['electronics' 'home & garden' 'clothing' 'stationery']

# Set columns to title casing - meaningful column names
df["department"] = df["department"].str.title()
print(df["department"].unique())
# ['Electronics' 'Home & Garden' 'Clothing' 'Stationery']

# --- Stripping whitespace ---
# Remove leading/trailing whitespaces
# Catches cases like "Colorado " that would otherwise fail to match
df["state"] = df["state"].str.strip()

# --- Checking string content ---
print(" === " * 4)
print(" Filtering with Contains (Colorado Sales Offices) ")
print(" === " * 4)
# Filter rows where sales_office contains "Colorado"
colorado_offices = df[df["sales_office"].str.contains("Colorado", na=False)]
print(colorado_offices["sales_office"].unique())
# ['Colorado North' 'Colorado East' 'Colorado South' 'Colorado West']

# na=False ensures nulls return False rather than NaN in the boolean mask
# Filter rows where product_id starts with "PRD-05"
print(" === " * 4)
print(" Filtering with StartsWith (PRD-05) ")
print(" === " * 4)
prd_05x = df[df["product_id"].str.startswith("PRD-05")]
print(prd_05x["product_id"].unique())
# ['PRD-054' 'PRD-056' 'PRD-058']

# --- Extracting parts of a string ---
print(" === " * 4)
print(" Extracting Parts of a String ")
print(" === " * 4)
# Extract the numeric portion of product_id into a new column
# The regex \d+ matches one or more digits
df["product_num"] = df["product_id"].str.extract(r"(\d+)")
print(df[["product_id", "product_num"]].head())
# product_id  product_num
# PRD-054     054
# PRD-021     021
# PRD-087     087
print(df.head())    # take note that we have a new 'product_num' column now
# product_id    sale_date   state       sales_office        ...     product_num
# PRD-054       2024-01-05  Colorado    Colorado North      ...     054
# PRD-021       2024-01-07  Colorado    Colorado East       ...     021
# PRD-087       2024-01-08  California  California South    ...     087
# PRD-056       2024-01-10  Colorado    Colorado South      ...     056
# PRD-023       2024-01-12  Arizona     Arizona             ...     023

# --- Splitting strings into separate columns ---
print(" === " * 4)
print(" Splitting Strings into Separate Columns ")
print(" === " * 4)
# Split sales_office into office_region and office_direction where applicable
# expand=True returns a DataFrame rather than a Series of lists
split_office = df["sales_office"].str.split(" ", n=1, expand=True)
split_office.columns = ["office_state", "office_direction"]
print(split_office.head(8))
# office_state  office_direction
# Colorado      North
# Colorado      East
# California    South
# Colorado      South
# Arizona       NaN             <- single-word offices produce NaN in second column
# Colorado      West
# Nevada        NaN
# Colorado      North

# --- Replacing substrings ---
print(" === " * 4)
print(" Replacing substrings ")
print(" === " * 4)
# Standardise "Home & Garden" to "Home and Garden" across the column
df["department"] = df["department"].str.replace("&", "and", regex=False)
print(df["department"].unique())
# ['Electronics' 'Home and Garden' 'Clothing' 'Stationery']

# Using a regular expression — remove any non-alphanumeric characters from product_id
df["product_id_clean"] = df["product_id"].str.replace(r"[^a-zA-Z0-9]", "", regex=True)
print(df[["product_id", "product_id_clean"]].head(3))
# product_id  product_id_clean
# PRD-054     PRD054
# PRD-021     PRD021
# PRD-087     PRD087

# --- String length ---
# Check for unexpectedly short or long values in a column
print(" === " * 4)
print(" Checking String Length ")
print(" === " * 4)
df["item_name_len"] = df["item_name"].str.len()
print(df[["item_name", "item_name_len"]].sort_values("item_name_len", ascending=False).head())
