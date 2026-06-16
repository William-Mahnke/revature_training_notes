import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sales_data.csv", parse_dates=["sale_date"])

# --- The Figure and Axes model ---

# Create a Figure and a single Axes explicitly
fig, ax = plt.subplots()
print(type(fig))  # <class 'matplotlib.figure.Figure'>
print(type(ax))   # <class 'matplotlib.axes.Axes'>

# --- A first simple plot using the plt. interface ---

monthly_qty = df.groupby(df["sale_date"].dt.to_period("M"))["quantity"].sum()

plt.plot(monthly_qty.index.astype(str), monthly_qty.values)
plt.title("Monthly Quantity Sold")
plt.xlabel("Month")
plt.ylabel("Quantity")
# plt.show()
# In a script: plt.show() is required to display the chart
# In a Jupyter notebook: charts render inline without plt.show()

# --- The same plot using the ax. object-oriented interface ---
fig, ax = plt.subplots()

ax.plot(monthly_qty.index.astype(str), monthly_qty.values)
ax.set_title("Monthly Quantity Sold")
ax.set_xlabel("Month")
ax.set_ylabel("Quantity")

# plt.show()
# Both approaches produce identical output
# ax. style is preferred when working with multiple subplots

# --- figsize: controlling the canvas size ---

# figsize is specified as (width, height) in inches
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_qty.index.astype(str), monthly_qty.values)
ax.set_title("Monthly Quantity Sold")
plt.show()

# # --- Saving a figure to file instead of displaying it ---
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(monthly_qty.index.astype(str), monthly_qty.values)
# ax.set_title("Monthly Quantity Sold")
# plt.tight_layout()
# plt.savefig("monthly_qty.png", dpi=150)
# # dpi controls image resolution — 150 is a good default for reports