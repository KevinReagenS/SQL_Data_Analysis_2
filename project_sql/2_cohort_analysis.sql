SELECT
	ca.cohort_year,
	COUNT(DISTINCT ca.customerkey) AS total_customers,
	SUM(ca.total_net_revenue) AS total_revenue,
	SUM(ca.total_net_revenue) / COUNT(DISTINCT ca.customerkey) AS customer_revenue
FROM
	cohort_analysis ca
GROUP BY
	ca.cohort_year