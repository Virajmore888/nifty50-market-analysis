# =================================================================
# SECTION A: IMPORTING LIBRARIES
# =================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os
import yfinance as yf
from datetime import timedelta
from scipy.stats import gaussian_kde

# Start Timer
start = time.time()

# Output folder — auto-created next to wherever the script runs
PATH = os.path.join(os.getcwd(), "output")

# Create folder if it does not exist (prevents save errors)
os.makedirs(PATH, exist_ok=True)


# =================================================================
# SECTION B: DATA_EXPLORATION
# =================================================================
print("<----------DATA_EXPLORATION---------->")

# Download Nifty 50 weekly data from Yahoo Finance (2016 to 2026)
# progress=False suppresses download spam in Pydroid3 console
# auto_adjust=True ensures clean adjusted prices (no manual split correction needed)
nifty_raw = yf.download("^NSEI", start="2016-01-01", end="2026-01-01", interval="1wk", progress=False, auto_adjust=True)

# Convert to DataFrame and reset index so Date becomes a normal column
# Fix: Flatten MultiIndex columns that yfinance returns (e.g. ('Close', '^NSEI') → 'Close')
data = pd.DataFrame(nifty_raw)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = [col[0] for col in data.columns]
data = data.reset_index()

# Rename 'Price' or 'index' to 'Date' if yfinance uses a different index name
if 'Price' in data.columns:
    data.rename(columns={'Price': 'Date'}, inplace=True)

# Save raw downloaded data as CSV backup (optional reference, not reloaded)
data.to_csv(os.path.join(PATH, "Nifty50_raw.csv"), index=False)
print("Raw CSV file saved successfully")

# 1. Displaying First 10 rows of the DATA_SET
head = data.head(10)
print("First 10 Rows of the DATA_SET\n", head)

# 2. Displaying Last 10 rows of the DATA_SET
tail = data.tail(10)
print("Last 10 Rows of the DATA_SET\n", tail)

# 3. Displaying Information of the DATA_SET
info = data.info()
print("Information of the DATA_SET\n", info)

# 4. Displaying Descriptive Statistics of the DATA_SET
describe = data.describe()
print("Descriptive Statistics of the DATA_SET\n", describe)

# 5. Displaying Shape of the DATA_SET (Rows, Columns)
shape = data.shape
print("Shape of the DATA_SET\n", shape)

# 6. Displaying Total Size of the DATA_SET (Total Elements)
size = data.size
print("Size of the DATA_SET\n", size)

# 7. Displaying Column Names of the DATA_SET
columns = data.columns
print("Column Names of the DATA_SET\n", columns)

# 8. Finding Null Values from the DATA_SET (True/False)
null = data.isnull()
print("Null Values of the DATA_SET\n", null)

# 9. Displaying Sum of the Null Values of each Column
Sum_Of_the_Null_Values = data.isnull().sum()
print("The Sum of the Null Values of each Column\n", Sum_Of_the_Null_Values)

# 10. Displaying Total Sum of the Null Values
Total_Sum_Of_the_Null_Values = data.isnull().sum().sum()
print("Total Sum of the Null Values\n", Total_Sum_Of_the_Null_Values)

# 11. Displaying Percentage of Null Values of Each Column
null_percentage = data.isnull().mean() * 100
print("Percentage of Null Values", null_percentage)

# 12. Displaying Total Percentage of the Null Values
Total_Percentage_of_Null_Values = (data.isnull().sum().sum() / data.size) * 100
print("Total Percentage of the Null Values", Total_Percentage_of_Null_Values)

# 13. Displaying Duplicated Values (Identification)
Duplicate_Values = data.duplicated()
print("Duplicate Values of the DATA_SET", Duplicate_Values)

# 14. Displaying Sum of the Duplicate Values
Sum_of_the_Duplicate_Values = data.duplicated().sum()
print("Sum of the Duplicated Values", Sum_of_the_Duplicate_Values)

# 15. Displaying Unique Values Count
Unique_Values = data.nunique()
print("Unique Values of the DATA_SET", Unique_Values)


# =================================================================
# SECTION C: DATA_CLEANING
# =================================================================
print("<----------DATA_CLEANING---------->")

# 1. Drop duplicate rows if any
data.drop_duplicates(inplace=True)

