"""
Amazon Sales Dashboard - Data Export for Visualization

This script generates CSV exports from cleaned data for dashboard creation.
It creates aggregated views by time periods, categories, products, and price ranges.

Input: Cleaned Excel dataset
Output: CSV files for Power BI and HTML dashboard visualization
"""

import pandas as pd
from pathlib import Path

# Get project root directory for relative paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXPORT_DIR = PROCESSED_DATA_DIR / "exports"

def load_cleaned_data():
    """Load cleaned data from processed directory."""
    cleaned_file = PROCESSED_DATA_DIR / "Amazon_Combined_Data_Cleaned.xlsx"
    if not cleaned_file.exists():
        raise FileNotFoundError(f"Cleaned data not found. Run analyze_data.py first: {cleaned_file}")
    return pd.read_excel(cleaned_file)

def export_sales_by_month(df):
    """Export monthly sales aggregation."""
    data = df.groupby('YearMonth').agg({
        'Price': 'sum',
        'ProductDescription': 'count'
    }).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

    output_file = EXPORT_DIR / "SalesByMonth.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} ({len(data)} months)")

def export_sales_by_category(df):
    """Export category-level sales."""
    data = df.groupby('ProductCategory').agg({
        'Price': 'sum',
        'ProductDescription': 'count',
        'NumberOfReviews': 'sum'
    }).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()
    data = data.sort_values('TotalSales', ascending=False)

    output_file = EXPORT_DIR / "SalesByCategory.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} ({len(data)} categories)")

def export_top_products(df):
    """Export top 5 products overall."""
    data = df.groupby('ProductDescription').agg({
        'Price': 'sum',
        'NumberOfReviews': 'sum'
    }).rename(columns={'Price': 'TotalSales'}).reset_index()
    data = data.sort_values('TotalSales', ascending=False).head(5)

    output_file = EXPORT_DIR / "Top5Products.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} (top 5 products)")

def export_top_products_by_year(df):
    """Export top 5 products per year."""
    data = df.groupby(['Year', 'ProductDescription']).agg({
        'Price': 'sum'
    }).rename(columns={'Price': 'TotalSales'}).reset_index()

    data = data.sort_values(['Year', 'TotalSales'], ascending=[True, False])
    data = data.groupby('Year').head(5)

    output_file = EXPORT_DIR / "Top5ProductsByYear.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} (top 5 by year)")

def export_sales_by_day_of_week(df):
    """Export day-of-week pattern analysis."""
    data = df.groupby('DayOfWeek').agg({
        'Price': 'sum',
        'ProductDescription': 'count'
    }).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

    # Sort by day order
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    data['DayOfWeek'] = pd.Categorical(data['DayOfWeek'], categories=day_order, ordered=True)
    data = data.sort_values('DayOfWeek')

    output_file = EXPORT_DIR / "SalesByDayOfWeek.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} (weekly patterns)")

def export_sales_by_year(df):
    """Export yearly aggregates."""
    data = df.groupby('Year').agg({
        'Price': 'sum',
        'ProductDescription': 'count',
        'NumberOfReviews': 'sum'
    }).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

    output_file = EXPORT_DIR / "SalesByYear.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} ({len(data)} years)")

def export_price_range_analysis(df):
    """Export price tier distribution."""
    df_copy = df.copy()
    df_copy['PriceRange'] = pd.cut(df_copy['Price'],
                                    bins=[0, 25, 50, 100, 200, 500, 20000],
                                    labels=['$0-25', '$25-50', '$50-100', '$100-200', '$200-500', '$500+'])

    data = df_copy.groupby('PriceRange').agg({
        'Price': 'sum',
        'ProductDescription': 'count'
    }).rename(columns={'Price': 'TotalSales', 'ProductDescription': 'ItemsSold'}).reset_index()

    output_file = EXPORT_DIR / "SalesByPriceRange.csv"
    data.to_csv(output_file, index=False)
    print(f"✅ Exported: {output_file.name} (price tier analysis)")

def main():
    """Main export workflow."""
    print("=" * 80)
    print("AMAZON SALES DASHBOARD - DATA EXPORT")
    print("=" * 80)

    try:
        # Create export directory
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
        print(f"\nExport directory: {EXPORT_DIR}")

        # Load cleaned data
        print("\nLoading cleaned data...")
        df = load_cleaned_data()
        print(f"Loaded: {len(df):,} records")

        # Generate exports
        print("\nGenerating dashboard datasets...")
        export_sales_by_month(df)
        export_sales_by_category(df)
        export_top_products(df)
        export_top_products_by_year(df)
        export_sales_by_day_of_week(df)
        export_sales_by_year(df)
        export_price_range_analysis(df)

        print("\n" + "=" * 80)
        print("✅ ALL EXPORTS COMPLETE")
        print("=" * 80)
        print(f"\n7 CSV files ready for dashboard visualization")

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
