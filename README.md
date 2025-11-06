# Correlation & Causation Analysis

A statistical analysis project examining relationships between automotive features and vehicle pricing using correlation coefficients and significance testing.

## Analysis Overview

This project performs correlation analysis to identify which vehicle characteristics have the strongest relationships with pricing and determine the statistical significance of these relationships.

## Key Statistical Findings

### Strong Positive Correlations with Price
- Curb-weight: 0.834 (P-value: 2.19e-53)
- Horsepower: 0.810 (P-value: 6.37e-48)
- Width: 0.751 (P-value: 9.20e-38)
- Length: 0.691 (P-value: 8.02e-30)
- Wheel-base: 0.585 (P-value: 8.08e-20)

### Strong Negative Correlations with Price
- Highway-mpg: -0.705 (P-value: 1.75e-31)
- City-mpg: -0.687 (P-value: 2.32e-29)

### Moderate Correlations
- Bore: 0.543 (P-value: 8.05e-17)
- Engine-size: 0.872 (P-value: < 0.001)

## Statistical Methodology

### Correlation Strength Interpretation
- ±0.8 to ±1.0: Very strong correlation
- ±0.6 to ±0.8: Strong correlation
- ±0.4 to ±0.6: Moderate correlation
- ±0.2 to ±0.4: Weak correlation
- ±0.0 to ±0.2: Very weak correlation

### Statistical Significance Testing
- P-value < 0.001: Very strong evidence
- P-value < 0.01: Strong evidence
- P-value < 0.05: Evidence
- P-value ≥ 0.05: Weak or no evidence

## File Structure

```
correlation-causation-analysis/
│
├── data/
│   ├── raw/
│   │   └── automotive_dataset.csv
│   ├── processed/
│   │   ├── cleaned_correlation_data.csv
│   │   └── normalized_features.csv
│   └── outputs/
│       ├── correlation_matrix.csv
│       ├── p_values_matrix.csv
│       └── statistical_summary/
│           ├── significant_correlations.json
│           ├── feature_relationships.csv
│           └── hypothesis_testing_results.csv
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── correlation_calculations.py
│   ├── statistical_significance.py
│   ├── visualization.py
│   └── report_generation.py
│
├── notebooks/
│   ├── 01_correlation_matrix_analysis.ipynb
│   ├── 02_significance_testing.ipynb
│   ├── 03_relationship_visualization.ipynb
│   └── 04_causation_analysis.ipynb
│
├── results/
│   ├── correlation_analysis/
│   │   ├── pearson_coefficients.json
│   │   ├── significant_relationships.csv
│   │   └── statistical_power_analysis.md
│   ├── visualizations/
│   │   ├── correlation_heatmap/
│   │   ├── scatter_plots/
│   │   │   ├── price_vs_curb_weight/
│   │   │   ├── price_vs_horsepower/
│   │   │   ├── price_vs_city_mpg/
│   │   │   └── price_vs_highway_mpg/
│   │   └── significance_plots/
│   │       ├── p_value_distribution/
│   │       └── confidence_intervals/
│   └── reports/
│       ├── technical_analysis_report.md
│       ├── business_insights.md
│       └── statistical_validations.md
│
├── tests/
│   ├── __init__.py
│   ├── test_correlation_methods.py
│   ├── test_significance_calculations.py
│   └── test_data_integrity.py
│
├── config/
│   └── analysis_parameters.yaml
│
├── docs/
│   ├── methodology.md
│   ├── statistical_assumptions.md
│   └── interpretation_guidelines.md
│
├── requirements.txt
├── main.py
└── README.md
```