# 2. Drop rows where Date is missing (Date is the primary key here)
data.dropna(subset=['Date'], inplace=True)

# 3. Reset index after dropping rows so index stays clean
data.reset_index(drop=True, inplace=True)

# 4. Convert Date column to proper datetime format (handles wrong formats as NaT)
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# 5. Convert price and volume columns to numeric (handles any bad string values as NaN)
cols_to_convert = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in cols_to_convert:
    data[col] = pd.to_numeric(data[col], errors='coerce')

# 6. Optimization: Downcast float columns to float32 for memory saving
for col in ['Open', 'High', 'Low', 'Close']:
    data[col] = data[col].astype('float32')

# 7. Optimization: Volume as int64 (it is a whole number count)
data['Volume'] = data['Volume'].fillna(0).astype('int64')

# Final check: Fill any remaining NaN in price columns using forward fill
# (carry last known price forward — standard practice in financial data)
data[['Open', 'High', 'Low', 'Close']] = data[['Open', 'High', 'Low', 'Close']].ffill()

print("<--- Dataset Summary after Cleaning --->")
After = data.info()
print(After)


# =================================================================
# SECTION D: SAVING PROCESSED FILES
# =================================================================
# Saving the cleaned data back to storage
data.to_csv(os.path.join(PATH, "Nifty50_cleaned.csv"), index=False)
print("Cleaned CSV_File Successfully saved in phone storage")


# =================================================================
# SECTION E: CREATING DATA SUBSET
# =================================================================
# Extracting key columns and calculating Weekly Return for Insight Generation
sub_set = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']].copy()

# Cast all price columns to float64 — float32 (set in cleaning) causes garbage decimal tails
# e.g. 7601.350098 instead of 7601.35009765625 (the actual stored value)
# float64 restores full IEEE-754 precision that yfinance originally provided
for col in ['Open', 'High', 'Low', 'Close']:
    sub_set[col] = sub_set[col].astype('float64')

# Sort by Date — guarantees correct pct_change, rolling MA, and fill_between order
sub_set = sub_set.sort_values('Date').reset_index(drop=True)

# Calculate Weekly Return % (how much the index moved each week)
sub_set['Weekly_Return_%'] = sub_set['Close'].pct_change() * 100

# Round return to 2 decimal places for clean display
sub_set['Weekly_Return_%'] = sub_set['Weekly_Return_%'].round(2)

# Extract Year and Month — needed for seasonality chart and yearly summary
sub_set['Year'] = sub_set['Date'].dt.year
sub_set['Month'] = sub_set['Date'].dt.month

# Calculate 50-week and 200-week Moving Averages — needed for MA chart
sub_set['MA_50'] = sub_set['Close'].rolling(window=50).mean()
sub_set['MA_200'] = sub_set['Close'].rolling(window=200).mean()

# Month_Name — needed for seasonality insight (Que 5); created here so it saves in SubSet CSV
# Previously this was created in Section F after to_csv, so it was missing from the saved file
sub_set['Month_Name'] = sub_set['Date'].dt.strftime('%b')

print(sub_set.head())

sub_set.to_csv(os.path.join(PATH, "Nifty50_SubSet.csv"), index=False)
print("SubSet CSV_File Successfully Saved in Phone Storage")


# =================================================================
# SECTION F: INSIGHTS_OF_THE_DATA_SET
# =================================================================

# Que 1: Top 3 Worst Weeks (Biggest Market Crashes)
worst_weeks = sub_set.dropna(subset=['Weekly_Return_%']).sort_values(by='Weekly_Return_%').head(3)
print("\n--- 1. Top 3 Biggest Market Crashes ---")
print(worst_weeks[['Date', 'Close', 'Weekly_Return_%']])

# Que 2: Top 3 Best Weeks (Biggest Market Jumps)
best_weeks = sub_set.dropna(subset=['Weekly_Return_%']).sort_values(by='Weekly_Return_%', ascending=False).head(3)
print("\n--- 2. Top 3 Biggest Market Jumps ---")
print(best_weeks[['Date', 'Close', 'Weekly_Return_%']])

# Que 3: Total 10-Year Growth from first close to last close
start_price = sub_set['Close'].iloc[0]
end_price = sub_set['Close'].iloc[-1]
total_growth = ((end_price - start_price) / start_price) * 100
print("\n--- 3. Total 10-Year Growth ---")
print("Start Price (2016):", round(start_price, 2))
print("End Price (2026):", round(end_price, 2))
print("Total Growth (%):", round(total_growth, 2))

