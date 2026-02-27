# Amazon Sales Unleashed: EDA + What Drives Revenue 🚀

**Uncovering the real levers behind Amazon sales** — discounts, categories, regions — using Exploratory Data Analysis and XGBoost feature importance.

## 🎯 Objective
Analyze ~50,000 Amazon sales records to answer:
- Which features most strongly drive **total revenue**?
- How do **categories**, **regions**, and **discounts** impact performance?
- Build a simple predictive model and extract business insights.

## 🔍 Key Findings
- **Discount percent** is by far the #1 driver of revenue (highest feature importance)
- **Asia region** shows strong positive influence
- Top categories: **Beauty**, **Fashion**, **Home & Kitchen** lead in revenue & profit
- High revenue categories don't always mean high unit profitability (e.g., Sports lags in profit per unit)

## 🛠️ Tech Stack
- **Language**: Python
- **Libraries**: pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost
- **Environment**: Jupyter Notebook (exported from Kaggle)

## 📊 Main Sections in the Notebook
1. **Correlation Heatmap** — spotting multicollinearity & revenue drivers  
2. **Category Performance** — Revenue vs Profit per Unit (dual-axis viz)  
3. **Absolute Revenue & Profit by Category** — identifying top contributors  
4. **XGBoost Model + Feature Importance** — what actually matters most

## 📈 Visual Highlights
- Correlation matrix (coolwarm)  
- Bar + line charts for category revenue/profit  
- Feature importance bar plot (discounts dominate!)
