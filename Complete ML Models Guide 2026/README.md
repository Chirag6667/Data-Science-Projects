# 🤖 Complete ML Models Guide 2026

> A comprehensive cheat sheet covering all major ML algorithms —
> concept, parameters, code, and when to use each model.
> Built for interview preparation and quick reference.

---

## 📊 Model Comparison Table

| Model | Accuracy | ROC-AUC | Needs Scaling | Best For |
|-------|----------|---------|---------------|----------|
| Logistic Regression | 97% | 99% | ✅ Yes | Binary classification |
| Decision Tree | 94% | 93% | ❌ No | Interpretability |
| Random Forest | 96% | 99% | ❌ No | Tabular data |
| XGBoost | 95% | 99% | ❌ No | Competitions |
| LightGBM | 97% | 99% | ❌ No | Large datasets |
| CatBoost | 96% | 99% | ❌ No | Categorical data |
| KNN | 95% | 99% | ✅ Yes | Small datasets |
| SVM | 94% | 99% | ✅ Yes | High dimensional |
| Naive Bayes | 97% | 99% | ❌ No | Text/Spam |
| K-Means | - | - | ✅ Yes | Clustering |
| PCA | - | - | ✅ Yes | Dimensionality reduction |

---

## 🧠 Key Concepts Covered

**Supervised Learning**
- Linear & Logistic Regression
- Tree based models (Decision Tree, Random Forest)
- Boosting models (XGBoost, LightGBM, CatBoost)
- Distance based models (KNN, SVM)
- Probabilistic models (Naive Bayes)

**Ensemble Methods**
- Bagging → parallel training, reduces variance
- Boosting → sequential training, reduces bias
- Stacking → meta learner combines predictions

**Unsupervised Learning**
- K-Means Clustering → discover hidden groups
- PCA → dimensionality reduction

---

## 💡 Quick Reference — When to Use What?
Tabular data competition  → XGBoost / LightGBM
Many categorical features → CatBoost
Need interpretability     → Decision Tree / Logistic Regression
Text classification       → Naive Bayes / SVM
Small dataset             → KNN / SVM
Large dataset             → LightGBM
No labels available       → K-Means
Too many features         → PCA first!
Best possible accuracy    → Stacking

---

## 🔧 Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost, LightGBM, CatBoost
- Matplotlib, Seaborn

---
