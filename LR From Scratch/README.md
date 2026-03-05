# 🧠 Logistic Regression From Scratch — Diabetes Prediction

## Overview
Implemented Logistic Regression completely from scratch using 
only NumPy — without using sklearn's LogisticRegression. 
Built every component manually including the sigmoid function, 
cost function, and gradient descent optimizer.

Achieved 79.87% accuracy, outperforming sklearn's default 
implementation (77.92%) on the Pima Indians Diabetes Dataset.

## Dataset
- Source: Kaggle — Pima Indians Diabetes Dataset
- Size: 768 rows, 9 columns
- Target: Outcome (1 = Diabetic, 0 = Not Diabetic)
- Class Distribution: 500 non-diabetic (65.1%), 268 diabetic (34.9%)

## Why From Scratch?
Using sklearn is easy. But understanding WHAT happens inside 
the model is what separates a good ML engineer from someone 
who just knows how to import libraries.

Building from scratch forces you to understand:
- How weights are initialized and updated
- How gradient descent actually works mathematically
- Why feature scaling is critical
- What the cost function actually measures

## EDA Insights
- Glucose is the strongest predictor of diabetes
- BMI and Age are second and third most important
- BloodPressure and SkinThickness have very weak correlation
- Age and Pregnancies are moderately correlated (0.54) — multicollinearity
- Dataset is moderately imbalanced — 65% vs 35%

## Implementation — Built From Scratch

### 1. Sigmoid Function
sigmoid(z) = 1 / (1 + e^(-z))
Converts any number to probability between 0 and 1.

### 2. Cost Function (Log Loss)
Cost = -1/m × Σ [y×log(prediction) + (1-y)×log(1-prediction)]
Measures how wrong predictions are. Lower cost = better model.

### 3. Gradient Descent
dw = 1/m × X^T × (predictions - y)
db = 1/m × sum(predictions - y)
weights = weights - learning_rate × dw
bias = bias - learning_rate × db

Ran for 1000 iterations with learning rate 0.1.
Cost decreased consistently from start to finish.

### 4. Predict Function
Convert probability to binary using 0.5 threshold.
probability >= 0.5 → Diabetic (1)
probability < 0.5 → Not Diabetic (0)

## Results

| Model | Accuracy |
|-------|----------|
| Logistic Regression From Scratch | 79.87% |
| Sklearn LogisticRegression | 77.92% |

Our scratch implementation outperforms sklearn's default!

## Key Concepts Demonstrated
- Sigmoid function and probability conversion
- Log Loss cost function
- Gradient descent optimization
- Matrix transpose in gradient calculation
- Feature scaling with StandardScaler
- Stratified train/test split
- Confusion matrix interpretation

## Why Feature Scaling Is Critical
Insulin values go up to 800 while DiabetesPedigreeFunction 
stays below 2.5. Without scaling, gradient descent becomes 
unstable — large features dominate small ones. 
StandardScaler brings all features to same scale.

## Libraries Used
- NumPy — entire implementation
- Pandas — data loading
- Matplotlib, Seaborn — visualizations
- Sklearn — only for data splitting, scaling, and comparison

## Key Learnings
- How logistic regression actually works mathematically
- Why gradient descent needs feature scaling
- What matrix transpose means and why it's needed
- Difference between dot product and sum in gradient calculation
- How to verify scratch implementation against sklearn
