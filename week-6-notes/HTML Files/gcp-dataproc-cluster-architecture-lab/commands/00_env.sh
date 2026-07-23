#!/usr/bin/env bash
set -euo pipefail
export PROJECT_ID="replace-with-your-gcp-project-id"
export REGION="asia-south1"
export CLUSTER_NAME="retail-dataproc-cluster"
export BUCKET_NAME="${PROJECT_ID}-dataproc-retail-lab"
export SERVICE_ACCOUNT_NAME="dataproc-retail-worker"
export SERVICE_ACCOUNT_EMAIL="${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
gcloud config set project "${PROJECT_ID}"
gcloud config set dataproc/region "${REGION}"
