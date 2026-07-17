from operator import add
from pyspark import StorageLevel
from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .appName("PythonPracticalRDD")
         .master("local[4]")
         .getOrCreate())

sc = spark.sparkContext
sc.setLogLevel("WARN")

# transaction data 
transactions_data = [
    (1001, "C101", "Laptop",      "Electronics", 1, 65000.0, "Chennai",   "PAID"),
    (1002, "C102", "Mouse",       "Electronics", 2,   800.0, "Coimbatore","PAID"),
    (1003, "C101", "Keyboard",    "Electronics", 1,  1500.0, "Chennai",   "PAID"),
    (1004, "C103", "Chair",       "Furniture",   1,  7000.0, "Bengaluru", "PENDING"),
    (1005, "C104", "Desk",        "Furniture",   1, 12000.0, "Hyderabad", "PAID"),
    (1006, "C105", "Notebook",    "Stationery",  5,   100.0, "Chennai",   "PAID"),
    (1007, "C102", "USB Cable",   "Electronics", 3,   300.0, "Coimbatore","CANCELLED"),
    (1008, "C106", "Monitor",     "Electronics", 2, 15000.0, "Hyderabad", "PAID"),
    (1009, "C103", "Pen",         "Stationery", 10,    20.0, "Bengaluru", "PAID"),
    (1010, "C107", "Office Lamp", "Furniture",   2,  1200.0, "Chennai",   "PAID"),
]

transactions = sc.parallelize(transactions_data, 4)

# 1. Validate and count rejected rows
invalid_rows = sc.accumulator(0)
valid_statuses = {"PAID", "PENDING", "CANCELLED"}

def validate(t):
    if t[STATUS] not in valid_statuses or t[QTY] <= 0 or t[PRICE] < 0:  # pyright: ignore[reportUndefinedVariable]
        invalid_rows.add(1)
        return False
    return True

valid = transactions.filter(validate)

# 2. Keep paid transactions and calculate gross amount
paid = (valid
    .filter(lambda t: t[STATUS] == "PAID")  # pyright: ignore[reportUndefinedVariable]
    .map(lambda t: (t, t[QTY] * t[PRICE]))  # pyright: ignore[reportUndefinedVariable]
    .persist(StorageLevel.MEMORY_AND_DISK))

# 3. First action materializes cache
paid_count = paid.count()

# 4. Revenue by category
category_revenue = (paid
    .map(lambda x: (x[0][CATEGORY], x[1]))  # pyright: ignore[reportUndefinedVariable]
    .reduceByKey(add, numPartitions=2)
    .sortBy(lambda pair: pair[1], ascending=False))

# 5. Customer statistics: total and order count
customer_stats = (paid
    .map(lambda x: (x[0][CUSTOMER], x[1]))  # pyright: ignore[reportUndefinedVariable]
    .aggregateByKey(
        (0.0, 0),
        lambda acc, amount: (acc[0] + amount, acc[1] + 1),  # pyright: ignore[reportArgumentType]
        lambda a, b: (a[0] + b[0], a[1] + b[1])  # pyright: ignore[reportArgumentType]
    )
    .mapValues(lambda x: {"total": x[0], "orders": x[1], "average": x[0] / x[1]}))

# 6. Join transactions to product segment
transaction_products = paid.map(lambda x: (x[0][PRODUCT], (x[0], x[1])))  # pyright: ignore[reportUndefinedVariable]
enriched = transaction_products.leftOuterJoin(products)  # pyright: ignore[reportUndefinedVariable]

# 7. Top three transactions without collecting everything
result_top3 = paid.takeOrdered(3, key=lambda x: -x[1])

# 8. Inspect and save small curated outputs
print("Paid count:", paid_count)
print("Invalid rows:", invalid_rows.value)
print("Category revenue:", category_revenue.collect())
print("Customer stats:", customer_stats.collect())
print("Top 3:", result_top3)

enriched.map(str).saveAsTextFile("output/retail_enriched")
paid.unpersist()