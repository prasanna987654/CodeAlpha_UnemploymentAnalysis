import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ==========================================
# 1. CREATE DATA REPRESENTING UNEMPLOYMENT TRENDS
# ==========================================
print("🔄 Generating Unemployment Trends Dataset...")

# Simulating monthly data from 2019 to 2022 to analyze the COVID-19 impact
dates = pd.date_range(start='2019-01-01', end='2022-12-01', freq='MS')
np.random.seed(42)

# Generate baseline unemployment rate around 5-7%
unemployment_rate = np.random.uniform(5.0, 7.5, len(dates))

# Simulate a massive spike during Covid-19 lockdown (April 2020 to late 2020)
for i, date in enumerate(dates):
    if date.year == 2020 and date.month in [4, 5, 6]:
        unemployment_rate[i] += np.random.uniform(15.0, 20.0) # Sharp lockdown spike
    elif date.year == 2020 and date.month > 6:
        unemployment_rate[i] += np.random.uniform(8.0, 12.0)  # Gradual recovery period

df = pd.DataFrame({
    'Date': dates,
    'Unemployment_Rate_Percent': unemployment_rate,
    'Estimated_Employed_Millions': np.random.uniform(20, 25, len(dates))
})

print("✅ Dataset Created! First 5 rows:")
print(df.head(), "\n")

# ==========================================
# 2. PLOT UNEMPLOYMENT TREND LINE OVER TIME
# ==========================================
print("📊 Creating visual data trend graphs...")
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Unemployment_Rate_Percent', color='red', marker='o', linewidth=2)

# Add visual markings to highlight the Covid-19 lockdown phase
plt.axvspan('2020-03-01', '2020-08-01', color='yellow', alpha=0.3, label='COVID-19 Initial Impact Phase')

plt.title('Unemployment Rate Analysis Trend (2019 - 2022)', fontsize=14, fontweight='bold')
plt.xlabel('Timeline (Years)', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save the visualization graph to submit later
plt.savefig('unemployment_trend_analysis.png')
print("💾 Graph saved as 'unemployment_trend_analysis.png'!")
plt.show()
