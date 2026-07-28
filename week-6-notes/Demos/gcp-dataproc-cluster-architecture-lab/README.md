# GCP Dataproc Cluster Architecture Lab

Open `gcp-dataproc-cluster-architecture-end-to-end.html`.

## Fast path

```bash
cd commands
# Edit PROJECT_ID in 00_env.sh
bash 01_prepare_gcp.sh
bash 02_upload_lab_files.sh
bash 03_create_cluster.sh
bash 04_submit_job.sh
bash 05_view_results.sh
bash 06_cleanup.sh
```

Google Cloud resources can incur charges. Delete the cluster after the lab.
