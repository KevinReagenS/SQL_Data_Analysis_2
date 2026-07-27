WITH customer_ltv AS (
	SELECT
		ca.customerkey,
		ca.full_name,
		SUM(ca.total_net_revenue) AS total_ltv
	FROM
		cohort_analysis ca
	GROUP BY
		ca.customerkey,
		ca.full_name
), customer_segments AS (
SELECT
	PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY total_ltv) AS ltv_25th_percentile,
	PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY total_ltv) AS ltv_75th_percentile
FROM
	customer_ltv
), segment_values AS (
SELECT
	c.*,
	CASE
		WHEN c.total_ltv <= cs.ltv_25th_percentile THEN '1 - Low Value Customer'
		WHEN c.total_ltv BETWEEN cs.ltv_25th_percentile AND cs.ltv_75th_percentile  THEN '2 - Mid Value Customer'
		ELSE '3 - High Value Customer'
	END AS customer_value
FROM
	customer_ltv c,
	customer_segments cs
)

SELECT
	customer_value,
	COUNT(customerkey),
	SUM(total_ltv) AS total_ltv,
	AVG(total_ltv) AS average_ltv
FROM segment_values
GROUP BY
	customer_value
ORDER BY
	customer_value