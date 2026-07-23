import argparse
from pyspark.sql import SparkSession, functions as F, types as T

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    spark = SparkSession.builder.appName("RetailSalesDataprocETL").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    schema = T.StructType([
        T.StructField("order_id", T.StringType(), True),
        T.StructField("order_date", T.StringType(), True),
        T.StructField("customer_id", T.StringType(), True),
        T.StructField("state", T.StringType(), True),
        T.StructField("category", T.StringType(), True),
        T.StructField("quantity", T.IntegerType(), True),
        T.StructField("unit_price", T.DoubleType(), True),
        T.StructField("payment_status", T.StringType(), True),
    ])

    raw = (spark.read.option("header", True).option("mode", "PERMISSIVE")
           .schema(schema).csv(args.input)
           .withColumn("order_date", F.to_date("order_date", "yyyy-MM-dd")))

    valid = (
        F.col("order_id").isNotNull() & (F.trim("order_id") != "") &
        F.col("order_date").isNotNull() & F.col("customer_id").isNotNull() &
        F.col("state").isNotNull() & F.col("category").isNotNull() &
        (F.col("quantity") > 0) & (F.col("unit_price") > 0) &
        (F.upper("payment_status") == "PAID")
    )

    rejected = (raw.filter(~valid)
        .withColumn("rejection_reason",
            F.when(F.col("order_id").isNull() | (F.trim("order_id") == ""), "MISSING_ORDER_ID")
             .when(F.col("order_date").isNull(), "INVALID_ORDER_DATE")
             .when(F.col("quantity").isNull() | (F.col("quantity") <= 0), "INVALID_QUANTITY")
             .when(F.col("unit_price").isNull() | (F.col("unit_price") <= 0), "INVALID_UNIT_PRICE")
             .when(F.upper("payment_status") != "PAID", "NOT_PAID")
             .otherwise("MISSING_REQUIRED_VALUE")))

    clean = (raw.filter(valid).dropDuplicates(["order_id"])
        .withColumn("revenue", F.round(F.col("quantity") * F.col("unit_price"), 2))
        .withColumn("processed_at_utc", F.current_timestamp()))

    summary = (clean.groupBy("order_date","state","category")
        .agg(F.countDistinct("order_id").alias("order_count"),
             F.sum("quantity").alias("units_sold"),
             F.round(F.sum("revenue"),2).alias("total_revenue"),
             F.round(F.avg("revenue"),2).alias("average_order_value"))
        .orderBy("order_date","state","category"))

    state_summary = (clean.groupBy("state")
        .agg(F.countDistinct("order_id").alias("order_count"),
             F.round(F.sum("revenue"),2).alias("total_revenue"))
        .orderBy(F.desc("total_revenue")))

    clean.write.mode("overwrite").parquet(f"{args.output}/clean_orders")
    rejected.write.mode("overwrite").json(f"{args.output}/rejected_orders")
    summary.coalesce(1).write.mode("overwrite").option("header",True).csv(f"{args.output}/daily_state_category_summary")
    state_summary.coalesce(1).write.mode("overwrite").option("header",True).csv(f"{args.output}/state_summary")

    print("="*60)
    print("Raw rows:", raw.count())
    print("Clean rows:", clean.count())
    print("Rejected rows:", rejected.count())
    print("Output:", args.output)
    print("="*60)
    state_summary.show(truncate=False)
    spark.stop()

if __name__ == "__main__":
    main()
