# ❤️ Heart Disease Prediction — ML Classification

> Predicting heart disease presence using clinical diagnostic features. Compared 3 models to find the best performer.

---

## 🏆 Final Results

| Model | Accuracy | ROC-AUC |
|-------|----------|---------|
| Logistic Regression | 88.33% | 0.9510 |
| Random Forest | 88.13% | 0.9473 |
| **XGBoost** | **88.78%** | **0.9549** ✅ |

---

## 📊 Dataset
- 630,000 patient records
- 13 clinical features — Age, BP, Cholesterol, Thallium, Chest pain type etc.
- Target: Heart Disease Presence / Absence (55% / 45%)

---

## 🔍 Key Findings

**Feature Importance**
- Thallium is the strongest predictor (0.60 importance score) — far above all others
- Chest pain type, Exercise angina, Number of vessels follow
- BP and Cholesterol are surprisingly weak predictors despite popular belief

**Thallium Analysis**
- Thallium = 3 → only 19% have heart disease
- Thallium = 6 → 68% have heart disease
- Thallium = 7 → 81% have heart disease

**Model Insight**
- XGBoost beats Random Forest despite RF having more complexity
- Logistic Regression performs surprisingly close to XGBoost — data has strong linear patterns

---

## 🛠️ Approach
- Encoded target column (Presence/Absence → 1/0)
- Correlation heatmap to identify key features
- StandardScaler for feature normalization
- Compared Logistic Regression, Random Forest, XGBoost
- Feature importance visualization

---

## 💻 Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Matplotlib, Seaborn

---
