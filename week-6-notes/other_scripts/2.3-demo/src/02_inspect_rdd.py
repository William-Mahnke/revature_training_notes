from pyspark.sql import SparkSession
from datetime import datetime
import csv
import json
import os
import shutil
from pathlib import Path

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

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOWNLOAD_FILE = PROJECT_ROOT / "data" / "01001099999.csv"
GENERATED_DIR = PROJECT_ROOT / "output" / "generated"
CLEAN_OUTPUT = GENERATED_DIR / "cleaned_weather_rdd"
REPORT_OUTPUT = GENERATED_DIR / "monthly_weather_report_rdd"

# accumulators
missing_precip = sc.accumulator(0)
missing_gust = sc.accumulator(0)
missing_snow = sc.accumulator(0)
rejected_rows = sc.accumulator(0)

# =========================================================
# Cleaning & Validating Functions
# =========================================================

def optional_float(value, sentinel):
    value = value.strip()

    if not value:
        return None

    number = float(value)

    return None if number >= sentinel else number

def parse_weather_flags(frshtt: str) -> dict[str, bool]:
    flags = frshtt.strip().ljust(6, "0")

    return {
        "fog": flags[0] == "1",
        "rain": flags[1] == "1",
        "snow_or_ice": flags[2] == "1",
        "hail": flags[3] == "1",
        "thunder": flags[4] == "1",
        "tornado": flags[5] == "1",
    }


def parse_partition(lines):
    reader = csv.reader(lines)

    for values in reader:
        observation_date = datetime.strptime(
            values[1].strip(),
            "%Y-%m-%d",
        ).date()

        temperature_f = optional_float(
            values[6],
            9999.9,
        )

        precipitation_in = optional_float(
            values[24],
            99.99,
        )

        gust_knots = optional_float(values[19], 999.9)
        snow_depth_in = optional_float(values[26], 999.9)
        weather_flags = parse_weather_flags(values[27])

        yield {
            "date": observation_date.isoformat(),
            "month": observation_date.strftime("%Y-%m"),
            "temperature_c": (
                None
                if temperature_f is None
                else (temperature_f - 32.0) * 5.0 / 9.0
            ),
            "precipitation_mm": (
                None
                if precipitation_in is None
                else precipitation_in * 25.4
            ),
            "gust_knots": gust_knots,
            "snow_depth_in": snow_depth_in,
            **weather_flags,
        }

def validate_and_count(row):
    # Required field: mean temperature must be present
    if row["temperature_c"] is None:
        rejected_rows.add(1)
        return False
    # Optional gaps: count them, but keep the row
    if row["precipitation_mm"] is None:
        missing_precip.add(1)
    if row["gust_knots"] is None:
        missing_gust.add(1)
    if row["snow_depth_in"] is None:
        missing_snow.add(1)
    return True

# =========================================================
# Aggregation Functions
# =========================================================

def add_month_value(acc, row):
    (
        days,
        temp_sum,
        temp_count,
        precip_sum,
        precip_count,
        rainy_days,
        max_gust,
        fog_days,
        rain_days,
        snow_days,
        hail_days,
        thunder_days,
        tornado_days,
    ) = acc

    days += 1
    temp_sum += row["temperature_c"]
    temp_count += 1

    if row["precipitation_mm"] is not None:
        precip_sum += row["precipitation_mm"]
        precip_count += 1
        if row["precipitation_mm"] > 0:
            rainy_days += 1
    
    if row["gust_knots"] is not None:
        max_gust = (
            row["gust_knots"]
            if max_gust is None
            else max(max_gust, row["gust_knots"])
        )
    
    fog_days += int(row["fog"])
    rain_days += int(row["rain"])
    snow_days += int(row["snow_or_ice"])
    hail_days += int(row["hail"])
    thunder_days += int(row["thunder"])
    tornado_days += int(row["tornado"])

    return (
        days,
        temp_sum,
        temp_count,
        precip_sum,
        precip_count,
        rainy_days,
        max_gust,
        fog_days,
        rain_days,
        snow_days,
        hail_days,
        thunder_days,
        tornado_days,
    )

