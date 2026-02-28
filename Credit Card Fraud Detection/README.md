# 💳 Credit Card Fraud Detection

## Overview
Built a machine learning model to detect fraudulent credit card transactions using XGBoost on a highly imbalanced dataset. The model achieves 97.88% ROC-AUC score with only 8 false positives out of 56,962 test transactions.

## Dataset
- Source: Kaggle — Credit Card Fraud Detection by ULB Machine Learning Group
- Size: 284,807 transactions, 31 columns
- Fraud: Only 492 transactions (0.173%) — extreme class imbalance
- Features: V1-V28 (PCA transformed), Time, Amount, Class

## The Challenge
With only 0.173% fraud transactions, a naive model predicting "Normal" for everything gets 99.8% accuracy but catches zero fraud. This project tackles that problem properly.

## EDA Insights
- Fraud transactions have higher average amount ($122) vs normal ($88)
- Fraudsters prefer smaller amounts to avoid detection
- V17, V14, V12, V10 are most negatively correlated with fraud
- V11, V4, V2 are most positively correlated with fraud

## Approach

### Data Preprocessing
- Sorted by Time to respect temporal order
- Stratified train/test split to maintain fraud ratio
- Scaled Time and Amount using StandardScaler
- Fit scaler only on train data to prevent data leakage

### Handling Class Imbalance
- Used scale_pos_weight (~578) — tells XGBoost to treat each fraud as 578 normal transactions
- Used PR-AUC as evaluation metric instead of accuracy

### Model — XGBoost Classifier
- n_estimators: 400
- learning_rate: 0.05
- max_depth: 6
- eval_metric: aucpr (precision-recall)
- Early stopping to prevent overfitting

## Results
- ROC-AUC: 0.9788 (outstanding)
- PR-AUC: 0.8422 (very strong for imbalanced data)
- Fraud Recall: 83% (caught 81 out of 98 frauds)
- Fraud Precision: 91%
- F1-Score: 0.87
- False Positives: only 8

## Why These Metrics?
Accuracy is misleading for imbalanced data. PR-AUC and Recall are the correct metrics because:
- Missing a fraud (False Negative) costs money
- False alarms (False Positives) block genuine customers

## Visualizations
- Fraud vs Normal class distribution
- Transaction amount comparison (fraud vs normal)
- Top correlated features comparison

## Libraries Used
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- XGBoost

## Key Learnings
- Handling extreme class imbalance using scale_pos_weight
- Why accuracy is not a good metric for imbalanced datasets
- PR-AUC vs ROC-AUC — when to use which
- Preventing data leakage by fitting scaler only on train data
