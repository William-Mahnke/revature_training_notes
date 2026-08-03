-- Sample source rows can be a Delta/Parquet table in production.
SELECT
    warehouse_id,
    order_id,
    priority,
    promised_at,
    item_count
FROM fulfilment_orders
WHERE fulfilment_status = 'READY'
DISTRIBUTE BY warehouse_id
SORT BY
    priority DESC,
    promised_at ASC,
    order_id ASC; 