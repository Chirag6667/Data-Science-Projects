🏠 Florida Real Estate Market Analysis (2026)
=============================================

This project provides an in-depth Exploratory Data Analysis (EDA) of the Florida real estate market using a 2026 "Sold" dataset. The analysis focuses on price drivers, negotiation trends, and geographic value distribution.

🚀 Project Overview
-------------------

The goal of this study was to move beyond raw pricing and understand the **Price-per-Square-Foot** efficiency and the **List-vs-Sold** relationship across different Florida ZIP codes and property types.

🛠️ Tech Stack
--------------
-   **Dataset**: https://www.kaggle.com/datasets/kanchana1990/florida-real-estate-sold-dataset-2026

-   **Python**

-   **Pandas**: Advanced data cleaning and `groupby.transform` imputation.

-   **Seaborn & Matplotlib**: Statistical visualizations and regression mapping.

-   **NumPy**: Numerical filtering and outlier detection.

📈 Analysis Highlights
----------------------

### 1\. Advanced Data Cleaning

Handled over 10,000 records with significant missing values.

-   Implemented **Categorical Imputation**: Filled missing `sqft` and `beds` using the median specific to the property type to maintain data integrity.

-   **Outlier Removal**: Filtered nonsensical data points (e.g., Sold Ratios > 1.5 or < 0.5) to ensure statistical robustness.

### 2\. Negotiation Metrics

Analyzed the "Sold-to-List" ratio. Findings show a seller-leaning market with a **0.97 median ratio**, indicating high demand and firm pricing across the state.

### 3\. Geographic Concentration

Mapped value by ZIP code, identifying **33109** as the most expensive micro-market in the study, significantly outpacing the state average.

### 4\. Property Age Correlation

Visualized the impact of property age on sale price, identifying the premium placed on new builds versus the varying value of historic Florida architecture.
