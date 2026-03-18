# Trader Performance vs Market Sentiment — Primetrade.ai Assignment

## Overview

This project analyzes how Bitcoin market sentiment (Fear/Greed Index) relates to trader behavior and performance on the Hyperliquid DEX platform. The goal is to uncover actionable patterns that inform smarter trading strategies.

-----

## Setup & How to Run

### Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Data

Place the following CSV files in the same directory as the notebook:

- `fear_greed_index.csv` — Bitcoin Fear/Greed sentiment (2018–2025)
- `historical_data.csv` — Hyperliquid trader history (2024, ~211K trades)

Download links:

- [Fear/Greed Index](https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view)
- [Historical Trader Data](https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view)

### Run

```bash
jupyter notebook Trader_Performance_vs_Market_Trade.ipynb
```

-----

## Methodology

### Part A — Data Preparation

- Loaded and audited both datasets (zero missing values, zero duplicates)
- Converted timestamps; aligned datasets at daily granularity by merging on `date`
- Engineered key metrics per trader and per day:
  - Daily PnL, cumulative PnL, win rate
  - Average trade size, leverage (start position as proxy)
  - Trades per day, long/short ratio

### Part B — Analysis

Five charts answer the core business questions:

|Chart                     |Question Answered                               |
|--------------------------|------------------------------------------------|
|Avg Daily PnL by Sentiment|Does performance differ across Fear/Greed?      |
|Trade Count by Sentiment  |Do traders trade more on certain sentiment days?|
|Win Rate by Sentiment     |Does sentiment affect trade accuracy?           |
|Long % by Sentiment       |Does sentiment shift directional bias?          |
|Trader Segmentation       |Who are the winners vs losers?                  |

**Key Findings:**

1. **Sentiment drives profitability** — Average daily PnL on Extreme Greed days (+$5,950) is 6× higher than Neutral (+$1,296) and dramatically better than Extreme Fear (−$949)
1. **Participation is sentiment-dependent** — Traders placed 188× more trades on Extreme Greed days (29,655) vs Extreme Fear (158), suggesting sentiment influences *whether* traders participate, not just *how*
1. **Win rate is never the edge** — No sentiment category achieves >50% win rate. Even on Extreme Greed, win rate is only 47.5%. Big Winners (68% of traders) average 46.9% win rate but earn $184K. The differentiator is risk/reward management, not accuracy
1. **Traders are predominantly short** — Even on Extreme Greed days, only 14.6% of trades are long. These are sophisticated traders who fade rallies and profit from shorting overbought conditions

### Part C — Strategy Recommendations

**Rule 1: Sentiment-Based Position Sizing**
Scale position size with sentiment:

- Extreme Greed → 100% normal size
- Greed → 75%
- Neutral → 50%
- Fear → 25%
- Extreme Fear → sit out or hedge only

*Evidence:* Avg daily PnL ranges from −$949 (Extreme Fear) to +$5,950 (Extreme Greed)

**Rule 2: Optimize Reward-to-Risk, Not Win Rate**
Never optimize for win rate. Set hard stop-loss at 1% per trade; only exit winners at 2%+ gain (2:1 R:R minimum).

*Evidence:* Big Winners average only 46.9% win rate but earn $184K avg. Losers have 0.9% win rate and lose $109K avg. The gap is in how losses are cut, not wins captured.

### Bonus — K-Means Clustering

Traders were segmented into 3 behavioral archetypes using KMeans (K=3, features: win rate, trade size, trade count, total PnL, long ratio):

|Cluster|Profile               |Avg PnL   |Win Rate|Trade Count|
|-------|----------------------|----------|--------|-----------|
|0      |Moderate Traders      |$51,696   |37.6%   |1,232      |
|1      |High-Frequency Winners|$1,088,096|42.7%   |8,556      |
|2      |High-Risk Speculators |$23,949   |31.6%   |1,145      |

**Key clustering insight:** High-frequency trading with controlled position sizes (Cluster 1) produces 21× more profit than high-risk speculation with large positions (Cluster 2), despite only slightly higher win rates.

-----

## Project Structure

```
├── Trader_Performance_vs_Market_Trade.ipynb   # Main analysis notebook
├── README.md                                   # This file
├── fear_greed_index.csv                        # Sentiment data (not included)
└── historical_data.csv                         # Trade data (not included)
```

-----

## Author

Chirag | Intern Applicant
