from pyspark.sql import SparkSession
import urllib.request
from pathlib import Path
import ssl
import certifi

spark = (SparkSession.builder
         .appName("PythonPracticalRDD")
         .master("local[4]")
         .getOrCreate())

sc = spark.sparkContext
sc.setLogLevel("WARN")

S3_URL = (
    "https://noaa-gsod-pds.s3.amazonaws.com/"
    "2024/01001099999.csv"
)

DOWNLOADED_FILE = (
    Path(__file__).resolve().parent.parent / "data" / "01001099999.csv"
)

DOWNLOADED_FILE.parent.mkdir(parents=True, exist_ok=True)
ssl_context = ssl.create_default_context(cafile=certifi.where())
with urllib.request.urlopen(S3_URL, context=ssl_context) as response:
    DOWNLOADED_FILE.write_bytes(response.read())

raw_lines = sc.textFile(
    DOWNLOADED_FILE.resolve().as_uri(),
    4,
)

header = raw_lines.first()

data_lines = raw_lines.filter(
    lambda line: line != header
)