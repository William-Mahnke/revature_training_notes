from typing import TypeAlias

from pyspark.sql import SparkSession
from pyspark import StorageLevel

spark = (SparkSession.builder
         .appName("PythonPracticalRDD")
         .master("local[4]")
         .getOrCreate())

sc = spark.sparkContext
sc.setLogLevel("WARN")

# ----------------------------------------------------
# Example of Creating and Using a RDD
# ----------------------------------------------------

transactions_data: list[tuple[int, str, str, str, int, float, str, str]] = [
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
products = sc.parallelize([
    ("Laptop", "Premium"), ("Mouse", "Standard"), ("Keyboard", "Standard"),
    ("Chair", "Standard"), ("Desk", "Premium"), ("Notebook", "Budget"),
    ("USB Cable", "Budget"), ("Monitor", "Premium"), ("Pen", "Budget"),
    ("Office Lamp", "Standard")
], 2)

# Tuple field positions used throughout
TXN_ID, CUSTOMER, PRODUCT, CATEGORY, QTY, PRICE, CITY, STATUS = range(8)

Transaction: TypeAlias = tuple[int, str, str, str, int, float, str, str]
SumCount: TypeAlias = tuple[float, int]


def txn_amount(txn: Transaction) -> float:
    return float(txn[4] * txn[5])


sum_count_zero: SumCount = (0.0, 0)


def add_amount_to_stats(acc: SumCount, value: float) -> SumCount:
    return (acc[0] + value, acc[1] + 1)


def add_int_to_sum_count(acc: SumCount, value: int) -> SumCount:
    return (acc[0] + value, acc[1] + 1)


def merge_sum_counts(left: SumCount, right: SumCount) -> SumCount:
    return (left[0] + right[0], left[1] + right[1])


def amount_to_stats(value: float) -> SumCount:
    return (value, 1)


def average_from_stats(stats: SumCount) -> float:
    return stats[0] / stats[1]


def rdd_debug_string(rdd) -> str:
    debug = rdd.toDebugString()
    return debug.decode("utf-8") if debug is not None else ""

# checking different aspects
print("Partitions:", transactions.getNumPartitions()) # 4
print("Rows:", transactions.count()) # 10
print("First row:", transactions.first()) # row with 1001
print("Sample rows:", transactions.take(3)) # rows with 1001, 1002, 1003
print("RDD name before setName:", transactions.name()) # None
transactions.setName("RetailTransactions")
print("RDD name after setName:", transactions.name()) # RetailTransactions

# ----------------------------------------------------
# Creation Examples
# ----------------------------------------------------

# 1. Python collection
numbers = sc.parallelize(range(1, 21), 4)

# 2. Distributed range
large_ids = sc.range(1, 1_000_001, 1, numSlices=8)

# 3. Text file: each record is one line
lines = sc.textFile("data/orders.csv", minPartitions=4)

# 4. Whole files: each record is (path, full content)
documents = sc.wholeTextFiles("data/policies/*.txt")

# 5. Empty RDD
empty = sc.emptyRDD()

# 6. Union many RDDs
jan_rdd = sc.parallelize([(1, "Jan")])
feb_rdd = sc.parallelize([(2, "Feb")])
mar_rdd = sc.parallelize([(3, "Mar")])
all_months = sc.union([jan_rdd, feb_rdd, mar_rdd])

# 7. Convert DataFrame rows to RDD
row_rdd = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "name"]).rdd

# ----------------------------------------------------
# Transformations Example
# ----------------------------------------------------

city_revenue = (transactions
    .filter(lambda t: t[STATUS] == "PAID")
    .map(lambda t: (t[CITY], txn_amount(t)))
    .reduceByKey(lambda a, b: a + b, numPartitions=2))

print(rdd_debug_string(city_revenue))
print(city_revenue.collect())

# ----------------------------------------------------
# Core Narrow Transformations
# ----------------------------------------------------

# map
amounts = transactions.map(lambda t: txn_amount(t))
print(amounts.collect())

# flatMap
sentences = sc.parallelize(["spark is fast", "python with spark"], 2)
words = sentences.flatMap(lambda line: line.split())
print(words.collect()) # ['spark', 'is', 'fast', 'python', 'with', 'spark']

# filter
paid = transactions.filter(lambda t: t[STATUS] == "PAID")
large_paid = paid.filter(lambda t: txn_amount(t) >= 10_000)
print(large_paid.collect())

