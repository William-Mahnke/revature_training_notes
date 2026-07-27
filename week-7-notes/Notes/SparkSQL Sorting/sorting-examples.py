from pyspark.sql import functions as F, SparkSession

spark = (
    SparkSession.builder
    .appName("Sorting Examples")
    .master("local[*]")
    .config("spark.sql.session.timeZone", "Asia/Kolkata")
    .getOrCreate()
)

orders_df = spark.table("retail_orders")

# PySpark global sort/ordeBy
report_df = (
    orders_df
    .filter(F.col("status") == "PAID")
    .withColumn("revenue", F.round(F.col("quantity") * F.col("unit_price"), 2))
    .orderBy(
        F.col("revenue").desc_nulls_last(),
        F.col("region").asc(),
        F.col("order_id").asc()
    )
)

report_df.show(truncate=False)

# range-organized output
range_sorted_df = (
    orders_df
    .filter(F.col("status") == "PAID")
    .withColumn("revenue", F.col("quantity") * F.col("unit_price"))
    .repartitionByRange(4, F.col("revenue").asc())
    .sortWithinPartitions(
        F.col("revenue").asc_nulls_last(),
        F.col("order_id").asc()
    )
)

range_sorted_df.explain("formatted")
range_sorted_df.write.mode("overwrite").parquet("/tmp/revenue_ranges")