from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("FirstPySparkApp")
    .master("local[*]")
    .getOrCreate()
)

sc = spark.sparkContext

# ----------------------------------------------------
# Normal Python Variables Not Working 
# ----------------------------------------------------

driver_counter = 0

def increment_on_worker(_):
    global driver_counter
    driver_counter += 1

sc.parallelize(range(1, 11), 4).foreach(
    increment_on_worker
)

print(driver_counter) # 0

# ----------------------------------------------------
# Broadcast Variables
# ----------------------------------------------------

"""
product_master = {{ 
    "P100": {{"category": "Electronics"}}, 
    "P200": {{"category": "Grocery"}},  
}}

product_broadcast = sc.broadcast(
    product_master
)

enriched = orders_rdd.map(
    lambda order: {{
        **order,
        **product_broadcast.value.get(
            order["product_id"],
            {{"category": "UNKNOWN"}},
        ),
    }}
)

product_broadcast.unpersist()
"""

# ----------------------------------------------------
# Numeric Accumulators
# ----------------------------------------------------

invalid_records = sc.accumulator(0)

orders_df = (
    spark.read
         .option("header", True)
         .option("inferSchema", True)
         .csv("orders.csv")
)

orders_rdd = orders_df.rdd.map(lambda row: row.asDict())

def validate(order):
    valid = (
        bool(order["city"])
        and order["quantity"] > 0
        and 0 <= order["discount_pct"] <= 100
    )

    if not valid:
        invalid_records.add(1)

    return valid

valid_orders = orders_rdd.filter(
    validate
).cache()

valid_count = valid_orders.count()

print(valid_count)
print(invalid_records.value)

# ----------------------------------------------------
# Broadcast Demo
# ----------------------------------------------------

"""
product_broadcast = sc.broadcast(
    load_product_master()
)

enriched = (
    lines
    .filter(lambda line: line != header)
    .map(parse_order)
    .filter(lambda row: "_parse_error" not in row)
    .map(lambda order: {{
        **order,
        **product_broadcast.value.get(
            order["product_id"],
            {{
                "product_name": "UNKNOWN",
                "category": "UNKNOWN",
                "manager": "UNASSIGNED",
                "cost_price": 0.0,
            }},
        ),
    }})
)
"""

# ----------------------------------------------------
# Accumulator Demo
# ----------------------------------------------------

invalid_records = sc.accumulator(0)
non_completed = sc.accumulator(0)

def validate2(order):
    if "_parse_error" in order:
        invalid_records.add(1)
        return False

    if (
        not order["city"]
        or order["quantity"] <= 0
        or not 0 <= order["discount_pct"] <= 100
    ):
        invalid_records.add(1)
        return False

    if order["status"] != "COMPLETED":
        non_completed.add(1)

    return True

# ----------------------------------------------------
# Custom Reason Updates
# ----------------------------------------------------

""""
updates = {{}}

if not order["city"]:
    updates["missing_city"] = 1

if order["quantity"] <= 0:
    updates["invalid_quantity"] = 1

if updates:
    quality_counts.add(updates)
"""

# ----------------------------------------------------
# Retail Pipeline Example
# ----------------------------------------------------

"""
product_broadcast = sc.broadcast(
    load_product_master()
)

quality_counts = sc.accumulator(
    {{
        "missing_city": 0,
        "invalid_quantity": 0,
        "invalid_discount": 0,
        "unknown_product": 0,
        "non_completed": 0,
    }},
    DictAccumulatorParam(),
)

valid_completed = (
    lines
    .filter(lambda line: line != header)
    .map(parse_order)
    .filter(validate_and_classify)
    .cache()
)

valid_count = valid_completed.count()

summary = (
    valid_completed
    .map(enrich)
    .reduceByKey(
        lambda left, right: (
            left[0] + right[0],
            left[1] + right[1],
            left[2] + right[2],
        )
    )
)
"""

spark.stop()