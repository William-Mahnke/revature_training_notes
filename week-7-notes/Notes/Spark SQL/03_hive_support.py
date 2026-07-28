from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Use enableHiveSupport() when your environment is configured for Hive catalog support.
spark = (
    SparkSession.builder
    .appName("RetailCatalogDemo")
    .enableHiveSupport()
    .getOrCreate()
)

spark.sql("CREATE DATABASE IF NOT EXISTS retail")
spark.sql("USE retail")

trusted_sales = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("data/trusted_sales")
)


trusted_sales.write.mode("overwrite").saveAsTable("silver_sales")

spark.sql("""
CREATE OR REPLACE VIEW city_sales_view AS
SELECT sale_date, city, SUM(revenue) AS total_revenue
FROM silver_sales
GROUP BY sale_date, city
""")

spark.sql("SHOW TABLES").show(truncate=False)
spark.sql("SELECT * FROM city_sales_view").show()

# ------------------------------------------------------------------------
# JDBC Read with Parallelism
# ------------------------------------------------------------------------

# jdbc_url = "jdbc:mysql://localhost:3306/retail"

# customers = (
#     spark.read
#     .format("jdbc")
#     .option("url", jdbc_url)
#     .option("dbtable", "customers")
#     .option("user", "retail_user")
#     .option("password", "${READ_FROM_SECRET_MANAGER}")
#     .option("driver", "com.mysql.cj.jdbc.Driver")
#     .option("partitionColumn", "customer_id")
#     .option("lowerBound", 1)
#     .option("upperBound", 1000000)
#     .option("numPartitions", 8)
#     .option("fetchsize", 10000)
#     .load()
# )

# ------------------------------------------------------------------------
# Caching
# ------------------------------------------------------------------------

# Inspect the plan before changing performance settings.
trusted_sales.explain("formatted")

# Cache only because the same expensive result is reused below.
trusted_sales.cache()
trusted_sales.count()  # Materialize the cache.

report_1 = trusted_sales.groupBy("city").agg(F.sum("revenue"))
report_2 = trusted_sales.groupBy("category").agg(F.avg("revenue"))

report_1.show()
report_2.show()

trusted_sales.unpersist()