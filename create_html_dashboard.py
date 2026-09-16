import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load all the CSV files we created
sales_by_month = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByMonth.csv")
sales_by_category = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByCategory.csv")
top_5_products = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Top5Products.csv")
top_5_by_year = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Top5ProductsByYear.csv")
sales_by_dayofweek = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByDayOfWeek.csv")
sales_by_pricerange = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByPriceRange.csv")
sales_by_year = pd.read_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByYear.csv")

# Colors
color_primary = '#1f77b4'
color_secondary = '#ff7f0e'
color_tertiary = '#2ca02c'
color_quaternary = '#d62728'
color_quinary = '#9467bd'

print("Creating interactive HTML dashboard...")

# Create separate figures and combine them
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "Sales Trend by Month",
        "Sales by Product Category",
        "Top 5 Products",
        "Top 5 Products by Year",
        "Sales by Day of Week",
        "Revenue by Price Range"
    ),
    specs=[
        [{"secondary_y": False}, {"secondary_y": False}],
        [{"secondary_y": False}, {"secondary_y": False}],
        [{"secondary_y": False}, {"type": "domain"}]
    ],
    vertical_spacing=0.12,
    horizontal_spacing=0.15,
)

# 1. Sales Trend by Month (Line Chart)
fig.add_trace(
    go.Scatter(
        x=sales_by_month['YearMonth'],
        y=sales_by_month['TotalSales'],
        mode='lines+markers',
        name='Monthly Sales',
        line=dict(color=color_primary, width=3),
        marker=dict(size=6),
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>'
    ),
    row=1, col=1
)

# 2. Sales by Category (Bar Chart)
fig.add_trace(
    go.Bar(
        y=sales_by_category['ProductCategory'],
        x=sales_by_category['TotalSales'],
        orientation='h',
        name='Category Sales',
        marker=dict(color=color_secondary),
        hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.0f}<extra></extra>'
    ),
    row=1, col=2
)

# 3. Top 5 Products (Bar Chart)
fig.add_trace(
    go.Bar(
        y=top_5_products['ProductDescription'].str[:45],
        x=top_5_products['TotalSales'],
        orientation='h',
        name='Product Sales',
        marker=dict(color=color_tertiary),
        hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.0f}<extra></extra>'
    ),
    row=2, col=1
)

# 4. Top 5 by Year (Grouped Bar)
colors_year = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for idx, year in enumerate(sorted(top_5_by_year['Year'].unique())):
    year_data = top_5_by_year[top_5_by_year['Year'] == year].head(5)
    fig.add_trace(
        go.Bar(
            y=year_data['ProductDescription'].str[:35],
            x=year_data['TotalSales'],
            name=f'{int(year)}',
            marker=dict(color=colors_year[idx % len(colors_year)]),
            hovertemplate='<b>%{y}</b><br>Sales: $%{x:,.0f}<extra></extra>'
        ),
        row=2, col=2
    )

# 5. Sales by Day of Week (Column Chart)
fig.add_trace(
    go.Bar(
        x=sales_by_dayofweek['DayOfWeek'],
        y=sales_by_dayofweek['TotalSales'],
        name='Daily Sales',
        marker=dict(color=color_quinary),
        hovertemplate='<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>'
    ),
    row=3, col=1
)

# 6. Price Range Distribution (Pie Chart)
fig.add_trace(
    go.Pie(
        labels=sales_by_pricerange['PriceRange'],
        values=sales_by_pricerange['TotalSales'],
        name='Price Range',
        marker=dict(colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']),
        hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.0f}<br>%{percent}<extra></extra>'
    ),
    row=3, col=2
)

# Update axes labels
fig.update_xaxes(title_text="Month", row=1, col=1)
fig.update_yaxes(title_text="Sales ($)", row=1, col=1)

fig.update_xaxes(title_text="Sales ($)", row=1, col=2)
fig.update_yaxes(title_text="Category", row=1, col=2)

fig.update_xaxes(title_text="Sales ($)", row=2, col=1)
fig.update_yaxes(title_text="Product", row=2, col=1)

fig.update_xaxes(title_text="Sales ($)", row=2, col=2)
fig.update_yaxes(title_text="Product", row=2, col=2)

fig.update_xaxes(title_text="Day of Week", row=3, col=1)
fig.update_yaxes(title_text="Sales ($)", row=3, col=1)

# Update layout
fig.update_layout(
    title_text="<b>Amazon Sales Analytics Dashboard</b><br><sub>Data from Jan 2019 - Dec 2022 | Total Sales: $8.41M | Items Sold: 88,947 | Total Reviews: 58.5M</sub>",
    title_font_size=22,
    height=1600,
    showlegend=True,
    hovermode='closest',
    template='plotly_white',
    font=dict(family="Segoe UI, sans-serif", size=11),
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#ffffff',
    margin=dict(l=80, r=80, t=140, b=80)
)

# Save to HTML
output_file = r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Amazon_Sales_Dashboard.html"
fig.write_html(output_file)

print(f"✅ Interactive HTML dashboard created!")
print(f"📁 File: {output_file}")
print(f"\n🎉 Dashboard is ready to use!")
