#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
gcloud dataproc clusters delete "${CLUSTER_NAME}" --region="${REGION}" --quiet || true
# Optional bucket cleanup:
# gcloud storage rm --recursive "gs://${BUCKET_NAME}/**"
# gcloud storage buckets delete "gs://${BUCKET_NAME}"
