# Twitter Sentiment Analysis

## Overview
Built a machine learning model to classify tweets into positive, neutral, and negative sentiments using NLP techniques.

## Dataset
- Source: Kaggle - Twitter Sentiment Analysis
- Size: 162,980 tweets
- Labels: Positive (1), Neutral (0), Negative (-1)

## Steps Followed
1. Loaded and explored the dataset
2. Cleaned text - removed URLs, mentions, special characters
3. Converted text to numbers using TF-IDF Vectorizer
4. Split data - 80% train, 20% test
5. Trained Logistic Regression model
6. Evaluated using accuracy and confusion matrix

## Results
- Accuracy: 92.75%
- Model performs best on neutral and positive tweets
- Negative tweets are hardest to classify due to sarcasm

## Libraries Used
- Pandas, NumPy, Matplotlib
- Scikit-learn

## What I Learned
- Text preprocessing for NLP
- TF-IDF vectorization
- Model evaluation using classification report
- Tried bigrams but reverted as accuracy dropped