# mapPartitions
def summarize_partition(rows):
    rows = list(rows)
    yield {
        "row_count": len(rows),
        "revenue": sum(txn_amount(t) for t in rows)
    }

partition_summaries = transactions.mapPartitions(summarize_partition)
print(partition_summaries.collect())

# mapPartitionsWithIndex
def inspect_partition(index, rows):
    rows = list(rows)
    yield (index, len(rows), [t[TXN_ID] for t in rows])

print(transactions.mapPartitionsWithIndex(inspect_partition).collect())

# glom
for partition_no, rows in enumerate(transactions.glom().collect()):
    print(partition_no, rows)

# key/value helpers
by_customer = transactions.keyBy(lambda t: t[CUSTOMER])
customer_keys = by_customer.keys()
original_rows = by_customer.values()

amount_by_customer = transactions.map(
    lambda t: (t[CUSTOMER], txn_amount(t))
)
with_tax = amount_by_customer.mapValues(lambda amount: round(amount * 1.18, 2))
expanded = sc.parallelize([("A", [1, 2]), ("B", [3])]).flatMapValues(lambda xs: xs)

print(customer_keys.take(3))
print(with_tax.take(3))
print(expanded.collect())

# ---------------------------------------------------------
# Set, Sampling, Sorting and Partition Transformations
# ---------------------------------------------------------

# 1. set-like operations
a = sc.parallelize([1, 2, 2, 3, 4], 2)
b = sc.parallelize([3, 4, 5], 2)

print(a.distinct().collect())
print(a.union(b).collect())       # duplicates remain
print(a.intersection(b).collect())
print(a.subtract(b).collect())
print(a.cartesian(b).take(8))

# 2. sampling and splitting
sample_without = transactions.sample(False, 0.4, seed=42)
sample_with = transactions.sample(True, 1.5, seed=42)
train, test = transactions.randomSplit([0.8, 0.2], seed=42)
fixed_sample = transactions.takeSample(False, 3, seed=42)

# Stratified sampling on a Pair RDD
by_category = transactions.map(lambda t: (t[CATEGORY], t))
fractions = {"Electronics": 0.5, "Furniture": 1.0, "Stationery": 0.5}
stratified = by_category.sampleByKey(False, fractions, seed=42)  # pyright: ignore[reportArgumentType]

# 3. sorting

# Sort complete records by transaction amount descending
sorted_transactions = transactions.sortBy(
    lambda t: txn_amount(t), ascending=False, numPartitions=2  # pyright: ignore[reportArgumentType]
)

# Pair-RDD key sort
city_amount = transactions.map(lambda t: (t[CITY], txn_amount(t)))
city_amount_sorted = city_amount.sortByKey(ascending=True, numPartitions=2)  # pyright: ignore[reportCallIssue]

print(sorted_transactions.take(5))

# 4. partition-count transformations
print("Original:", transactions.getNumPartitions())

more = transactions.repartition(8)       # full shuffle; increase or decrease
fewer = more.coalesce(2)                  # usually no shuffle; best for decreasing
balanced_fewer = more.coalesce(2, shuffle=True)

print(more.getNumPartitions(), fewer.getNumPartitions())

# 5. zips and IDs
names = sc.parallelize(["A", "B", "C"], 2)
scores = sc.parallelize([80, 90, 70], 2)
print(names.zip(scores).collect())
print(names.zipWithIndex().collect())
print(names.zipWithUniqueId().collect())

# ---------------------------------------------------------
# Pair RDD Operations
# ---------------------------------------------------------

# 1. aggregation choices

amount_by_category = transactions.map(
    lambda t: (t[CATEGORY], txn_amount(t))
)

# Sum values; map-side combine reduces shuffle traffic
sum_by_category = amount_by_category.reduceByKey(lambda a, b: a + b)

# Collect every value per key; can consume large memory
all_amounts = amount_by_category.groupByKey().mapValues(list)

# Zero value + within-partition function + between-partition function
stats_by_category = amount_by_category.aggregateByKey(
    sum_count_zero,
    add_amount_to_stats,
    merge_sum_counts,
)
average_by_category = stats_by_category.mapValues(average_from_stats)

# Generic aggregation foundation
average2 = amount_by_category.combineByKey(
    amount_to_stats,
    add_amount_to_stats,
    merge_sum_counts,
).mapValues(average_from_stats)

