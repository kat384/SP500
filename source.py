# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Analysis of S&P 500 Stocks: Insights into Performance, Trends, and Market Dynamics

# ## Introduction

# This project explores the S&P 500, a critical benchmark of U.S. economic performance, by analyzing key drivers of stock performance, sectoral dynamics, and market trends. Using historical stock prices, index data, and company fundamentals, the project covers:
#
# 1. Performance Drivers: Relationships between revenue growth, EBITDA, and market capitalization.
# 2. Sectoral Insights: Market capitalization distribution, growth opportunities, and operational efficiency across industries.
# 3. Market Trends: Broader trends influenced by dominant sectors and companies.
#    
# The methodology includes data preparation, visualization, and statistical analysis to derive actionable insights for investment decisions.

# + _cell_guid="b1076dfc-b9ad-4769-8c92-a6c4dae69d19" _uuid="8f2839f25d086af736a60e9eeb907d3b93b6e0e5"
# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import yfinance as yf

# +
companies = pd.read_csv('sp500_companies.csv')
index = pd.read_csv('sp500_index.csv')

companies.tail(), companies.info()

index.head(), index.info()
# -

# # Data preparation
#

companies.isna().sum()

columns_to_fill = ['Ebitda', 'Revenuegrowth', 'Fulltimeemployees']
for column in columns_to_fill:
    companies[column] = companies[column].fillna(companies[column].median())
companies.State = companies.State.fillna(companies.State.mode()[0])
index.Date = pd.to_datetime(index.Date)

# # Exploratory Analysis

fig_index = px.line(index, x=index["Date"], y=index["S&P500"], title='S&P500 Index Value', height=400)


# The Index Value has shown a consistent upward trend, except for a significant drop in 2020 caused by the COVID-19 pandemic.

X=index['S&P500'].to_numpy().reshape(-1,1)
y=index.Date
model=LinearRegression()
model.fit(X, y)

model.score(X, y)

cross_val_score(model, X, y, cv=5).mean()

y_pred =model.predict(X)
y_pred

sns.scatterplot(data=index, x='S&P500', y='Date')

sns.lineplot(x=index['S&P500'], y=y_pred, color='red') 

# +
companies_sorted = companies.sort_values(by=["Marketcap"], ascending=False)

fig_mcap_sector = px.bar(
    companies_sorted, 
    x="Sector", 
    y="Marketcap", 
    barmode='overlay',
    hover_data = 'Industry',
    title='Market Capitalization By Sector',
    color = 'Industry', 
    height=650)



# +
companies_sorted = companies.sort_values(by=['Marketcap'], ascending=False)

fig_mcap_outliers = px.box(
    companies_sorted, 
    x='Sector', 
    y='Marketcap', 
    points='suspectedoutliers',
    hover_data = ['Industry', 'Symbol'],
    title='Market Capitalization By Sector - Outliers - Top Companies', 
    height=650,
    color='Sector')
fig_mcap_outliers.update_layout(showlegend=False)
fig_mcap_outliers.update_traces(marker={'size': 8})

# -

# The sectors with the highest market capitalization are Technology, Consumer Cyclical and Communication Services. 
#
# **Reframing Outliers as Indicators - Technology Sector Example:**
# Instead of being outliers in the traditional sense, these companies are leaders that define the sector's performance - holding 51.68%, $18,937T of its total sector market capitalization. Their dominance shifts the focus from "anomalies to exclude" to "key drivers to analyze."
#
# **Sector Dynamics:**
# The data suggests a highly skewed distribution in the sector, where a few dominant players disproportionately control market capitalization. This reflects a power-law distribution. Their outsized impact suggests a level of stability, but it also raises concerns about sector dependency.
#
# **Implications for Risk Analysis:**
# The concentration of influence among a few outliers may require a shift in how risks are assessed. Instead of focusing on the average performance of companies in the sector, attention must be paid to these dominant players and their vulnerabilities.
#
# **Strategic Opportunities:**
# From a business or investment perspective, these outliers serve as benchmarks and offer insights into the characteristics that drive success in the sector. However, their dominance also creates opportunities for smaller firms to innovate in niche areas.
#
# **S&P index**. The dominance of technology outliers in the S&P index has significant implications. Their substantial market-cap weight makes the S&P heavily reliant on their performance, driving index movements and amplifying sectoral influence. This concentration poses risks during tech downturns, as their underperformance can disproportionately drag the index down. Conversely, their innovation and growth can boost investor confidence and attract capital flows into S&P-linked funds. However it may skew perceptions of market health by masking weaknesses in other sectors.
#

