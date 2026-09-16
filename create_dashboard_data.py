import pandas as pd
import json
from datetime import datetime

# Load cleaned data
df = pd.read_excel(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Amazon_Combined_Data_Cleaned.xlsx")

print("Creating Power BI Dashboard Components...")
print("=" * 80)

# ===== KPIs =====
total_sales = float(df['Price'].sum())
total_reviews = int(df['NumberOfReviews'].sum())
total_sold = len(df)

print(f"\n✅ KPIs Created:")
print(f"   - Total Sales: ${total_sales:,.2f}")
print(f"   - Total Reviews: {total_reviews:,}")
print(f"   - Total Sold: {total_sold:,}")

# ===== Sales by Month =====
sales_by_month = df.groupby('YearMonth').agg({
    'Price': 'sum',
    'ProductDescription': 'count'
}).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

sales_by_month.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByMonth.csv", index=False)
print(f"\n✅ Sales by Month chart data created (48 months)")

# ===== Sales by Product Category =====
sales_by_category = df.groupby('ProductCategory').agg({
    'Price': 'sum',
    'ProductDescription': 'count',
    'NumberOfReviews': 'sum'
}).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index().sort_values('TotalSales', ascending=False)

sales_by_category.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByCategory.csv", index=False)
print(f"✅ Sales by Product Category chart data created ({len(sales_by_category)} categories)")

# ===== Top 5 Products Overall =====
top_5_products = df.groupby('ProductDescription').agg({
    'Price': 'sum',
    'NumberOfReviews': 'sum'
}).rename(columns={'Price': 'TotalSales'}).reset_index().sort_values('TotalSales', ascending=False).head(5)

top_5_products.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Top5Products.csv", index=False)
print(f"✅ Top 5 Products chart data created")

# ===== Top 5 Products by Year =====
top_5_by_year = df.groupby(['Year', 'ProductDescription']).agg({
    'Price': 'sum'
}).rename(columns={'Price': 'TotalSales'}).reset_index()

# Get top 5 for each year
top_5_by_year = top_5_by_year.sort_values(['Year', 'TotalSales'], ascending=[True, False]).groupby('Year').head(5)

top_5_by_year.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Top5ProductsByYear.csv", index=False)
print(f"✅ Top 5 Products by Year chart data created")

# ===== Additional Analysis: Sales by Day of Week =====
sales_by_dayofweek = df.groupby('DayOfWeek').agg({
    'Price': 'sum',
    'ProductDescription': 'count'
}).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

# Sort by day order
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sales_by_dayofweek['DayOfWeek'] = pd.Categorical(sales_by_dayofweek['DayOfWeek'], categories=day_order, ordered=True)
sales_by_dayofweek = sales_by_dayofweek.sort_values('DayOfWeek')

sales_by_dayofweek.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByDayOfWeek.csv", index=False)
print(f"✅ Sales by Day of Week chart data created (bonus insight)")

# ===== Sales by Year =====
sales_by_year = df.groupby('Year').agg({
    'Price': 'sum',
    'ProductDescription': 'count',
    'NumberOfReviews': 'sum'
}).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

sales_by_year.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByYear.csv", index=False)
print(f"✅ Sales by Year chart data created")

# ===== Price Range Analysis =====
df['PriceRange'] = pd.cut(df['Price'], 
                          bins=[0, 25, 50, 100, 200, 500, 20000],
                          labels=['$0-25', '$25-50', '$50-100', '$100-200', '$200-500', '$500+'])

price_range_analysis = df.groupby('PriceRange').agg({
    'Price': 'sum',
    'ProductDescription': 'count'
}).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

price_range_analysis.to_csv(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\SalesByPriceRange.csv", index=False)
print(f"✅ Sales by Price Range chart data created (bonus insight)")

# Save dashboard metadata
dashboard_info = {
    "DashboardName": "Amazon Sales Analytics Dashboard",
    "CreatedDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "DataSource": "Amazon_Combined_Data.xlsx",
    "TotalRecords": int(total_sold),
    "DateRange": f"{df['OrderDate'].min().date()} to {df['OrderDate'].max().date()}",
    "KPIs": {
        "TotalSales": float(total_sales),
        "TotalReviews": int(total_reviews),
        "TotalSold": int(total_sold)
    },
    "Charts": [
        "Sales by Month (Line Chart)",
        "Sales by Product Category (Bar Chart)",
        "Top 5 Products (Bar Chart)",
        "Top 5 Products by Year (Clustered Bar Chart)",
        "Sales by Day of Week (Column Chart - Bonus)",
        "Sales by Price Range (Donut Chart - Bonus)"
    ],
    "Filters": [
        "Year (Slicer)",
        "Product Category (Slicer)",
        "Month (Slicer)",
        "Date Range (Date Slicer)"
    ]
}

with open(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\DashboardInfo.json", 'w') as f:
    json.dump(dashboard_info, f, indent=2)

print("\n" + "=" * 80)
print("✅ ALL DASHBOARD COMPONENTS CREATED SUCCESSFULLY!")
print("=" * 80)
print(f"\n📁 Files created in: C:\\Users\\LENOVO\\Desktop\\Power Bi\\project 1\\")
print("   - Amazon_Combined_Data_Cleaned.xlsx (Main cleaned dataset)")
print("   - SalesByMonth.csv")
print("   - SalesByCategory.csv")
print("   - Top5Products.csv")
print("   - Top5ProductsByYear.csv")
print("   - SalesByDayOfWeek.csv (Bonus)")
print("   - SalesByYear.csv")
print("   - SalesByPriceRange.csv (Bonus)")
print("   - DashboardInfo.json (Dashboard metadata)")
