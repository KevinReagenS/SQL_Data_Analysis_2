import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'cohort_year': [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024],
    'total_customers': [2825,3397,4068,7446,7755,3031,4663,9010,5890,1402],
    'total_revenue': [14892230.47,18360521.74,21979733.96,36460385.42,
                       36696243.88,11921900.97,18387736.18,29872808.30,
                       14979328.33,2856649.33]
})

fig, ax1 = plt.subplots(figsize=(11, 6))

# Bar chart: Total Revenue (right axis)
ax2 = ax1.twinx()
bars = ax2.bar(df['cohort_year'], df['total_revenue'], color='#eb6834',
                alpha=0.7, width=0.6, label='Total Revenue')
ax2.set_ylabel('Total Revenue ($)', color='#eb6834', fontsize=11)
ax2.tick_params(axis='y', labelcolor='#eb6834')
ax2.ticklabel_format(style='plain', axis='y')

# Line chart: Total Customers (left axis) — drawn after bars so it renders on top
line = ax1.plot(df['cohort_year'], df['total_customers'], color='#2a78d6',
                 marker='o', linewidth=2.5, markersize=6, label='Total Customers', zorder=5)
ax1.set_ylabel('Total Customers', color='#2a78d6', fontsize=11)
ax1.tick_params(axis='y', labelcolor='#2a78d6')
ax1.set_xlabel('Cohort Year', fontsize=11)
ax1.set_xticks(df['cohort_year'])
ax1.set_zorder(ax2.get_zorder() + 1)   # keep line chart axis on top layer
ax1.patch.set_visible(False)           # let bars show through

plt.title('Total Customers vs Total Revenue by Cohort Year', fontsize=13, fontweight='500')

# Combined legend
bars_legend, bars_label = ax2.get_legend_handles_labels()
line_legend, line_label = ax1.get_legend_handles_labels()
ax1.legend(line_legend + bars_legend, line_label + bars_label, loc='upper left')

plt.show()