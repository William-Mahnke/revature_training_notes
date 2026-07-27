from pyspark.sql import SparkSession
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

sales_raw.printSchema()
sales_raw.show(truncate=False)

spark.stop()