# +
companies_sorted = companies.sort_values(by=['Ebitda'], ascending=False)

fig_Ebitda = px.bar(
    companies_sorted, 
    x="Sector", 
    y="Ebitda", 
    barmode='overlay',
    hover_data = 'Industry',
    title='EBITDA By Sector',
    color = 'Industry', 
    height=650)


# -

# The data shows a disparity between market capitalization and EBITDA rankings across sectors, highlighting different investor and operational dynamics.
#
# Market Cap reflects investor optimism for growth, with Technology and Consumer Cyclical seen as high-reward, high-risk sectors.
# EBITDA indicates operational efficiency, with Financial Services and Energy having stable cash flows but lower growth expectations.
#
# Sectors like Technology and Communication Services face a trade-off between growth investment and current profitability. Technology leads in market cap, driven by growth potential and scalability, but ranks lower in EBITDA due to high reinvestment in R&D and infrastructure.
# Financial Services and Energy are more focused on steady profits. Financial Services has the highest EBITDA, indicating strong profitability from stable, cash-generating business models, but its market cap is lower, suggesting slower growth expectations.
#
# Overall, these discrepancies highlight the different ways investors value future growth versus current profitability, influencing sector performance and risk assessment.

# +
companies_sorted = companies.sort_values(by=['Revenuegrowth'], ascending=False)

fig_Revenue = px.bar(
    companies_sorted, 
    x="Sector", 
    y="Revenuegrowth", 
    barmode='overlay',
    hover_data = 'Industry',
    title='Revenue Growth or Decline By Sector',
    color = 'Industry', 
    height=650)


# -

# Technology remains a high-risk, high-reward sector, driven by innovation and future growth but impacted by short-term profitability pressures. While tech has high revenue growth potential, many firms are still reinvesting heavily into innovation, marketing, and infrastructure, which can depress profitability in the short term. The volatility in revenue suggests uneven profitability, which is typical for tech companies in growth or scale-up phases.
#
# Financial Services shows a wide range of revenue growth. It indicates some underperformance, likely from traditional financial institutions, and outperformance from fintech or other high-growth financial sectors. Companies in this sector can generate strong margins even in tough times, explaining the high EBITDA despite the narrower revenue growth range.
#
# Consumer Cyclical Sector Revenue Growth at -14.8% indicates that the sector is currently experiencing a contraction. Despite it, Market Cap is ranked 2nd, which reflects investor confidence in the sector’s potential. 

