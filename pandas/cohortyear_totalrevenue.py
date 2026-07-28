import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'cohort_year': [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'total_revenue': [14892230.47,18360521.74,21979733.96,36460385.42,
                       36696243.88,11921900.97,18387736.18,29872808.30,
                       14979328.33,2856649.33]
})

plt.figure(figsize=(10,6))
plt.bar(df['cohort_year'], df['total_revenue'], color='#eb6834')
plt.title('Total Revenue by Cohort Year')
plt.xlabel('Cohort Year')
plt.ylabel('Total Revenue ($)')
plt.xticks(df['cohort_year'])
plt.ticklabel_format(style='plain', axis='y')
plt.tight_layout()
plt.show()