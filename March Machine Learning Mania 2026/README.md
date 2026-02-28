# 🏀 March Machine Learning Mania 2026

## Overview
Predicted the probability of win outcomes for NCAA Men's Basketball Tournament 2026 matchups. Submitted to Kaggle's March Machine Learning Mania 2026 competition and achieved a public leaderboard score of 0.22065 (Log Loss).

## Competition
- Platform: Kaggle
- Competition: March Machine Learning Mania 2026
- Metric: Log Loss (lower is better)
- Public Score: 0.22065

## Dataset
- MTeams.csv — 381 teams with IDs and names
- MNCAATourneySeeds.csv — Tournament seeds per season
- MRegularSeasonCompactResults.csv — 196,823 regular season games
- MNCAATourneyCompactResults.csv — 2,585 tournament games
- SampleSubmissionStage1.csv — 519,144 matchups to predict

## Feature Engineering
Built team strength features from regular season data:

- Win Rate — wins divided by total games per season
- Seed Number — extracted from tournament seeds (1=best, 16=worst)
- Average Points Scored — mean points scored per season
- Average Points Allowed — mean points allowed per season
- All features used as differences between two teams (Team1 - Team2)

## Approach
1. Calculated team stats from 196,823 regular season games
2. Extracted seed numbers from tournament seed strings
3. Built pairwise feature differences for each matchup
4. Added losing perspective to training data (doubled dataset to 5,170 rows)
5. Used vectorized merge operations for fast submission generation

## Models Compared
- Logistic Regression — Log Loss: 0.534 ✅ Best
- Gradient Boosting — Log Loss: 0.572
- Random Forest — Log Loss: 1.03

Logistic Regression won because features are linear differences — simple models work better here.

## Results
- Local Log Loss: 0.534
- Kaggle Public Score: 0.22065
- Model: Logistic Regression

## Key Learnings
- Feature engineering from raw game results
- Why Log Loss is used instead of accuracy for probability predictions
- Vectorized merge operations for fast large scale predictions
- Adding losing perspective to balance training data
- Difference between local validation score and competition score

## Libraries Used
- Pandas, NumPy, Scikit-learn, Matplotlib

## Future Improvements
- Add more features like home/away performance
- Use team coach data
- Try neural networks for better probability calibration
- Add Women's tournament predictions
