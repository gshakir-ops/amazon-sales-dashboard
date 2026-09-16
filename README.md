# Amazon Sales Dashboard

A comprehensive Power BI dashboard analyzing Amazon sales data with interactive visualizations, trend analysis, and data-driven insights.

## 📊 Project Overview

This project showcases a complete data analysis workflow from raw data to interactive Power BI dashboard. It includes data cleaning, Python-based analysis, and multiple visualization outputs to understand sales patterns, product performance, and temporal trends.

### Key Features
- **Interactive Power BI Dashboard** - Explore sales metrics with drill-down capabilities
- **Data Cleaning Pipeline** - Python scripts to preprocess and clean raw data
- **Multi-format Exports** - CSV files for key metrics and insights
- **HTML Dashboard** - Standalone web-based dashboard for easy sharing
- **Comprehensive Documentation** - Step-by-step instructions for setup and usage

## 📁 Project Structure

```
amazon-sales-dashboard/
├── amazon dash board.pbix          # Main Power BI dashboard file
├── Amazon_Combined_Data.xlsx       # Raw Amazon sales data
├── Amazon_Combined_Data_Cleaned.xlsx # Cleaned and processed data
├── create_dashboard_data.py        # Script to generate dashboard datasets
├── analyze_data.py                 # Data analysis and insights generation
├── create_html_dashboard.py        # Script to generate HTML dashboard
├── Amazon_Sales_Dashboard.html     # Standalone HTML dashboard
├── DashboardInfo.json              # Dashboard metadata and configuration
├── summary.json                    # Analysis summary and statistics
├── PowerBI_Dashboard_Instructions.md # Setup and usage guide
├── DATA_ANALYSIS_SUMMARY.md        # Detailed analysis findings
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
│
└── Exports (CSV files)/
    ├── SalesByMonth.csv            # Monthly sales trends
    ├── SalesByYear.csv             # Yearly performance
    ├── SalesByCategory.csv         # Sales by product category
    ├── SalesByDayOfWeek.csv        # Day-of-week patterns
    ├── SalesByPriceRange.csv       # Sales distribution by price
    ├── Top5Products.csv            # Top 5 products overall
    └── Top5ProductsByYear.csv      # Top 5 products per year
```

## 🎯 Key Metrics & Insights

The dashboard analyzes:

- **Sales Performance**: Total sales, revenue trends, and growth rates
- **Product Analysis**: Top-performing products and categories
- **Temporal Patterns**: Monthly, yearly, and day-of-week trends
- **Price Analysis**: Sales distribution across price ranges
- **Seasonal Trends**: Identification of peak and low seasons

## 🛠️ Tech Stack

- **Power BI** - Interactive dashboard creation and visualization
- **Python 3** - Data processing and analysis
- **Pandas** - Data manipulation and cleaning
- **Excel** - Data storage and export
- **HTML/CSS/JavaScript** - Web-based dashboard

## 📋 Prerequisites

To run this project locally, you'll need:

- **Power BI Desktop** (to open `.pbix` files)
- **Python 3.7+** (to run analysis scripts)
- **Required Python libraries**:
  - pandas
  - openpyxl
  - json

## 🚀 Getting Started

### 1. View the Power BI Dashboard
- Open `amazon dash board.pbix` in Power BI Desktop
- Navigate through different tabs to explore sales insights
- Use filters to drill down into specific time periods or categories

### 2. View the HTML Dashboard
- Simply open `Amazon_Sales_Dashboard.html` in any web browser
- No installation required - fully standalone
- Ideal for sharing with stakeholders

### 3. Run Python Analysis Scripts

```bash
# Install required packages
pip install pandas openpyxl

# Generate dashboard data from raw Excel file
python create_dashboard_data.py

# Run detailed data analysis
python analyze_data.py

# Generate HTML dashboard
python create_html_dashboard.py
```

### 4. Review Documentation
- See `PowerBI_Dashboard_Instructions.md` for detailed dashboard navigation
- Check `DATA_ANALYSIS_SUMMARY.md` for comprehensive findings

## 📊 Dashboard Components

### Main Dashboard Tabs
1. **Overview** - High-level KPIs and sales summary
2. **Products** - Product performance and category analysis
3. **Trends** - Temporal patterns and seasonal analysis
4. **Geography** (if applicable) - Location-based insights

### Key Visualizations
- Sales trend line charts
- Category performance bar charts
- Top products rankings
- Day-of-week heatmaps
- Price range distribution

## 💾 Data Files

| File | Description | Format |
|------|-------------|--------|
| `Amazon_Combined_Data.xlsx` | Raw, uncleaned data | Excel |
| `Amazon_Combined_Data_Cleaned.xlsx` | Processed data ready for analysis | Excel |
| `SalesByMonth.csv` | Aggregated monthly sales | CSV |
| `SalesByCategory.csv` | Sales breakdown by category | CSV |
| `Top5Products.csv` | Top performing products | CSV |

## 📈 Key Findings

Refer to `DATA_ANALYSIS_SUMMARY.md` for detailed insights including:
- Best-performing product categories
- Seasonal trends and peak sales periods
- Price sensitivity analysis
- Growth trends over time

## 🔄 Data Pipeline

```
Raw Data (Excel) 
    ↓
Data Cleaning (analyze_data.py)
    ↓
Cleaned Data (Excel)
    ↓
Dashboard Creation (Power BI / HTML)
    ↓
Export CSVs (create_dashboard_data.py)
    ↓
Interactive Visualizations
```

## 🎨 Customization

### Modifying the Power BI Dashboard
1. Open `amazon dash board.pbix` in Power BI Desktop
2. Edit visualizations by clicking on them
3. Add new measures and columns as needed
4. Publish to Power BI Service for cloud sharing

### Updating Data
1. Update `Amazon_Combined_Data.xlsx` with new data
2. Run `create_dashboard_data.py` to refresh CSVs
3. Refresh Power BI dataset (Right-click → Refresh)

## 📝 Files Reference

- **PowerBI_Dashboard_Instructions.md** - Comprehensive guide for using the Power BI dashboard
- **DATA_ANALYSIS_SUMMARY.md** - Detailed statistical analysis and findings
- **DashboardInfo.json** - Metadata about dashboard configuration
- **summary.json** - Quantitative summary of key metrics

## 🤝 Contributing

Feel free to fork this project and enhance it with:
- Additional visualizations
- Forecasting models
- Real-time data integration
- Performance optimizations

## 📧 Contact & Support

For questions or suggestions about this project, please reach out or open an issue.

## 📜 License

This project is open source and available for educational and commercial use.

---

**Last Updated**: September 2026

**Version**: 1.0

**Author**: Data Analyst Portfolio

---

## 🔗 Related Resources

- [Power BI Official Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Data Analysis Best Practices](https://www.example.com)

## ✅ Checklist for Dashboard Usage

- [ ] Installed Power BI Desktop
- [ ] Opened the .pbix file successfully
- [ ] Reviewed the DATA_ANALYSIS_SUMMARY.md
- [ ] Explored all dashboard tabs
- [ ] Opened the HTML dashboard in browser
- [ ] Reviewed the instructions document

---

**Note**: Power BI files (.pbix) are binary files and may be large. The HTML dashboard provides a lightweight alternative for viewing and sharing insights.
