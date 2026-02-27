# 📈 Coca-Cola Stock Price Prediction using LSTM

This project applies a Deep Learning approach using Long Short-Term Memory (LSTM) networks to predict Coca-Cola (KO) stock closing prices based on historical data and technical indicators.

---

# 🚀 Project Overview

Instead of relying only on historical price data, this model incorporates multiple technical indicators to provide richer market context:

- Close Price
- RSI (Relative Strength Index)
- 50-Day Moving Average (MA_50)
- Bollinger Band Width (BB_Width)
- Daily Return Percentage

The model learns patterns from the previous 60 days to predict the next day’s closing price.

---

# 🧠 Model Architecture

The neural network consists of:

- LSTM Layer (50 units, return_sequences=True)
- Dropout (20%)
- LSTM Layer (50 units)
- Dropout (20%)
- Dense Layer (25 units)
- Output Layer (1 unit)

**Loss Function:** Mean Squared Error
**Optimizer:** Adam

---

# 📊 Data Preprocessing Steps

1. Load historical stock dataset
2. Convert Date column to datetime format
3. Sort data chronologically
4. Drop rows with missing technical indicator values
5. Normalize features using MinMaxScaler
6. Create 60-day sliding window sequences for time-series learning

---

# 🔄 Time-Series Windowing Strategy

For each training example:

- **Input:** Previous 60 days of market data
- **Output:** Closing price of the next day

Example:

Day 1–60 → Predict Day 61
Day 2–61 → Predict Day 62

This sliding window mechanism allows the LSTM network to capture temporal dependencies and market trends.

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- TensorFlow / Keras

---

# 📈 Results

The model demonstrates reasonable trend alignment between predicted and actual prices.

- Black Line → Actual Market Price
- Red Dashed Line → Model Prediction

The model performs well during stable market conditions but may show lag during periods of high volatility.

---

# ⚠️ Limitations

- Stock prices are influenced by external macroeconomic events and news.
- The model does not incorporate sentiment analysis or fundamental data.
- Predictions are based purely on historical technical indicators.
- This project is intended for educational and research purposes only.

---

# 🔮 Future Improvements

- Add EarlyStopping and ModelCheckpoint
- Experiment with GRU or Bidirectional LSTM
- Implement Attention Mechanism
- Perform Hyperparameter Tuning
- Introduce validation split by date
- Use a separate scaler for the target variable
