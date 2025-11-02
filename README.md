# Analyzing Individual Feature Patterns using Visualization

This repository contains a comprehensive analysis of automobile feature patterns using data visualization techniques. 
The project explores relationships between various automobile characteristics and their prices through statistical plots and correlation analysis.

## Analysis Components

### Data Source
- Dataset: automobileEDA.csv
- Source: IBM Developer Skills Network
- Contains various automobile features and pricing information

### Numerical Variable Analysis
The project examines linear relationships between numerical features and price using scatter plots with regression lines:

- Engine size vs Price (Positive correlation)
<img width="500" height="500" alt="Figure_1" src="https://github.com/user-attachments/assets/07531961-8613-4f3f-a98b-08865b7297c9" />

- Highway MPG vs Price (Negative correlation) 
<img width="500" height="500" alt="Figure_2" src="https://github.com/user-attachments/assets/64997415-9a5d-4ad4-b624-a72c9267b5c7" />

- Peak RPM vs Price (Weak correlation)
<img width="500" height="500" alt="Figure_3" src="https://github.com/user-attachments/assets/3e7b3474-6013-4953-baaa-df171d1d2009" />

- Stroke vs Price (Weak correlation)
<img width="500" height="500" alt="Figure_4" src="https://github.com/user-attachments/assets/1e86d8a8-d7c7-4589-b081-f042c095be66" />

### Categorical Variable Analysis
Box plots are used to analyze how categorical features affect price distribution:

- Body style vs Price
<img width="500" height="500" alt="Figure_5" src="https://github.com/user-attachments/assets/f6f45bc4-ec52-4489-b49f-1955415f0d59" />

- Engine location vs Price
<img width="500" height="500" alt="Figure_6" src="https://github.com/user-attachments/assets/388e2382-57b1-4622-8f45-d94edf9c453b" />

- Drive wheels vs Price
<img width="500" height="500" alt="Figure_7" src="https://github.com/user-attachments/assets/c60b68f8-f6ce-40db-819e-951b8a9f5020" />

### Correlation Analysis
The script includes comprehensive correlation analysis between:
- Bore, stroke, compression-ratio, and horsepower
- Engine-size and price
- Highway-mpg and price
- Peak-rpm and price

## Technical Implementation

### Libraries Used
- pandas: Data manipulation and analysis
- numpy: Numerical computations
- matplotlib: Basic plotting and visualization
- seaborn: Statistical data visualization
- scikit-learn: Data preprocessing (LabelEncoder)

### Key Features
- Automated data type detection and handling
- Correlation matrix generation for numerical variables
- Encoding of categorical variables for analysis
- Regression plots for linear relationship analysis
- Box plots for categorical variable analysis

## Usage

Run the main script to:
1. Load and inspect the automobile dataset
2. Perform data type analysis and cleaning
3. Generate correlation matrices
4. Create visualization plots for feature analysis
5. Save figures to the figures directory

## Insights

The visualizations help identify:
- Strong positive correlation between engine size and price
- Strong negative correlation between highway MPG and price
- Price variations across different body styles
- Significant price differences based on drive wheel types
- Impact of engine location on vehicle pricing

## File Structure

```
Analyzing-Individual-Feature-Patterns-using-Visualization/
│
├── automobile_analysis.py          # Main analysis script
├── automobileEDA.csv               # Dataset (referenced from external source)
├── README.md                       # Project documentation
│
└── figures/                        # Generated visualization plots
    ├── Figure_1.png                # Engine size vs Price scatter plot
    ├── Figure_2.png                # Highway MPG vs Price scatter plot  
    ├── Figure_3.png                # Peak RPM vs Price scatter plot
    ├── Figure_4.png                # Stroke vs Price scatter plot
    ├── Figure_5.png                # Body style vs Price box plot
    ├── Figure_6.png                # Engine location vs Price box plot
    └── Figure_7.png                # Drive wheels vs Price box plot
```


This analysis provides valuable insights for understanding the factors that influence automobile pricing in the market.
