#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
gcloud services enable dataproc.googleapis.com compute.googleapis.com storage.googleapis.com iam.googleapis.com
if ! gcloud storage buckets describe "gs://${BUCKET_NAME}" >/dev/null 2>&1; then
  gcloud storage buckets create "gs://${BUCKET_NAME}" --location="${REGION}" --uniform-bucket-level-access
fi
if ! gcloud iam service-accounts describe "${SERVICE_ACCOUNT_EMAIL}" >/dev/null 2>&1; then
  gcloud iam service-accounts create "${SERVICE_ACCOUNT_NAME}" --display-name="Dataproc Retail Lab Worker"
fi
gcloud projects add-iam-policy-binding "${PROJECT_ID}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/dataproc.worker" --quiet
gcloud storage buckets add-iam-policy-binding "gs://${BUCKET_NAME}" --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" --role="roles/storage.objectAdmin" --quiet
CURRENT_USER="$(gcloud config get-value account)"
gcloud iam service-accounts add-iam-policy-binding "${SERVICE_ACCOUNT_EMAIL}" --member="user:${CURRENT_USER}" --role="roles/iam.serviceAccountUser" --quiet
