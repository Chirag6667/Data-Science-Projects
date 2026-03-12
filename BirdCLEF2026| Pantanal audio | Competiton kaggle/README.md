# 🌿 BirdCLEF 2026 | Pantanal Audio Classification

> Identifying wildlife species from audio recordings in the
> Brazilian Pantanal wetland using Deep Learning.
> Submitted to Kaggle BirdCLEF+ 2026 Competition.

---

## 🏆 Competition Results

| Metric | Score |
|--------|-------|
| Public Leaderboard Score | 0.50 |
| Rank | 1485 / 5983 |
| Model | CNN Baseline |

---

## 🌍 About the Competition

The Pantanal is the world's largest tropical wetland spanning
150,000 km² in Brazil. With over 650 species under threat from
wildfires and climate change, traditional field surveys cannot
scale to meet conservation needs.

This competition challenges participants to identify species
from audio recordings — turning sound into conservation tools.

---

## 📊 Dataset Overview

35,549 audio recordings
206 species to classify
5 animal classes:
→ Birds (Aves)      : 162 species (78%)
→ Frogs (Amphibia)  : 35 species
→ Insects (Insecta) : 28 species
→ Mammals           : 8 species
→ Reptiles          : 1 species

---

## 🔍 Key EDA Findings

- Recordings sourced from Xeno-canto (65%) and iNaturalist (35%)
- Dataset perfectly balanced — ~493-499 recordings per species
- Recordings concentrated in South America matching test region
- Birds call at HIGH frequencies (2000-8000 Hz)
- Frogs call at LOW frequencies (0-512 Hz)
- Insects produce BROADBAND noise across all frequencies

---

## 🧠 Modeling Approach

Audio (.ogg file)
↓ librosa.load()
Raw audio array (160,000 numbers @ 32kHz)
↓ melspectrogram()
Mel Spectrogram (128 × 313)
↓ resize()
Fixed image (128 × 128)
↓ normalize()
Values between 0 and 1
↓ CNN
206 species probabilities
↓ submission.csv
Kaggle leaderboard!


---

## 🏗️ CNN Architecture

Input (128 × 128 × 1)
↓ Conv2D(32) + BatchNorm + MaxPool
↓ Conv2D(64) + BatchNorm + MaxPool
↓ Conv2D(128) + BatchNorm + MaxPool
↓ Flatten → Dense(256) → Dropout(0.5)
↓ Dense(206, softmax)
Output: 206 species probabilities
Total parameters: 6,569,294

---

## 💻 Tech Stack
- Python, Pandas, NumPy
- Librosa — audio processing
- TensorFlow / Keras — CNN model
- Matplotlib, Seaborn — visualization

---
