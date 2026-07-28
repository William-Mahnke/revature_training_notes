from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as spark_sum
from pyspark.sql.types import (
    StructType, StructField, StringType,
    DoubleType, TimestampType
)

spark = (
    SparkSession.builder
    .appName("FoodOrderStreaming")
    .master("local[*]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# A streaming file source requires a predefined schema.
order_schema = StructType([
    StructField("event_id", StringType(), False),
    StructField("event_type", StringType(), False),
    StructField("order_id", StringType(), False),
    StructField("city", StringType(), True),
    StructField("order_amount", DoubleType(), True),
    StructField("event_time", TimestampType(), True)
])

# Read new JSON files arriving in the input directory.
orders_df = (
    spark.readStream
    .schema(order_schema)
    .json("data/incoming_orders")
)

# Retain only valid order-created events.
valid_orders_df = orders_df.filter(
    (col("event_type") == "ORDER_CREATED") &
    col("order_id").isNotNull() &
    (col("order_amount") > 0)
)

# Calculate live order count and sales amount by city.
city_summary_df = (
    valid_orders_df
    .groupBy("city")
    .agg(
        count("*").alias("order_count"),
        spark_sum("order_amount").alias("sales_amount")
    )
)

query = (
    city_summary_df.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .option(
        "checkpointLocation",
        "checkpoints/food_order_summary"
    )
    .start()
)

query.awaitTermination()

spark.stop()