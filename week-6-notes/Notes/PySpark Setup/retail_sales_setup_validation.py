from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, sum as spark_sum

spark = (
    SparkSession.builder
    .appName("RetailSalesSetupValidation")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

sales = [
    ("O1001", "Laptop", "Electronics", 1, 72000.0, "COMPLETE"),
    ("O1002", "Mouse", "Electronics", 3, 850.0, "COMPLETE"),
    ("O1003", "Chair", "Furniture", 2, 6500.0, "CANCELLED"),
    ("O1004", "Desk", "Furniture", 1, 11000.0, "COMPLETE"),
    ("O1005", "Notebook", "Stationery", 10, 75.0, "COMPLETE"),
    ("O1006", "Pen Pack", "Stationery", 4, 120.0, "COMPLETE"),
]

columns = [
    "order_id", "product", "category",
    "quantity", "unit_price", "status"
]

df = spark.createDataFrame(sales, columns)

completed = (
    df.filter(col("status") == "COMPLETE")
      .withColumn(
          "line_revenue",
          round(col("quantity") * col("unit_price"), 2)
      )
)

summary = (
    completed.groupBy("category")
    .agg(round(spark_sum("line_revenue"), 2).alias("revenue"))
    .orderBy(col("revenue").desc())
)

completed.show(truncate=False)
summary.show(truncate=False)

top_category = summary.first()
print(
    f"Top category: {top_category['category']} "  # pyright: ignore[reportOptionalSubscript]
    f"with revenue {top_category['revenue']}"  # pyright: ignore[reportOptionalSubscript]
)

spark.stop()