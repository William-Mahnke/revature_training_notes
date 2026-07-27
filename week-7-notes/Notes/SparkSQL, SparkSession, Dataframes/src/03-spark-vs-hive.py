"""Historical SQLContext and HiveContext compatibility demo."""
from pyspark.sql import SQLContext,HiveContext,SparkSession
def main():
    spark = (
    SparkSession.builder
    .appName("03 Legacy Contexts")
    .master("local[*]")
    .config("spark.sql.session.timeZone", "Asia/Kolkata")
    .getOrCreate()
    )
    sc=spark.sparkContext
    try:
        sql_context=SQLContext.getOrCreate(sc); hive_context=HiveContext(sc)
        print('SparkSession:',type(spark).__name__);print('SQLContext:',type(sql_context).__name__);print('HiveContext:',type(hive_context).__name__)
        df=sql_context.createDataFrame([('Electronics',131540.0),('Fashion',19340.0),('Grocery',5744.0)],['category','revenue'])
        df.createOrReplaceTempView('legacy_sales')
        hive_context.sql('SELECT category,revenue FROM legacy_sales ORDER BY revenue DESC').show()
        print('Use SparkSession for all new applications.')
    finally: spark.stop()
if __name__=='__main__': main()