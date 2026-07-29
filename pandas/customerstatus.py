import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'customer_status': ['Active', 'Churned'],
    'customer_counts': [4441, 42472],
    'total_customers': [46913, 46913],
    'customer_status_pct': [9.47, 90.53]
})

colors = ['#2a78d6', '#eb6834']

fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(
    df['customer_status_pct'],
    labels=df['customer_status'],
    autopct='%1.2f%%',
    colors=colors,
    startangle=90,
    radius=0.85,
    pctdistance=0.75,
    labeldistance=1.1,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
    textprops={'fontsize': 11}
)
ax.set_title('Customer Status Distribution', fontsize=14, fontweight='medium', pad=30)
ax.axis('equal')
plt.show()