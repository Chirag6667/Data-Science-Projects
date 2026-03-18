# Netflix User Watching Behavior - EDA

## 📌 Project Overview
Exploratory Data Analysis on Netflix User Watching 
Behavior Dataset (50,000 users, 20 features)

## 📊 Dataset
- Source: [Kaggle](https://www.kaggle.com/datasets/rhythmghai/netflix-user-watching-behavior-dataset)
-Rows: 50,000
- Columns: 20
- Target Variable: `churned` (Yes/No)

## 🔍 Analysis Performed
- Shape, dtypes, null value check
- Descriptive statistics
- Categorical value counts
- Churn distribution analysis
- Correlation heatmap
- Genre distribution
- Churn rate by country

## 💡 Key Insights
1. Dataset is synthetically generated
2. Churn rate is ~20% (class imbalance exists)
3. Standard plan users churn the most
4. Days since last login is best churn indicator
5. Watch time does NOT predict churn
6. No strong correlations between any features
7. All countries have equal ~20% churn rate

## 🛠️ Libraries Used
- Pandas
- Matplotlib
- Seaborn

## 🚀 Next Steps
- Build Churn Prediction Model (Random Forest / XGBoost)
