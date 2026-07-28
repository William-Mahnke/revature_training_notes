from pyspark.sql import SparkSession

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

# Expected output 
# Expected output:
# +------+----------+------+
# |  name|department|salary|
# +------+----------+------+
# |  Asha|     Sales| 50000|
# |  Bala|        IT| 65000|
# |Charan|        IT| 72000|
# +------+----------+------+

spark.stop()