# 🚀 DataOps for Freshers

**DataOps Lifecycle • CI/CD for dbt & Airflow • Automated Testing**

> **Learning Goal:** Understand how modern data teams develop, test, deploy, orchestrate, and monitor reliable data pipelines using DataOps practices.

---

## 📌 Table of Contents

1. [What is DataOps?](#1-what-is-dataops)
2. [Why DataOps?](#2-why-do-we-need-dataops)
3. [DataOps Lifecycle](#3-dataops-lifecycle)
4. [Key Practice — Collaboration](#4-key-practice--collaboration)
5. [Key Practice — Automation](#5-key-practice--automation)
6. [Key Practice — Monitoring](#6-key-practice--monitoring)
7. [CI/CD in Data Engineering](#7-cicd-in-data-engineering)
8. [CI/CD for dbt](#8-cicd-for-dbt)
9. [Automated Testing with dbt](#9-automated-testing-with-dbt)
10. [CI/CD for Airflow](#10-cicd-for-airflow)
11. [Automated Testing in Data Workflows](#11-automated-testing-in-data-workflows)
12. [End-to-End Real-World Mini Project](#12-end-to-end-real-world-mini-project)
13. [Complete DataOps Execution Flow](#13-complete-dataops-execution-flow)
14. [Recommended Classroom Demo Order](#14-recommended-classroom-demo-order)
15. [Key Takeaways](#15-key-takeaways)

---

## 1. What is DataOps?

> [!IMPORTANT]
> **DataOps = Data Operations**

DataOps is a set of practices used to **develop, test, deploy, operate, and monitor data pipelines reliably and collaboratively**.

It brings DevOps-style practices into data engineering.

### 💡 Simple comparison

| Software Engineering | Data Engineering |
| --- | --- |
| Application Code | SQL / Python / dbt / DAG Code |
| Unit Testing | Data & Pipeline Testing |
| Build | dbt Compile / Build |
| Deployment | Deploy Models / DAGs |
| Application Monitoring | Pipeline & Data Monitoring |
| CI/CD | Data Pipeline CI/CD |

---

### 🎯 Simple real-world scenario

Imagine an e-commerce company receiving customer orders every day.

🛒 **Website Orders** → 📥 **Raw Data** → 🧱 **Transformation** → 🏢 **Data Warehouse** → 📊 **Dashboard**

The data team must make sure that:

- new data arrives correctly,
- transformations are correct,
- bad data is detected,
- code changes are reviewed,
- deployments are automated,
- failures are monitored,
- business dashboards stay reliable.

That complete operating approach is **DataOps**.

---

## 2. Why do we need DataOps?

Suppose a developer changes this model:

```sql
select
    order_id,
    customer_id,
    amount
from orders
```

to:

```sql
select
    order_id,
    customer_id
from orders
```

The `amount` column is accidentally removed.

### ❌ Without DataOps

👨‍💻 **Developer Changes Code** → 🚀 **Deploy** → 📊 **Dashboard Breaks** → 📞 **User Complains**

### ✅ With DataOps

👨‍💻 **Code Change** → 🔁 **CI Starts** → 🧪 **Tests Run** → 🛑 **Failure Detected**

> [!TIP]
> **Goal:** Detect problems before bad code or bad data reaches production.

---

## 3. DataOps Lifecycle

The DataOps lifecycle can be remembered as:

📝 **PLAN** → 💻 **DEVELOP** → 🌿 **VERSION CONTROL** → 🧪 **TEST** → 🚀 **DEPLOY** → ⚙️ **ORCHESTRATE** → 👀 **MONITOR** → 📈 **IMPROVE**

---

### 3.1 📝 Plan

The team decides:

- What data is required?
- Where does the data come from?
- What transformations are required?
- Which analytical tables should be created?
- What data quality rules should exist?

#### Example requirement

> Management wants **daily revenue by region**.

Required data may include:

- Customers
- Orders
- Products
- Region information

Final output:

**`daily_sales_summary`**

---

### 3.2 💻 Develop

Data engineers create:

- SQL
- Python
- dbt models
- Airflow DAGs
- configuration files
- data tests

#### Example dbt staging model

```sql
-- models/staging/stg_orders.sql

select
    order_id,
    customer_id,
    order_date,
    amount
from raw.orders
```

#### Example mart model

```sql
-- models/marts/daily_sales.sql

select
    order_date,
    sum(amount) as revenue
from {{ ref('stg_orders') }}
group by order_date
```

---

### 3.3 🌿 Version Control

Instead of files like:

```text
orders_final.sql
orders_final2.sql
orders_latest.sql
orders_final_latest2.sql
```

use **Git**.

👨‍💻 **Developer** → 🌿 **Feature Branch** → 🔃 **Pull Request** → ✅ **Review & Merge**

#### Commands

```bash
git checkout -b feature/customer-model
```

```bash
git add .
```

```bash
git commit -m "Add customer transformation"
```

```bash
git push origin feature/customer-model
```

---

## 4. Key Practice — Collaboration

Collaboration means multiple data engineers can safely work on the same project.

### Common tools

- Git
- GitHub / GitLab
- Branches
- Pull Requests
- Code Reviews
- Issues
- Documentation

### Example

| Engineer | Responsibility | Branch |
| --- | --- | --- |
| Engineer A | Customer Model | `feature/customers` |
| Engineer B | Orders Model | `feature/orders` |
| Engineer C | Products Model | `feature/products` |

- 👩‍💻 **Engineer A**
- 👨‍💻 **Engineer B**
- 👩‍💻 **Engineer C**

All changes go through: 🐙 **Git Repository** (shared source of truth) → 🔍 **Review** → 🚀 **Production**

---

## 5. Key Practice — Automation

Automation means:

> **Do not repeatedly perform predictable tasks manually.**

### ❌ Manual approach

1. Run SQL.
2. Run transformation.
3. Check output.
4. Execute tests.
5. Copy files.
6. Deploy.
7. Run pipeline.

### ✅ Automated approach

📤 **Git Push** → 🤖 **CI Pipeline** → 🧪 **Tests** → 🚀 **Deploy**

For dbt, automation may execute:

```text
dbt deps
dbt compile
dbt build
```

For Python:

```text
pytest
```

For Airflow:

```text
airflow dags list
airflow dags test ...
```

---

## 6. Key Practice — Monitoring

Automation is incomplete without monitoring.

Imagine an Airflow pipeline is scheduled every day at **6:00 AM**.

### Normal run

⏰ **6:00 AM** → 📥 **Extract** → 🧱 **Transform** → 📤 **Load**

### Failure run

❌ **Task Failure** → 📝 **Logs** → 🔔 **Alert** → 🛠️ **Investigation**

---

### What should we monitor?

#### ⚙️ Pipeline Health

- Did the pipeline execute?
- Did it complete successfully?
- Which task failed?
- How long did it take?
- How many retries occurred?

#### 🧪 Data Health

- Did expected rows arrive?
- Are key columns null?
- Are IDs duplicated?
- Did row count suddenly drop?
- Is today's data available?
- Is revenue unexpectedly zero?

---

## 7. CI/CD in Data Engineering

### CI = Continuous Integration

Whenever code changes, automatically validate and test it.

👨‍💻 **Developer** → 📤 **Push / PR** → 🤖 **CI** → 🧪 **Validate & Test** → ✅ / ❌ **Pass or Fail**

---

### CD = Continuous Delivery / Deployment

After CI succeeds:

✅ **CI Passed** → 🧪 **DEV / TEST** → 🚀 **PRODUCTION**

In data engineering, deployment may include:

- dbt models,
- SQL scripts,
- Python code,
- Airflow DAGs,
- configuration files.

---

## 8. CI/CD for dbt

### Example project structure

```text
dataops-demo/
│
├── models/
│   ├── staging/
│   │   └── stg_orders.sql
│   │
│   └── marts/
│       └── daily_sales.sql
│
├── tests/
│
├── dbt_project.yml
│
└── .github/
    └── workflows/
        └── dbt-ci.yml
```

---

### 8.1 Check dbt configuration

```bash
dbt debug
```

Use it to check:

- profile configuration,
- project configuration,
- database connection,
- warehouse connectivity.

---

### 8.2 Compile

```bash
dbt compile
```

📝 **dbt Model** → 🧩 **Resolve Jinja/ref()** → 📄 **Executable SQL**

---

### 8.3 Execute models

```bash
dbt run
```

Example:

📦 **RAW.ORDERS** → 🧱 **STG_ORDERS** → 📊 **DAILY_SALES**

---

## 9. Automated Testing with dbt

Suppose the data contains:

| order_id | customer_id | amount |
| ---: | ---: | ---: |
| 1001 | 1 | 200 |
| 1002 | 2 | 300 |
| 1002 | 3 | 500 |
| NULL | 4 | 400 |

Problems:

- duplicate `order_id`,
- null `order_id`.

---

### 9.1 Unique and Not Null Tests

```yaml
version: 2

models:
  - name: stg_orders

    columns:
      - name: order_id
        data_tests:
          - unique
          - not_null
```

Execute:

```bash
dbt test
```

---

### 9.2 Relationship Test

Customers:

| customer_id |
| ---: |
| 101 |
| 102 |
| 103 |

Orders contain customer `999`.

```yaml
- name: customer_id
  data_tests:
    - relationships:
        arguments:
          to: ref('stg_customers')
          field: customer_id
```

The test detects records that reference customers that do not exist.

---

### 9.3 Accepted Values

Valid statuses:

- NEW
- SHIPPED
- DELIVERED
- CANCELLED

```yaml
- name: status
  data_tests:
    - accepted_values:
        arguments:
          values:
            - NEW
            - SHIPPED
            - DELIVERED
            - CANCELLED
```

---

### 9.4 dbt build

Instead of:

```bash
dbt run
dbt test
```

you can often execute:

```bash
dbt build
```

🧱 **Models** + 🧪 **Tests** + 🔗 **Dependencies** → 🚀 **dbt build**

---

## 10. CI/CD for Airflow

Airflow is commonly used for **workflow orchestration**.

Example pipeline:

📥 **Extract** → 📦 **Load** → 🧱 **dbt Run** → 🧪 **dbt Test** → 📊 **Publish**

---

### 10.1 Simple Airflow DAG

```python
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="ecommerce_data_pipeline",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False
) as dag:

    extract = BashOperator(
        task_id="extract_orders",
        bash_command="python /opt/scripts/extract_orders.py"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/dbt && dbt run"
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/dbt && dbt test"
    )

    extract >> dbt_run >> dbt_test
```

---

### 10.2 Validate the DAG

List DAGs:

```bash
airflow dags list
```

List tasks:

```bash
airflow tasks list ecommerce_data_pipeline
```

Test the DAG:

```bash
airflow dags test ecommerce_data_pipeline
```

---

### 10.3 `dag.test()`

You can also add:

```python
if __name__ == "__main__":
    dag.test()
```

Then:

```bash
python ecommerce_data_pipeline.py
```

This is useful while developing and debugging locally.

---

## 11. Automated Testing in Data Workflows

Automated testing can be understood in layers.

| 🧑‍💻 Code Tests | ⚙️ Pipeline Tests | 🧪 Data Tests | 💼 Business Tests | 🕒 Freshness Tests |
| --- | --- | --- | --- | --- |
| pytest | Airflow DAG validation | dbt tests | Business rules | Latest data checks |

---

### 11.1 Code Testing

Python function:

```python
def calculate_total(price, quantity):
    return price * quantity
```

Test:

```python
def test_calculate_total():
    assert calculate_total(100, 2) == 200
```

Run:

```bash
pytest
```

If someone changes the function to:

```python
return price + quantity
```

the automated test fails.

---

### 11.2 Pipeline Testing

Check that:

- the DAG parses,
- expected tasks exist,
- dependencies are correct,
- required configuration is available.

Useful commands:

```bash
airflow dags list
```

```bash
airflow dags test ecommerce_data_pipeline
```

---

### 11.3 Data Testing

Examples:

#### Null Rule

```text
order_id cannot be NULL
```

#### Unique Rule

```text
order_id must be unique
```

#### Relationship Rule

```text
orders.customer_id must exist in customers.customer_id
```

#### Accepted Value Rule

```text
status must be one of:
NEW, SHIPPED, DELIVERED, CANCELLED
```

---

### 11.4 Business Rule Testing

Technical validity does not always mean business validity.

Examples:

```text
quantity = -50
```

or:

```text
order_amount = -20000
```

Possible custom test:

```sql
select *
from orders
where amount < 0
```

If rows are returned:

> ❌ **Business-rule test failed**

---

### 11.5 Freshness Testing

A pipeline can succeed but still process stale data.

Example:

- Latest source date: August 15
- Expected date: August 17

Pipeline status:

> ✅ SUCCESS

Data status:

> ⚠️ STALE

Things to monitor:

- last record timestamp,
- source freshness,
- missing partitions,
- row-count changes,
- unexpected volume changes.

---

## 12. End-to-End Real-World Mini Project

### 🛒 Scenario

An e-commerce company wants:

> **Daily sales reporting by product and customer region.**

#### Modern box view

🛒 **Orders** (Source) → 📥 **Raw Layer** (Snowflake) → ⚙️ **Airflow** (Orchestration) → 🧱 **dbt Staging** → 📈 **dbt Marts** → 🧪 **Automated Tests** → 🏢 **Data Mart** → 📊 **Dashboard**

---

### Project Structure

```text
dataops-ecommerce/
│
├── dags/
│   └── ecommerce_pipeline.py
│
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_orders.sql
│   │   └── marts/
│   │       └── daily_sales.sql
│   │
│   ├── dbt_project.yml
│   └── models.yml
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
│
└── .github/
    └── workflows/
        └── data-ci.yml
```

---

## 13. Complete DataOps Execution Flow

### Stage A — Local Development

💻 **VS Code** → 📝 **SQL / Python** → 🧪 **Local Tests**

Useful dbt commands:

```bash
dbt debug
dbt compile
dbt run
dbt test
dbt build
```

---

### Stage B — Collaboration

```bash
git checkout -b feature/order-transform
```

```bash
git add .
git commit -m "Add order staging model"
git push origin feature/order-transform
```

Then create a Pull Request.

🌿 **Feature Branch** → 🔃 **Pull Request** → 👀 **Review**

---

### Stage C — CI

Example GitHub Actions workflow:

```yaml
name: Data Pipeline CI

on:
  pull_request:

jobs:
  test-data-pipeline:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Python syntax validation
        run: |
          python -m compileall dags

      - name: Run Python tests
        run: |
          pytest

      - name: Compile dbt
        run: |
          cd dbt_project
          dbt compile

      - name: Run dbt build
        run: |
          cd dbt_project
          dbt build
```

#### CI box flow

🔃 **Pull Request** → 🐍 **Python Validation** → 🧩 **dbt Compile** → 🧪 **dbt Build** → ✅ **PASS**

If any step fails:

> 🛑 **Do not merge until the problem is fixed.**

---

### Stage D — CD

✅ **CI Passed** → 👀 **Approval** → 🔀 **Merge** → 🚀 **Deploy**

---

### Stage E — Production Orchestration

Airflow handles scheduled data workflow execution.

⏰ **Schedule** → 📥 **Extract** → 🧱 **dbt Run** → 🧪 **dbt Test** → 📊 **Publish**

---

### Stage F — Monitoring

⚙️ **Pipeline** → 📝 **Logs** → 📈 **Metrics** → 🔔 **Alerts** → 🛠️ **Fix**

---

## 14. Recommended Classroom Demo Order

### 🟦 Demo 1 — Manual Pipeline

📄 **CSV** → ❄️ **Snowflake** → 🧱 **dbt run** → 📊 **Table**

Goal: Understand transformation first.

---

### 🟩 Demo 2 — Add dbt Tests

🧱 **dbt run** → 🧪 **dbt test** → ✅ / ❌ **Result**

Introduce duplicate or null data intentionally.

---

### 🟨 Demo 3 — Add Airflow

⚙️ **Airflow** → 🧱 **dbt run** → 🧪 **dbt test**

Goal: Automate pipeline execution.

---

### 🟪 Demo 4 — Add Git Collaboration

🌿 **Branch** → 💾 **Commit** → 📤 **Push** → 🔃 **PR**

---

### 🟥 Demo 5 — Add CI

🔃 **PR** → 🤖 **GitHub Actions** → 🧩 **Compile** → 🧪 **Test** → ✅ **Pass**

---

### 🔥 Demo 6 — Intentionally Create an Error

Good data:

| ORDER_ID | CUSTOMER_ID | AMOUNT |
| ---: | --- | ---: |
| 101 | C01 | 500 |
| 102 | C02 | 700 |
| 103 | C03 | 300 |

Result:

> ✅ Tests pass

Change to:

| ORDER_ID | CUSTOMER_ID | AMOUNT |
| ---: | --- | ---: |
| 101 | C01 | 500 |
| 102 | C02 | 700 |
| 102 | C03 | 300 |

Execute:

```bash
dbt test
```

Result:

> ❌ `unique` test fails.

This gives trainees a clear reason for automated testing.

---

### 🟧 Demo 7 — Merge and Deploy

🔃 **Pull Request** → ✅ **CI Pass** → 👀 **Review** → 🔀 **Merge**

---

### 🟦 Demo 8 — Production Pipeline

📥 **Extract** → 🧱 **Transform** → 🧪 **Test** → 📊 **Publish**

---

### 🟥 Demo 9 — Monitoring Failure

Break one task intentionally.

Then inspect:

```text
Airflow
  → DAG
  → Failed Task
  → Logs
  → Root Cause
```

Ask trainees to identify:

- Which task failed?
- When did it fail?
- Why did it fail?
- Should it be retried?
- Did downstream tasks execute?

---

## 15. Key Takeaways

### 🟦 DataOps

> **Collaborate → Automate → Test → Deploy → Monitor → Improve**

DataOps is the overall operating methodology for reliable data platforms.

---

### 🟩 CI/CD

> **CI/CD protects code changes before they reach production.**

CI answers:

> “Is this new pipeline code safe?”

CD answers:

> “How do we reliably move the approved change into the target environment?”

---

### 🟨 Airflow

> **Airflow orchestrates when and in what order data pipeline tasks run.**

Example:

```text
Every day at 6 AM
```

---

### 🟪 dbt

> **dbt transforms warehouse data and provides strong data testing capabilities.**

---

### 🟥 Automated Testing

> **Automated testing continuously checks code, pipelines, transformations, data quality, and business rules.**

---

## 🧠 CI/CD vs Airflow vs dbt

| Tool / Practice | Main Question |
| --- | --- |
| **Git** | What changed? |
| **GitHub** | How do team members collaborate? |
| **GitHub Actions** | Is the code safe to integrate/deploy? |
| **dbt** | How should raw data become analytical data? |
| **dbt Tests** | Is the transformed data valid? |
| **Airflow** | When and in what order should pipeline tasks run? |
| **pytest** | Does the Python code behave correctly? |
| **Snowflake** | Where is data stored and processed? |
| **Power BI / Looker** | How does the business consume the result? |

---

## 🌟 Final End-to-End Mental Model

👨‍💻 **DEVELOP** (SQL • Python • dbt • DAG) → 🤝 **COLLABORATE** (Git • Branch • PR) → 🤖 **VALIDATE** (CI • Tests) → 🚀 **OPERATE** (Deploy • Airflow • dbt) → 👀 **MONITOR** (Logs • Alerts • Quality) → ♻️ **IMPROVE** (Fix • Commit • Repeat)

> [!NOTE]
> Once trainees understand this lifecycle, they move from simply **writing data pipelines** to understanding how professional teams **operate production-quality data platforms**.
