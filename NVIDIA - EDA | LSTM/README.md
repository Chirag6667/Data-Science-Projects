# NVIDIA: From $0.03 to $186 — EDA + LSTM Forecasting

Analyzing 27 years of NVIDIA stock data (1999–2026) across 7,079 trading days using exploratory data analysis and LSTM deep learning for price forecasting.
---

## Results
- LSTM MAE: $0.3832
- LSTM RMSE: $0.5527
- Test Period: ~1,400 trading days
---

## What This Project Covers
- Full price journey across 5 market eras (Pre-GPU → Generative AI)
- Volume analysis showing the explosive growth in trading activity post-2020
- Price vs Moving Averages (SMA 20, 50, 200) zoomed into the AI era
- RSI analysis identifying overbought/oversold zones across 27 years
- Key events annotated on price chart (253 real-world events)
- Feature engineering: daily returns, volatility, price momentum
- 2-layer LSTM model predicting next-day closing price
---

## Key Insight
80% of NVIDIA's total price appreciation happened after ChatGPT launched in November 2022 — from $3 to $20 (split-adjusted) in just 3 years.
---

## Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn · TensorFlow/Keras
---
