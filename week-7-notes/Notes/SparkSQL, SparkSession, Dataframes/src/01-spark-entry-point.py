from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("01 Retail Spark SQL Demo")
    .master("local[*]")
    .getOrCreate()
)