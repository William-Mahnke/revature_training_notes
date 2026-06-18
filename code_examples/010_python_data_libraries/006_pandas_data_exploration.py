import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Shape and structure ---

print(df.shape)       # (50, 8) — 50 rows, 8 columns
print(df.columns.tolist())
# ['product_id', 'sale_date', 'state', 'sales_office',
#  'department', 'item_name', 'quantity', 'unit_price']
import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Shape and structure ---

print(" === " * 4)
print(" Data Shape & Structure ")
print(" === " * 4)
print(df.shape)       # (50, 8) — 50 rows, 8 columns
print(df.columns.tolist())
# ['product_id', 'sale_date', 'state', 'sales_office',
#  'department', 'item_name', 'quantity', 'unit_price']

# --- First look at the data ---

print(" === " * 4)
print(" Sample of Some Rows ")
print(" === " * 4)
print(df.head())      # First 5 rows
print(df.tail(3))     # Last 3 rows
print(df.sample(5))   # 5 randomly selected rows — less biased than head()

# --- Info and dtypes ---

print(" === " * 4)
print(" df.info() ")
print(" === " * 4)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 50 entries, 0 to 49
# Data columns (total 8 columns):
#  #   Column        Non-Null Count  Dtype
# ---  ------        --------------  -----
#  0   product_id    50 non-null     object
#  1   sale_date     50 non-null     datetime64[ns]
#  2   state         48 non-null     object   <- 2 nulls visible immediately
#  3   sales_office  50 non-null     object
#  4   department    50 non-null     object
#  5   item_name     50 non-null     object
#  6   quantity      50 non-null     int64
#  7   unit_price    45 non-null     float64  <- 5 nulls visible immediately

# --- Null counts ---
print(" === " * 4)
print(" Count of Null Values [df.isnull().sum()] ")
print(" === " * 4)
print(df.isnull().sum())
# product_id      0
# sale_date       0
# state           2
# sales_office    0
# department      0
# item_name       0
# quantity        0
# unit_price      5

# Express nulls as a percentage of total rows
print((df.isnull().sum() / len(df) * 100).round(2))

# --- Summary statistics ---

print(" === " * 4)
print(" Summary Stats [df.describe()] ")
print(" === " * 4)
print(df.describe())
# Covers quantity and unit_price (numeric columns only by default)
#          quantity   unit_price
# count   50.000000    45.000000   <- unit_price count is 45, not 50 due to nulls
# mean     3.740000    46.214444
# std      2.100000    29.870000
# min      1.000000     8.990000
# 25%      2.000000    22.990000
# 50%      3.000000    39.990000
# 75%      5.000000    64.990000
# max     10.000000   119.990000

# Include categorical columns as well
print(" === " * 4)
print(" df.describe(include='all') ")
print(" === " * 4)
print(df.describe(include="all"))

# --- Categorical exploration ---
print(" === " * 4)
print(" value_counts() ")
print(" === " * 4)
# Frequency of each value in a column
print(df["department"].value_counts())
# Electronics      18
# Home & Garden    15
# Clothing         11
# Stationery        6

# As proportions rather than counts
print(" === " * 4)
print(" Proportions of sales/department using normalize [df.describe()] ")
print(" === " * 4)
print(df["department"].value_counts(normalize=True).round(2))
# Electronics      0.36
# Home & Garden    0.30
# Clothing         0.22
# Stationery       0.12

# Number of unique values per column
print(" === " * 4)
print(" Unique Counts, per column [df.unique()] ")
print(" === " * 4)
print(df.nunique())
# product_id      16
# sale_date       44
# state            4   <- NaN is not counted as a unique value
# sales_office     8
# department       4
# item_name       16
# quantity         8
# unit_price      18

# Unique values in a specific column — good sanity check
print(" === " * 4)
print(" Uniqueness [state + sales offices for our dataset] ")
print(" === " * 4)
print(df["state"].unique())
# ['Colorado' 'California' 'Arizona' nan 'Nevada']
# nan confirms the 2 nulls spotted in df.info()

print(df["sales_office"].unique())
# ['Colorado North' 'Colorado East' 'California South' 'Colorado South'
#  'Arizona' 'Colorado West' 'Nevada' 'California North']