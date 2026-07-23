#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
RUN_ID="$(date -u +%Y%m%d-%H%M%S)"
OUTPUT_URI="gs://${BUCKET_NAME}/output/${RUN_ID}"
gcloud dataproc jobs submit pyspark "gs://${BUCKET_NAME}/scripts/retail_sales_etl.py"   --cluster="${CLUSTER_NAME}" --region="${REGION}" --   --input="gs://${BUCKET_NAME}/input/retail_orders.csv" --output="${OUTPUT_URI}"
echo "OUTPUT_URI=${OUTPUT_URI}"
gcloud storage ls --recursive "${OUTPUT_URI}"