# Que 4: Max Drawdown — peak to trough drop (how deep market fell from its highest point)
# Rolling cummax gives highest price seen so far at each point in time
rolling_max = sub_set['Close'].cummax()
drawdown = (sub_set['Close'] - rolling_max) / rolling_max * 100
max_drawdown = drawdown.min()
max_drawdown_date = sub_set.loc[drawdown.idxmin(), 'Date']
print("\n--- 4. Maximum Drawdown ---")
print("Max Drawdown (%):", round(max_drawdown, 2))
print("Date of Max Drawdown:", max_drawdown_date)

# Que 5: Monthly Seasonality — which month gives best average return historically
# Month_Name already created in Section E (before SubSet CSV save)
monthly_avg = sub_set.groupby('Month')['Weekly_Return_%'].mean().reset_index()
monthly_avg['Month_Name'] = pd.to_datetime(monthly_avg['Month'], format='%m').dt.strftime('%b')
monthly_avg = monthly_avg.sort_values('Month')
best_month = monthly_avg.loc[monthly_avg['Weekly_Return_%'].idxmax(), 'Month_Name']
worst_month = monthly_avg.loc[monthly_avg['Weekly_Return_%'].idxmin(), 'Month_Name']
print("\n--- 5. Monthly Seasonality ---")
print("Best Month on Average:", best_month)
print("Worst Month on Average:", worst_month)
print(monthly_avg[['Month_Name', 'Weekly_Return_%']])

# Que 6: Sharpe Ratio — risk-adjusted return (how much return per unit of risk taken)
# Using 6% annual risk-free rate (approximate India 10-yr bond yield)
# Converting to weekly: 6% / 52 = ~0.1154% per week
risk_free_weekly = 6.0 / 52
clean_returns = sub_set['Weekly_Return_%'].dropna()
excess_returns = clean_returns - risk_free_weekly
sharpe_ratio = (excess_returns.mean() / excess_returns.std()) * np.sqrt(52)
print("\n--- 6. Sharpe Ratio (Annualized) ---")
print("Sharpe Ratio:", round(sharpe_ratio, 4))
print("Interpretation: >1 is Good, >2 is Great, <0 means Risk not worth it")

# Bonus: Annualized Volatility — measures total risk taken
annualized_volatility = clean_returns.std() * np.sqrt(52)
print("\n--- 6b. Annualized Volatility ---")
print("Annualized Volatility (%):", round(annualized_volatility, 2))
print("Interpretation: Higher = more risk/swings in the index")

# Yearly summary — used in chart 4
yearly_summary = sub_set.groupby('Year').agg(
    Avg_Close=('Close', 'mean'),
    Avg_Return=('Weekly_Return_%', 'mean'),
    Total_Volume=('Volume', 'sum')
).reset_index()
print("\n--- Yearly Summary ---")
print(yearly_summary)


# =================================================================
# SECTION G: DATA_VISUALISATION
# =================================================================

# Question 1: How did Nifty 50 weekly returns vary over 10 years? (Crashes & Jumps)

