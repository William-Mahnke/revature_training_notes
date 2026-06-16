import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- pd.to_datetime: ensuring correct dtype ---

# parse_dates on read_csv handles this at load time (preferred)
# If loading without parse_dates, convert explicitly:
df["sale_date"] = pd.to_datetime(df["sale_date"])
print(df["sale_date"].dtype)  # datetime64[ns]

# A string date looks correct but cannot be used for time-based operations
# pd.to_datetime() fixes this — always verify dtype after loading date columns

# --- The .dt accessor ---
print(" === " * 4)
print(" .dt accessor ")
print(" === " * 4)
# Extract datetime components into new columns
df["year"]       = df["sale_date"].dt.year
df["month"]      = df["sale_date"].dt.month
df["month_name"] = df["sale_date"].dt.month_name()
df["quarter"]    = df["sale_date"].dt.quarter
df["day_name"]   = df["sale_date"].dt.day_name()

print(df[["sale_date", "year", "month", "month_name", "quarter", "day_name"]].head())
#   sale_date  year  month month_name  quarter   day_name
# 0 2024-01-05  2024      1    January        1  Friday
# 1 2024-01-07  2024      1    January        1  Sunday
# 2 2024-01-08  2024      1    January        1  Monday

# --- Time-based filtering using .dt ---
print(" === " * 4)
print(" Time-based filtering ")
print(" === " * 4)
# Filter to Q1 sales only
q1_sales = df[df["sale_date"].dt.quarter == 1]
print(q1_sales.shape)


# Filter to a specific month
march = df[df["sale_date"].dt.month == 3]
print(march.shape)

# --- groupby with .dt — no DatetimeIndex required ---
# This has been enabled using datetime to derive month/year/day/etc...from sale_date (lines 9 - 24)
print(" === " * 4)
print(" Groupby (no DatetimeIndex) ")
print(" === " * 4)
# Total quantity sold per month
monthly_qty = df.groupby(df["sale_date"].dt.to_period("M"))["quantity"].sum()
print(monthly_qty)
# sale_date
# 2024-01    43
# 2024-02    62
# 2024-03    55
# 2024-04    23

# Total quantity per department per month
dept_monthly = df.groupby([
    df["sale_date"].dt.to_period("M"),
    "department"
])["quantity"].sum()
print(dept_monthly)

# --- set_index: creating a DatetimeIndex for resample ---
print(" === " * 4)
print(" Resample (set_index with DatetimeIndex) ")
print(" === " * 4)
# resample() requires the datetime column to be the index
df_indexed = df.set_index("sale_date").sort_index()
print(df_indexed.index)  # DatetimeIndex

# --- resample: time-bucketed aggregation ---
# Total quantity sold per month
monthly = df_indexed["quantity"].resample("ME").sum()
print(monthly)
# sale_date
# 2024-01-31    43
# 2024-02-29    62
# 2024-03-31    55
# 2024-04-30    23
# Freq: ME, Name: quantity, dtype: int64

print(" === " * 4)
print(" Resample - weekly sales filter ")
print(" === " * 4)
# Total quantity sold per week
weekly = df_indexed["quantity"].resample("W").sum()
print(weekly)

print(" === " * 4)
print(" Resample - Monthly Stats ")
print(" === " * 4)
# Multiple aggregations in one resample call
monthly_stats = df_indexed["quantity"].resample("ME").agg(
    total="sum",
    average="mean",
    transactions="count"
)
print(monthly_stats)
#             total    average  transactions
# sale_date
# 2024-01-31     43   3.071429            14
# 2024-02-29     62   4.428571            14
# 2024-03-31     55   3.666667            15
# 2024-04-30     23   3.285713             7