import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'cohort_year': [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'total_customers': [2825,3397,4068,7446,7755,3031,4663,9010,5890,1402]
})

plt.figure(figsize=(10,6))
plt.bar(df['cohort_year'], df['total_customers'], color='#2a78d6')
plt.title('Total Customers by Cohort Year')
plt.xlabel('Cohort Year')
plt.ylabel('Total Customers')
plt.xticks(df['cohort_year'])
plt.tight_layout()
plt.show()