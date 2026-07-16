import os
import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

# fix hostname warning (set before Spark starts)
os.environ["SPARK_LOCAL_HOSTNAME"] = "127.0.0.1"

# quiet bridge messages
logging.getLogger("py4j").setLevel(logging.ERROR)

# -------------------------------------------------------
# Part 1 - First PySpark Program
# -------------------------------------------------------
spark = (
    SparkSession.builder
    .appName("FirstPySparkApp")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("Asha", "Sales", 50000),
    ("Bala", "IT", 65000),
    ("Charan", "IT", 72000)
]

df = spark.createDataFrame(data, ["name", "department", "salary"])

df.show()

# -------------------------------------------------------
# Part 2 - Creating a DataFrame
# -------------------------------------------------------
employees = [
    (101, "Anu", "IT", 70000),
    (102, "Bala", "HR", 48000),
    (103, "Cathy", "IT", 82000),
    (104, "Deepak", "Sales", 55000)
]

df = spark.createDataFrame(
    employees,
    ["id", "name", "department", "salary"]
)

df.printSchema()
df.show()

# -------------------------------------------------------
# Part 3 - Select and Filter
# -------------------------------------------------------
# Transformation: choose columns
selected = df.select("name", "salary")

# Transformation: keep salaries above 60,000
high_paid = selected.filter(selected.salary > 60000)

# Action: execute and display
high_paid.show()

# -------------------------------------------------------
# Part 4 - Group and Aggregate
# -------------------------------------------------------
summary = (
    df.groupBy("department")
      .agg(
          count("*").alias("employee_count"),
          avg("salary").alias("average_salary")
      )
)

summary.show()

# -------------------------------------------------------
# Part 5 - Saving to File
# -------------------------------------------------------
sales = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv("sales.csv")
)

sales.write.mode("overwrite").parquet("output/sales_parquet")

spark.stop()