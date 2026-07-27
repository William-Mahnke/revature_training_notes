SELECT
  order_date,
  region,
  category,
  COUNT(DISTINCT order_id) AS orders,
  SUM(net_amount) AS revenue
FROM `retail.gold.sales`
WHERE order_date BETWEEN DATE '2026-07-01' AND DATE '2026-07-31'
GROUP BY order_date, region, category
ORDER BY order_date, region, category;