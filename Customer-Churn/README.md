# Customer Churn Prediction

## Overview
Predicted which telecom customers are likely to cancel their subscription
using customer demographics and service usage data.

## Dataset
- Source: Kaggle - Telco Customer Churn IBM Dataset
- Size: 7043 rows, 33 columns
- Target: Churn Label (Yes/No)

## Steps Followed
1. Exploratory Data Analysis with visualizations
2. Dropped irrelevant columns (location, IDs, post-churn data)
3. Fixed Total Charges column (was object type, converted to float)
4. Applied One Hot Encoding for categorical columns
5. Trained Logistic Regression and Random Forest models
6. Evaluated using classification report and confusion matrix

## Results
- Logistic Regression: 80%
- Random Forest: 80.6%
- Model struggles with recall for churners due to class imbalance

## Key Insights from EDA
- Month-to-month contract customers churn the most
- Higher monthly charges = higher churn rate
- Gender has no significant impact on churn

## What I Learned
- One Hot Encoding vs Label Encoding and when to use each
- Class imbalance problem in real world datasets
- Business importance of churn prediction
- Dropping columns that would cause data leakage

## Libraries Used
- Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
