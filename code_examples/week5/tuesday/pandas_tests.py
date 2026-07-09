import pandas as pd
import numpy as np

# 1. Build a small dataset (normally you'd read_csv here)
df = pd.DataFrame({
    "employee": ["Ada", "Linus", "Grace", "Guido", "Bjarne", "Margaret"],
    "dept":     ["Web", "Kernel", "Web", "Web", "Kernel", "Web"],
    "salary":   [120000, 150000, np.nan, 135000, 145000, 110000],
    "years":    [4, 12, 8, 10, 15, 20],
})

# 2. INSPECT — always look before you leap
print(df.info())
print(df.describe())
print("missing per column:\n", df.isna().sum())

# 3. CLEAN — fill the missing salary with the department average
df["salary"] = df["salary"].fillna(df.groupby("dept")["salary"].transform("mean"))

# 4. DERIVE — a tenure band and salary-per-year
df["band"] = np.where(df["years"] >= 10, "senior", "junior")
df["salary_per_year"] = (df["salary"] / df["years"]).round(0)

# 5. FILTER — seniors only
seniors = df[df["band"] == "senior"]

# 6. AGGREGATE — per-department summary
summary = (
    df.groupby("dept")
      .agg(headcount=("employee", "count"),
           avg_salary=("salary", "mean"),
           max_years=("years", "max"))
      .reset_index()
      .sort_values("avg_salary", ascending=False)
)
print(summary)

# 7. MERGE — attach a lookup table
locations = pd.DataFrame({"dept": ["Web", "Kernel"], "office": ["NYC", "Austin"]})
enriched = df.merge(locations, on="dept", how="left")

# 8. EXPORT — pandas writes many formats (see note 203)
enriched.to_parquet("employees.parquet", index=False)
print("wrote employees.parquet")