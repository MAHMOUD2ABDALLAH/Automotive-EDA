# ANOVA Analysis

A statistical analysis project examining the impact of different drive wheel types on vehicle pricing using Analysis of Variance (ANOVA) testing.

## Analysis Overview

This project performs ANOVA analysis to determine if different types of drive wheels have statistically significant impacts on vehicle pricing. The analysis compares price distributions across front-wheel drive (fwd), rear-wheel drive (rwd), and four-wheel drive (4wd) vehicle categories.

## Key Statistical Findings

### Overall ANOVA Results
- **F-Score**: 67.95
- **P-Value**: 3.39e-23

The extremely low p-value (p < 0.001) indicates very strong evidence that drive wheel type has a statistically significant effect on vehicle price.

### Pairwise Comparisons

#### fwd vs rwd
- **F-Score**: 130.55
- **P-Value**: 2.24e-23
- **Conclusion**: Very strong statistical significance

#### 4wd vs rwd
- **F-Score**: 8.58
- **P-Value**: 0.0044
- **Conclusion**: Strong statistical significance

#### 4wd vs fwd
- **F-Score**: 0.67
- **P-Value**: 0.416
- **Conclusion**: No statistical significance

## Statistical Methodology

### ANOVA Interpretation
- **P-value < 0.001**: Very strong evidence of group differences
- **P-value < 0.01**: Strong evidence of group differences
- **P-value < 0.05**: Evidence of group differences
- **P-value ≥ 0.05**: Weak or no evidence of group differences

### F-test Score
Higher F-scores indicate greater between-group variance relative to within-group variance, suggesting stronger group differences.

## File Structure

```
anova-analysis/
│
├── data/
│   ├── raw/
│   │   └── automotive_dataset.csv
│   ├── processed/
│   │   ├── grouped_drive_wheels.csv
│   │   └── anova_prepared_data.csv
│   └── outputs/
│       ├── anova_results.csv
│       ├── pairwise_comparisons.csv
│       └── statistical_summary/
│           ├── group_statistics.json
│           ├── variance_analysis.csv
│           └── hypothesis_testing_results.csv
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── anova_calculations.py
│   ├── statistical_significance.py
│   ├── visualization.py
│   └── report_generation.py
│
├── notebooks/
│   ├── 01_data_grouping_analysis.ipynb
│   ├── 02_anova_testing.ipynb
│   ├── 03_pairwise_comparisons.ipynb
│   └── 04_variance_visualization.ipynb
│
├── results/
│   ├── anova_analysis/
│   │   ├── overall_anova_results.json
│   │   ├── pairwise_comparisons.csv
│   │   └── statistical_power_analysis.md
│   ├── visualizations/
│   │   ├── group_distributions/
│   │   ├── variance_plots/
│   │   └── significance_charts/
│   └── reports/
│       ├── technical_analysis_report.md
│       ├── business_insights.md
│       └── statistical_validations.md
│
├── tests/
│   ├── __init__.py
│   ├── test_anova_methods.py
│   ├── test_pairwise_comparisons.py
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
