import streamlit as st
from source import (companies, companies_sorted,
                    correlation_matrix, mask, cor_fig, mega_cap, large_cap, fig,
                    fig_hist_mega_cap, fig_hist_large_cap, large_cap_df, mega_cap_df)

st.set_page_config(page_title='Exploratory analysis, p.2')
st.header('Market Capitalization-to-EBITDA Ratio in Mega Cap and Large Cap Companies Data')

st.pyplot(cor_fig)
col1, col2 = st.columns(2, gap='large')
col1.markdown('\n**Market Capitalization-to-EBITDA ratio** as seen in Correlation matrix '
              'is essential parameter in stocks analysis. It often referred to as the '
              'EV/EBITDA and provides insight into how much investors are willing to '
              'pay for a company relative to its earnings before interest, taxes, '
              'depreciation, and amortization (EBITDA). A high ratio suggests that '
              'investors have strong expectations for the company\'s future growth or '
              'profitability. A low ratio - undervaluation or concerns about the company’s growth '
              'potential or efficiency.\n'
              '\n')
col2.markdown('\nWe will explore Market Capitalization-to-EBITDA ratio for 2 groups of companies:'
              '\n- Mega Cap Companies - 42 of 501 companies, they are upper outliers and leaders at the same time. They summative Market Cap '
              'equals over 50% of total Market Cap of S&P 500 Index.\n'
              '\n- Large Cap Companies - the rest 459 companies of S&P 500 Index. \n')
st.plotly_chart(fig)
st.pyplot(fig_hist_mega_cap)
st.pyplot(fig_hist_large_cap)

col1, col2 = st.columns(2, gap='large')
with col1:
    st.write('**Mega Cap Dataframe Description**')
    st.table(mega_cap_df)
with col2:
    st.write('**Large Cap Dataframe Description**')
    st.table(large_cap_df)

st.markdown('\n**Comparison:**\n')
col1, col2 = st.columns(2, gap='large')
col1.markdown('\n **Higher Ratios for Large Caps:**\n The mega cap group has a higher mean '
              '(36.07 vs. 16.02) and median (19.05 vs. 11.88) Market Cap/EBITDA, '
              'reflecting stronger investor confidence and valuation relative to earnings.\n'
              '\n**Negative and Extreme Outliers:** For the technology sector outliers Market '
              'Cap/EBITDA ratios are high due to their dominant market positions, high '
              'investor expectations, and the sector’s growth-oriented nature. However, '
              'excessively high ratios could signal overvaluation, making it essential to '
              'benchmark them against peers and historical averages. Smaller companies '
              'exhibit a wider range, with extreme negative and positive outliers (e.g., '
              '-1,170.90 and 475.95), likely due to highly volatile earnings or companies '
              'with minimal EBITDA relative to valuation.\n'
              '\n')
col2.markdown('\n**Reliability of Ratios:** Mega cap companies, often well-established, '
              'exhibit ratios that are easier to interpret. Large cap may include growth-phase '
              'firms or those with inconsistent profitability, leading to outliers.\n'
              '\n'
              '\n**Implications:**\n'
              '\n'
              '\n **Mega Caps:** Represent sector leaders with stable and premium valuations. '
              'Their dominance justifies higher ratios due to strong earnings visibility '
              'and market position.\n'
              '\n**Large Caps:** A more diverse and volatile group, with valuations reflecting '
              'either high growth potential or operational challenges.\n'
              '\n')

st.divider()

st.subheader('**Conclusion:**\n'
                          '\nThis analysis highlights the critical drivers of S&P 500 '
                          'performance, including sector dynamics, financial metrics, and '
                          'market cap disparities.\n'
                          '\n**Key takeaways**:\n'
                          '\n**Investor Strategy:** Focus on sector outliers as benchmarks '
                          'for growth and stability.\n'
                          '\n**Risk Management:** Monitor high-cap technology firms due '
                          'to their disproportionate influence on the index.\n'
                          '\n**Opportunities:** Identify undervalued large caps with '
                          'potential for growth.\n'
                          '\nBy leveraging these insights, businesses and '
                          'investors can make informed decisions, balancing growth and '
                          'risk in their strategies.')
