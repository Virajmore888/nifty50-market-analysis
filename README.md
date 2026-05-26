<div align="center">

# 📈 Nifty 50 - Market Performance & Trend Analysis

### *522 weekly data points. 10 years of market cycles. 6 visualizations that decode India's benchmark index.*

---

<!-- Tech Stack -->
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4+-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11+-4c72b0?style=for-the-badge&logo=python&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-1.7+-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white)

<!-- Links -->
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/code/vitajmore88/nifty-50-market-analysis-2016-2026/notebook)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Viraj%20More-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/viraj-uttam-more-a24a80391)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

---

**[🚀 Live Kaggle Notebook](https://www.kaggle.com/code/vitajmore88/nifty-50-market-analysis-2016-2026/notebook) · [📦 Kaggle Output](https://www.kaggle.com/code/vitajmore88/nifty-50-market-analysis-2016-2026/output) · [📊 Presentation](https://github.com/Virajmore888/nifty50-market-analysis/blob/916014f016cc4375aeeec69b1c7bdbe95cb740bf/Nifty50_Analysis_Presentation.pdf) · [📝 Full Report](https://github.com/Virajmore888/nifty50-market-analysis/blob/6745fc539d8c82019a5210e6094d38dd10eb520c/Nifty50_Analysis_Report.pdf)**

</div>

---

## 👋 About This Project

Hi, I'm **Viraj More** - an aspiring Data Analyst with a passion for turning raw market data into decisions that actually matter. Currently expanding into Data Science and AI/ML - one project at a time.

This project is not just an EDA. It's an **end-to-end financial data analytics pipeline** - from live API data ingestion, through feature engineering and statistical analysis, all the way to a stakeholder-ready report and presentation. Built entirely on **Android (Pydroid3/Termux + Acode)** with zero cloud infrastructure.

I am a retail investor who tracks the Nifty 50 on a near-daily basis. Every week, I found myself manually checking closing prices, reading financial news, and trying to intuit whether the market was in a bullish or bearish phase - all without a structured data foundation. At some point, I asked myself: *"Why am I relying on gut feel when I can let the data speak?"*

As a fresher straddling both finance and data analytics, this project was my opportunity to merge both domains into something genuinely useful - not a textbook exercise, but a real-world validation of my own investment thesis. Rather than simply downloading a pre-cleaned CSV, I chose to fetch live market data via the **Yahoo Finance API (yfinance)**, engineer features from scratch, and build every chart with a clear analytical question in mind.

> If you're a recruiter or fellow analyst - the TL;DR below tells you everything in 30 seconds. The rest of the README is for those who want to go deeper.

> ⚠️ **Data Confidence Note:** Real-world financial data is never 100% clean. This analysis operates within a **90-95% confidence range** - insights are data-driven and reliable, but acknowledge API rounding, survivorship bias in index composition changes, and retroactive dividend adjustment factors. Claiming 100% data purity in financial market analysis is a methodological red flag. See the [Full Report](https://github.com/Virajmore888/nifty50-market-analysis/blob/6745fc539d8c82019a5210e6094d38dd10eb520c/Nifty50_Analysis_Report.pdf) for the complete Data Disclaimer.

---

## ⚡ TL;DR - 6 Findings That Change How You See the Market

| # | Finding | Investor Impact |
|---|---------|----------------|
| 1 | 📈 13.15% CAGR - ₹1L grows to **₹3.44L** in 10 years | Beats FDs (6-7%) and gold (8-10%) hands down |
| 2 | 🦠 Worst crash & best recovery **just 4 weeks apart** (Mar-Apr 2020) | Panic selling is the single most destructive investor behaviour |
| 3 | ✅ **Golden Cross ACTIVE** - MA-50 (24,629) > MA-200 (21,243) | Bull market structurally intact as of Dec 2025 |
| 4 | 📅 **April is the best month** (+0.84%), **February the worst** (-0.34%) | Seasonal edge is real and exploitable by SIP investors |
| 5 | 📊 **58.2% of weeks are positive** - 303 vs 216 negative weeks | Long-term compounding works in your favour statistically |
| 6 | 📱 Entire pipeline built on **Android (Termux)** - zero cloud cost | Reproducible anywhere, no infrastructure needed |

---

## 🎯 What Makes This Project Different

Most market EDA projects stop at charts. This one answers **"So what?"**

| Standard EDA | This Project |
|---|---|
| Shows price trend | Quantifies wealth creation + mean reversion risk |
| Lists moving averages | Identifies Golden Cross / Death Cross signals with spread analysis |
| Computes return stats | Translates weekly distribution into probability edge for SIP investors |
| Runs on cloud/Colab | Built natively on **Android** - zero infrastructure cost |
| Static notebook | End-to-end delivery: API → pipeline → insights → report + presentation |

---

## 💡 Key Business Insights

### 1. 📈 10-Year Wealth Creation Trend (2016-2026)

A buy-and-hold investor who stayed invested from the **COVID low (Mar 2020: 8,084)** to **Dec 2025 (26,147)** would have generated a **223% return in under 6 years** - showcasing the power of long-term conviction. The 10-year CAGR stands at **13.15%**, turning ₹1 lakh into ₹3.44 lakhs.

Post-2021, the index mean has permanently shifted above 15,000 - reflecting structurally higher earnings multiples and deeper FII participation. The current price (~26,000) is **71.6% above the 10-year average of 15,144** - a mean reversion risk signal worth watching.

---

### 2. 📉📈 Moving Average: Golden Cross & Death Cross

As of **December 2025**, the **50-Week MA (24,629) remains decisively above the 200-Week MA (21,243)** - a spread of 3,386 points - confirming a long-running **Golden Cross** (bullish structural alignment). This is the hallmark of a secular bull market. The 200-Week MA (~21,243) acts as the strategic support floor for long-term SIP investors. Any future **Death Cross** (50-Week MA falling below 200-Week MA) should be treated as a major exit or reallocation signal.

---

### 3. 🌪️ Weekly Volatility & Market Crashes

The **worst week was -12.15% (Mar 2020)** and the **best week was +12.72% (Apr 2020)** - separated by just 4 weeks. This is the central lesson of a decade: both the greatest risk and the greatest opportunity were separated by a matter of weeks. Outside of 2020, **~96% of all weeks fall within a -5% to +5% corridor**. Post-2022, weekly volatility has visibly declined - consistent with a maturing bull market.

---

### 4. 📊 Distribution of Weekly Returns (Risk vs Reward)

With **303 positive weeks vs. 216 negative weeks (58.2% win rate)**, the Nifty 50 delivers a statistically favorable base rate for long-term investors. A modest average of **+0.26%/week**, compounded over 521 weeks, has delivered **244% total returns** - the mathematical argument for long-term equity investing. The distribution also shows **excess kurtosis (leptokurtosis)** - fat tails mean black swan events (±5% weeks) occur more frequently than a normal distribution predicts. Investors must maintain liquidity buffers to withstand these tail weeks.

---

### 5. 📅 Year-wise Average Close Price (2016-2025)

The average annual close price rose **every single year** - from 8,096 (2016) to 24,579 (2025), a **203% rise with zero negative annual averages** in 10 years. Best return years were **2017 (+0.49%/wk)** and **2021 (+0.44%/wk)** - both following periods of macro uncertainty. 2022 had the worst average weekly return (0.11%) despite an average close of 17,248 - proof that absolute price level does not equal positive momentum.

---

### 6. 🗓️ Monthly Seasonality Heatmap - The Seasonal Edge

**April (+0.84%)** is historically the strongest month - Q4 earnings season + new FY capital deployment. **February (-0.34%)** is the weakest - budget uncertainty + FPI rebalancing. **July-August (+0.48-0.51%)** are consistently strong - Q1 results + festive pre-rally. A simple seasonal strategy of accumulating in Feb-Mar dips and avoiding Dec window dressing can add **~1.5-2.5% annual alpha**.

---

## 📋 Key Metrics At A Glance

| Metric | Value |
|--------|-------|
| **Weekly Data Points** | 522 |
| **Period** | Jan 2016 - Dec 2025 |
| **10-Year CAGR** | 13.15% |
| **10-Year Total Return** | 244% |
| **Starting Close (Jan 2016)** | 7,601 pts |
| **Ending Close (Dec 2025)** | 26,147 pts |
| **All-Time High** | 26,203 pts (Nov 2025) |
| **COVID Low** | 8,084 pts (Mar 2020) |
| **10-Year Avg Close** | 15,144 pts |
| **MA-50 (Dec 2025)** | 24,629 pts |
| **MA-200 (Dec 2025)** | 21,243 pts |
| **Mean Weekly Return** | +0.26% |
| **Median Weekly Return** | +0.40% |
| **Std Deviation** | 2.15% |
| **Best Week** | +12.72% (Apr 2020) |
| **Worst Week** | -12.15% (Mar 2020) |
| **Positive Weeks** | 303 / 521 (58.2%) |

---

## 🏛️ Phase-wise Market Analysis

| Phase | Period | Price Range | Catalyst | Character |
|-------|--------|-------------|----------|-----------|
| **Phase 1** - Steady Build | 2016-2019 | 7,600 - 12,200 | Post-election optimism, GST rollout, FII inflows | Gradual uptrend, low volatility, avg +0.24%/wk |
| **Phase 2** - COVID Crash | Mar 2020 | 12,200 → 8,084 | Global pandemic lockdowns, FPI panic selling | Fastest 40% drawdown in NSE history. Worst week: -12.15% |
| **Phase 3** - V-Recovery | Apr-Dec 2020 | 8,084 → 13,000 | Liquidity injection, vaccine news, retail boom | Explosive V-shaped recovery. Best week: +12.72% |
| **Phase 4** - Bull Run | 2021-2024 | 13,000 → 26,203 | Earnings upgrades, SIP inflows, global risk-on | Sustained bull market. ATH 26,203 in Nov 2025 |
| **Phase 5** - Consolidation | 2024-2025 | 21,000 - 26,000 | Rate cuts, election volatility, high base effect | Range-bound near ATH; lower volatility, moderate returns |

---

## 🎯 Real-World Problems This Project Solves

### Problem 1: The "Panic Seller" Trap
Most retail investors exit during crashes and miss recoveries. The March 2020 crash (-12.15%) was followed by an April 2020 recovery (+12.72%) - panic sellers missed both sides of the trade. **The data shows 58.2% of weeks are positive over a full cycle** - systematic investing beats emotional timing every time.

### Problem 2: Ignoring Seasonal Entry/Exit Windows
Historical patterns clearly show February and March are weak months while April, July, and August are strong - yet almost no retail investor adjusts their SIP timing accordingly. **A simple "seasonal SIP" model** - deploying more in Feb/Mar dips and reducing in Dec - could add 1-2% additional annual alpha over time.

### Problem 3: Missing the Structural Bull Signal
The **Golden Cross** (50-Week MA > 200-Week MA) is a well-established institutional signal, yet retail investors rarely track moving average crossovers to guide their allocation decisions. **The 200-Week MA (~21,243) = strategic floor** for long-term investors. Any correction toward this level represents a multi-year buying opportunity.

---

## 💡 What I Analyzed, Why It Matters & How I Did It

**WHAT:** 10 years (2016-2026) of weekly Nifty 50 OHLCV data - 522 data points fetched live via Yahoo Finance API. Price trends, moving average crossovers, weekly return volatility, return distribution, year-wise performance, and monthly seasonality patterns.

**WHY:** As a retail investor, I needed data-backed answers to questions I face every month: *Is it a good time to invest? Should I increase my SIP this month? Is the market in a structural uptrend or a temporary rally?* This analysis converts those questions into quantifiable, data-driven answers accessible to any retail investor.

**HOW:** API data ingestion (yfinance) → pandas cleaning & feature engineering (Weekly_Return_%, MA_50, MA_200, Year, Month) → 6 purpose-built visualizations using Matplotlib and Seaborn → phase-wise and seasonality analysis → investor-actionable recommendations. Every step is documented and reproducible.

### 🎓 Key Learnings as a Fresher

- **Real data is messy:** The yfinance API returned float64 values with 10+ decimal places, legitimate NaN rows, and required careful DatetimeIndex setup. Cleaning is not optional - it is where most of the analytical precision is won or lost.
- **Domain knowledge amplifies data skills:** Understanding Golden Cross signals, FII rebalancing cycles, and budget-driven seasonality helped me ask better questions of the data. Pure coding without finance context would have produced technically correct but analytically shallow outputs.
- **Visualization is communication:** Every chart was built to answer a specific investor question, not just to display data. The process of choosing chart type, axis, color scale, and annotation taught me that a good visualization is the final 50% of the analytical work.
- **Confidence ranges, not false precision:** Claiming 100% accuracy on financial data analysis is a methodological red flag. Operating within a stated 90-95% confidence range is the mark of a rigorous, honest analyst.

---

## ⚙️ Technical Architecture

Engineered under **extreme resource constraints** - developed and executed entirely on **Android (Pydroid3/Termux + Acode)**, with no cloud compute, no Colab, no shortcuts.

| Technique | Implementation Detail |
|---|---|
| **Live API Data Ingestion** | Weekly OHLCV data fetched via `yfinance` (^NSEI ticker) - no pre-downloaded CSV |
| **Feature Engineering** | `Weekly_Return_%` via `pct_change()`, `MA_50`, `MA_200` via `rolling().mean()`, `Year`, `Month`, `Month_Name` |
| **NaN Handling** | First-row NaN in `Weekly_Return_%` retained (mathematically valid). MA NaNs retained and conditionally plotted - historical data never discarded |
| **Data Precision** | Float64 API values with 10+ decimals rounded to 2dp via `pd.round(2)` for analytical clarity |
| **Date Indexing** | `pd.to_datetime()` + `set_index()` - enables correct time-series rolling operations across leap years and market holidays |
| **Seasonality Aggregation** | `groupby(['Year', 'Month']).mean()` + `pivot_table()` → 10×12 heatmap matrix |

---

## 🛠️ Skills Demonstrated

`Python` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `SciPy` · `yfinance API` · `Exploratory Data Analysis` · `Feature Engineering` · `Time Series Analysis` · `Moving Averages` · `Statistical Distribution Analysis` · `Seasonality Analysis` · `Business Intelligence` · `Data Visualization` · `Mobile DevOps (Termux)`

---

## 🚀 Run This Project Locally

### Prerequisites
- Python 3.10+
- pip
- Internet connection (for yfinance API)

### Step 1: Clone
```bash
git clone https://github.com/Virajmore888/nifty50-market-analysis.git
cd nifty50-market-analysis
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Pipeline
```bash
python Nifty50_Analysis.py
```
📄 [View Full Source Code](https://github.com/Virajmore888/nifty50-market-analysis/blob/d56369807059f08455971dac796439d328b91041/Nifty50_Analysis.py)

### Step 4: Explore the Notebook (Optional)
```bash
jupyter notebook nifty-50-market-analysis-2016-2026.ipynb
```
📓 [View Kaggle Notebook](https://www.kaggle.com/code/vitajmore88/nifty-50-market-analysis-2016-2026/notebook) · [View GitHub Notebook](https://github.com/Virajmore888/nifty50-market-analysis/blob/f9ffef7d8f86997704464122bb464442b62cd85a/nifty-50-market-analysis-2016-2026.ipynb)

### 📱 Mobile Setup (Termux / Pydroid3)
```bash
pkg install python
pip install pandas numpy matplotlib seaborn yfinance scipy jupyter
```

---

## 📦 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
yfinance>=0.2.0
jupyter>=1.0.0
```

---

## 📊 Dataset At A Glance

| Attribute | Value |
|---|---|
| **Source** | Yahoo Finance API (yfinance) - ^NSEI ticker |
| **Total Weekly Records** | 522 |
| **Period** | January 2016 - December 2025 |
| **Raw Columns** | 6 (Date, Open, High, Low, Close, Volume) |
| **Engineered Columns** | 6 additional (Weekly_Return_%, MA_50, MA_200, Year, Month, Month_Name) |
| **Total Nulls After Cleaning** | 0 (actionable dataset) |

---

## 📂 Repository Structure

```
nifty50-market-analysis/
|
+-- 📊 Nifty50_Analysis_Presentation.pdf        # Stakeholder-ready visual summary
+-- 📝 Nifty50_Analysis_Report.pdf              # Deep-dive statistical consulting report
+-- 💻 Nifty50_Analysis.py                      # Production ETL & EDA pipeline
+-- 📓 nifty-50-market-analysis-2016-2026.ipynb # Full Kaggle notebook
|
+-- nifty50_price_trend_line.png                # Viz 1 - 10-Year Wealth Creation Trend
+-- nifty50_moving_avg.png                      # Viz 2 - Golden Cross & Death Cross
+-- nifty50_weekly_volatility_bar.png           # Viz 3 - Weekly Volatility & Market Crashes
+-- nifty50_returns_distribution_hist.png       # Viz 4 - Distribution of Weekly Returns
+-- nifty50_yearly_avg_close_bar.png            # Viz 5 - Year-wise Average Close Price
+-- nifty50_monthly_seasonality.png             # Viz 6 - Monthly Seasonality Heatmap
|
+-- requirements.txt
+-- CONTRIBUTING.md
+-- README.md
```

---

## 🤝 Connect & Contribute

- 🔗 **LinkedIn:** [Viraj More](https://www.linkedin.com/in/viraj-uttam-more-a24a80391)
- 📓 **Kaggle:** [View Full Notebook](https://www.kaggle.com/code/vitajmore88/nifty-50-market-analysis-2016-2026/notebook)
- 💻 **GitHub:** [nifty50-market-analysis](https://github.com/Virajmore888/nifty50-market-analysis)

Found something to improve? Open an **Issue** or submit a **Pull Request** - contributions are welcome!
Read the **[Contributing Guide](https://github.com/Virajmore888/nifty50-market-analysis/blob/1fff7610b6f68f3875fedadca0ed4ca459aa32c7/CONTRIBUTING.md)** before submitting.

---

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.

---

## ⚠️ Data Disclaimer & Copyright

This report is based on weekly OHLCV data sourced via the **Yahoo Finance API (yfinance)** for the Nifty 50 index (^NSEI ticker). While this source is widely used by institutional and retail analysts globally, real-world financial data is inherently subject to occasional API rounding, survivorship bias in index composition changes, and retroactive dividend adjustment factors.

Claiming 100% data purity in financial market analysis is a methodological red flag. True data integrity is achieved by retaining maximum business value while handling inconsistencies logically. Statistical insights, return calculations, and investment recommendations operate within a realistic and highly reliable **90-95% confidence range**.

**All content, visualizations, code, and analysis in this repository are the original work of Viraj More © 2026. All rights reserved.**

This project is intended for **educational and research purposes only** and does not constitute financial advice. Past index performance is not a guarantee of future returns. Always consult a **SEBI-registered investment advisor** before making financial decisions.

---

<div align="center">

**Built with ❤️ on Android · Pydroid3/Termux + Acode · Zero Cloud Cost**

*If this project added value, consider leaving a ⭐ on the repo - it helps others find it too.*

</div>
