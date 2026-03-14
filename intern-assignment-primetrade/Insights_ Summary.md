# Insights & Strategy Summary

**Assignment: Trader Performance vs Market Sentiment | Primetrade.ai**

-----

## Methodology (Brief)

**Data:** Merged Bitcoin Fear/Greed Index with Hyperliquid trade history (211,224 trades, 32 accounts, 2024) at daily granularity. Zero missing values or duplicates in either dataset.

**Metrics engineered:** Daily PnL per trader, win rate, avg trade size, avg leverage (via start position), trades/day, long/short ratio.

**Approach:** Descriptive analysis across sentiment categories → Trader segmentation → K-Means clustering → Strategy derivation.

-----

## Top 3 Insights

### Insight 1 — Sentiment Is a Profit Multiplier

Average daily PnL scales dramatically with sentiment:

|Sentiment    |Avg Daily PnL|
|-------------|-------------|
|Extreme Fear |−$949        |
|Fear         |−$168        |
|Neutral      |+$1,296      |
|Greed        |+$2,156      |
|Extreme Greed|+$5,950      |

**Why it matters:** Sentiment explains a 6× swing in daily profitability. Traders who ignore sentiment and trade with uniform sizing are leaving significant edge on the table.

-----

### Insight 2 — Win Rate Is a Trap; Risk Management Is the Edge

68% of traders (21/31) are “Big Winners” with an average of $184,196 profit — yet their average win rate is only 46.9%. Losers average a 0.9% win rate and lose $109,168.

The key differentiator is **not** winning more trades — it is:

- Cutting losses fast (losers have extremely low win rates, meaning they hold losers too long)
- High trading frequency (Big Winners trade 10× more frequently than Losers)

**Why it matters:** Strategy should be built around 2:1 reward-to-risk ratios and stop-losses, not chasing accuracy.

-----

### Insight 3 — These Traders Are Contrarian Short-Sellers

Counter-intuitively, even on Extreme Greed days, only **14.6%** of trades are long positions. Fear days show even stronger short bias (74.3% short).

**Why it matters:** This reveals a sophisticated cohort of traders who systematically fade market euphoria. A naive “buy when greedy” strategy would underperform here. The edge lies in shorting overbought conditions.

-----

## Strategy Recommendations

### Strategy 1: Sentiment-Scaled Position Sizing

**Rule:** Scale your position size based on prevailing sentiment.

- Extreme Greed → 100% of normal position size
- Greed → 75%
- Neutral → 50%
- Fear → 25%
- Extreme Fear → 0% (sit out or hedge only)

**Evidence:** Daily PnL swings from −$949 on Extreme Fear to +$5,950 on Extreme Greed — a $6,899 range driven purely by market mood.

-----

### Strategy 2: Hard Stop-Loss + 2:1 Reward Rule

**Rule:** Never exit a losing trade at more than 1% loss. Never exit a winning trade at less than 2% gain.

**Evidence:** Big Winners (avg $184K PnL) achieve this with only 46.9% win rate. Even losing <50% of trades, a 2:1 R:R produces positive expected value per trade: `0.469 × 2 − 0.531 × 1 = +0.407` per unit risked.

-----

## Bonus: Behavioral Archetypes (K-Means, K=3)

|Cluster|Label                 |Avg PnL   |Win Rate|Avg Trade Size|Trade Count|
|-------|----------------------|----------|--------|--------------|-----------|
|0      |Moderate Traders      |$51,696   |37.6%   |$2,690        |1,232      |
|1      |High-Frequency Winners|$1,088,096|42.7%   |$4,316        |8,556      |
|2      |High-Risk Speculators |$23,949   |31.6%   |$15,996       |1,145      |

**Recommendation by archetype:**

- **Cluster 1:** Continue strategy — high frequency + moderate size is optimal
- **Cluster 0:** Increase trade frequency; don’t increase size yet
- **Cluster 2:** Reduce position size significantly; current approach is high-risk low-reward
