import csv
from datetime import datetime

def optional_float(value, sentinel):
    value = value.strip()

    if not value:
        return None

    number = float(value)

    return None if number >= sentinel else number


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

        yield {
            "date": observation_date.isoformat(),
            "month": observation_date.strftime("%Y-%m"),
            "temperature_c": (
                temperature_f - 32.0  # pyright: ignore[reportOptionalOperand]
            ) * 5.0 / 9.0,
            "precipitation_mm": (
                None
                if precipitation_in is None
                else precipitation_in * 25.4
            ),
        }