# Neutral zero value added with an associative function
folded = amount_by_category.foldByKey(0.0, lambda a, b: a + b)

# 2. joins and grouped relationships
txn_by_product = transactions.map(lambda t: (t[PRODUCT], t))

inner = txn_by_product.join(products)
left = txn_by_product.leftOuterJoin(products)
right = txn_by_product.rightOuterJoin(products)
full = txn_by_product.fullOuterJoin(products)

# Values from each RDD are grouped separately per key
co_grouped = txn_by_product.cogroup(products)
grouped_many = txn_by_product.groupWith(products)

print(inner.take(3))

# 3. other tools
# Remove keys found in another RDD
blocked_customers = sc.parallelize([("C102", True), ("C105", True)])
by_customer = transactions.map(lambda t: (t[CUSTOMER], t))
allowed = by_customer.subtractByKey(blocked_customers)

# Return matching values to the driver
print(by_customer.lookup("C101"))

# Number of records per key, returned as a driver dictionary
print(by_customer.countByKey())

# Reduce and return a driver dictionary
print(amount_by_category.reduceByKeyLocally(lambda a, b: a + b))

# Apply a stable partitioner
partitioned = amount_by_category.partitionBy(4)

# Partition and sort in one operation
sorted_partitioned = amount_by_category.repartitionAndSortWithinPartitions(numPartitions=4)  # pyright: ignore[reportCallIssue]

# ---------------------------------------------------------
# Actions and Statistical Operations
# ---------------------------------------------------------

# 1. safe inspection actions
print(transactions.count())
print(transactions.first())
print(transactions.take(3))
print(transactions.takeOrdered(3, key=lambda t: txn_amount(t)))  # pyright: ignore[reportArgumentType]
print(transactions.top(3, key=lambda t: txn_amount(t)))  # pyright: ignore[reportArgumentType]
print(transactions.isEmpty())

# Stream partitions through an iterator instead of building one huge list immediately
for row in transactions.toLocalIterator():
    pass

# 2. driver-return actions
small_result = transactions.collect()       # all records to driver
small_map = products.collectAsMap()       # keys should be unique
category_counts = transactions.map(lambda t: t[CATEGORY]).countByValue()
customer_counts = transactions.map(lambda t: (t[CUSTOMER], 1)).countByKey()

print(category_counts)
print(customer_counts)

# 3. aggregation actions
numbers = sc.parallelize([10, 20, 30, 40, 50], 2)

print(numbers.reduce(lambda a, b: a + b))
print(numbers.fold(0, lambda a, b: a + b))
print(numbers.aggregate(sum_count_zero, add_int_to_sum_count, merge_sum_counts))
print(numbers.treeReduce(lambda a, b: a + b, depth=2))
print(numbers.treeAggregate(
    sum_count_zero,
    add_int_to_sum_count,
    merge_sum_counts,
    depth=2
))

# 4. numeric and approximate actions
print(numbers.sum())
print(numbers.min(key=lambda x: x), numbers.max(key=lambda x: x))  # pyright: ignore[reportArgumentType]
print(numbers.mean())
print(numbers.variance(), numbers.stdev())
print(numbers.sampleVariance(), numbers.sampleStdev())
print(numbers.stats())
print(numbers.histogram([0, 20, 40, 60]))  # pyright: ignore[reportAttributeAccessIssue]

print(numbers.countApprox(timeout=1000, confidence=0.95))
print(numbers.countApproxDistinct(relativeSD=0.05))
print(numbers.meanApprox(timeout=1000, confidence=0.95))
print(numbers.sumApprox(timeout=1000, confidence=0.95))

# 5. side effect and output actions
def print_partition(rows):
    for row in rows:
        print(row)

transactions.foreach(lambda row: None)
transactions.foreachPartition(print_partition)
transactions.saveAsTextFile("output/transactions_text")
transactions.saveAsPickleFile("output/transactions_pickle")

# ---------------------------------------------------------
# Persistence, Checkpointing, and Lineage
# ---------------------------------------------------------

# 1. persistence

paid_enriched = (transactions
    .filter(lambda t: t[STATUS] == "PAID")
    .map(lambda t: (t, txn_amount(t))))

# Shortcut: default RDD cache level in PySpark
paid_enriched.cache()

