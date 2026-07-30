# --------------------------------------------------------------------
# First DAG Example
# --------------------------------------------------------------------
import pendulum
from airflow.sdk import dag, task, Asset

"""
--------------------------------------------------------------------
dag parameter
--------------------------------------------------------------------
dag_id: unique logical workflow name
schedule: defines when or what condition DAG runs
start_date: beginning of scheduling calculation
catchup: controls creation of historical scheduled runs
tags: classifies DAGs in the UI
default_args: resuable task defaults such as retries
--------------------------------------------------------------------
"""

@dag(
    dag_id="hello_airflow",
    schedule=None, 
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["training"],
)
def hello_airflow():

    @task
    def greet():
        return "Hello from Apache Airflow"

    @task
    def display(message: str):
        print(message)

    display(greet())

hello_airflow()

# --------------------------------------------------------------------
# Classic BashOperator for Airflow 3
# --------------------------------------------------------------------
from airflow.providers.standard.operators.bash import BashOperator

print_date = BashOperator(
    task_id="print_date",
    bash_command="date",
)

# --------------------------------------------------------------------
# Retries & Timeout Example 
# --------------------------------------------------------------------
from datetime import timedelta
from airflow.sdk import task

@task(
    retries=3,
    retry_delay=timedelta(minutes=5),
    execution_timeout=timedelta(minutes=30),
)
def call_partner_api():
    # Raise an exception on failure.
    # Airflow records the attempt and applies retry policy.
    pass

# --------------------------------------------------------------------
# XCom Task
# --------------------------------------------------------------------

@task
def extract() -> dict:
    return {"file_path": "/data/orders.csv", "row_count": 25000}

@task
def validate(metadata: dict):
    print(metadata["row_count"])

# --------------------------------------------------------------------
# Advanced Patterns
# --------------------------------------------------------------------

# branching
@task.branch
def choose_path(row_count: int) -> str:
    if row_count == 0:
        return "skip_processing"
    return "process_data"

# dynamic task mapping
@task
def discover_files():
    return ["store_01.csv", "store_02.csv", "store_03.csv"]

@task
def process_file(file_name: str):
    print(f"Processing {file_name}")

process_file.expand(file_name=discover_files())

# Asset-aware scheduling
sales_asset = Asset("s3://company-data/sales/daily/")

@task(outlets=[sales_asset])
def publish_sales():
    ...

# A downstream DAG can use the asset as its schedule.