import pandas as pd
import numpy as np
from datetime import datetime
import json

# Load the Excel file
excel_file = r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Amazon_Combined_Data.xlsx"
df = pd.read_excel(excel_file)

print("=" * 80)
print("DATA ANALYSIS REPORT - AMAZON SALES DATA")
print("=" * 80)

# ===== 1. DATA ASSESSMENT =====
print("\n1. DATASET OVERVIEW")
print(f"   Total Rows: {len(df):,}")
print(f"   Total Columns: {len(df.columns)}")
print(f"   Columns: {list(df.columns)}")

print("\n2. DATA TYPES & INFO")
print(df.dtypes)

print("\n3. MISSING VALUES")
print(df.isnull().sum())

print("\n4. FIRST 5 ROWS")
print(df.head())

# ===== 2. DATA CLEANING =====
print("\n" + "=" * 80)
print("DATA CLEANING IN PROGRESS...")
print("=" * 80)

df_clean = df.copy()

# Clean column names
df_clean.columns = ['ProductCategory', 'ProductDescription', 'Price', 'NumberOfReviews', 'Shipment', 'OrderDate']

# Convert Price to numeric
df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce')

# Convert NumberOfReviews to numeric
df_clean['NumberOfReviews'] = pd.to_numeric(df_clean['NumberOfReviews'], errors='coerce')

# Convert OrderDate to datetime
df_clean['OrderDate'] = pd.to_datetime(df_clean['OrderDate'], errors='coerce')

# Handle missing values
print(f"\nMissing values before cleaning:")
print(df_clean.isnull().sum())

# Fill missing prices with median
df_clean['Price'].fillna(df_clean['Price'].median(), inplace=True)

# Fill missing reviews with 0
df_clean['NumberOfReviews'].fillna(0, inplace=True)

# Drop rows with missing OrderDate
df_clean = df_clean.dropna(subset=['OrderDate'])

# Remove duplicates
df_clean = df_clean.drop_duplicates()

print(f"\nMissing values after cleaning:")
print(df_clean.isnull().sum())

print(f"\nRows after cleaning: {len(df_clean):,}")
print(f"Rows removed: {len(df) - len(df_clean):,}")

# ===== 3. EXPLORATORY DATA ANALYSIS =====
print("\n" + "=" * 80)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 80)

# Calculate KPIs
total_sales = df_clean['Price'].sum()
total_reviews = df_clean['NumberOfReviews'].sum()
total_sold = len(df_clean)
avg_price = df_clean['Price'].mean()
avg_reviews = df_clean['NumberOfReviews'].mean()

print(f"\n📊 KEY PERFORMANCE INDICATORS (KPIs)")
print(f"   Total Sales (Revenue): ${total_sales:,.2f}")
print(f"   Total Reviews: {total_reviews:,.0f}")
print(f"   Total Items Sold: {total_sold:,}")
print(f"   Average Price: ${avg_price:.2f}")
print(f"   Average Reviews per Product: {avg_reviews:.2f}")

# Statistics
print(f"\n📈 PRICE STATISTICS")
print(df_clean['Price'].describe())

print(f"\n⭐ REVIEW STATISTICS")
print(df_clean['NumberOfReviews'].describe())

# Product categories
print(f"\n🏷️  PRODUCT CATEGORIES")
category_sales = df_clean.groupby('ProductCategory').agg({
    'Price': 'sum',
    'NumberOfReviews': 'sum',
    'ProductDescription': 'count'
}).rename(columns={'ProductDescription': 'ItemCount'}).sort_values('Price', ascending=False)
print(category_sales)

# Date range
print(f"\n📅 DATE RANGE")
print(f"   From: {df_clean['OrderDate'].min().date()}")
print(f"   To: {df_clean['OrderDate'].max().date()}")

# ===== 4. FEATURE ENGINEERING FOR DASHBOARD =====
print("\n" + "=" * 80)
print("CREATING FEATURES FOR DASHBOARD...")
print("=" * 80)

# Extract date components
df_clean['Year'] = df_clean['OrderDate'].dt.year
df_clean['Month'] = df_clean['OrderDate'].dt.month
df_clean['MonthName'] = df_clean['OrderDate'].dt.strftime('%B')
df_clean['YearMonth'] = df_clean['OrderDate'].dt.strftime('%Y-%m')
df_clean['Quarter'] = df_clean['OrderDate'].dt.quarter
df_clean['DayOfWeek'] = df_clean['OrderDate'].dt.day_name()

# Sales by Month
sales_by_month = df_clean.groupby('YearMonth').agg({
    'Price': 'sum',
    'ProductDescription': 'count',
    'NumberOfReviews': 'sum'
}).rename(columns={'ProductDescription': 'ItemsSold', 'Price': 'TotalSales'})

print(f"\n✅ Sales by Month created")
print(sales_by_month.head(10))

# Top 5 products overall
top_5_products = df_clean.groupby('ProductDescription').agg({
    'Price': 'sum',
    'ProductDescription': 'count',
    'NumberOfReviews': 'sum'
}).rename(columns={'ProductDescription': 'ItemCount', 'Price': 'TotalSales'}).sort_values('TotalSales', ascending=False).head(5)

print(f"\n✅ Top 5 Products created")
print(top_5_products)

# Top 5 products by year
top_5_by_year = df_clean.groupby(['Year', 'ProductDescription']).agg({
    'Price': 'sum'
}).rename(columns={'Price': 'TotalSales'}).reset_index().sort_values(['Year', 'TotalSales'], ascending=[True, False]).groupby('Year').head(5)

print(f"\n✅ Top 5 Products by Year created")
print(top_5_by_year)

# ===== 5. SAVE CLEANED DATA =====
cleaned_file = r"C:\Users\LENOVO\Desktop\Power Bi\project 1\Amazon_Combined_Data_Cleaned.xlsx"
df_clean.to_excel(cleaned_file, index=False, sheet_name='CleanedData')

print(f"\n✅ Cleaned data saved to: {cleaned_file}")

# Create summary for Power BI
summary_data = {
    'TotalSales': total_sales,
    'TotalReviews': int(total_reviews),
    'TotalSold': total_sold,
    'AvgPrice': avg_price,
    'AvgReviews': avg_reviews,
    'DateFrom': str(df_clean['OrderDate'].min().date()),
    'DateTo': str(df_clean['OrderDate'].max().date())
}

# Save summary
with open(r"C:\Users\LENOVO\Desktop\Power Bi\project 1\summary.json", 'w') as f:
    json.dump(summary_data, f, indent=2)

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE!")
print("=" * 80)
