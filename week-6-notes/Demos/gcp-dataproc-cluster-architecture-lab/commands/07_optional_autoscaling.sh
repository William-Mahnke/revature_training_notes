#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/00_env.sh"
LAB_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
POLICY_ID="retail-lab-autoscaling"
gcloud dataproc autoscaling-policies import "${POLICY_ID}" --region="${REGION}" --source="${LAB_ROOT}/autoscaling-policy.yaml"
gcloud dataproc clusters update "${CLUSTER_NAME}" --region="${REGION}" --autoscaling-policy="${POLICY_ID}"
gcloud dataproc autoscaling-policies describe "${POLICY_ID}" --region="${REGION}"
