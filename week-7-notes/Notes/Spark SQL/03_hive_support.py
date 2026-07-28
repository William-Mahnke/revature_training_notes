from spark.sql import SparkSession

# Use enableHiveSupport() when your environment is configured for Hive catalog support.
spark = (
    SparkSession.builder
    .appName("RetailCatalogDemo")
    .enableHiveSupport()
    .getOrCreate()
)

spark.sql("CREATE DATABASE IF NOT EXISTS retail")
spark.sql("USE retail")

trusted_sales.write.mode("overwrite").saveAsTable("silver_sales")

spark.sql("""
CREATE OR REPLACE VIEW city_sales_view AS
SELECT sale_date, city, SUM(revenue) AS total_revenue
FROM silver_sales
GROUP BY sale_date, city
""")

spark.sql("SHOW TABLES").show(truncate=False)
spark.sql("SELECT * FROM city_sales_view").show()