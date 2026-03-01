# 🌸 Iris Flower Classification

## Overview
Classic machine learning project to classify iris flowers into 3 species 
(Setosa, Versicolor, Virginica) based on sepal and petal measurements.
Achieved 96.67% accuracy using Random Forest Classifier.

## Dataset
- Source: Built-in sklearn dataset (originally UCI Machine Learning Repository)
- Size: 150 samples, 4 features
- Classes: Setosa, Versicolor, Virginica (50 each — perfectly balanced)
- Features: Sepal Length, Sepal Width, Petal Length, Petal Width

## EDA Insights
- Perfectly balanced dataset — 50 flowers per species
- Setosa is clearly separable from other two species
- Versicolor and Virginica slightly overlap
- Petal length and petal width are strongest separating features

## Model
- Algorithm: Random Forest Classifier
- n_estimators: 100
- Test size: 20%

## Results
- Accuracy: 96.67%
- Setosa: 100% precision and recall
- Versicolor: 89% precision, 100% recall
- Virginica: 100% precision, 90% recall

## Visualizations
- Species distribution bar chart
- Pairplot showing feature separation by species
- Feature importance chart

## Libraries Used
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn

## Key Learnings
- Multiclass classification
- Pairplot for visualizing feature separation
- Feature importance in Random Forest
- Balanced vs imbalanced datasets
