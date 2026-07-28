from pyspark.sql import SparkSession
from pyspark import AccumulatorParam

spark = (
        SparkSession.builder
        .appName("EmployeeDepartmentAnalysis")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

sc = spark.sparkContext

# ------------------------------------------------
# Broadcast
# ------------------------------------------------

product_master = {
    "P100": {"category": "Electronics"},
    "P200": {"category": "Grocery"},
}

product_broadcast = sc.broadcast(
    product_master
)

enriched = orders_rdd.map(  # pyright: ignore[reportUndefinedVariable]
    lambda order: {
        **order,
        **product_broadcast.value.get(
            order["product_id"],
            {"category": "UNKNOWN"},
        ),
    }
)

product_broadcast.unpersist()

# ------------------------------------------------
# Accumulator
# ------------------------------------------------

invalid_records = sc.accumulator(0)

def validate(order):
    valid = (
        bool(order["city"])
        and order["quantity"] > 0
        and 0 <= order["discount_pct"] <= 100
    )

    if not valid:
        invalid_records.add(1)

    return valid

valid_orders = orders_rdd.filter(  # pyright: ignore[reportUndefinedVariable]
    validate
).cache()

valid_count = valid_orders.count()

print(valid_count)
print(invalid_records.value)

# ------------------------------------------------
# Custom Accumulator Types
# ------------------------------------------------

class DictAccumulatorParam(AccumulatorParam):
    def zero(self, value):
        return {key: 0 for key in value}

    def addInPlace(self, left, right):  # pyright: ignore[reportIncompatibleMethodOverride]
        for key, count in right.items():
            left[key] = left.get(key, 0) + count
        return left

quality_counts = sc.accumulator(
    {
        "missing_city": 0,
        "invalid_quantity": 0,
        "invalid_discount": 0,
    },
    DictAccumulatorParam(),
)
