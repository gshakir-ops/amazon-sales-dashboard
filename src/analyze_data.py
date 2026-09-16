"""
Amazon Sales Data Analysis

This script performs comprehensive exploratory data analysis on Amazon sales data.
It handles data cleaning, feature engineering, and generates key performance indicators
suitable for dashboard visualization.

Input: Raw Amazon sales Excel file
Output: Cleaned dataset and analysis summary
"""

import pandas as pd
import json
from datetime import datetime
from pathlib import Path

# Get project root directory for relative paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

def load_raw_data():
    """Load raw Excel data from the data/raw directory."""
    excel_file = RAW_DATA_DIR / "Amazon_Combined_Data.xlsx"
    if not excel_file.exists():
        raise FileNotFoundError(f"Raw data file not found: {excel_file}")
    return pd.read_excel(excel_file)

def clean_data(df):
    """
    Clean and prepare data for analysis.

    Operations:
    - Standardize column names
    - Convert data types (numeric, datetime)
    - Handle missing values (median for prices, 0 for reviews)
    - Remove duplicates
    - Drop invalid dates
    """
    df_clean = df.copy()

    # Standardize column names
    df_clean.columns = ['ProductCategory', 'ProductDescription', 'Price',
                        'NumberOfReviews', 'Shipment', 'OrderDate']

    # Convert data types
    df_clean['Price'] = pd.to_numeric(df_clean['Price'], errors='coerce')
    df_clean['NumberOfReviews'] = pd.to_numeric(df_clean['NumberOfReviews'], errors='coerce')
    df_clean['OrderDate'] = pd.to_datetime(df_clean['OrderDate'], errors='coerce')

    # Handle missing values
    df_clean['Price'].fillna(df_clean['Price'].median(), inplace=True)
    df_clean['NumberOfReviews'].fillna(0, inplace=True)

    # Drop rows with missing critical fields
    df_clean = df_clean.dropna(subset=['OrderDate'])

    # Remove duplicates
    df_clean = df_clean.drop_duplicates()

    return df_clean

def engineer_features(df):
    """Extract temporal and categorical features from date column."""
    df['Year'] = df['OrderDate'].dt.year
    df['Month'] = df['OrderDate'].dt.month
    df['MonthName'] = df['OrderDate'].dt.strftime('%B')
    df['YearMonth'] = df['OrderDate'].dt.strftime('%Y-%m')
    df['Quarter'] = df['OrderDate'].dt.quarter
    df['DayOfWeek'] = df['OrderDate'].dt.day_name()
    return df

def calculate_kpis(df):
    """Calculate key performance indicators."""
    return {
        'TotalSales': float(df['Price'].sum()),
        'TotalReviews': int(df['NumberOfReviews'].sum()),
        'TotalSold': len(df),
        'AvgPrice': float(df['Price'].mean()),
        'AvgReviews': float(df['NumberOfReviews'].mean()),
        'DateFrom': str(df['OrderDate'].min().date()),
        'DateTo': str(df['OrderDate'].max().date())
    }

def main():
    """Main analysis workflow."""
    print("=" * 80)
    print("AMAZON SALES DATA ANALYSIS")
    print("=" * 80)

    try:
        # Load and clean data
        print("\n1. Loading raw data...")
        df = load_raw_data()
        print(f"   Loaded: {len(df):,} rows, {len(df.columns)} columns")

        print("\n2. Cleaning data...")
        df_clean = clean_data(df)
        rows_removed = len(df) - len(df_clean)
        print(f"   Rows removed: {rows_removed:,}")
        print(f"   Final dataset: {len(df_clean):,} rows")
        print(f"   Data completeness: {(1 - rows_removed/len(df)) * 100:.2f}%")

        print("\n3. Engineering features...")
        df_clean = engineer_features(df_clean)
        print(f"   Added temporal features (Year, Month, DayOfWeek, etc.)")

        print("\n4. Calculating KPIs...")
        kpis = calculate_kpis(df_clean)
        for key, value in kpis.items():
            if key.startswith('Date'):
                print(f"   {key}: {value}")
            elif key in ['TotalSales']:
                print(f"   {key}: ${value:,.2f}")
            else:
                print(f"   {key}: {value:,}")

        print("\n5. Saving cleaned data...")
        output_file = PROCESSED_DATA_DIR / "Amazon_Combined_Data_Cleaned.xlsx"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        df_clean.to_excel(output_file, index=False, sheet_name='CleanedData')
        print(f"   ✅ Saved: {output_file}")

        print("\n6. Saving analysis summary...")
        summary_file = PROJECT_ROOT / "summary.json"
        with open(summary_file, 'w') as f:
            json.dump(kpis, f, indent=2)
        print(f"   ✅ Saved: {summary_file}")

        print("\n" + "=" * 80)
        print("✅ ANALYSIS COMPLETE")
        print("=" * 80)

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        raise

if __name__ == "__main__":
    main()