def plot_pro_bar(df, x_col="Date", y_col="Weekly_Return_%", title="Nifty 50: Weekly Volatility & Market Crashes (2016–2026)"):
    # 1. Global Professional Setup — dark theme for stock market feel
    sns.set_theme(
        context='talk',
        style='dark',
        rc={"axes.spines.right": False, "axes.spines.top": False,
            "figure.facecolor": "#0d1117", "axes.facecolor": "#0d1117",
            "axes.labelcolor": "white", "xtick.color": "white", "ytick.color": "white"}
    )
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(16, 7), dpi=100)
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')

    # 3. Core Bar Chart — bright red for crashes, bright green for gains
    colors = ['#ff4d4d' if val < 0 else '#00e676' for val in df[y_col]]
    # width=timedelta(days=5): datetime axis treats width in days; weekly bars are 7 days apart so 5 = clean gap
    ax.bar(df[x_col], df[y_col], color=colors, width=timedelta(days=5), alpha=0.9)

    # 4. Annotate Biggest Crash week
    min_idx = df[y_col].idxmin()
    crash_val = df.loc[min_idx, y_col]
    crash_date = df.loc[min_idx, x_col]
    ax.annotate(
        f'Biggest Crash\n{crash_val:.2f}%',
        xy=(crash_date, crash_val),
        xytext=(30, -45),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='#ff4d4d', lw=1.8),
        fontsize=10, fontweight='bold', color='#ff4d4d'
    )

    # 5. Annotate Biggest Jump week
    max_idx = df[y_col].idxmax()
    jump_val = df.loc[max_idx, y_col]
    jump_date = df.loc[max_idx, x_col]
    ax.annotate(
        f'Biggest Jump\n{jump_val:.2f}%',
        xy=(jump_date, jump_val),
        xytext=(30, 30),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='#00e676', lw=1.8),
        fontsize=10, fontweight='bold', color='#00e676'
    )

    # 6. Zero line — separates profit and loss weeks
    ax.axhline(0, color='white', linewidth=1.2, alpha=0.6)

    # 7. Average Return reference line
    avg_val = df[y_col].mean()
    ax.axhline(avg_val, color='#ffd700', linestyle='--', linewidth=1.5,
               alpha=0.8, label=f'Avg Return: {avg_val:.2f}%')

    # 8. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=20, fontweight='bold', color='white')
    ax.set_xlabel("Timeline (Years)", fontsize=13, labelpad=10, color='white')
    ax.set_ylabel("Weekly Return (%)", fontsize=13, labelpad=10, color='white')

    # 9. Legend & Grid Polish
    ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', frameon=False, labelcolor='white')
    ax.grid(axis='y', linestyle='-', alpha=0.08, color='white')

    plt.tight_layout()

    # 10. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_weekly_volatility_bar.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_weekly_volatility_bar.png")

    # 11. Show chart on screen
    plt.show()

    # 12. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# Question 2: What is the 10-year price trend of Nifty 50?

