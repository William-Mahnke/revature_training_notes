import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# Prepare aggregated data used across examples
dept_qty       = df.groupby("department")["quantity"].sum()
office_qty     = df.groupby("sales_office")["quantity"].sum().sort_values()
monthly_qty    = df.groupby(df["sale_date"].dt.to_period("M"))["quantity"].sum()
state_qty      = df.groupby("state")["quantity"].sum()

# --- Basic subplot grid: 1 row, 2 columns ---
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].bar(dept_qty.index, dept_qty.values, color="steelblue", edgecolor="white")
ax[0].set_title("Quantity by Department")
ax[0].set_xlabel("Department")
ax[0].set_ylabel("Total Quantity")
ax[0].tick_params(axis="x", rotation=45)

ax[1].barh(office_qty.index, office_qty.values, color="goldenrod", edgecolor="white")
ax[1].set_title("Quantity by Sales Office")
ax[1].set_xlabel("Total Quantity")

fig.suptitle("Sales Summary", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.show()

# --- 2x2 subplot grid ---

fig, ax = plt.subplots(2, 2, figsize=(12, 9))

# Top left: quantity by department
ax[0, 0].bar(dept_qty.index, dept_qty.values, color="cornflowerblue", edgecolor="white")
ax[0, 0].set_title("Quantity by Department")
ax[0, 0].tick_params(axis="x", rotation=45)

# Top right: monthly trend
ax[0, 1].plot(monthly_qty.index.astype(str), monthly_qty.values,
              marker="o", color="coral", linewidth=2)
ax[0, 1].set_title("Monthly Quantity Sold")
ax[0, 1].set_xlabel("Month")

# Bottom left: quantity by state
ax[1, 0].bar(state_qty.index, state_qty.values, color="springgreen", edgecolor="white")
ax[1, 0].set_title("Quantity by State")

# Bottom right: unit price distribution
ax[1, 1].hist(df["unit_price"].dropna(), bins=12, color="gold", edgecolor="white")
ax[1, 1].set_title("Unit Price Distribution")
ax[1, 1].set_xlabel("Unit Price")
ax[1, 1].set_ylabel("Frequency")

fig.suptitle("Sales Data Overview", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.show()

# --- Iterating over subplots with flatten() ---

# Useful when populating many subplots from a loop
departments = df["department"].unique()
colors = ["brown", "darkorange", "seagreen", "mediumpurple"]
fig, axes = plt.subplots(2, 2, figsize=(10, 6))

for ax, dept, color in zip(axes.flatten(), departments, colors):
    dept_data = df[df["department"] == dept].groupby(
        df["sale_date"].dt.to_period("M")
    )["quantity"].sum()
    ax.plot(dept_data.index.astype(str), dept_data.values,
            marker="o", color=color, linewidth=2)
    ax.set_title(f"{dept}")
    ax.set_xlabel("Month")
    ax.set_ylabel("Quantity")
    ax.tick_params(axis="x", rotation=45)

fig.suptitle("Monthly Quantity by Department", fontsize=11, fontweight="bold")
plt.tight_layout()
plt.show()

# --- Passing an ax object to pandas .plot() ---

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Tell pandas exactly which panel to draw into using the ax parameter
dept_qty.plot(kind="bar", ax=axes[0], color="royalblue",
              edgecolor="white", legend=False)
axes[0].set_title("Quantity by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Total Quantity")
axes[0].tick_params(axis="x", rotation=45)

monthly_qty_plot = monthly_qty.copy()
monthly_qty_plot.index = monthly_qty_plot.index.astype(str)
monthly_qty_plot.plot(kind="line", ax=axes[1], marker="o",
                      color="coral", linewidth=2, legend=False)
axes[1].set_title("Monthly Quantity Sold")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Total Quantity")

fig.suptitle("Sales Summary", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()