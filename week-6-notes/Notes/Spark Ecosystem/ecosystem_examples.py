from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

spark = SparkSession.builder.appName("SparkEcosystemExamples").getOrCreate()
sc = spark.sparkContext

# ---------------------------------------------------------
# CORE
# ---------------------------------------------------------
numbers = sc.parallelize([1, 2, 3, 4, 5])
squares = numbers.map(lambda x: x * x)

print(squares.collect())

# ---------------------------------------------------------
# SPARK SQL
# ---------------------------------------------------------
employees = [
    ("Asha", "IT", 70000),
    ("Bala", "HR", 50000),
    ("Cathy", "IT", 82000)
]

df = spark.createDataFrame(
    employees,
    ["name", "department", "salary"]
)

df.createOrReplaceTempView("employees")

spark.sql("""
    SELECT department, AVG(salary) AS average_salary
    FROM employees
    GROUP BY department
""").show()

# ---------------------------------------------------------
# STRUCTURED STREAMING
# ---------------------------------------------------------

stream_df = (
    spark.readStream
         .format("rate")
         .option("rowsPerSecond", 5)
         .load()
)

result = stream_df.selectExpr("timestamp", "value * 10 AS score")

query = (
    result.writeStream
          .format("console")
          .outputMode("append")
          .start()
)

query.awaitTermination()

# ---------------------------------------------------------
# MLlib
# ---------------------------------------------------------

training = spark.createDataFrame([
    (1.0, 10.0, 100.0),
    (2.0, 20.0, 200.0),
    (3.0, 30.0, 300.0)
], ["feature1", "feature2", "label"])

assembler = VectorAssembler(
    inputCols=["feature1", "feature2"],
    outputCol="features"
)

prepared = assembler.transform(training)

model = LinearRegression(
    featuresCol="features",
    labelCol="label"
).fit(prepared)

model.transform(prepared).show()

spark.stop()