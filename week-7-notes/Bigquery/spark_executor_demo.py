from pyspark.sql import SparkSession, functions as F

spark = (
    SparkSession.builder
    .appName("SlotVsExecutorRetailDemo")
    .master("local[4]")       # remove this line in Databricks
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")

orders = (
    spark.range(1, 500001)
    .withColumnRenamed("id", "order_id")
    .withColumn(
        "order_date",
        F.date_add(F.lit("2025-01-01").cast("date"),
                   (F.col("order_id") % 730).cast("int"))
    )
    .withColumn(
        "customer_id",
        F.concat(F.lit("C"), F.lpad((F.col("order_id") % 20000).cast("string"), 5, "0"))
    )
    .withColumn(
        "category",
        F.element_at(
            F.array(*[F.lit(x) for x in ["Electronics","Grocery","Fashion","Furniture","Sports"]]),
            ((F.col("order_id") % 5) + 1).cast("int")
        )
    )
    .withColumn("quantity", ((F.col("order_id") % 5) + 1).cast("int"))
    .withColumn("unit_price", (F.lit(10) + ((F.col("order_id") * 17) % 990)).cast("decimal(10,2)"))
    .repartition(8, "order_date")
)

orders.createOrReplaceTempView("orders")
print("Input partitions:", orders.rdd.getNumPartitions())

# --------------------------------------------------------------------------------------------------------------
# SQL QUERY
# --------------------------------------------------------------------------------------------------------------

result = spark.sql("""
SELECT category,
       ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM orders
WHERE order_date BETWEEN DATE '2026-07-01' AND DATE '2026-07-31'
GROUP BY category
ORDER BY revenue DESC
""")

result.explain("formatted")
result.show(truncate=False)

# --------------------------------------------------------------------------------------------------------------
# VIEW SPARK UI
# --------------------------------------------------------------------------------------------------------------

input("Open http://localhost:4040, inspect Jobs/Stages/Executors, then press Enter...")
spark.stop()