def merge_month_values(a, b):
    (
        days_a, temp_sum_a, temp_count_a,
        precip_sum_a, precip_count_a, rainy_a, max_gust_a,
        fog_a, rain_a, snow_a, hail_a, thunder_a, tornado_a,
    ) = a
    (
        days_b, temp_sum_b, temp_count_b,
        precip_sum_b, precip_count_b, rainy_b, max_gust_b,
        fog_b, rain_b, snow_b, hail_b, thunder_b, tornado_b,
    ) = b

    if max_gust_a is None:
        max_gust = max_gust_b
    elif max_gust_b is None:
        max_gust = max_gust_a
    else:
        max_gust = max(max_gust_b, max_gust_a)
    
    return (
        days_a + days_b,
        temp_sum_a + temp_sum_b,
        temp_count_a + temp_count_b,
        precip_sum_a + precip_sum_b,
        precip_count_a + precip_count_b,
        rainy_a + rainy_b,
        max_gust,
        fog_a + fog_b,
        rain_a + rain_b,
        snow_a + snow_b,
        hail_a + hail_b,
        thunder_a + thunder_b,
        tornado_a + tornado_b,
    )

def to_report_metrics(acc):
    (
        days,
        temp_sum,
        temp_count,
        precip_sum,
        precip_count,
        rainy_days,
        max_gust,
        fog_days,
        rain_days,
        snow_days,
        hail_days,
        thunder_days,
        tornado_days,
    ) = acc
    return {
        "observation_days": days,
        "avg_temperature_c": round(temp_sum / temp_count, 2),
        "total_precipitation_mm": round(precip_sum, 2),
        "rainy_days": rainy_days,
        "max_gust_knots": max_gust,
        "fog_days": fog_days,
        "rain_indicator_days": rain_days,
        "snow_days": snow_days,
        "hail_days": hail_days,
        "thunder_days": thunder_days,
        "tornado_days": tornado_days,
    }

# =========================================================
# Save helpers
# =========================================================

def reset_output(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)


def format_report_csv(month_metrics: tuple[str, dict]) -> str:
    month, metrics = month_metrics
    return ",".join(
        [
            month,
            str(metrics["observation_days"]),
            str(metrics["avg_temperature_c"]),
            str(metrics["total_precipitation_mm"]),
            str(metrics["rainy_days"]),
            str(metrics["max_gust_knots"]),
            str(metrics["fog_days"]),
            str(metrics["snow_days"]),
        ]
    )


raw_rdd = sc.textFile(DOWNLOAD_FILE.resolve().as_uri(), 4)
header = raw_rdd.first()

cleaned_rdd = (
    raw_rdd
    .filter(lambda line: line != header and bool(line.strip()))
    .mapPartitions(parse_partition)
    .filter(validate_and_count)
    .cache()
)

clean_count = cleaned_rdd.count()

print(f"Clean observations: {clean_count}")
print(f"Rejected rows (missing temperature): {rejected_rows.value}")
print(f"Missing precipitation: {missing_precip.value}")
print(f"Missing gust: {missing_gust.value}")
print(f"Missing snow depth: {missing_snow.value}")

zero = (
    0,       # observation days
    0.0,     # temperature sum
    0,       # temperature count
    0.0,     # precipitation sum
    0,       # precipitation count
    0,       # rainy days
    None,    # maximum gust
    0, 0, 0, 0, 0, 0
)

monthly_report = (
    cleaned_rdd
    .map(lambda row: (row["month"], row))
    .aggregateByKey(
        zero,
        add_month_value,
        merge_month_values,
    )
    .mapValues(to_report_metrics)
    .sortByKey()
)

GENERATED_DIR.mkdir(parents=True, exist_ok=True)

reset_output(CLEAN_OUTPUT)
cleaned_rdd.map(json.dumps).coalesce(1).saveAsTextFile(
    CLEAN_OUTPUT.resolve().as_uri()
)

reset_output(REPORT_OUTPUT)
monthly_report.map(format_report_csv).coalesce(1).saveAsTextFile(
    REPORT_OUTPUT.resolve().as_uri()
)

print(f"Saved cleaned RDD to: {CLEAN_OUTPUT}")
print(f"Saved monthly report to: {REPORT_OUTPUT}")

