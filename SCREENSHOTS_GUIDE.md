# Screenshots Guide

This document identifies the screenshots that should be added to the `screenshots/` folder for the GitHub portfolio.

## Required Screenshots

The following screenshots should be captured from the interactive HTML dashboard (`dashboards/Amazon_Sales_Dashboard.html`) and saved to `screenshots/`:

### 1. Dashboard Overview (`dashboard-overview.png`)
- Full dashboard view showing all 6 visualizations
- Capture: Open the HTML dashboard in a browser at standard desktop resolution (1200x800 or similar)
- Should show: KPI cards, sales trend line chart, category bar chart, top products, day-of-week column chart, and price range pie chart
- Purpose: Executive summary of the entire dashboard

### 2. Product & Category Analysis (`category-analysis.png`)
- Focus on the "Sales by Product Category" visualization (bar chart)
- Capture: Zoom/focus on the category bar chart section
- Should clearly show: All 8 product categories ranked by revenue, with Camera and Men's Shoes prominent
- Alternative: Screenshot showing both the category chart and the top 5 products chart together

### 3. Sales & Trend Analysis (`sales-trends.png`)
- Focus on the "Sales Trend by Month" visualization (line chart)
- Capture: The line chart showing monthly sales from January 2019 to December 2022
- Should clearly show: The sales trajectory, peak points (especially September 2019), and Q4 patterns
- Alternative: Could include the "Sales by Day of Week" chart as a bonus showing weekly patterns

## How to Capture Screenshots

**Option 1: Browser Screenshots (Recommended)**
1. Open `dashboards/Amazon_Sales_Dashboard.html` in Chrome, Firefox, or Safari
2. Use built-in browser screenshot tools (right-click → "Take a screenshot" or similar)
3. Crop to focus on specific charts as needed
4. Save as PNG files

**Option 2: Keyboard Shortcuts**
- Windows: Snip & Sketch (Win + Shift + S) → Save as PNG
- macOS: Screenshot (Cmd + Shift + 4) → Select area
- Linux: Screenshot tool or `import` command

**Option 3: Third-party Tools**
- Snagit, Greenshot, or similar screenshot tools
- Screen recording software (capture frames)

## File Naming Convention

Save screenshots to `screenshots/` folder with these names:
- `dashboard-overview.png` — Full dashboard view
- `category-analysis.png` — Category and product performance
- `sales-trends.png` — Monthly sales trends

## What NOT to Include in Screenshots

- Personal browser information (bookmarks, address bar URLs)
- System taskbars or notifications
- Large empty areas or unused screen space
- Cursor or selection artifacts
- Private/sensitive information if any appears

## Optional: Additional Screenshots

If desired, you could add one more screenshot:
- `price-distribution.png` — Pie chart showing revenue by price tier

This is optional but would provide a complete visual overview of all 6 charts.

## After Capturing

Once you have screenshots:
1. Create `screenshots/` folder in repository root
2. Save PNG files with names above
3. Update README.md to include a "Dashboard Preview" section with images (template provided below)
4. Commit and push to GitHub

## README.md Integration (Template)

Add this section to README after the project description:

```markdown
## 📸 Dashboard Preview

### Executive Overview
![Dashboard Overview](screenshots/dashboard-overview.png)
*Full dashboard showing all KPIs and visualizations*

### Product & Category Analysis
![Category Analysis](screenshots/category-analysis.png)
*Sales by product category and top 5 products*

### Sales Trends
![Sales Trends](screenshots/sales-trends.png)
*Monthly sales trends from January 2019 to December 2022*
```

## Status

- ✅ HTML dashboard exists and is fully functional
- ⚠️ Screenshots need to be captured manually (cannot be auto-generated)
- ⏳ Once captured, README.md will be updated with image references

---

**Note:** The interactive Plotly dashboard is a living visualization that updates based on interactivity. Static screenshots provide a quick visual reference for recruiters, while the HTML file provides full interactivity for deeper exploration.
