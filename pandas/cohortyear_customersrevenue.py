import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'cohort_year': [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'customer_revenue': [5271.59,5404.92,5403.08,4896.64,4731.95,
                          3933.32,3943.33,3315.52,2543.18,2037.55]
})

plt.figure(figsize=(10,6))
plt.bar(df['cohort_year'], df['customer_revenue'], color='#199e70')
plt.title('Average Revenue per Customer by Cohort Year')
plt.xlabel('Cohort Year')
plt.ylabel('Customer Revenue ($)')
plt.xticks(df['cohort_year'])
plt.tight_layout()
plt.show()