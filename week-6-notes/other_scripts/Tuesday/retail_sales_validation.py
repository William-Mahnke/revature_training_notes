from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, sum as spark_sum, to_date, date_trunc, when
import time

spark = (
    SparkSession.builder
    .appName("RetailSalesSetupValidation")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# input("Open http://localhost:4040, inspect the UI, then press Enter...")
# time.sleep(10)

sales = [
    ("O1001", "Laptop", "Electronics", 1, 72000.0, "2026-07-01", "COMPLETE"),
    ("O1002", "Mouse", "Electronics", 3, 850.0, "2026-07-05", "COMPLETE"),
    ("O1003", "Chair", "Furniture", 2, 6500.0, "2026-07-10", "CANCELLED"),
    ("O1004", "Desk", "Furniture", 1, 11000.0, "2026-08-02", "COMPLETE"),
    ("O1005", "Notebook", "Stationery", 10, 75.0, "2026-08-15", "COMPLETE"),
    ("O1006", "Pen Pack", "Stationery", 4, 120.0, "2026-08-20", "COMPLETE"),
]
columns = [
    "order_id", "product", "category",
    "quantity", "unit_price", "order_date", "status"
]

df = (
    spark.createDataFrame(sales, columns)
    .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
)


completed = (
    df.filter(col("status") == "COMPLETE")
      .withColumn("gross_revenue", col("quantity") * col("unit_price"))
      .withColumn(
          "discount_rate",
          when(col("quantity") >= 5, 0.05).otherwise(0.0)
      )
      .withColumn(
          "line_revenue",
          round(col("gross_revenue") * (1 - col("discount_rate")), 2)
      )
)

monthly_revenue = (
    completed
    .withColumn("order_month", date_trunc("month", col("order_date")))
    .groupBy("order_month")
    .agg(round(spark_sum("line_revenue"), 2).alias("revenue"))
    .orderBy(col("order_month"))
)

summary = (
    completed.groupBy("category")
    .agg(round(spark_sum("line_revenue"), 2).alias("revenue"))
    .orderBy(col("revenue").desc())
)

completed.show(truncate=False)
summary.show(truncate=False)
monthly_revenue.show(truncate=False)

# save summary to csv using coalesce(1)
(
    summary
    .coalesce(1)
    .write.mode("overwrite")
    .option("header", True)
    .csv("output/summary")
)


top_category = summary.first()
print(
    f"Top category: {top_category['category']} "  # pyright: ignore[reportOptionalSubscript]
    f"with revenue {top_category['revenue']}"  # pyright: ignore[reportOptionalSubscript]
)

print("Summary physical plan:")
summary.explain("formatted")

spark.stop()