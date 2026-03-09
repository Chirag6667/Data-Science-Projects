# 📱 Customer Churn Prediction — Kaggle Playground S6E3

> Predicting customer churn using EDA-driven feature engineering
> and gradient boosting models. Submitted to Kaggle competition.

---

## 🏆 Results

| Model | ROC-AUC |
|-------|---------|
| Logistic Regression | 0.9058 |
| Random Forest | 0.8962 |
| XGBoost | 0.9154 |
| **LightGBM** | **0.9165** ✅ |
| Ensemble (XGB+LGBM) | 0.9162 |

---

## 📊 Dataset
- 594,194 customer records
- 19 features — demographics, services, billing, contract type
- Target: Churn (Yes/No) — imbalanced 77/22 split
- Competition: Kaggle Playground Series Season 6 Episode 3

---

## 🔍 Key EDA Findings
- Month-to-month customers churn at **42%** vs 1% on two-year contracts
- Churned customers have average tenure of only **17 months**
- Churned customers pay **$81/month** vs $61 for loyal customers
- Contract type is the #1 business predictor of churn

---

## 🔧 Feature Engineering
- `HighCharges` — flag for monthly charges above $70
- `NewCustomer` — flag for tenure ≤ 6 months
- `ChargesPerMonth` — TotalCharges / tenure ratio
- `TotalServices` — count of subscribed services

---

## 💡 Business Recommendations
- Incentivize month-to-month customers to switch to annual contracts
- Focus retention on first 6 months — highest risk period
- Target high-paying customers with loyalty rewards

---

## 💻 Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost, LightGBM
- Matplotlib, Seaborn

---


