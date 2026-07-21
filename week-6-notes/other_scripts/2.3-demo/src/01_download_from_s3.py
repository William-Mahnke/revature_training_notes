from pyspark.sql import SparkSession
import os
import urllib.request
from pathlib import Path
import ssl
import certifi

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DOWNLOAD_FILE = DATA_DIR / '01001099999.csv'

DATA_DIR.mkdir(parents=True, exist_ok=True)

spark = (
        SparkSession.builder
        .appName("NOAAWeatherRDD")
        .master("local[4]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.ui.showConsoleProgress", "false")
        .config("spark.local.dir", "C:/spark-temp" if os.name == "nt" else "/tmp/spark-temp")
        .config("spark.sql.warehouse.dir", "C:/spark-warehouse" if os.name == "nt" else "/tmp/spark-warehouse")
        .getOrCreate()
    )

sc = spark.sparkContext

S3_URL = (
    "https://noaa-gsod-pds.s3.amazonaws.com/"
    "2024/01001099999.csv"
)

def download_file(url: str, destination: Path) -> None:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(url, context=ssl_context) as response:
        destination.write_bytes(response.read())

if not DOWNLOAD_FILE.exists():
    download_file(S3_URL, DOWNLOAD_FILE)

raw_lines = sc.textFile(
    DOWNLOAD_FILE.resolve().as_uri(),
    4,
)

header = raw_lines.first()

data_lines = raw_lines.filter(
    lambda line: line != header
)

# diagnostic check
print(f"Partitions: {raw_lines.getNumPartitions()}")
print(f"Rows including header: {raw_lines.count()}")
print(f"Header: {header}")
print(f"First data row: {data_lines.first()}")