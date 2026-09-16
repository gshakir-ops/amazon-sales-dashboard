# 📊 Amazon Sales Dashboard & Analysis

## Professional Data Analytics Portfolio Project

A comprehensive analysis of 4 years of Amazon sales data (88,947 transactions, $8.41M revenue) demonstrating end-to-end data analytics workflow: from raw data cleaning through exploratory analysis to interactive dashboard visualization.

**Status:** ✅ Complete & Production-Ready  
**Data Quality:** 99.85% Complete | **Time Period:** Jan 2019 - Dec 2022

---

## 🎯 What This Project Shows

### Business Questions Answered

1. **Which product categories drive revenue?**  
   Camera & Men's Shoes = 56% of all sales

2. **What are the top-performing products?**  
   Atomos Ninja V Camera leads with $107K in sales

3. **How do sales vary seasonally?**  
   Q4 consistently outperforms; September 2019 peak at $193K

4. **What price points generate most revenue?**  
   Premium ($500+) and mid-range ($50-100) drive majority of revenue

5. **How engaged are customers?**  
   Men's Clothes highest engagement (18.9M reviews)

### Key Findings

| Metric | Value |
|--------|-------|
| **Total Revenue** | $8,409,992 |
| **Items Sold** | 88,947 |
| **Customer Reviews** | 58,516,965 |
| **Top Category** | Camera (29.4% of revenue) |
| **Avg Price** | $94.55 |
| **Data Completeness** | 99.85% |

---

## 📂 Repository Contents

```
✅ Clean, organized structure
├── README.md                           Project overview
├── INSTALLATION.md                    Setup & reproduction guide
├── requirements.txt                   Python dependencies
│
├── src/                               Data analysis scripts
│   ├── analyze_data.py               Main cleaning & EDA
│   └── create_dashboard_data.py      Export for dashboards
│
├── data/
│   ├── raw/                          Original data
│   │   └── Amazon_Combined_Data.xlsx
│   └── processed/                    Cleaned & exports
│       ├── Amazon_Combined_Data_Cleaned.xlsx
│       └── exports/                  7 CSV files
│
├── dashboards/
│   └── Amazon_Sales_Dashboard.html   Interactive Plotly dashboard
│
└── docs/
    ├── PowerBI_Dashboard_Instructions.md
    └── DATA_ANALYSIS_SUMMARY.md
```

---

## 🚀 Quick Start

**View dashboard (30 seconds):**
```bash
# Open in browser
dashboards/Amazon_Sales_Dashboard.html
```

**Reproduce analysis (5 minutes):**
```bash
pip install -r requirements.txt
python src/analyze_data.py
python src/create_dashboard_data.py
# Open dashboards/Amazon_Sales_Dashboard.html
```

---

## 📊 Dashboard Features

**6 Interactive Visualizations:**
- Sales Trend by Month (line chart)
- Sales by Category (bar chart)
- Top 5 Products (product ranking)
- Top 5 by Year (year-over-year comparison)
- Weekly Patterns (day-of-week analysis)
- Price Distribution (revenue by tier)

**Technology:** Interactive Plotly dashboard, fully responsive, browser-based

---

## 🛠️ Skills Demonstrated

✅ Data Cleaning & Preprocessing  
✅ Exploratory Data Analysis  
✅ Feature Engineering (temporal features)  
✅ SQL-like aggregations (Pandas groupby)  
✅ Data Visualization & Dashboard Design  
✅ Python Best Practices (error handling, documentation)  
✅ Project Organization & Reproducibility  
✅ Business Intelligence & Insights

---

## 📌 Data Overview

**Dataset:** Amazon product sales transactions  
**Records:** 88,947 (after cleaning)  
**Time Span:** 4 years (Jan 2019 - Dec 2022)  
**Categories:** 8 product categories  
**Data Quality:** 99.85% complete

**Cleaning Applied:**
- Removed 135 duplicates
- Handled missing values (median imputation for prices)
- Converted to proper data types
- Added temporal features
- Validated dates

---

## 💡 Top Insights

**Revenue Concentration**
- Camera & Men Shoes = 56% of total revenue
- Top 5 products = $356K (4.2% of revenue)

**Seasonal Patterns**
- Q4 consistently strong
- September typically peaks ($193K in 2019)
- December sustained high sales

**Customer Engagement**
- 658 reviews per product (average)
- Men's Clothes: 18.9M reviews (most engaged)
- Camera: Lower reviews but highest revenue

**Price Performance**
- 50% of products priced under $46
- Premium items ($500+) drive significant revenue
- Wide price range ($0 - $16,775)

---

## 🔍 For Recruiters/Code Review

**Code Quality:** Professional Python with relative paths, error handling, docstrings  
**Data Work:** 99.85% data quality, comprehensive cleaning pipeline  
**Analysis:** Extracted from real data, honest findings with actual numbers  
**Documentation:** Complete reproducibility guide included  
**Deliverables:** Interactive dashboard + cleaned datasets + analysis

---

## 📖 Documentation

- **README.md** — Project overview and findings
- **INSTALLATION.md** — Step-by-step setup and reproduction
- **DATA_ANALYSIS_SUMMARY.md** — Detailed analytical findings
- **PowerBI_Dashboard_Instructions.md** — How to build in Power BI

---

**Ready to explore?** Start with the dashboard or follow INSTALLATION.md to reproduce the full analysis.
