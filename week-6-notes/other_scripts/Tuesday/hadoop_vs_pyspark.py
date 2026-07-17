# ---------------------------------------------------
# Hadoop Mapper & Reducer
# ---------------------------------------------------

"""
--- Mapper ---
String[] f = line.split(",", -1);
String city = f[2].trim();
String category = f[3].trim();
int quantity = Integer.parseInt(f[4].trim());
long unitPrice = Long.parseLong(f[5].trim());
int discount = Integer.parseInt(f[6].trim());
String status = f[7].trim();

if (!"COMPLETED".equalsIgnoreCase(status)) return;

long netRevenuePaise =
    quantity * unitPrice * (100L - discount);

context.write(
    new Text(city + "|" + category),
    new LongWritable(netRevenuePaise)
);
--- Reducer ---
long totalPaise = 0L;
for (LongWritable value : values) {
    totalPaise += value.get();
}
context.write(key, new Text(
    BigDecimal.valueOf(totalPaise)
      .divide(BigDecimal.valueOf(100), 2, RoundingMode.HALF_UP)
      .toPlainString()
));
--- Command to Run ---
hdfs dfs -put sales.csv /training/input/
hadoop jar retail-revenue-mapreduce-1.0.0.jar \
  /training/input /training/output
hdfs dfs -cat /training/output/part-r-00000
"""

# ---------------------------------------------------
# PySpark Equivalent
# ---------------------------------------------------

from pyspark.sql import SparkSession
import pyspark.sql.functions as F

spark = (
    SparkSession.builder
    .appName("FirstPySparkApp")
    .master("local[*]")
    .getOrCreate()
)

sales = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv("sales.csv")
)

result = (
    sales
    .filter(
        (F.col("status") == "COMPLETED")
        & (F.col("quantity") > 0)
        & (F.col("unit_price") >= 0)
        & F.col("discount_pct").between(0, 100)
    )
    .withColumn(
        "net_revenue",
        F.round(
            F.col("quantity") * F.col("unit_price")
            * (F.lit(1) - F.col("discount_pct") / F.lit(100)),
            2
        )
    )
    .groupBy("city", "category")
    .agg(
        F.count("*").alias("order_count"),
        F.sum("quantity").alias("units_sold"),
        F.round(F.sum("net_revenue"), 2).alias("total_revenue")
    )
    .orderBy(F.desc("total_revenue"))
)
result.show(truncate=False)

spark.stop()