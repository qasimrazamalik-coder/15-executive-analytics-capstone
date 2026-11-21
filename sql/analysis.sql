
-- Executive Analytics Capstone: decision queries (SQLite compatible)
WITH segment_performance AS (
  SELECT business_unit, COUNT(*) AS records, SUM(volume) AS total_volume,
         ROUND(SUM(revenue), 2) AS revenue,
         ROUND(SUM(revenue - cost), 2) AS margin,
         ROUND(AVG(quality_score), 2) AS avg_quality,
         ROUND(AVG(risk_flag) * 100, 2) AS risk_rate_pct
  FROM observations GROUP BY business_unit
)
SELECT *, ROUND(margin * 100.0 / NULLIF(revenue, 0), 2) AS margin_pct
FROM segment_performance ORDER BY revenue DESC;

-- Month-over-month performance
SELECT SUBSTR(date, 1, 7) AS month, ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(revenue-cost), 2) AS margin
FROM observations GROUP BY month ORDER BY month;

-- High-risk, low-quality intervention queue
SELECT record_id, date, business_unit, revenue, quality_score
FROM observations WHERE risk_flag = 1 AND quality_score < 65
ORDER BY revenue DESC LIMIT 50;
