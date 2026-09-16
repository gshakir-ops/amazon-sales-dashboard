# Amazon Sales Dashboard

Analysis of 4 years of Amazon sales data: $8.41M revenue, 88,947 transactions, 58.5M customer reviews.

## 🎯 Business Questions

- **Which product categories drive the most revenue?** Camera and Men's Shoes account for 56% of total sales ($4.7M combined).
- **What are the top-performing products?** Atomos Ninja V Camera leads with $107,191 in sales.
- **When do peak sales occur?** September 2019 recorded the highest monthly sales ($193,021); Q4 shows sustained high sales across all years.
- **What price points generate the most revenue?** Products under $100 account for majority of sales; 50% priced under $46; premium items ($500+) contribute significantly.
- **How engaged are customers?** Men's Clothes category has highest engagement (18.9M reviews); average product receives 658 reviews.

## 💡 Key Insights

**1. Revenue Concentration**
Camera and Men's Shoes generate $4.7M (56% of total revenue). Camera: $2.48M (29.4%), Men's Shoes: $2.23M (26.5%).

**2. Top Sellers**
- Atomos Ninja V Camera: $107,191
- Canal Toys Photo Creator: $75,857
- Solid Gear Hydra Safety Shoe: $66,361

**3. Q4 Performance**
December shows sustained high sales across 2019-2022. Q4 consistently outperforms Q1-Q3.

**4. Customer Engagement by Category**
Men's Clothes leads with 18.9M total reviews, despite lower revenue than Camera products ($1.16M vs $2.48M).

**5. Price Distribution**
Products range $0-$16,775. Median: $46. 25% under $24. Premium segment ($500+) drives significant revenue.

**6. Data Quality**
135 duplicates removed during cleaning. Final dataset: 88,947 rows with 100% completeness in price, date, category fields.

## 🛠 Tools

- **Python** — Data processing and analysis
- **Pandas** — Data aggregation and transformation
- **Plotly** — Interactive dashboard
- **Power BI** — Alternative dashboard (file included)
- **Excel** — Data storage

---

## 📊 Dashboard

**Interactive HTML Dashboard:** Open `dashboards/Amazon_Sales_Dashboard.html` in any web browser.
- 6 visualizations: Sales by month, category, top products, day of week, price tier, year-over-year
- Fully interactive: hover, zoom, toggle series
- No installation required

**Power BI Dashboard:** `dashboards/amazon dash board.pbix` (requires Power BI Desktop)
- Instructions for building from cleaned data in `docs/PowerBI_Dashboard_Instructions.md`

## 🗂️ Dataset

**Records:** 88,947 transactions (after cleaning)  
**Time Period:** January 3, 2019 — December 31, 2022  
**Data Quality:** 99.85% complete (135 duplicates removed)  
**Categories:** 8 product categories  

**Fields:** Product category, description, price, customer reviews, order date, shipment type

## 🧹 Data Cleaning

**Steps:**
- Column standardization
- Data type conversion (numeric prices, datetime stamps)
- Missing value handling (median imputation for prices, 0 for reviews)
- Duplicate removal (135 rows)
- Temporal feature engineering (Year, Month, Quarter, DayOfWeek)

**Results:** 89,082 → 88,947 rows. Rows removed: 135 (0.15%).

## 📁 Repository Structure

```
amazon-sales-dashboard/
├── README.md                           # This file
├── INSTALLATION.md                     # Setup guide
├── requirements.txt                    # Python dependencies
│
├── src/
│   ├── analyze_data.py                # Data cleaning and analysis
│   └── create_dashboard_data.py       # Export for dashboards
│
├── data/
│   ├── raw/
│   │   └── Amazon_Combined_Data.xlsx
│   └── processed/
│       ├── Amazon_Combined_Data_Cleaned.xlsx
│       └── exports/
│           ├── SalesByMonth.csv
│           ├── SalesByCategory.csv
│           ├── Top5Products.csv
│           ├── Top5ProductsByYear.csv
│           ├── SalesByDayOfWeek.csv
│           ├── SalesByYear.csv
│           └── SalesByPriceRange.csv
│
├── dashboards/
│   ├── Amazon_Sales_Dashboard.html
│   └── amazon dash board.pbix
│
├── docs/
│   ├── PowerBI_Dashboard_Instructions.md
│   └── DATA_ANALYSIS_SUMMARY.md
│
└── .gitignore
```

## 🚀 Quick Start

**View dashboard (no setup):**
1. Open `dashboards/Amazon_Sales_Dashboard.html` in web browser
2. Interact with charts — hover for values, click legend to toggle series

**Reproduce analysis:**
```bash
pip install -r requirements.txt
python src/analyze_data.py
python src/create_dashboard_data.py
```

See `INSTALLATION.md` for detailed instructions.

## 📌 Data Limitations

- Historical data only (no real-time updates)
- Revenue analysis only (no profit or cost data)
- No customer demographic information
- No return or refund data
- Performance based on revenue, not unit sales or margins

## 📚 Files Reference

| File | Purpose |
|------|---------|
| `README.md` | This file |
| `INSTALLATION.md` | Setup and reproduction |
| `requirements.txt` | Python dependencies |
| `src/analyze_data.py` | Data cleaning and analysis |
| `src/create_dashboard_data.py` | Export script |
| `docs/DATA_ANALYSIS_SUMMARY.md` | Detailed findings |
| `docs/PowerBI_Dashboard_Instructions.md` | Power BI setup |
| `dashboards/Amazon_Sales_Dashboard.html` | Interactive dashboard |
| `dashboards/amazon dash board.pbix` | Power BI file |

## 🎓 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory data analysis with Python and Pandas
- Feature engineering
- Data aggregation
- Data visualization (Plotly, Power BI)
- Documentation and reproducibility

---

**Analysis Period:** January 2019 — December 2022  
**Data Quality:** 99.85% Complete  
**Status:** ✅ Ready for Review
