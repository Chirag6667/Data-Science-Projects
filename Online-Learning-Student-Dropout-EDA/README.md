# 🎓 Online Learning Student Dropout — EDA

> Exploratory Data Analysis on 5,000 student records to uncover 
> what separates students who complete courses from those who drop out.

---

## 🏆 Key Findings

**Dropout Rate**
- 65.92% of students are either at-risk or have dropped out
- Only 1 in 3 students successfully completes their course

**Top Dropout Predictors**
- Completion rate is the strongest signal (-0.73 correlation)
- Login frequency drops to 0.86 for dropped students vs 6.67 for active
- Forum engagement and assignment completion follow closely
- Age has virtually zero impact (-0.02) — dropout is purely behavioural

**Early Warning Signals**
- Completion rate below 20% → high dropout risk
- Login frequency below 2 → immediate intervention needed

---

## 📊 Dataset
- 5,000 student records
- 15 features — age, region, login frequency, completion rate, forum posts etc.
- Target: Active / At-risk / Dropped (3 class problem)
- Zero missing values ✅

---

## 📈 Visualizations
- Student dropout distribution
- Age distribution by student status
- Completion rate vs dropout (boxplot)
- Login frequency vs dropout (boxplot)
- Correlation heatmap

---

## 💡 Recommendations
- Alert students when completion rate drops below 20%
- Send re-engagement emails when login frequency drops below 2
- Gamify forum participation to boost engagement
- Push notifications for students inactive for 7+ days

---

## 💻 Tech Stack
- Python, Pandas, NumPy
- Matplotlib, Seaborn

---
