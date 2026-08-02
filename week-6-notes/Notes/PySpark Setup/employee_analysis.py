from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, desc

def main() -> None:
    spark = (
        SparkSession.builder
        .appName("EmployeeDepartmentAnalysis")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    employees = [
        (101, "Anu", "Data", 72000),
        (102, "Bala", "Data", 68000),
        (103, "Charan", "Cloud", 80000),
        (104, "Divya", "Cloud", 76000),
        (105, "Esha", "QA", 61000),
    ]

    df = spark.createDataFrame(
        employees,
        ["employee_id", "name", "department", "salary"]
    )

    print("=== Source Data ===")
    df.show()

    print("=== Employees earning at least 70,000 ===")
    df.filter(col("salary") >= 70000).show()

    print("=== Average salary by department ===")
    (
        df.groupBy("department")
        .agg(avg("salary").alias("average_salary"))
        .orderBy(desc("average_salary"))
        .show()
    )

    spark.stop()

if __name__ == "__main__":
    main()