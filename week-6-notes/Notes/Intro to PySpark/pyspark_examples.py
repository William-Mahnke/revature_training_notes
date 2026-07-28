from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

spark = (
    SparkSession.builder
    .appName("PySparkExamples")
    .master("local[*]")
    .getOrCreate()
)


# CREATE DATAFRAME
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

# ---------------------------------------------------------
# SELECT AND FILTER
# ---------------------------------------------------------

# Transformation: choose columns
selected = df.select("name", "salary")

# Transformation: keep salaries above 60,000
high_paid = selected.filter(selected.salary > 60000)

# Action: execute and display
high_paid.show()

# ---------------------------------------------------------
# GROUP AND AGGREGATE
# ---------------------------------------------------------

summary = (
    df.groupBy("department")
      .agg(
          count("*").alias("employee_count"),
          avg("salary").alias("average_salary")
      )
)

summary.show()

# ---------------------------------------------------------
# READ AND WRITE FILES 
# ---------------------------------------------------------

# won't work, no sales.csv data exists
sales = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv("sales.csv")
)

sales.write.mode("overwrite").parquet("output/sales_parquet")



spark.stop()