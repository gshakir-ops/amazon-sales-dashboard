# Amazon Sales Dashboard & Analysis

A professional data analytics portfolio project analyzing 4 years of Amazon sales data with interactive visualizations, comprehensive data cleaning, and business insights.

## 📊 Project Overview

This project demonstrates end-to-end data analysis workflow: from raw data to cleaned dataset to interactive dashboard. The analysis covers 88,947 sales transactions spanning January 2019 to December 2022, revealing key sales drivers, product performance patterns, and customer engagement insights.

**Total Revenue Analyzed:** $8.41M | **Items Sold:** 88,947 | **Customer Reviews:** 58.5M

## 🎯 Business Questions Addressed

This analysis answers critical business questions:

- **Which product categories drive the most revenue?**
  - Camera and Men's Shoes combined account for 56% of total sales ($4.7M)

- **What are the top-performing products?**
  - Atomos Ninja V Camera leads with $107K in sales
  - Identified 5 consistent top performers across the dataset

- **How do sales vary by season and day of week?**
  - Peak sales occur in September-December (Q4)
  - September 2019 recorded highest monthly sales ($193K)

- **What price points generate the most revenue?**
  - Premium segment ($500+) and mid-range ($50-100) drive majority of revenue
  - 50% of products priced under $46

- **How engaged are customers with products?**
  - Men's Clothes category has highest engagement (18.9M reviews)
  - Average product receives 658 reviews

## 📈 Key Findings

**Top Revenue Categories**
| Rank | Category | Revenue | % Total |
|------|----------|---------|--------|
| 1 | Camera | $2.48M | 29.4% |
| 2 | Men Shoes | $2.23M | 26.5% |
| 3 | Men Clothes | $1.16M | 13.8% |

**Best-Selling Products (All-Time)**
1. Atomos Ninja V Camera — $107,191
2. Canal Toys Photo Creator — $75,857
3. Solid Gear Hydra Safety Shoe — $66,361
4. KODAK Step Slim Printer — $60,968
5. Vince Camuto Dress Shoe — $46,260

**Seasonal Trends**
- Q4 consistently outperforms other quarters
- December shows sustained high sales across all years
- Monthly volatility suggests promotional/seasonal factors

## 🗂️ Dataset

**Source:** Amazon sales transactions (4-year period)
**Records:** 88,947 transactions (after cleaning)
**Time Period:** January 3, 2019 — December 31, 2022
**Data Quality:** 99.85% complete

**Key Fields:**
- Product Category (8 categories)
- Product Description
- Sale Price
- Number of Customer Reviews
- Order Date
- Shipment Type

## 🧹 Data Cleaning & Preparation

**Cleaning Steps Performed:**
- ✅ Column name standardization
- ✅ Data type conversion (numeric prices, datetime stamps)
- ✅ Missing value handling (median imputation for prices, 0 for reviews)
- ✅ Duplicate removal (135 rows eliminated)
- ✅ Invalid date removal
- ✅ Temporal feature engineering (Year, Month, Quarter, Day of Week)

**Results:**
- Original rows: 89,082
- Cleaned rows: 88,947
- Rows removed: 135 (0.15%)
- Final data quality: 100% complete

## 🔍 Analysis Performed

**Exploratory Data Analysis:**
- Descriptive statistics on prices and review counts
- Category-level aggregation and ranking
- Time-series decomposition by month and year
- Product performance ranking
- Weekly pattern analysis
- Price distribution analysis

**Data Exports:**
- Monthly sales trends (48 months)
- Category performance metrics
- Top 5 products overall and per-year
- Day-of-week sales patterns
- Price range distribution

## 📊 Dashboard

### Interactive HTML Dashboard
An interactive Plotly-based dashboard is included with 6 visualizations:

1. **Sales Trend by Month** — Line chart showing revenue trajectory
2. **Sales by Category** — Bar chart ranking categories
3. **Top 5 Products** — Product performance comparison
4. **Top 5 by Year** — Year-over-year product winners
5. **Sales by Day of Week** — Weekly pattern analysis
6. **Revenue by Price Tier** — Price range distribution

**View the dashboard:** Open `dashboards/Amazon_Sales_Dashboard.html` in any web browser (fully interactive, no installation required)

## 🛠️ Tech Stack

- **Python 3** — Data processing and analysis
- **Pandas** — Data manipulation and aggregation
- **Plotly** — Interactive visualizations
- **Excel** — Data storage
- **Markdown** — Documentation

