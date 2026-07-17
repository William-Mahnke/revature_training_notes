from pyspark.sql import SparkSession

"""
Commands to run before smoke test to verify successful installations within terminal:
python --version
java -version
python -m pip show pyspark
python -c "import pyspark; print('PySpark:', pyspark.__version__)"

Quick test of PySpark shell:
spark.version
spark.range(1, 6).show()
spark.stop()
exit()
"""


spark = (
    SparkSession.builder
    .appName("PySparkSetupSmokeTest")
    .master("local[2]")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

print("Spark version:", spark.version)
print("Master:", spark.sparkContext.master)
print("Application:", spark.sparkContext.appName)

df = spark.createDataFrame(
    [(1, "Java"), (2, "Python"), (3, "PySpark")],
    ["id", "technology"]
)

df.show()
print("Row count:", df.count())

spark.stop()