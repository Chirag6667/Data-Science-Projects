# 🌍 World Happiness Report EDA (2015-2019)

## Overview
Exploratory Data Analysis on the World Happiness Report dataset 
covering 5 years (2015-2019). This project explores what factors 
make countries happy and how global happiness has changed over time.

## Dataset
- Source: Kaggle — World Happiness Report
- Years: 2015, 2016, 2017, 2018, 2019
- Size: 782 rows, 9 columns after combining all years
- Features: Happiness Score, GDP, Social Support, 
  Life Expectancy, Freedom, Generosity, Corruption

## Key Questions Answered
- Which countries are happiest and unhappiest?
- Does money = happiness?
- Which factors predict happiness most?
- How has global happiness changed 2015-2019?

## Challenges
- Each year had different column names
- Standardized all 5 datasets to common column names
- Combined using pd.concat with Year column added

## EDA Steps & Visualizations

### 1. Top & Bottom 10 Countries (2019)
- Top 10: Finland, Denmark, Norway, Iceland, Netherlands
- Bottom 10: South Sudan, Central African Republic, Afghanistan
- Insight: Nordic countries dominate happiness, conflict zones dominate unhappiness

### 2. Correlation Heatmap
- GDP vs Happiness: 0.79 — strongest predictor
- Life Expectancy vs Happiness: 0.74 — second strongest
- Social Support vs Happiness: 0.65 — third strongest
- Generosity vs Happiness: 0.14 — weakest predictor
- Insight: Money and health matter most, generosity barely matters

### 3. GDP vs Happiness Scatter Plot
- Clear upward trend — richer countries are happier
- Some low GDP countries still achieve decent happiness
- Pattern consistent across all 5 years

### 4. Global Happiness Trend (2015-2019)
- 2015: 5.37
- 2016: 5.38
- 2017: 5.35 — worst year
- 2018: 5.37
- 2019: 5.40 — best year
- Insight: World happiness is very stable, slight upward trend

### 5. Boxplot Distribution by Year
- Median happiness around 5.1-5.3 every year
- Range consistently 3.0 to 7.5
- Distribution barely changes year to year

## Key Insights
1. GDP is the strongest predictor of happiness (0.79 correlation)
2. Nordic countries — Finland, Denmark, Norway — consistently happiest
3. Conflict zones — South Sudan, Afghanistan — consistently unhappiest
4. Global happiness barely changes year to year — very stable
5. Generosity has almost no impact on national happiness score
6. 2017 was the worst year globally, 2019 was the bes
