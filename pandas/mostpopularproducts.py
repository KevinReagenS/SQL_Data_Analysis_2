import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

df = pd.DataFrame({
    'categoryname': [
        'Audio','Audio','Audio',
        'Cameras and camcorders','Cameras and camcorders','Cameras and camcorders','Cameras and camcorders',
        'Cell phones','Cell phones','Cell phones','Cell phones',
        'Computers','Computers','Computers','Computers','Computers','Computers',
        'Games and Toys','Games and Toys',
        'Home Appliances','Home Appliances','Home Appliances','Home Appliances','Home Appliances','Home Appliances','Home Appliances','Home Appliances',
        'Music, Movies and Audio Books',
        'TV and Video','TV and Video','TV and Video','TV and Video'
    ],
    'subcategoryname': [
        'MP4&MP3','Recording Pen','Bluetooth Headphones',
        'Camcorders','Digital Cameras','Cameras & Camcorders Accessories','Digital SLR Cameras',
        'Home & Office Phones','Cell phones Accessories','Touch Screen Phones','Smart phones & PDAs',
        'Printers, Scanners & Fax','Laptops','Computers Accessories','Monitors','Projectors & Screens','Desktops',
        'Download Games','Boxed Games',
        'Washers & Dryers','Fans','Lamps','Air Conditioners','Refrigerators','Coffee Machines','Microwaves','Water Heaters',
        'Movie DVD',
        'Home Theater System','Car Video','VCD & DVD','Televisions'
    ],
    'order_counts': [
        2315, 4315, 8653,
        3195, 3245, 3284, 3748,
        6579, 6916, 13373, 14844,
        5643, 5729, 5746, 5780, 5864, 17739,
        9186, 11077,
        1117, 1135, 1207, 1457, 1960, 1970, 3831, 4276,
        32017,
        1787, 2195, 3002, 6688
    ]
})

# Order categories top-to-bottom by total order count (largest at top)
category_totals = df.groupby('categoryname')['order_counts'].sum().sort_values(ascending=True)
categories = category_totals.index.tolist()

base_colors = ['#e6194b', '#3cb44b', '#4363d8', '#f58231',
                '#911eb4', '#17b8c4', '#d63bd6', '#8bc34a']
# Keep consistent hue assignment regardless of sort order used for display
color_order = category_totals.sort_values(ascending=False).index.tolist()
cat_color_map = {cat: base_colors[i % len(base_colors)] for i, cat in enumerate(color_order)}

fig, ax = plt.subplots(figsize=(13, 15))

bar_height = 0.16
group_gap = 0.5
y_cursor = 0
ytick_positions = []

for cat in categories:
    sub = df[df['categoryname'] == cat].sort_values('order_counts', ascending=False).reset_index(drop=True)
    n = len(sub)
    base_rgb = mcolors.to_rgb(cat_color_map[cat])

    cluster_center = y_cursor + (n - 1) / 2 * bar_height

    for rank, row in sub.iterrows():
        shade = 1 - 0.13 * rank
        light_rgb = tuple(min(1, c + (1 - c) * (1 - shade)) for c in base_rgb)

        ypos = y_cursor + rank * bar_height
        ax.barh(ypos, row['order_counts'], height=bar_height * 0.9,
                color=light_rgb, edgecolor='white', linewidth=0.8)

        ax.text(row['order_counts'] + df['order_counts'].max() * 0.012, ypos,
                 f"{row['subcategoryname']} ({row['order_counts']:,})",
                 ha='left', va='center', fontsize=8, color=base_rgb, fontweight='bold')

    ytick_positions.append(cluster_center)
    y_cursor += n * bar_height + group_gap

ax.set_yticks(ytick_positions)
ax.set_yticklabels(categories, fontsize=11)
ax.set_ylabel('Category Name', fontsize=11, labelpad=10)
ax.set_xlabel('Order Counts', fontsize=11)
ax.set_title('Order Counts by Category and Subcategory', fontsize=15, fontweight='medium', pad=20)
ax.set_xlim(0, df['order_counts'].max() * 1.35)
ax.spines[['top', 'right']].set_visible(False)
ax.margins(y=0.01)

plt.show()