#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
gcloud dataproc clusters create "${CLUSTER_NAME}"   --region="${REGION}"   --image-version="2.3-debian12"   --master-machine-type="e2-standard-4"   --worker-machine-type="e2-standard-4"   --num-workers="2"   --service-account="${SERVICE_ACCOUNT_EMAIL}"   --scopes="cloud-platform"   --bucket="${BUCKET_NAME}"   --temp-bucket="${BUCKET_NAME}"   --enable-component-gateway   --delete-max-idle="30m"   --labels="environment=training,workload=retail-etl"
