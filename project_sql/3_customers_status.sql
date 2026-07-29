WITH last_purchase AS (
	SELECT
		ca.customerkey,
		ca.full_name,
		ca.first_purchase_date,
		ca.orderdate,
		ROW_NUMBER() OVER (PARTITION BY ca.customerkey ORDER BY ca.orderdate DESC) AS rn,
		ca.cohort_year
	FROM
		cohort_analysis ca
), customer_status AS (
SELECT
	customerkey,
	full_name,
	orderdate AS last_purchase_date,
	cohort_year,
	CASE
		WHEN orderdate < (SELECT (MAX(orderdate)) FROM sales) - INTERVAL '6 months' THEN 'Churned'
		ELSE 'Active'
	END AS customer_status
FROM
	last_purchase
WHERE
	rn = 1 AND
	first_purchase_date < (SELECT (MAX(orderdate)) FROM sales) - INTERVAL '6 months'
)

SELECT
	cs.cohort_year,
	cs.customer_status,
	COUNT(cs.customerkey) AS customer_counts,
	SUM(COUNT(cs.customerkey)) OVER (PARTITION BY cohort_year) AS total_customers,
	ROUND(100 * (COUNT(cs.customerkey) / SUM(COUNT(cs.customerkey)) OVER (PARTITION BY cohort_year)), 2) AS customer_status_pct
FROM
	customer_status cs
GROUP BY
	cs.cohort_year,
	cs.customer_status