# Descriptive Statistical Analysis

This branch focuses on performing comprehensive descriptive statistical analysis on the automotive dataset using Python's pandas library.

## Analysis Performed

### 1. Numerical Variables Summary
Applied `describe()` method to analyze numerical variables including:
- **symboling**: Insurance risk rating (-2 to 3)
- **normalized-losses**: Relative average loss payment
- **wheel-base**: Vehicle wheelbase measurement
- **length**: Vehicle length
- **price**: Vehicle price in dollars
- **city-L/100km**: Fuel consumption in city
- **diesel/gas**: Fuel type indicators

### 2. Categorical Variables Analysis
Used `describe()` on object-type variables to examine:
- **make**: Vehicle manufacturer (22 unique values)
- **aspiration**: Turbo vs standard (2 types)
- **num-of-doors**: Door count (2 types)
- **body-style**: Vehicle body type (5 styles)
- **engine-type**: Engine configuration (6 types)
- **num-of-cylinders**: Cylinder count (7 variations)
- **fuel-system**: Fuel delivery system (8 types)
- **horsepower-binned**: Categorized horsepower (3 bins)

### 3. Specific Categorical Distributions

#### Drive Wheels Distribution:
```
fwd    118  (58.7%)
rwd     75  (37.3%)
4wd      8  (4.0%)
```

#### Engine Location Distribution:
```
front    198  (98.5%)
rear       3  (1.5%)
```

## Key Insights

### Numerical Data:
- Average vehicle price: $13,207
- Price range: $5,118 to $45,400
- Average city fuel consumption: 9.94 L/100km
- Majority vehicles use gas (90%) vs diesel (10%)

### Categorical Data:
- **Most common manufacturer**: Toyota (32 vehicles)
- **Most common body style**: Sedan (94 vehicles)
- **Most common engine type**: OHC (145 vehicles)
- **Most common aspiration**: Standard (165 vehicles)
- **Dominant drive wheels**: Front-wheel drive (118 vehicles)

## File Structure

```
descriptive-statistical-analysis/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py          # Data loading and preprocessing
│   ├── numerical_analysis.py   # Numerical variables analysis
│   ├── categorical_analysis.py # Categorical variables analysis
│   └── statistical_tests.py    # Additional statistical tests
│
├── data/
│   ├── raw/
│   │   └── automotive_data.csv
│   ├── processed/
│   │   ├── cleaned_data.csv
│   │   └── encoded_data.csv
│   └── outputs/
│       ├── numerical_summary.csv
│       ├── categorical_summary.csv
│       └── value_counts/
│           ├── drive_wheels.csv
│           ├── engine_location.csv
│           └── fuel_type.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_descriptive_stats.ipynb
│   └── 03_visualization.ipynb
│
├── reports/
│   ├── statistical_report.md
│   ├── numerical_insights.md
│   └── categorical_insights.md
│
├── tests/
│   ├── __init__.py
│   ├── test_numerical.py
│   └── test_categorical.py
│
├── config/
│   └── analysis_config.yaml
│
├── requirements.txt
├── main.py
└── README.md
```