# Or choose a level explicitly before materialization
paid_enriched.persist(StorageLevel.MEMORY_AND_DISK)

# First action computes and stores partitions
print(paid_enriched.count())
# Later action can reuse cached partitions
print(paid_enriched.take(3))

print(paid_enriched.getStorageLevel())
paid_enriched.unpersist(blocking=False)

# 2. reliable checkpoint
sc.setCheckpointDir("checkpoint/rdd")
long_lineage = transactions.map(lambda x: x).filter(lambda x: True)
long_lineage.checkpoint()
long_lineage.count()  # materializes the checkpoint
print(long_lineage.isCheckpointed())
print(long_lineage.getCheckpointFile())

# 3. local checkpoint
temporary_lineage_cut = transactions.map(lambda x: x)
temporary_lineage_cut.localCheckpoint()
temporary_lineage_cut.count()
print(temporary_lineage_cut.isLocallyCheckpointed())

# ---------------------------------------------------------
# Partitions & Performance Tuning
# ---------------------------------------------------------

# 1. partitions
print(transactions.getNumPartitions())
print(transactions.glom().map(len).collect())
print(rdd_debug_string(transactions))

# Inspect records per partition
sizes = transactions.mapPartitionsWithIndex(
    lambda idx, rows: [(idx, sum(1 for _ in rows))]
)
print(sizes.collect())

# 2. custom partition function
def customer_partitioner(customer_id):
    return int(customer_id[1:]) % 4

customer_amount = transactions.map(
    lambda t: (t[CUSTOMER], txn_amount(t))
)
partitioned = customer_amount.partitionBy(4, customer_partitioner)
print(partitioned.glom().collect())

# ---------------------------------------------------------
# Broadcast Variables & Acculumators
# ---------------------------------------------------------

# 1. broadcast variable
tax_rate_by_category = {
    "Electronics": 0.18,
    "Furniture": 0.12,
    "Stationery": 0.05
}
tax_rates_bc = sc.broadcast(tax_rate_by_category)

def add_tax(t: Transaction) -> tuple[int, float, float]:
    amount = txn_amount(t)
    return (t[0], amount, amount * tax_rates_bc.value[t[3]])


with_tax = transactions.map(add_tax)
print(with_tax.collect())

tax_rates_bc.unpersist() 
# tax_rates_bc.destroy()  # permanent; cannot use afterward

# 2. accumulator - executor-to-driver counter
invalid_status_count = sc.accumulator(0)
valid_statuses = {"PAID", "PENDING", "CANCELLED"}

def validate(row):
    if row[STATUS] not in valid_statuses:
        invalid_status_count.add(1)
    return row

validated = transactions.map(validate)
validated.count()  # an action is required
print("Invalid statuses:", invalid_status_count.value)

# ---------------------------------------------------------
# Input, Output, and Advanced APIs
# ---------------------------------------------------------

# 1. Text, Pickle, SequenceFile, & Hadoop output
# Directory output: one part file per output partition
transactions.map(str).saveAsTextFile("output/transactions")
transactions.saveAsPickleFile("output/transactions_pickle", batchSize=10)

pair_output = transactions.map(lambda t: (str(t[TXN_ID]), t[PRODUCT]))
pair_output.saveAsSequenceFile("output/transaction_products")

# Hadoop APIs require the correct Java InputFormat/OutputFormat classes and config
# pair_output.saveAsNewAPIHadoopFile(path, outputFormatClass, keyClass, valueClass)

# 2. External commands with pipe
# UNIX-like environment example; every partition is piped to the command
upper = sc.parallelize(["spark", "python"], 2).pipe("tr a-z A-Z")
print(upper.collect())

# 3. Barrier execution
# Advanced/experimental: all tasks in the barrier stage must launch together
def barrier_task(rows):
    from pyspark import BarrierTaskContext
    ctx = BarrierTaskContext.get()
    ctx.barrier()
    return rows

barrier_rdd = transactions.barrier().mapPartitions(barrier_task)

# 4. Resource profiles and lifecycle utilities
print(transactions.id())
print(transactions.name())
print(transactions.getResourceProfile())
print(transactions.getStorageLevel())

# Advanced cleanup; use only when you understand recomputation implications
# transactions.cleanShuffleDependencies(blocking=False)

# A job-group-aware collection option
# result = transactions.collectWithJobGroup("retail-audit", "Collect retail audit")