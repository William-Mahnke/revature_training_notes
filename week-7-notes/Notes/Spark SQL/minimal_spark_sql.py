from pyspark.sql import SparkSession

# Create or reuse a SparkSession.
spark = SparkSession.builder \
    .appName("SparkSQLSimpleExample") \
    .master("local[*]") \
    .getOrCreate()

# Each tuple is one row: sale_id, city, amount.
data = [
    (1, "Coimbatore", 1200.0),
    (2, "Chennai", 850.0),
    (3, "Coimbatore", 600.0),
    (4, "Chennai", 1050.0)
]

# Create a DataFrame with named columns.
sales_df = spark.createDataFrame(data, ["sale_id", "city", "amount"])

# Register a session-scoped temporary view.
sales_df.createOrReplaceTempView("sales")

# spark.sql returns another DataFrame.
city_totals = spark.sql("""
    SELECT city,
           ROUND(SUM(amount), 2) AS total_revenue
    FROM sales
    GROUP BY city
    ORDER BY total_revenue DESC
""")

city_totals.show()
spark.stop()

# Expected Output
# +----------+-------------+
# |city      |total_revenue|
# +----------+-------------+
# |Chennai   |1900.0       |
# |Coimbatore|1800.0       |
# +----------+-------------+