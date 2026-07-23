#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
LAB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
gcloud storage cp "${LAB_ROOT}/data/retail_orders.csv" "gs://${BUCKET_NAME}/input/retail_orders.csv"
gcloud storage cp "${LAB_ROOT}/scripts/retail_sales_etl.py" "gs://${BUCKET_NAME}/scripts/retail_sales_etl.py"
gcloud storage ls --recursive "gs://${BUCKET_NAME}"
