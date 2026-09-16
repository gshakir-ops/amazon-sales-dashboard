# Amazon Sales Dashboard - Power BI Instructions

## 📊 Dashboard Overview

**Your Amazon Sales Analytics Dashboard includes:**
- **3 KPIs**: Total Sales, Total Reviews, Total Items Sold
- **6 Main Charts**: Sales trends, category analysis, top performers
- **4 Interactive Filters**: Year, Category, Month, Date Range
- **2 Bonus Insights**: Day of week patterns, price range distribution

---

## 🚀 How to Build This Dashboard in Power BI Desktop

### Step 1: Open Power BI Desktop
1. Launch **Power BI Desktop** (Download from microsoft.com/power-bi if needed)
2. Click **Get Data** → **Excel**

### Step 2: Import Your Cleaned Data
1. Navigate to: `C:\Users\LENOVO\Desktop\Power Bi\project 1\`
2. Select: **Amazon_Combined_Data_Cleaned.xlsx**
3. Check the **CleanedData** sheet
4. Click **Load**

### Step 3: Create KPI Cards (Top Section)

**KPI 1: Total Sales**
1. Click **Card** visual from Visualizations pane
2. Drag **Price** to **Fields**
3. Click dropdown on Price → **Sum**
4. Format:
   - Display units: None
   - Value: Font size 48, Bold
   - Category label: "Total Sales"
   - Background: Light blue (#E8F4F8)

**KPI 2: Total Reviews**
1. Add another **Card** visual
2. Drag **NumberOfReviews** to Fields
3. Sum aggregation
4. Format similarly with label "Total Reviews"
5. Background: Light green (#E8F8E8)

**KPI 3: Total Items Sold**
1. Add **Card** visual
2. Drag **ProductDescription** to Fields
3. Change to **Count** (not Count Distinct)
4. Label: "Total Items Sold"
5. Background: Light orange (#FFF4E8)

**Position these 3 cards at the TOP of your dashboard in a row**

---

### Step 4: Sales by Month (Line Chart)

1. Select **Line Chart** visual
2. **X-axis**: Drag **YearMonth** field
3. **Y-axis**: Drag **Price** field (Sum)
4. Format:
   - Title: "Sales Trend by Month"
   - X-axis label angle: 45°
   - Data labels: On
   - Line color: #1f77b4 (Blue)
   - Markers: On
5. Size: Wide rectangle, place below KPIs

---

### Step 5: Sales by Product Category (Bar Chart)

1. Select **Clustered Bar Chart**
2. **Y-axis**: **ProductCategory**
3. **X-axis**: **Price** (Sum)
4. Sort by: Price (Descending)
5. Format:
   - Title: "Sales by Product Category"
   - Data labels: On
   - Bar color: #2ca02c (Green)
6. Place on left side below line chart

---

### Step 6: Top 5 Products (Bar Chart)

**Option A: Use the main dataset**
1. Select **Clustered Bar Chart**
2. **Y-axis**: **ProductDescription**
3. **X-axis**: **Price** (Sum)
4. Click **Filters** pane → **ProductDescription**
5. Filter type: **Top N**
6. Show items: **Top 5**
7. By value: **Sum of Price**
8. Format:
   - Title: "Top 5 Products (Overall)"
   - Data labels: On
   - Bar color: #ff7f0e (Orange)
9. Place on right side

**Option B: Import Top5Products.csv**
1. Get Data → CSV → Select `Top5Products.csv`
2. Create relationship if needed
3. Use this cleaner data for the visual

---

### Step 7: Top 5 Products by Year (Clustered Bar Chart)

1. Import **Top5ProductsByYear.csv** (Get Data → CSV)
2. Select **Clustered Bar Chart**
3. **Y-axis**: **ProductDescription**
4. **X-axis**: **TotalSales**
5. **Legend**: **Year**
6. Format:
   - Title: "Top 5 Products by Year"
   - Colors: Different color per year
   - Data labels: On
7. Place below the overall Top 5 chart

---

### Step 8: Add Interactive Filters (Slicers)

**Filter 1: Year Slicer**
1. Add **Slicer** visual
2. Field: **Year**
3. Format: Vertical list with checkboxes
4. Position: Top-right corner

**Filter 2: Product Category Slicer**
1. Add **Slicer** visual
2. Field: **ProductCategory**
3. Format: Dropdown (saves space)
4. Position: Below Year slicer

**Filter 3: Month Slicer**
1. Add **Slicer** visual
2. Field: **MonthName**
3. Format: Tile style (visual buttons)
4. Position: Below Category slicer

**Filter 4: Date Range Slicer**
1. Add **Slicer** visual
2. Field: **OrderDate**
3. Format: Between (range slider)
4. Position: Bottom of filter column

---

### Step 9: BONUS Charts (Optional but Recommended)

**Bonus 1: Sales by Day of Week**
1. Import **SalesByDayOfWeek.csv**
2. Create **Column Chart**
3. X-axis: DayOfWeek
4. Y-axis: TotalSales
5. Title: "Best Selling Days"
6. Insight: See which weekdays perform best

**Bonus 2: Sales by Price Range**
1. Import **SalesByPriceRange.csv**
2. Create **Donut Chart**
3. Legend: PriceRange
4. Values: TotalSales
5. Title: "Revenue Distribution by Price Tier"
6. Insight: Understand which price brackets drive revenue

---

### Step 10: Dashboard Formatting & Design

**Theme & Colors**
1. View → Themes → Select **Executive** or **Colorblind Safe**
2. Or use custom colors:
   - Primary: #1f77b4 (Blue)
   - Secondary: #2ca02c (Green)
   - Accent: #ff7f0e (Orange)
   - Warning: #d62728 (Red)

**Layout Best Practices**
```
┌─────────────────────────────────────────────────────────┐
│  KPI: Sales     KPI: Reviews     KPI: Items Sold        │
├─────────────────────────────────────────────────────────┤
│              Sales Trend by Month (Line)                │
├──────────────────────────────┬──────────────────────────┤
│  Sales by Category (Bar)     │  Filters:                │
│                              │  - Year                  │
│                              │  - Category              │
│                              │  - Month                 │
├──────────────────────────────┤  - Date Range            │
│  Top 5 Products (Bar)        │                          │
│                              │                          │
├──────────────────────────────┤                          │
│  Top 5 by Year (Clustered)   │                          │
└──────────────────────────────┴──────────────────────────┘
```

**Professional Touches**
1. Add **Text Box** at top: "Amazon Sales Analytics Dashboard"
   - Font: Segoe UI, 24pt, Bold
2. Add logo if available
3. Consistent margins: 10px between visuals
4. Align all visuals properly (use Align tools)
5. Add subtle backgrounds to sections

---

### Step 11: Create DAX Measures (Advanced)

Add these calculated measures for more insights:

**Average Order Value**
```DAX
Avg Order Value = AVERAGE('CleanedData'[Price])
```

**Revenue Growth (Month over Month)**
```DAX
Revenue Growth % = 
VAR CurrentMonth = SUM('CleanedData'[Price])
VAR PreviousMonth = CALCULATE(
    SUM('CleanedData'[Price]),
    DATEADD('CleanedData'[OrderDate], -1, MONTH)
)
RETURN
DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth, 0)
```

**Total Customers (if customer data available)**
```DAX
Total Customers = DISTINCTCOUNT('CleanedData'[CustomerId])
```

**Year-to-Date Sales**
```DAX
YTD Sales = TOTALYTD(SUM('CleanedData'[Price]), 'CleanedData'[OrderDate])
```

---

### Step 12: Add Drill-Through Feature

1. Create a new page: "Product Details"
2. Add drill-through field: **ProductDescription**
3. Add detailed visuals:
   - Sales trend for that product
   - Review count over time
   - Categories it belongs to
4. User can now right-click any product → Drill through → See details

---

### Step 13: Save and Publish

**Save Locally**
1. File → Save As
2. Name: `Amazon_Sales_Dashboard.pbix`
3. Location: `C:\Users\LENOVO\Desktop\Power Bi\project 1\`

**Publish to Power BI Service** (if you have Pro license)
1. Click **Publish** button
2. Select workspace
3. Share link with team
4. Enable auto-refresh

---

## 📈 Key Insights from Your Data

Based on the analysis:

1. **Total Revenue**: $8.4 Million from 88,947 items
2. **Top Category**: Camera products ($2.48M)
3. **Most Reviewed Category**: Men Clothes (18.9M reviews)
4. **Date Range**: January 2019 - December 2022 (4 years)
5. **Average Price**: $94.55
6. **Peak Month**: September 2019 ($193K)

**Top 5 Products Overall:**
1. Atomos Ninja V Camera - $107,191
2. Canal Toys Photo Creator - $75,857
3. Solid Gear Hydra Safety Shoe - $66,361
4. KODAK Step Slim Printer - $60,968
5. Vince Camuto Dress Shoe - $46,260

---

## 🎯 Dashboard Usage Tips

**For Executive Reports:**
- Focus on KPI cards first
- Use Year filter to compare performance
- Export to PowerPoint: File → Export → PowerPoint

**For Deep Analysis:**
- Use all slicers together for segment analysis
- Right-click charts → "Show as table" for numbers
- Enable drill-through for product-level details

**For Presentations:**
- Use Focus mode (click visual, press Ctrl+F)
- Create bookmarks for key views
- Add text annotations to highlight insights

---

## 🔧 Troubleshooting

**Issue: Date not recognized**
- Solution: Ensure OrderDate column is set to Date type

**Issue: Charts not filtering together**
- Solution: Check relationships in Model view

**Issue: Top 5 showing wrong products**
- Solution: Verify filter is set to "Top N by Sum of Price"

**Issue: Numbers look wrong**
- Solution: Check aggregation (Sum vs Average vs Count)

---

## 📚 Next Steps

1. ✅ Build the basic dashboard following steps above
2. ✅ Add the bonus charts for extra insights
3. ✅ Publish to Power BI Service
4. ✅ Schedule auto-refresh if connected to live data
5. ✅ Share with stakeholders
6. ✅ Gather feedback and iterate

---

## 💡 Pro Tips

- **Use consistent colors** across all charts
- **Keep it simple** - don't overcrowd the dashboard
- **Test on mobile** - Power BI mobile app layout
- **Add tooltips** - Hover information for context
- **Use bookmarks** - Save different filter states
- **Enable cross-filtering** - Click one chart to filter others

---

**Need Help?** 
- Power BI Documentation: docs.microsoft.com/power-bi
- Community: community.powerbi.com
- YouTube: "Power BI Dashboard Tutorial"

**Dashboard Created By:** Kiro AI Assistant  
**Date:** August 30, 2026  
**Version:** 1.0
