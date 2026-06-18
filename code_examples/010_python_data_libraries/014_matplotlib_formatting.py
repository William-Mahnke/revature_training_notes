import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- Titles, axis labels, and legends ---
monthly_by_dept = df.groupby([
    df["sale_date"].dt.to_period("M").astype(str),
    "department"
])["quantity"].sum().unstack()

fig, ax = plt.subplots(figsize=(9, 5))
for dept in monthly_by_dept.columns:
    ax.plot(monthly_by_dept.index, monthly_by_dept[dept], marker="o", label=dept)

ax.set_title("Monthly Quantity Sold by Department (with legend)", fontsize=14)
ax.set_xlabel("Month", fontsize=11)
ax.set_ylabel("Total Quantity", fontsize=11)
ax.legend(title="Department")   # legend title is optional but adds clarity
plt.tight_layout()
plt.show()

# --- Line properties ---
monthly_qty = df.groupby(
    df["sale_date"].dt.to_period("M")
)["quantity"].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(
    monthly_qty.index.astype(str),
    monthly_qty.values,
    color="steelblue",   # line colour
    linestyle="--",      # dashed line
    linewidth=2,         # line thickness
    marker="o",          # circle marker at each data point
    markersize=8
)
ax.set_title("Monthly Quantity Sold (line styled)")
ax.set_xlabel("Month")
ax.set_ylabel("Total Quantity")
plt.tight_layout()
plt.show()

# --- Bar properties: color, edgecolor, alpha ---
dept_qty = df.groupby("department")["quantity"].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(
    dept_qty.index,
    dept_qty.values,
    color="steelblue",
    edgecolor="white",  # border around each bar
    alpha=0.85          # slight transparency
)
ax.set_title("Total Quantity Sold by Department (formatted)")
ax.set_xlabel("Department")
ax.set_ylabel("Total Quantity")
plt.xticks(rotation=45, ha="right")  # rotate labels to prevent overlap
plt.tight_layout()
plt.show()

# --- Scatter properties: alpha for overlapping points ---
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(
    df["unit_price"],
    df["quantity"],
    color="steelblue",
    edgecolor="purple",
    alpha=0.4,    # transparency helps reveal density where points overlap
    s=90          # marker size
)
ax.set_title("Unit Price vs Quantity Sold (formatted)")
ax.set_xlabel("Unit Price")
ax.set_ylabel("Quantity")
plt.tight_layout()
plt.show()

# --- Axis limits ---
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(dept_qty.index, dept_qty.values, color="steelblue", edgecolor="white")
ax.set_title("Total Quantity Sold by Department (axis limited)")
ax.set_ylim(0, 60)   # set y-axis range explicitly
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
