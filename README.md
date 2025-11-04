# Grouping Vehicle Price by Body Style and Drive Wheels

This analysis examines vehicle pricing patterns based on body style and drive wheel configuration using grouping operations and visualization techniques.

## Analysis Steps

### 1. Basic Grouping by Drive Wheels
Grouped data by drive wheel type and calculated average prices:
- **4wd**: $10,241.00
- **fwd**: $9,244.78  
- **rwd**: $19,757.61

**Key Insight**: Rear-wheel drive (rwd) vehicles command significantly higher prices on average.

### 2. Two-Dimensional Grouping
Grouped by both 'drive-wheels' and 'body-style' to analyze price variations:
- Highest priced combination: rwd hardtop at $24,202.71
- Lowest priced combination: 4wd hatchback at $7,603.00
- rwd vehicles consistently show premium pricing across all body styles

### 3. Pivot Table Creation
Created a pivot table with:
- Rows: drive-wheels (4wd, fwd, rwd)
- Columns: body-style (convertible, hardtop, hatchback, sedan, wagon)
- Values: average price

### 4. Body Style Price Analysis
Calculated average prices by body style alone:
- **hardtop**: $22,208.50
- **convertible**: $21,890.50
- **sedan**: $14,459.76
- **wagon**: $12,371.96
- **hatchback**: $9,957.44

### 5. Visualization
Generated heat maps to visualize:
- Body Style vs Price relationships
<img width="500" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/ce22c314-8ff1-4f31-a970-c0487a862d03" />

- Combined effects of Body Style & Drive Wheels on Price
<img width="500" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/e93d970e-7494-4895-99d9-63fd9fdf4358" />

## File Structure

```
vehicle-price-analysis/
│
├── data/
│   ├── raw/
│   │   └── automotive_data.csv
│   └── processed/
│       ├── drive_wheels_prices.csv
│       ├── body_style_prices.csv
│       └── grouped_prices.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── grouping_analysis.ipynb
│   └── visualization.ipynb
│
├── src/
│   ├── data_processor.py
│   ├── analysis.py
│   └── visualizer.py
│
├── outputs/
│   ├── figures/
│   │   ├── Figure_1.png
│   │   └── Figure_2.png
│   └── tables/
│       ├── summary_statistics.csv
│       └── pivot_tables.csv
│
├── reports/
│   └── analysis_findings.md
│
├── requirements.txt
└── README.md
```
