# Installation & Reproduction Guide

This guide walks you through setting up the project locally and reproducing the analysis from start to finish.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (to clone the repository)

## Quick Setup (5 minutes)

### 1. Clone or Download the Repository

```bash
git clone https://github.com/gshakir-ops/amazon-sales-dashboard.git
cd amazon-sales-dashboard
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pandas` — Data manipulation
- `openpyxl` — Excel file handling
- `plotly` — Interactive visualizations

### 3. View the Dashboard (No Python Required)

```bash
# On macOS/Linux:
open dashboards/Amazon_Sales_Dashboard.html

# On Windows:
start dashboards/Amazon_Sales_Dashboard.html

# Or simply open in your web browser by double-clicking the file
```

**That's it!** You now have an interactive dashboard with 6 visualizations.

---

## Full Analysis Reproduction (10 minutes)

To re-run the complete analysis from raw data:

### Step 1: Clean the Data

```bash
python src/analyze_data.py
```

**What this does:**
- Loads raw data from `data/raw/Amazon_Combined_Data.xlsx`
- Cleans missing values, removes duplicates
- Adds temporal features (Year, Month, DayOfWeek, etc.)
- Outputs cleaned data to `data/processed/Amazon_Combined_Data_Cleaned.xlsx`
- Saves KPI summary to `summary.json`

**Expected output:**
```
================================================================================
AMAZON SALES DATA ANALYSIS
================================================================================

1. Loading raw data...
   Loaded: 89,082 rows, 6 columns

2. Cleaning data...
   Rows removed: 135
   Final dataset: 88,947 rows
   Data completeness: 99.85%

3. Engineering features...
   Added temporal features (Year, Month, DayOfWeek, etc.)

4. Calculating KPIs...
   TotalSales: $8,409,992.00
   TotalReviews: 58,516,965
   TotalSold: 88,947
   DateFrom: 2019-01-03
   DateTo: 2022-12-31

5. Saving cleaned data...
   ✅ Saved: data/processed/Amazon_Combined_Data_Cleaned.xlsx

6. Saving analysis summary...
   ✅ Saved: summary.json

================================================================================
✅ ANALYSIS COMPLETE
================================================================================
```

### Step 2: Generate Dashboard Data

```bash
python src/create_dashboard_data.py
```

**What this does:**
- Loads cleaned data from Step 1
- Creates CSV exports for each visualization:
  - Monthly sales trends
  - Category performance
  - Top 5 products
  - Day-of-week patterns
  - Price range analysis
  - Yearly aggregates

**Expected output:**
```
================================================================================
AMAZON SALES DASHBOARD - DATA EXPORT
================================================================================

Export directory: data/processed/exports

Loading cleaned data...
Loaded: 88,947 records

Generating dashboard datasets...
✅ Exported: SalesByMonth.csv (48 months)
✅ Exported: SalesByCategory.csv (8 categories)
✅ Exported: Top5Products.csv (top 5 products)
✅ Exported: Top5ProductsByYear.csv (top 5 by year)
✅ Exported: SalesByDayOfWeek.csv (weekly patterns)
✅ Exported: SalesByYear.csv (4 years)
✅ Exported: SalesByPriceRange.csv (price tier analysis)

================================================================================
✅ ALL EXPORTS COMPLETE
================================================================================

7 CSV files ready for dashboard visualization
```

### Step 3: View the Dashboard

```bash
# macOS/Linux
open dashboards/Amazon_Sales_Dashboard.html

# Windows
start dashboards/Amazon_Sales_Dashboard.html
```

All analysis outputs are now generated and the dashboard is ready to explore.

---

## Accessing the Results

After running the analysis, check these locations:

| Location | Contains |
|----------|----------|
| `data/processed/Amazon_Combined_Data_Cleaned.xlsx` | Full cleaned dataset (88,947 rows) |
| `data/processed/exports/` | 7 CSV files for each visualization |
| `dashboards/Amazon_Sales_Dashboard.html` | Interactive Plotly dashboard |
| `summary.json` | KPI summary |

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

**Solution:** Install dependencies again:
```bash
pip install -r requirements.txt
```

### "FileNotFoundError: raw/Amazon_Combined_Data.xlsx"

**Solution:** Ensure you're running scripts from the project root directory:
```bash
cd amazon-sales-dashboard
python src/analyze_data.py
```

### Scripts run but produce no output files

**Solution:** Check that the `data/processed/` directory structure exists:
```bash
# Create directories if needed (scripts do this automatically)
mkdir -p data/processed/exports
```

### Dashboard opens but shows no charts

**Solution:** Ensure you ran Step 2 (create_dashboard_data.py) to generate the CSV exports.

---

## Alternative: Power BI Desktop

To build a professional Power BI dashboard:

1. Download [Power BI Desktop](https://powerbi.microsoft.com/en-us/desktop/) (free)
2. Follow instructions in `docs/PowerBI_Dashboard_Instructions.md`
3. Use the cleaned data: `data/processed/Amazon_Combined_Data_Cleaned.xlsx`
4. Import CSV files from `data/processed/exports/` for individual visualizations

---

## Project Structure After Running

```
amazon-sales-dashboard/
├── data/
│   ├── raw/
│   │   └── Amazon_Combined_Data.xlsx        # Original (input)
│   └── processed/
│       ├── Amazon_Combined_Data_Cleaned.xlsx # Generated
│       └── exports/                          # Generated
│           ├── SalesByMonth.csv
│           ├── SalesByCategory.csv
│           ├── Top5Products.csv
│           ├── Top5ProductsByYear.csv
│           ├── SalesByDayOfWeek.csv
│           ├── SalesByYear.csv
│           └── SalesByPriceRange.csv
├── dashboards/
│   └── Amazon_Sales_Dashboard.html          # ✅ Your interactive dashboard
├── src/
│   ├── analyze_data.py                      # Run first
│   └── create_dashboard_data.py             # Run second
├── summary.json                             # Generated KPIs
└── ...
```

---

## For Recruiters / Code Review

- **Code quality:** See `src/` — well-documented, error-handled scripts with relative paths
- **Data work:** Check `data/processed/Amazon_Combined_Data_Cleaned.xlsx` — see cleaning applied
- **Analysis:** Read `docs/DATA_ANALYSIS_SUMMARY.md` — detailed findings with actual numbers
- **Dashboard:** Open `dashboards/Amazon_Sales_Dashboard.html` — interactive visualizations
- **Reproducibility:** Follow this guide — all analysis is fully reproducible from raw data

---

## Questions?

All Python scripts include docstrings and comments. For detailed analysis methodology, see `docs/DATA_ANALYSIS_SUMMARY.md`.
