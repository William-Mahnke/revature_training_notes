import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Color pallete used to standardize color for all visualizations
PALETTE = [
    "#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F",
    "#EDC948", "#B07AA1", "#FF9DA7", "#9C755F", "#BAB0AC",
    "#86BCB6", "#D4A6C8",
]
# Accent color
ACCENT = "#4E79A7"
# Background color
BG      = "#F8F9FA"
# Grid color
GRID    = "#E0E0E0"

# Utility function used to style axis'
def style_ax(ax, title="", xlabel="", ylabel=""):
    ax.set_facecolor(BG)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    if title:  ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
    if xlabel: ax.set_xlabel(xlabel, fontsize=9)
    if ylabel: ax.set_ylabel(ylabel, fontsize=9)

# Utility function to format numeric output for millions
def millions_fmt(x, _):
    return f"{x:,.0f}M"

# ── Load & clean ─────────────────────────────────────────────────────────────
# Load sales data: retrieved from: https://www.kaggle.com/datasets/gregorut/videogamesales
df = pd.read_csv("vgsales.csv")

# Drop rows where both Year and Publisher are null (not useful for any analysis)
df = df.dropna(subset=["Name", "Genre", "Platform"])

# Clean Year: convert to int where possible, keep NaN rows for non-year charts
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df_with_year = df.dropna(subset=["Year"]).copy()
df_with_year["Year"] = df_with_year["Year"].astype(int)

# Remove obvious outlier years (data goes to 2020 but has sparse future entries)
df_with_year = df_with_year[df_with_year["Year"] <= 2016]

# Clean Publisher: fill NaN with "Unknown"
df["Publisher"] = df["Publisher"].fillna("Unknown")

# Utility Values to be used 
REGIONS   = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
REG_NAMES = ["North America", "Europe", "Japan", "Other"]
SALES_COL = "Global_Sales"


# FIGURE 1 – Sales by Platform
plat_global = (df.groupby("Platform")[SALES_COL].sum()
                 .sort_values(ascending=False).head(15))
plat_region = (df.groupby("Platform")[REGIONS].sum()
                 .loc[plat_global.index])           # same order

fig, axes = plt.subplots(2, 1, figsize=(14, 12))
fig.patch.set_facecolor("white")
fig.suptitle("Video Game Sales by Platform", fontsize=16, fontweight="bold", y=0.98)

# --- top panel: global bar ---
ax = axes[0]
bars = ax.bar(plat_global.index, plat_global.values,
              color=PALETTE[:len(plat_global)], edgecolor="white", linewidth=0.5)