## 📁 Repository Structure

```
amazon-sales-dashboard/
│
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── INSTALLATION.md                     # Setup and reproduction guide
│
├── src/                                # Python analysis scripts
│   ├── analyze_data.py                # Data cleaning and EDA
│   └── create_dashboard_data.py       # Export aggregations for dashboards
│
├── data/
│   ├── raw/
│   │   └── Amazon_Combined_Data.xlsx   # Original data (4 years)
│   └── processed/
│       ├── Amazon_Combined_Data_Cleaned.xlsx  # Cleaned dataset
│       └── exports/                           # CSV files
│           ├── SalesByMonth.csv
│           ├── SalesByCategory.csv
│           ├── Top5Products.csv
│           ├── Top5ProductsByYear.csv
│           ├── SalesByDayOfWeek.csv
│           ├── SalesByYear.csv
│           └── SalesByPriceRange.csv
│
├── dashboards/
│   └── Amazon_Sales_Dashboard.html     # Interactive dashboard
│
├── docs/
│   ├── PowerBI_Dashboard_Instructions.md    # How to build in Power BI
│   └── DATA_ANALYSIS_SUMMARY.md             # Detailed findings
│
└── .gitignore
```

## 🚀 How to Use

### Quick Start (No Installation)
1. Open `dashboards/Amazon_Sales_Dashboard.html` in any web browser
2. Interact with the visualizations — hover, zoom, toggle series

### To Reproduce the Analysis

**Step 1: Install Python dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Run data cleaning**
```bash
python src/analyze_data.py
```
This generates the cleaned dataset and summary statistics.

**Step 3: Export dashboard data**
```bash
python src/create_dashboard_data.py
```
This creates CSV exports for visualization.

**Step 4: View the dashboard**
Open `dashboards/Amazon_Sales_Dashboard.html` in your browser.

### Alternative: Power BI
For building a Power BI dashboard:
1. Follow instructions in `docs/PowerBI_Dashboard_Instructions.md`
2. Use cleaned data: `data/processed/Amazon_Combined_Data_Cleaned.xlsx`
3. Use CSV exports from `data/processed/exports/`

## 📌 Limitations & Considerations

**Data Limitations:**
- Historical data only (no real-time updates)
- Limited to Amazon product categories shown
- No customer demographic information
- No profit/cost data (revenue analysis only)
- No return/refund data (sales only)

**Analysis Scope:**
- This is retrospective analysis of completed transactions
- Patterns may not hold for future periods
- Seasonal effects observed may vary by year
- Product performance rankings based on revenue, not profit margin

## 🔮 Potential Future Enhancements

- **Automated Pipeline:** Connect to live data source with scheduled refreshes
- **Forecasting:** Build time-series models to predict future sales
- **Customer Segmentation:** Cluster customers by purchase behavior
- **Cohort Analysis:** Track customer groups over time
- **Profit Analysis:** Incorporate cost data for margin analysis
- **Sentiment Analysis:** Extract insights from review text
- **Real-time Dashboard:** Publish to Power BI Service for live updates

## 📚 Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Project overview (this file) |
| `INSTALLATION.md` | Detailed setup and reproduction steps |
| `requirements.txt` | Python package dependencies |
| `src/analyze_data.py` | Main data cleaning and analysis script |
| `src/create_dashboard_data.py` | Export script for dashboard datasets |
| `docs/DATA_ANALYSIS_SUMMARY.md` | Comprehensive analytical findings |
| `docs/PowerBI_Dashboard_Instructions.md` | Step-by-step Power BI guide |

## 🎓 Skills Demonstrated

This portfolio project demonstrates:

- **Data Cleaning** — Handling missing values, duplicates, type conversions
- **Exploratory Data Analysis** — Descriptive statistics, distributions, patterns
- **Feature Engineering** — Creating temporal and categorical features
- **Data Aggregation** — Group-by operations, multi-level analysis
- **Data Visualization** — Interactive charts and professional dashboards
- **Documentation** — Clear guides for reproducibility
- **Business Acumen** — Deriving actionable insights from data

## 📧 Questions?

Refer to the documentation files for detailed information. All analysis is reproducible using the Python scripts and included datasets.

---

**Project Created:** August 2026  
**Analysis Period:** January 2019 — December 2022  
**Data Quality:** 99.85% Complete  
**Status:** ✅ Complete & Ready for Review
