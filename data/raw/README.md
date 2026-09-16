# Raw Data

This directory contains the original, unmodified dataset.

## Files

- **Amazon_Combined_Data.xlsx** — Original data (89,082 rows before cleaning)

## Important Notes

- This is the source data - do not modify
- Data cleaning is performed by `src/analyze_data.py`
- Cleaned output goes to `data/processed/`

## Data Structure

The raw Excel file contains these columns:
1. Product Category
2. Product Description
3. Price
4. Number of Reviews
5. Shipment
6. Order Date

## Next Step

To process this data, run:
```bash
python src/analyze_data.py
```

This will:
- Clean missing values and duplicates
- Convert data types
- Add temporal features
- Output cleaned data to `data/processed/`
