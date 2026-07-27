from pyspark.sql import functions as F

clean_orders = (
    raw_orders  # pyright: ignore[reportUndefinedVariable]
    .filter(F.col("order_id").isNotNull())
    .withColumn("order_date", F.to_date("order_timestamp"))
    .withColumn("net_amount",
                F.col("quantity") * F.col("unit_price")
                * (1 - F.col("discount_pct") / 100))
    .dropDuplicates(["order_id"])
)

clean_orders.createOrReplaceTempView("clean_orders")

daily_sales = spark.sql( # pyright: ignore[reportUndefinedVariable]
    """ 
    SELECT order_date, region, category,
        COUNT(DISTINCT order_id) AS orders,
        SUM(net_amount) AS revenue
    FROM clean_orders
    GROUP BY order_date, region, category
    """
) 