def plot_pro_line(df, x_col="Date", y_col="Close", title="Nifty 50: 10-Year Wealth Creation Trend (2016–2026)"):
    # 1. Global Professional Setup — light theme for clean line visibility
    sns.set_theme(
        context='talk',
        style='white',
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(16, 7), dpi=100)

    # 3. Use only rows with valid Close for plotting (NaN would break fill_between)
    df_plot = df.dropna(subset=[y_col]).copy()

    # 4. Gradient fill under line — shows wealth accumulation visually
    ax.fill_between(df_plot[x_col], df_plot[y_col], alpha=0.12, color='#1a73e8')

    # 5. Core Line Plot — bold corporate blue
    sns.lineplot(
        data=df_plot, x=x_col, y=y_col,
        linewidth=2.5, color='#1a73e8', ax=ax
    )

    # 6. Annotate All-Time High peak
    max_idx = df_plot[y_col].idxmax()
    peak_val = df_plot.loc[max_idx, y_col]
    peak_x = df_plot.loc[max_idx, x_col]
    ax.annotate(
        f'All-Time High\n{peak_val:,.0f}',
        xy=(peak_x, peak_val),
        xytext=(-90, -35),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='#e53935', lw=1.8),
        fontsize=11, fontweight='bold', color='#e53935'
    )

    # 7. Annotate COVID crash low point
    covid_start = pd.Timestamp('2020-01-01')
    covid_end = pd.Timestamp('2020-06-01')
    covid_data = df_plot[(df_plot[x_col] >= covid_start) & (df_plot[x_col] <= covid_end)]
    if not covid_data.empty:
        covid_min_idx = covid_data[y_col].idxmin()
        covid_val = df_plot.loc[covid_min_idx, y_col]
        covid_x = df_plot.loc[covid_min_idx, x_col]
        ax.annotate(
            f'COVID Crash\n{covid_val:,.0f}',
            xy=(covid_x, covid_val),
            xytext=(30, -40),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='#f57c00', lw=1.8),
            fontsize=10, fontweight='bold', color='#f57c00'
        )

    # 8. Global 10-Year Average reference line
    avg_val = df_plot[y_col].mean()
    ax.axhline(avg_val, color='#43a047', linestyle=':', linewidth=1.8,
               alpha=0.8, label=f'10-Yr Avg: {avg_val:,.0f}')

    # 9. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax.set_xlabel("Timeline (Years)", fontsize=13, labelpad=10)
    ax.set_ylabel("Index Points", fontsize=13, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    # 10. Legend & Grid Polish
    ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', frameon=False)
    ax.grid(axis='y', linestyle='-', alpha=0.1)
    sns.despine()

    plt.tight_layout()

    # 11. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_price_trend_line.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_price_trend_line.png")

    # 12. Show chart on screen
    plt.show()

    # 13. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# Question 3: How are weekly returns distributed? (Risk vs Reward view)

def plot_pro_hist(df, x_col="Weekly_Return_%", title="Nifty 50: Distribution of Weekly Returns (Risk vs Reward)"):
    # 1. Global Professional Setup
    sns.set_theme(
        style='white',
        context='talk',
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(13, 7), dpi=100)

    # 3. Split data into loss weeks and profit weeks for two-color histogram
    loss_data = df[df[x_col] < 0][x_col]
    gain_data = df[df[x_col] >= 0][x_col]

    # 4. Plot loss bars red and gain bars green — instant visual clarity
    ax.hist(loss_data, bins=30, color='#e53935', alpha=0.75, label='Loss Weeks')
    ax.hist(gain_data, bins=30, color='#43a047', alpha=0.75, label='Gain Weeks')

    # 5. KDE overlay — smooth curve showing overall distribution shape
    all_returns = df[x_col].dropna().values
    kde = gaussian_kde(all_returns, bw_method=0.4)
    x_range = np.linspace(all_returns.min(), all_returns.max(), 300)
    # Bug Fix: use actual bin width from data range instead of hardcoded /30
    bin_width = (all_returns.max() - all_returns.min()) / 30
    kde_scaled = kde(x_range) * len(all_returns) * bin_width
    ax.plot(x_range, kde_scaled, color='#1a73e8', linewidth=2.5, label='Distribution Curve')

    # 6. Zero line — separates profit and loss
    ax.axvline(0, color='black', linestyle='-', linewidth=1.8, alpha=0.6)

    # 7. Mean return reference line
    mean_val = df[x_col].mean()
    ax.axvline(mean_val, color='#f57c00', linestyle='--', linewidth=2, alpha=0.9)
    # Bug Fix: guard against empty kde_scaled; use ax.get_ylim() after plotting for reliable y position
    y_top = kde_scaled.max() if len(kde_scaled) > 0 and kde_scaled.max() > 0 else ax.get_ylim()[1]
    ax.text(mean_val + 0.3, y_top * 0.88,
            f"Avg: {mean_val:.2f}%", color='#f57c00', fontweight='bold', fontsize=11)

    # 8. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax.set_xlabel("Weekly Return (%)", fontsize=13, labelpad=12)
    ax.set_ylabel("Number of Weeks", fontsize=13, labelpad=12)

    # 9. Legend & Grid Polish
    ax.legend(frameon=False, loc='upper left')
    ax.grid(axis='y', linestyle='-', alpha=0.1)
    sns.despine()

    plt.tight_layout()

    # 10. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_returns_distribution_hist.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_returns_distribution_hist.png")

    # 11. Show chart on screen
    plt.show()

    # 12. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# Question 4: How does Nifty 50's average Close price grow each year?

def plot_pro_yearly_bar(df, x_col="Year", y_col="Avg_Close", title="Nifty 50: Year-wise Average Close Price (2016–2026)"):
    # 1. Global Professional Setup
    sns.set_theme(
        context='talk',
        style='white',
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization — dual Y-axis for price + return overlay
    fig, ax1 = plt.subplots(figsize=(13, 7), dpi=100)
    ax2 = ax1.twinx()

    # 3. Color each bar by yearly avg return — green = positive year, red = negative year
    bar_colors = ['#43a047' if r >= 0 else '#e53935' for r in df['Avg_Return']]

    # 4. Bar chart on ax1 — Avg Close Price per year
    bars = ax1.bar(df[x_col].astype(str), df[y_col], color=bar_colors, alpha=0.75, width=0.6)

    # 5. Line chart on ax2 — Avg Weekly Return % overlaid on same chart
    ax2.plot(df[x_col].astype(str), df['Avg_Return'], color='#1a73e8',
             linewidth=2.5, marker='o', markersize=7, label='Avg Weekly Return %')
    ax2.axhline(0, color='grey', linestyle=':', linewidth=1, alpha=0.5)

    # 6. Data labels on top of each bar
    for bar, val in zip(bars, df[y_col]):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 150,
                 f'{val:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax1.set_ylim(0, df[y_col].max() * 1.18)

    # 7. Labeling & Typography
    ax1.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax1.set_xlabel("Year", fontsize=13, labelpad=10)
    ax1.set_ylabel("Average Close Price (Points)", fontsize=12, labelpad=10)
    ax2.set_ylabel("Avg Weekly Return (%)", fontsize=12, labelpad=10, color='#1a73e8')
    ax2.tick_params(axis='y', labelcolor='#1a73e8')

    # 8. Legend & Grid Polish
    ax2.legend(loc='upper left', frameon=False)
    ax1.grid(axis='y', linestyle=':', alpha=0.4)
    sns.despine(ax=ax1, right=False)

    plt.tight_layout()

    # 9. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_yearly_avg_close_bar.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_yearly_avg_close_bar.png")

    # 10. Show chart on screen
    plt.show()

    # 11. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# Question 5: Where are Golden Cross and Death Cross events on Nifty 50?

def plot_pro_moving_avg(df, x_col="Date", y_col="Close", title="Nifty 50: Moving Average — Golden Cross & Death Cross"):
    # 1. Global Professional Setup
    sns.set_theme(
        context='talk',
        style='white',
        rc={"axes.spines.right": False, "axes.spines.top": False}
    )
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Object-Oriented Initialization
    fig, ax = plt.subplots(figsize=(16, 7), dpi=100)

    # 3. Drop rows where MA columns are NaN (first 200 weeks will be NaN by design)
    df_clean = df.dropna(subset=['MA_50', 'MA_200']).copy()

    # 4. Actual Close price as thin background line for context
    ax.plot(df[x_col], df[y_col], color='#b0bec5', linewidth=1.2, alpha=0.6, label='Nifty 50 Close')

    # 5. 50-week MA — orange (faster moving average, reacts quicker to price changes)
    ax.plot(df_clean[x_col], df_clean['MA_50'], color='#f57c00', linewidth=2.2, label='50-Week MA')

    # 6. 200-week MA — blue (slower moving average, shows long-term trend)
    ax.plot(df_clean[x_col], df_clean['MA_200'], color='#1a73e8', linewidth=2.2, label='200-Week MA')

    # 7. Detect Golden Cross (50 crosses above 200 = bullish) and Death Cross (50 crosses below 200 = bearish)
    cross = df_clean.copy()
    cross['signal'] = np.where(cross['MA_50'] > cross['MA_200'], 1, -1)
    # Round and cast to int — diff() returns float which can cause == 2 / == -2 to miss
    cross['cross'] = cross['signal'].diff().fillna(0).round().astype(int)

    golden_cross = cross[cross['cross'] == 2]
    death_cross = cross[cross['cross'] == -2]

    # 8. Set ylim explicitly from data — reliable on non-interactive backends (Pydroid3)
    y_min = df[y_col].min()
    y_max = df[y_col].max()
    y_padding = (y_max - y_min) * 0.08
    ax.set_ylim(y_min - y_padding, y_max + y_padding)
    y_top = ax.get_ylim()[1]

    # 9. Mark Golden Cross events with green dashed vertical lines
    y_top = ax.get_ylim()[1]
    y_label_pos = y_min + (y_max - y_min) * 0.93  # Bug Fix: use data-relative position, not axis-limit * 0.93
    for _, row in golden_cross.iterrows():
        ax.axvline(row[x_col], color='#43a047', linestyle='--', linewidth=1.2, alpha=0.7)
        ax.text(row[x_col], y_label_pos, 'GC',
                color='#43a047', fontsize=8, fontweight='bold', ha='center')

    # 10. Mark Death Cross events with red dashed vertical lines
    for _, row in death_cross.iterrows():
        ax.axvline(row[x_col], color='#e53935', linestyle='--', linewidth=1.2, alpha=0.7)
        ax.text(row[x_col], y_label_pos, 'DC',
                color='#e53935', fontsize=8, fontweight='bold', ha='center')

    # 11. Labeling & Typography
    ax.set_title(title, loc='left', fontsize=20, pad=25, fontweight='bold')
    ax.set_xlabel("Timeline (Years)", fontsize=13, labelpad=10)
    ax.set_ylabel("Index Points", fontsize=13, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    # 12. Legend & Grid Polish
    ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left', frameon=False)
    ax.grid(axis='y', linestyle='-', alpha=0.1)
    fig.text(0.01, -0.02, 'GC = Golden Cross (Bullish Signal)   |   DC = Death Cross (Bearish Signal)',
             fontsize=10, color='grey', style='italic')
    sns.despine()

    plt.tight_layout()

    # 13. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_moving_avg.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_moving_avg.png")

    # 14. Show chart on screen
    plt.show()

    # 15. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# Question 6: Which month is historically best and worst for Nifty 50?

def plot_pro_seasonality(df, title="Nifty 50: Monthly Seasonality — Best & Worst Months (2016–2026)"):
    # 1. Global Professional Setup — white theme for heatmap clarity
    sns.set_theme(style='white', context='talk')
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['figure.dpi'] = 100

    # 2. Build pivot table: rows = Year, columns = Month, values = Avg Weekly Return
    df_clean = df.dropna(subset=['Weekly_Return_%']).copy()
    pivot = df_clean.pivot_table(
        index='Year',
        columns='Month',
        values='Weekly_Return_%',
        aggfunc='mean'
    )

    # 3. Rename columns from month number to month name for readability
    month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                   7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    pivot.columns = [month_names.get(m, m) for m in pivot.columns]

    # 4. Core Heatmap — RdYlGn: red = bad months, yellow = neutral, green = good months
    fig, ax = plt.subplots(figsize=(14, 8), dpi=100)
    sns.heatmap(
        pivot,
        cmap='RdYlGn',
        center=0,
        annot=True, fmt='.1f',
        linewidths=0.6,
        linecolor='white',
        annot_kws={"size": 10, "weight": "bold"},
        cbar_kws={"shrink": 0.7, "label": "Avg Weekly Return (%)"},
        ax=ax
    )

    # 5. Find best and worst months across all years
    monthly_avg = pivot.mean()
    best_month = monthly_avg.idxmax()
    worst_month = monthly_avg.idxmin()

    # 6. Professional Polish
    ax.set_title(title, loc='left', fontsize=20, fontweight='bold', pad=25)
    ax.set_xlabel("Month", fontsize=13, labelpad=12)
    ax.set_ylabel("Year", fontsize=13, labelpad=12)
    plt.xticks(rotation=0, fontsize=11)
    plt.yticks(rotation=0, fontsize=11)

    # 7. Best and worst month summary note at bottom
    fig.text(0.01, -0.02,
             f'Best Month Historically: {best_month}   |   Worst Month Historically: {worst_month}',
             fontsize=11, color='#424242', fontweight='bold')

    plt.tight_layout()

    # 8. Save chart to Pydroid3 folder
    plt.savefig(
        os.path.join(PATH, "nifty50_monthly_seasonality.png"),
        dpi=500,
        transparent=False,
        bbox_inches="tight"
    )
    print("Chart saved: nifty50_monthly_seasonality.png")

    # 9. Show chart on screen
    plt.show()

    # 10. Close figure to free memory (prevents overlap in next chart)
    plt.close()


# =================================================================
# SECTION H: FINAL EXECUTION
# =================================================================
print("\n[PROCESS] Generating high-resolution insights...")

# 1. Analyzing weekly volatility — crashes and jumps over 10 years
plot_pro_bar(sub_set.dropna(subset=['Weekly_Return_%']))

# 2. Benchmarking the 10-year price growth trend with COVID annotation
plot_pro_line(sub_set)

# 3. Distribution of weekly returns — red/green split for risk view
plot_pro_hist(sub_set.dropna(subset=['Weekly_Return_%']))

# 4. Year-wise average close price with return % overlay
plot_pro_yearly_bar(yearly_summary)

# 5. Moving Average chart — Golden Cross and Death Cross signals
plot_pro_moving_avg(sub_set)

# 6. Monthly Seasonality Heatmap — best and worst months year-wise
plot_pro_seasonality(sub_set)

print("[DONE] All 6 charts saved successfully!")

end = time.time()
print(f"-----Required Data Loading Time: {end - start:.4f} seconds------")
