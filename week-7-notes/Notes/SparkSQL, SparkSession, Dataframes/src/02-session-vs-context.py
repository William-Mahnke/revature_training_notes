from pyspark.sql import SparkSession

"""SparkSession versus SparkContext."""
def main():
    spark = (
    SparkSession.builder
    .appName("02 SparkSession vs Spark Context")
    .master("local[*]")
    .config("spark.sql.session.timeZone", "Asia/Kolkata")
    .getOrCreate()
    )
    sc=spark.sparkContext
    try:
        print('SparkSession object:',spark); print('SparkContext object:',sc)
        rdd=sc.parallelize([10,20,30,40],2)
        print('RDD total:',rdd.reduce(lambda a,b:a+b))
        df=spark.createDataFrame([(1,'Anita','Data Engineering'),(2,'Rahul','Analytics'),(3,'Meena','Data Engineering')],['employee_id','name','department'])
        df.createOrReplaceTempView('employees')
        spark.sql("SELECT department,COUNT(*) employee_count FROM employees GROUP BY department ORDER BY employee_count DESC").show()
    finally: spark.stop()
if __name__=='__main__': main()