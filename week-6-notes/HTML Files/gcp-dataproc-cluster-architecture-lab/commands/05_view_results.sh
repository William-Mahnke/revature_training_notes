#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
LATEST_RUN="$(gcloud storage ls "gs://${BUCKET_NAME}/output/" 2>/dev/null | sort | tail -1)"
test -n "${LATEST_RUN}" || { echo "No output run found"; exit 1; }
echo "Latest run: ${LATEST_RUN}"
gcloud storage cat "${LATEST_RUN}state_summary/part-*.csv"
gcloud storage cat "${LATEST_RUN}daily_state_category_summary/part-*.csv"
gcloud storage cat "${LATEST_RUN}rejected_orders/part-*.json"
