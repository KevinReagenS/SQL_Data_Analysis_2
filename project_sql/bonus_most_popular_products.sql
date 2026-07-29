WITH category AS  (
	SELECT
		s.orderkey,
		p.categoryname,
		p.subcategoryname
	FROM
		sales s
		INNER JOIN product p ON p.productkey = s.productkey
)

SELECT
	c.categoryname,
	c.subcategoryname,
	COUNT(c.orderkey) AS order_counts
FROM
	category c
GROUP BY
	c.categoryname,
	c.subcategoryname
ORDER BY
	c.categoryname,
	order_counts