correlation_matrix = companies.corr(numeric_only=True)
mask=np.triu(correlation_matrix).round(3)
cor_fig = plt.figure(figsize=(10, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='icefire', linewidths=0.5, mask=mask)
plt.title('Correlation Heatmap')


# +
fig_revenue_ebitda_cap = px.scatter(
    companies_sorted, 
    x='Ebitda', 
    y='Revenuegrowth',
    hover_data=['Industry', 'Symbol'],
    size = 'Marketcap',
    title='Revenue Growth vs EBITDA vs Market Capitalization',
    color = 'Symbol', 
    height=650)



# +
mega_cap = px.scatter(companies[companies.Marketcap > 2.00e+11],
    x='Ebitda', 
    y='Marketcap',
    hover_data=['Industry', 'Symbol'],
    color = 'Symbol',
    height=850)
large_cap = px.scatter(
    companies[companies.Marketcap < 2.00e+11], 
    x='Ebitda', 
    y='Marketcap',
    hover_data=['Industry', 'Symbol'],
    color = 'Symbol',
    height=850)

fig = make_subplots(
    rows=1, cols=2,
    shared_xaxes=True,
    vertical_spacing=0.02, subplot_titles=('Mega Cap Companies > $200B', 'Large Cap Companies < $200B')
    )

# add each trace (or traces) to its specific subplot
for i in mega_cap.data :
    fig.add_trace(i, row=1, col=1)

for i in large_cap.data :
    fig.add_trace(i, row=1, col=2)

fig.update_layout(height=850, title_text='EBITDA vs Market Capitalization Comparison')
fig.update_traces(marker={'size': 9})




fig_hist_mega_cap, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(companies[companies.Marketcap > 2.00e+11].Marketcap, ax=ax1, color = '#6bb30c', bins=30, kde=True)
ax1.set_title('Mega Cap - Market Capitalisation Distribution')
ax1.set_xticks(np.arange(5, 31, 5))
sns.histplot(companies[companies.Marketcap > 2.00e+11].Ebitda, color = '#81A9F1', ax=ax2, bins=30, kde=True)
ax2.set_title('Mega Cap - EBITDA Distribution')

fig_hist_large_cap, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(companies[companies.Marketcap < 2.00e+11].Marketcap, ax=ax1, color = '#6bb30c', bins=30, kde=True)
ax1.set_title('Large Cap - Market Capitalisation Distribution')
ax1.set_xticks(np.arange(5, 31, 5))
sns.histplot(companies[companies.Marketcap < 2.00e+11].Ebitda, color = '#81A9F1', ax=ax2, bins=30, kde=True)
ax2.set_title('Large Cap - EBITDA Distribution')


# +
companies['Mc/EBITDA'] = companies.Marketcap/companies.Ebitda

mega_cap_df = companies['Mc/EBITDA'][companies.Marketcap > 2.00e+11].describe()
large_cap_df = companies['Mc/EBITDA'][companies.Marketcap < 2.00e+11].describe()

# -

# Market Capitalization-to-EBITDA ratio (often referred to as the EV/EBITDA) provides insight into how much investors are willing to pay for a company relative to its earnings before interest, taxes, depreciation, and amortization (EBITDA). A high ratio suggests that investors have strong expectations for the company's future growth or profitability.
# A low ratio - undervaluation or concerns about the company’s growth potential or efficiency. 
#
# **Comapison:**
#
# **Higher Ratios for Large Caps:**
# The mega cap group has a higher mean (36.07 vs. 16.02) and median (19.05 vs. 11.88) Market Cap/EBITDA, reflecting stronger investor confidence and valuation relative to earnings.
#
# **Negative and Extreme Outliers:**
# For the technology sector outliers Market Cap/EBITDA ratios are high due to their dominant market positions, high investor expectations, and the sector’s growth-oriented nature. However, excessively high ratios could signal overvaluation, making it essential to benchmark them against peers and historical averages. Smaller companies exhibit a wider range, with extreme negative and positive outliers (e.g., -1,170.90 and 475.95), likely due to highly volatile earnings or companies with minimal EBITDA relative to valuation.
#
# **Reliability of Ratios:**
# Mega cap companies, often well-established, exhibit ratios that are easier to interpret. Large cap may include growth-phase firms or those with inconsistent profitability, leading to outliers.
#
# **Implications:**
# Mega Caps: Represent sector leaders with stable and premium valuations. Their dominance justifies higher ratios due to strong earnings visibility and market position.
# Large Caps: A more diverse and volatile group, with valuations reflecting either high growth potential or operational challenges.

# # Conclusion 

# This analysis highlights the critical drivers of S&P 500 performance, including sector dynamics, financial metrics, and market cap disparities. 
#
# Key takeaways:
#
# **Investor Strategy:** Focus on sector outliers as benchmarks for growth and stability.
#
# **Risk Management:** Monitor high-cap technology firms due to their disproportionate influence on the index.
#
# **Opportunities:** Identify undervalued large caps with potential for growth.
#
# By leveraging these insights, businesses and investors can make informed decisions, balancing growth and risk in their strategies.
#
#
