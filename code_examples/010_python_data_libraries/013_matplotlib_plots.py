import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Line chart: trend over time ---
monthly_qty = df.groupby(
    df["sale_date"].dt.to_period("M")
)["quantity"].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(monthly_qty.index.astype(str), monthly_qty.values)
ax.set_title("Monthly Quantity Sold (Line Chart)")
ax.set_xlabel("Month")
ax.set_ylabel("Total Quantity")
plt.tight_layout()
plt.show()

# --- Bar chart: comparing categories ---

dept_qty = df.groupby("department")["quantity"].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(dept_qty.index, dept_qty.values)
ax.set_title("Total Quantity Sold by Department (Bar Chart)")
ax.set_xlabel("Department")
ax.set_ylabel("Total Quantity")
plt.tight_layout()
plt.show()

# --- Horizontal bar chart: better for longer category labels ---

office_qty = df.groupby("sales_office")["quantity"].sum().sort_values()

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(office_qty.index, office_qty.values)
ax.set_title("Total Quantity Sold by Sales Office (H Bar Chart)")
ax.set_xlabel("Total Quantity")
plt.tight_layout()
plt.show()

# --- Grouped bar chart: two categorical dimensions ---

import numpy as np

dept_monthly = df.groupby([
    df["sale_date"].dt.to_period("M").astype(str),
    "department"
])["quantity"].sum().unstack()

months = dept_monthly.index.tolist()
departments = dept_monthly.columns.tolist()
x = np.arange(len(months))
width = 0.2  # width of each individual bar

fig, ax = plt.subplots(figsize=(10, 6))
for i, dept in enumerate(departments):
    ax.bar(x + i * width, dept_monthly[dept], width=width, label=dept)

ax.set_title("Monthly Quantity Sold by Department (GroupedBar Chart)")
ax.set_xlabel("Month")
ax.set_ylabel("Total Quantity")
ax.set_xticks(x + width)
ax.set_xticklabels(months)
ax.legend()
plt.tight_layout()
plt.show()

# --- Scatter plot: relationship between two numeric columns ---
# Drop nulls first so polyfit (trend line) receives clean arrays
clean = df[["unit_price", "quantity"]].dropna()

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(clean["unit_price"], clean["quantity"])

# The following showcases how we can calculate and showcase a trend line on
# our scatterplot. We'll follow these steps:
# Calculate and plot a linear trend line
# np.polyfit returns coefficients for a polynomial of the specified degree
# degree 1 = linear (y = mx + c)
m, c = np.polyfit(clean["unit_price"], clean["quantity"], deg=1)
x_line = np.linspace(clean["unit_price"].min(), clean["unit_price"].max(), 100)
ax.plot(x_line, m * x_line + c, color="red", linestyle="--", label="Trend")

ax.set_title("Unit Price vs Quantity Sold (Scatterplot)")
ax.set_xlabel("Unit Price")
ax.set_ylabel("Quantity")
plt.tight_layout()
plt.show()

# --- Histogram: distribution of a numeric column ---

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(df["unit_price"].dropna(), bins=15, edgecolor="white")
ax.set_title("Distribution of Unit Prices (Histogram)")
ax.set_xlabel("Unit Price")
ax.set_ylabel("Frequency")
plt.tight_layout()
plt.show()