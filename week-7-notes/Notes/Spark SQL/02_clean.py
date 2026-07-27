from pyspark.sql import functions as F, SparkSession
from pyspark.sql.window import Window
from pyspark.sql.types import (
    StructType, StructField, StringType,
    IntegerType, DecimalType
)

spark = (
    SparkSession.builder
    .appName("RetailSparkSQL")
    .master("local[*]")
    .config("spark.sql.session.timeZone", "Asia/Kolkata")
    .getOrCreate()
)

sales_schema = StructType([
    StructField("sale_id", StringType(), False),
    StructField("sale_ts", StringType(), True),
    StructField("store_id", StringType(), True),
    StructField("city", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("unit_price", DecimalType(12, 2), True),
    StructField("payment_mode", StringType(), True),
])

sales_raw = (
    spark.read
    .option("header", True)
    .option("mode", "PERMISSIVE")
    .schema(sales_schema)
    .csv("data/sales.csv")
)

parsed = (
    sales_raw
    .withColumn("sale_timestamp", F.try_to_timestamp("sale_ts"))
    .withColumn("sale_date", F.try_to_date("sale_timestamp"))
    .withColumn("city", F.initcap(F.trim("city")))
    .withColumn("payment_mode", F.upper(F.trim("payment_mode")))
    .withColumn("revenue", F.col("quantity") * F.col("unit_price"))
)

# Build a readable reason instead of silently discarding invalid rows.
validated = parsed.withColumn(
    "reject_reason",
    F.when(F.col("sale_id").isNull(), "MISSING_SALE_ID")
     .when(F.col("sale_timestamp").isNull(), "INVALID_TIMESTAMP")
     .when(F.col("product_id").isNull(), "MISSING_PRODUCT")
     .when(F.col("quantity").isNull() | (F.col("quantity") <= 0), "INVALID_QUANTITY")
     .when(F.col("unit_price").isNull() | (F.col("unit_price") < 0), "INVALID_PRICE")
)

rejected = validated.filter(F.col("reject_reason").isNotNull())
valid_candidates = validated.filter(F.col("reject_reason").isNull())

# Deterministic deduplication: keep the latest timestamp for each sale_id.
dedup_window = Window.partitionBy("sale_id").orderBy(F.col("sale_timestamp").desc())
clean_sales = (
    valid_candidates
    .withColumn("row_num", F.row_number().over(dedup_window))
    .filter(F.col("row_num") == 1)
    .drop("row_num", "reject_reason", "sale_ts")
)

clean_sales.show(truncate=False)
rejected.select("sale_id", "reject_reason").show(truncate=False)

# ------------------------------------------------------------------------
# SQL VIEW, AGGREGATION, HAVING
# ------------------------------------------------------------------------
clean_sales.createOrReplaceTempView("clean_sales")

city_daily = spark.sql("""
SELECT
    sale_date,
    city,
    COUNT(*)                    AS transaction_count,
    SUM(quantity)               AS units_sold,
    ROUND(SUM(revenue), 2)      AS total_revenue,
    ROUND(AVG(revenue), 2)      AS average_transaction_value
FROM clean_sales
GROUP BY sale_date, city
HAVING SUM(revenue) >= 500
ORDER BY sale_date, total_revenue DESC
""")

print('-' * 60)
print("SQL VIEW, AGGREGATION, HAVING")
print('-' * 60)
city_daily.show(truncate=False)

# ------------------------------------------------------------------------
# JOIN FACT & DIMENSION DATA
# ------------------------------------------------------------------------

products = (
    spark.read
    .option("header", True)
    .option("inferSchema", False)
    .csv("data/products.csv")
)

# The product master is small in this demo, so broadcasting is reasonable.
enriched = clean_sales.join(
    F.broadcast(products),
    on="product_id",
    how="left"
)

unmatched_products = enriched.filter(F.col("product_name").isNull())
trusted_sales = enriched.filter(F.col("product_name").isNotNull())

trusted_sales.select(
    "sale_id", "city", "product_name", "category", "revenue"
).show(truncate=False)

unmatched_products.select("sale_id", "product_id").show()


# ------------------------------------------------------------------------
# WINDOW FUNCTIONS: RANK & RUNNING TOTAL
# ------------------------------------------------------------------------
product_revenue = (
    trusted_sales
    .groupBy("category", "product_id", "product_name")
    .agg(F.sum("revenue").alias("product_revenue"))
)

rank_window = Window.partitionBy("category").orderBy(
    F.col("product_revenue").desc()
)

ranked_products = product_revenue.withColumn(
    "category_rank",
    F.dense_rank().over(rank_window)
)

running_window = (
    Window.partitionBy("city")
    .orderBy("sale_date")
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)
)

daily_city = (
    trusted_sales
    .groupBy("sale_date", "city")
    .agg(F.sum("revenue").alias("daily_revenue"))
    .withColumn("running_revenue", F.sum("daily_revenue").over(running_window))
)

print('-' * 60)
print("WINDOW FUNCTION RESULTS")
print('-' * 60)

ranked_products.show(truncate=False)
daily_city.show(truncate=False)

# ------------------------------------------------------------------------
# EXAMPLE OF COMMON FUNCTIONS
# ------------------------------------------------------------------------

function_demo = (
    trusted_sales
    .withColumn("store_sale_key", F.concat_ws("-", "store_id", "sale_id"))
    .withColumn("sale_year", F.year("sale_date"))
    .withColumn("sale_month", F.month("sale_date"))
    .withColumn("price_band",
        F.when(F.col("unit_price") >= 1000, "Premium")
         .when(F.col("unit_price") >= 500, "Standard")
         .otherwise("Budget")
    )
    .withColumn("safe_category", F.coalesce("category", F.lit("Unknown")))
)

print('-' * 60)
print("FUNCTION DEMO RESULTS")
print('-' * 60)

function_demo.select(
    "store_sale_key", "sale_year", "sale_month", "price_band", "safe_category"
).show(truncate=False)

# ------------------------------------------------------------------------
# PARQUET OUTPUT
# ------------------------------------------------------------------------

output_path = "output/gold_sales"

(
    trusted_sales
    .repartition("sale_date")
    .write
    .mode("overwrite")
    .partitionBy("sale_date")
    .parquet(output_path)
)

# Filtering on the partition column lets Spark skip unrelated directories.
selected_day = (
    spark.read.parquet(output_path)
    .filter(F.col("sale_date") == F.lit("2026-07-02"))
)

print('-' * 60)
print("PARQUET DEMO RESULTS")
print('-' * 60)

selected_day.explain("formatted")
selected_day.show(truncate=False)

spark.stop()