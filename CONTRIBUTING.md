# Contributing to Nifty50 EDA 2016–2026

> Thank you for your interest in contributing to this project.
> This repository contains a complete Exploratory Data Analysis pipeline for 10 years of Nifty 50 weekly market data - covering data cleaning, feature engineering, 6 purpose-built visualizations, and investor-actionable insights.
> All contributions are welcome, whether it's a bug fix, a new chart, a new indicator, or an extended analysis.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Branch Naming Convention](#branch-naming-convention)
- [Commit Message Format](#commit-message-format)
- [Pull Request Checklist](#pull-request-checklist)
- [Contribution Ideas](#contribution-ideas)
- [Code Style Guidelines](#code-style-guidelines)
- [Reporting Bugs](#reporting-bugs)

---

## Code of Conduct

By participating in this project, you agree to:
- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the project and community

---

## Getting Started

### 1. Fork & Clone the Repository

```bash
# Click "Fork" on GitHub, then clone your fork
git clone https://github.com/Virajmore888/nifty50-market-analysis.git
cd nifty50-market-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy matplotlib seaborn yfinance scipy
```

### 3. Data Source

This project fetches live data via the **Yahoo Finance API (yfinance)** - no CSV download required.

```python
import yfinance as yf
data = yf.download("^NSEI", start="2016-01-01", end="2026-01-01", interval="1wk")
```

> **Internet access required** to fetch live Nifty 50 data. On Kaggle, enable Internet in Session Options before running.

---

## Development Workflow

```bash
# Run the full analysis pipeline
python Nifty50_Analysis_Final.py

# Launch Jupyter Notebook for interactive EDA
jupyter notebook Nifty50_EDA.ipynb
```

> All output files (cleaned CSVs + chart PNGs) will be saved to the working directory automatically.

---

## Branch Naming Convention

| Type          | Pattern                   | Example                              |
|---------------|---------------------------|--------------------------------------|
| Feature       | `feat/<description>`      | `feat/rsi-indicator-analysis`        |
| Bug Fix       | `fix/<description>`       | `fix/ma200-nan-handling`             |
| New Chart     | `viz/<description>`       | `viz/bollinger-bands-chart`          |
| Data Update   | `data/<description>`      | `data/update-2026-weekly-data`       |
| Documentation | `docs/<description>`      | `docs/update-readme`                 |
| ML Model      | `ml/<description>`        | `ml/lstm-price-prediction`           |

---

## Commit Message Format

```bash
git commit -m "feat: add RSI indicator analysis for 2016-2026"
```

| Prefix       | Use for                        |
|--------------|--------------------------------|
| `feat:`      | New feature or analysis        |
| `fix:`       | Bug fix                        |
| `docs:`      | Documentation changes          |
| `viz:`       | New or updated visualizations  |
| `refactor:`  | Code restructuring             |
| `perf:`      | Performance improvements       |
| `data:`      | Dataset or CSV updates         |

---

## Pull Request Checklist

Before submitting a Pull Request, verify the following:

- [ ] Script runs end-to-end without errors (`python Nifty50_Analysis_Final.py`)
- [ ] All 6 visualizations regenerate correctly as `.png` files
- [ ] No hardcoded absolute file paths - use `os.path.join()` with relative paths only
- [ ] Every new function includes a comment explaining its analytical purpose
- [ ] No new null values introduced after any data transformation
- [ ] `README.md` updated if new charts or sections are added
- [ ] Code is clean, readable, and follows the existing section structure
- [ ] Internet access confirmed working for yfinance API calls

---

## Contribution Ideas

| Area              | Idea                                                                      |
|-------------------|---------------------------------------------------------------------------|
| Indicators        | Add RSI (14-week) and MACD analysis for trend confirmation                |
| Indicators        | Add Bollinger Bands overlay on price trend chart                          |
| Machine Learning  | Build LSTM or ARIMA model for Nifty 50 price prediction                  |
| Dashboard         | Build a Streamlit dashboard for interactive EDA exploration               |
| Analysis          | Add FII vs DII flow correlation with weekly returns                       |
| Analysis          | Add sector rotation analysis (Bank Nifty, IT, Pharma vs Nifty 50)        |
| Statistical       | Add normality tests (Shapiro-Wilk, Jarque-Bera) on weekly return data    |
| Visualisation     | Add interactive Plotly charts for zoom-in analysis                        |
| Data              | Extend dataset to include Nifty 50 PE Ratio and dividend yield data       |

---

## Code Style Guidelines

### Python Code

```python
# Good: Clear variable names + comments
weekly_return = data['Close'].pct_change() * 100
print(f"Mean Weekly Return: {weekly_return.mean():.2f}%")  # Expected: ~0.26%

# Bad: Cryptic names, no comments
x = data['Close'].pct_change() * 100
print(x.mean())
```

- Use **snake_case** for variables and functions
- Add comments for non-obvious logic
- Keep functions under 30 lines where possible
- Use f-strings over `.format()` or `%`
- Use **object-oriented matplotlib** (`fig, ax = plt.subplots()`) for all charts
- All chart functions must include `plt.savefig()` and `plt.close()` at the end
- Use `sns.set_theme()` at the start of every chart function

### Notebooks
- Clear markdown cells before each section
- Run all cells before committing (`Kernel > Restart & Run All`)
- Remove unnecessary print statements

---

## Reporting Bugs

Open an [Issue](https://github.com/Virajmore888/nifty50-market-analysis/issues) with:

- **Title:** Short, descriptive summary
- **Description:** What happened vs what you expected
- **Steps to Reproduce:** Numbered list
- **Environment:** OS, Python version, library versions
- **Screenshots/Output:** If applicable

**Example:**
```
Title: yfinance API returns empty DataFrame for ^NSEI

Steps:
1. Run Nifty50_Analysis_Final.py
2. Observe empty DataFrame after yf.download()
3. No data fetched, script crashes

Expected: 522 rows of weekly OHLCV data
Actual: Empty DataFrame with 0 rows

Environment: Python 3.11, yfinance 0.2.x, Windows 11
```

---

*Prepared by Viraj More | virajmore.data888@gmail.com | May 2026*

<p align="center">Questions? Reach out on <a href="https://www.linkedin.com/in/viraj-uttam-more-a24a80391">LinkedIn</a> | <a href="https://www.kaggle.com/virajmore88">Kaggle</a></p>
