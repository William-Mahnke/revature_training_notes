from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Create the Spark session.
spark = (
    SparkSession.builder
    .appName("StreamingWordCount")
    .master("local[*]")
    .getOrCreate()
)

# Reduce unnecessary log output.
spark.sparkContext.setLogLevel("WARN")

# Read continuously arriving text from the socket.
lines_df = (
    spark.readStream
    .format("socket")
    .option("host", "localhost")
    .option("port", 9999)
    .load()
)

# Split every line into individual words.
words_df = lines_df.select(
    explode(split(lines_df["value"], " ")).alias("word")
)

# Maintain a running count for every word.
word_counts_df = words_df.groupBy("word").count()

# Write the continuously updated result to the console.
query = (
    word_counts_df.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", "false")
    .start()
)

# Keep the application running until it is stopped.
query.awaitTermination()

spark.stop()