# House Price Prediction

## Overview
Predicted residential house prices in Ames, Iowa using structured housing data from the Kaggle competition  
House Prices - Advanced Regression Techniques.

## Dataset
- Source: Kaggle – House Prices Competition
- Training: 1460 rows, 81 features
- Test: 1459 rows
- Target: SalePrice

## Steps Followed
1. Loaded and explored the dataset
2. Handled missing values – Numerical (mean), Categorical ("None")
3. Converted categorical columns using Label Encoding
4. Split data (80% train, 20% validation)
5. Trained Linear Regression model
6. Evaluated using RMSE and R²
7. Created submission file for Kaggle

## Results
- Validation RMSE: ~25,272
- R² Score: ~0.87
- Kaggle Public Score (Log RMSE): ~0.34

## Libraries Used
- Pandas
- NumPy
- Scikit-learn

## What I Learned
- Importance of consistent preprocessing between train and test
- Encoding strategy impacts model performance
- Difference between local validation and leaderboard score
- Need for better feature engineering and transformation