style_ax(ax, "Top 20 Platforms – Global Sales", ylabel="Sales (millions)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.set_xticklabels(plat_global.index, rotation=40, ha="right", fontsize=9)
for bar, val in zip(bars, plat_global.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f"{val:,.0f}M", ha="center", va="bottom", fontsize=7.5, fontweight="bold")

# --- bottom panel: stacked regional bar ---
ax = axes[1]
bottom = np.zeros(len(plat_region))
for i, (col, name) in enumerate(zip(REGIONS, REG_NAMES)):
    vals = plat_region[col].values
    ax.bar(plat_region.index, vals, bottom=bottom,
           label=name, color=PALETTE[i], edgecolor="white", linewidth=0.4)
    bottom += vals
style_ax(ax, "Top 20 Platforms – Regional Breakdown", ylabel="Sales (millions)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.set_xticklabels(plat_region.index, rotation=40, ha="right", fontsize=9)
ax.legend(loc="upper right", framealpha=0.9, fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig(f"01_sales_by_platform.png", dpi=150, bbox_inches="tight")
plt.close()


# FIGURE 2 – Sales by Year
year_global = df_with_year.groupby("Year")[SALES_COL].sum()
year_region = df_with_year.groupby("Year")[REGIONS].sum()

fig, axes = plt.subplots(2, 1, figsize=(14, 11))
fig.patch.set_facecolor("white")
fig.suptitle("Video Game Sales by Year", fontsize=16, fontweight="bold", y=0.98)

# --- global line ---
ax = axes[0]
ax.fill_between(year_global.index, year_global.values, alpha=0.15, color=ACCENT)
ax.plot(year_global.index, year_global.values, color=ACCENT, linewidth=2.5, marker="o",
        markersize=4)
style_ax(ax, "Global Sales per Year", ylabel="Sales (millions)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.set_xticks(year_global.index[::2])
ax.tick_params(axis="x", rotation=45)
# annotate peak
peak_yr = year_global.idxmax()
peak_val = year_global.max()
ax.annotate(f"Peak: {peak_yr}\n{peak_val:,.0f}M",
            xy=(peak_yr, peak_val), xytext=(peak_yr - 4, peak_val * 0.92),
            arrowprops=dict(arrowstyle="->", color="grey"), fontsize=8.5)

# --- stacked area by region ---
ax = axes[1]
years = year_region.index
stack_data = [year_region[c].values for c in REGIONS]
ax.stackplot(years, stack_data, labels=REG_NAMES,
             colors=PALETTE[:4], alpha=0.85)
style_ax(ax, "Regional Sales per Year", ylabel="Sales (millions)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.set_xticks(years[::2])
ax.tick_params(axis="x", rotation=45)
ax.legend(loc="upper left", framealpha=0.9, fontsize=9)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig(f"02_sales_by_year.png", dpi=150, bbox_inches="tight")
plt.close()


# FIGURE 3 – Sales by Publisher (Top 15)
pub_global = (df.groupby("Publisher")[SALES_COL].sum()
                .sort_values(ascending=False).head(15))
pub_region = df.groupby("Publisher")[REGIONS].sum().loc[pub_global.index]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.patch.set_facecolor("white")
fig.suptitle("Video Game Sales by Publisher (Top 15)", fontsize=16, fontweight="bold", y=1.01)

# --- horizontal bar global ---
ax = axes[0]
y_pos = np.arange(len(pub_global))
colors = [PALETTE[i % len(PALETTE)] for i in range(len(pub_global))]
bars = ax.barh(y_pos, pub_global.values, color=colors, edgecolor="white", linewidth=0.4)
ax.set_yticks(y_pos)
ax.set_yticklabels(pub_global.index, fontsize=9)
ax.invert_yaxis()
style_ax(ax, "Global Sales", xlabel="Sales (millions)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.grid(axis="y", visible=False)
for bar, val in zip(bars, pub_global.values):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            f"{val:,.0f}M", va="center", fontsize=7.5)

# --- stacked horizontal regional ---
ax = axes[1]
bottom = np.zeros(len(pub_region))
for i, (col, name) in enumerate(zip(REGIONS, REG_NAMES)):
    vals = pub_region[col].values
    ax.barh(y_pos, vals, left=bottom, label=name,
            color=PALETTE[i], edgecolor="white", linewidth=0.4)
    bottom += vals
ax.set_yticks(y_pos)
ax.set_yticklabels(pub_region.index, fontsize=9)
ax.invert_yaxis()
style_ax(ax, "Regional Breakdown", xlabel="Sales (millions)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", framealpha=0.9, fontsize=9)

plt.tight_layout()
plt.savefig(f"03_sales_by_publisher.png", dpi=150, bbox_inches="tight")
plt.close()


# FIGURE 4 – Sales by Genre
genre_global = df.groupby("Genre")[SALES_COL].sum().sort_values(ascending=False)
genre_region = df.groupby("Genre")[REGIONS].sum().loc[genre_global.index]
genre_count  = df.groupby("Genre")["Name"].count().loc[genre_global.index]

fig, axes = plt.subplots(1, 3, figsize=(18, 7))
fig.patch.set_facecolor("white")
fig.suptitle("Video Game Sales by Genre", fontsize=16, fontweight="bold", y=1.01)

genre_colors = PALETTE[:len(genre_global)]

# --- donut chart global share ---
ax = axes[0]
wedges, texts, autotexts = ax.pie(
    genre_global.values,
    labels=genre_global.index,
    autopct=lambda p: f"{p:.1f}%" if p > 3 else "",
    colors=genre_colors,
    pctdistance=0.82,
    startangle=140,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.2),
)
for t in texts:     t.set_fontsize(8)
for at in autotexts: at.set_fontsize(7.5)
ax.set_title("Global Sales Share", fontsize=12, fontweight="bold", pad=10)

# --- bar chart absolute sales ---
ax = axes[1]
y_pos = np.arange(len(genre_global))
ax.barh(y_pos, genre_global.values, color=genre_colors, edgecolor="white", linewidth=0.4)
ax.set_yticks(y_pos)
ax.set_yticklabels(genre_global.index, fontsize=9)
ax.invert_yaxis()
style_ax(ax, "Total Global Sales", xlabel="Sales (millions)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.grid(axis="y", visible=False)
for i, val in enumerate(genre_global.values):
    ax.text(val + 0.3, i, f"{val:,.0f}M", va="center", fontsize=8)

# --- stacked regional ---
ax = axes[2]
bottom = np.zeros(len(genre_region))
for i, (col, name) in enumerate(zip(REGIONS, REG_NAMES)):
    vals = genre_region[col].values
    ax.barh(y_pos, vals, left=bottom, label=name,
            color=PALETTE[i], edgecolor="white", linewidth=0.4)
    bottom += vals
ax.set_yticks(y_pos)
ax.set_yticklabels(genre_region.index, fontsize=9)
ax.invert_yaxis()
style_ax(ax, "Regional Breakdown", xlabel="Sales (millions)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(millions_fmt))
ax.grid(axis="x", color=GRID, linewidth=0.8)
ax.grid(axis="y", visible=False)
ax.legend(loc="lower right", framealpha=0.9, fontsize=9)

plt.tight_layout()
plt.savefig(f"04_sales_by_genre.png", dpi=150, bbox_inches="tight")
plt.close()

# ── Summary stats printout ───────────────────────────────────────────────────
print("\n=== SUMMARY STATS ===")
print(f"Total records  : {len(df):,}")
print(f"Total global sales: {df[SALES_COL].sum():,.1f}M units")
print(f"\nTop 5 Platforms (global):\n{plat_global.head().to_string()}")
print(f"\nTop 5 Publishers (global):\n{pub_global.head().to_string()}")
print(f"\nTop 5 Genres (global):\n{genre_global.head().to_string()}")
print(f"\nBest sales year: {year_global.idxmax()} ({year_global.max():,.1f}M units)")
