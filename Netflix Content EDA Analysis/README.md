# 📺 Netflix Content Strategy — EDA

> Exploratory Data Analysis on Netflix Movies & TV Shows dataset to uncover content strategy, viewing trends, and production patterns.

---

## 📊 Dataset
- **8807 titles** — Movies & TV Shows
- **12 features** — title, type, country, rating, director, date_added, release_year, etc.

---

## 🔍 Key Findings

**Content Distribution**
- Netflix has **2.4x more Movies than TV Shows**
- 60% of all content targets adults (TV-MA + TV-14)

**Growth Trend**
- Flat content library pre-2015
- Explosive growth from 2015-2019 as Netflix original strategy kicked in
- Sharp drop in late 2020 due to **COVID-19 production shutdowns**

**Top Producing Countries**
- USA dominates with **2.5x more content than India**
- India is #2 — strong Bollywood presence on platform
- UK, Japan, South Korea follow

**Seasonality**
- Most content added in **July & December** — holiday season strategy
- February has lowest additions — no major holiday season

**Top Directors**
- **Rajiv Chilaka** (#1) — Indian director, Chhota Bheem creator
- **Steven Spielberg** in top 10 — Hollywood presence

---

## 🛠️ Data Cleaning
- Filled missing `director`, `cast`, `country` with "Unknown"
- Dropped rows with missing `date_added`, `rating`, `duration` (< 0.1% of data)
- Converted `date_added` to datetime, extracted `month` and `year`

---

## 📈 Visualizations
- Movies vs TV Shows distribution
- Rating distribution across all content
- Content growth over years (1925-2021)
- Top 10 content producing countries
- Monthly content addition pattern
- Top 10 directors by content count

---
