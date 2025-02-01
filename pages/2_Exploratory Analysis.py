import streamlit as st
from source import (companies, index, companies_sorted,
                    fig_index, fig_mcap_sector, fig_mcap_outliers, fig_Ebitda, fig_Revenue, fig_revenue_ebitda_cap)

st.set_page_config(page_title='Exploratory analysis, p.1')
st.header('Performance Drivers: Relationships between Revenue Growth, EBITDA, and Market Capitalization.')

st.plotly_chart(fig_index)
st.markdown('The Index Value has shown a consistent upward trend, '
            'except for a significant drop in 2020 caused by the COVID-19 pandemic.')
st.plotly_chart(fig_mcap_sector)
st.plotly_chart(fig_mcap_outliers)
st.markdown('The sectors with the highest market capitalization are Technology, '
            'Consumer Cyclical and Communication Services.\n')
col1, col2 = st.columns(2)
col1.markdown('\n**Reframing Outliers as Indicators - Technology Sector Example:**'
            '\nInstead of being outliers in the traditional sense, these companies are '
            'leaders that define the sector\'s performance - holding 51.68/%, $18,937T '
            'of its total sector market capitalization. Their dominance shifts the focus '
            'from "anomalies to exclude" to "key drivers to analyze."'
            '\n'
            '\n**Sector Dynamics:**\n'
            'The data suggests a highly skewed distribution in the sector, where a '
            'few dominant players disproportionately control market capitalization. This '
            'reflects a power-law distribution. Their outsized impact suggests a level of '
            'stability, but it also raises concerns about sector dependency.'
            '\n'
            '\n**Implications for Risk Analysis:**\n'
            'The concentration of influence among a few outliers may require a shift in '
            'how risks are assessed. Instead of focusing on the average performance of companies '
            'in the sector, attention must be paid to these dominant players and their '
            'vulnerabilities.'
            '\n')
col2.markdown('\n**Strategic Opportunities:**'
            '\nFrom a business or investment perspective, these outliers serve as benchmarks and '
            'offer insights into the characteristics that drive success in the sector. However, '
            'their dominance also creates opportunities for smaller firms to innovate in niche '
            'areas.\n'
            '\n'
            '\n**S&P index**.'
            '\nThe dominance of technology outliers in the S&P index has significant '
            'implications. Their substantial market-cap weight makes the S&P heavily reliant '
            'on their performance, driving index movements and amplifying sectoral influence. '
            'This concentration poses risks during tech downturns, as their underperformance can '
            'disproportionately drag the index down. Conversely, their innovation and growth '
            'can boost investor confidence and attract capital flows into S&P-linked funds. '
            'However it may skew perceptions of market health by masking weaknesses in other '
            'sectors.')

st.plotly_chart(fig_Ebitda)
col1, col2 = st.columns(2)
col1.markdown('The data shows a disparity between market capitalization and EBITDA '
            'rankings across sectors, highlighting different investor and operational dynamics.\n'
            '\nMarket Cap reflects investor optimism for growth, with Technology and Consumer Cyclical '
            'seen as high-reward, high-risk sectors.\n'
            '\nEBITDA indicates operational efficiency, with Financial Services and '
            'Energy having stable cash flows but lower growth expectations.\n')
col2.markdown('\nSectors like Technology and Communication Services face a trade-off '
            'between growth investment and current profitability. Technology leads in '
            'market cap, driven by growth potential and scalability, but ranks lower in EBITDA '
            'due to high reinvestment in R&D and infrastructure.\n'
            '\nFinancial Services and Energy are more focused on steady profits. '
            'Financial Services has the highest EBITDA, indicating strong profitability '
            'from stable, cash-generating business models, but its market cap is lower, '
            'suggesting slower growth expectations.\n')
st.markdown('\nOverall, these discrepancies highlight the different ways investors value '
            'future growth versus current profitability, influencing sector performance and '
            'risk assessment.')

st.plotly_chart(fig_Revenue)
col1, col2 = st.columns(2)
col1.markdown('\n**Technology** remains a high-risk, high-reward sector, driven by innovation and '
            'future growth but impacted by short-term profitability pressures. While tech has '
            'high revenue growth potential, many firms are still reinvesting heavily into '
            'innovation, marketing, and infrastructure, which can depress profitability in the '
            'short term. The volatility in revenue suggests uneven profitability, which is typical '
            'for tech companies in growth or scale-up phases.\n'
            '\n**Consumer Cyclical Sector** Revenue Growth at -14.8% indicates that the sector is '
            'currently experiencing a contraction. Despite it, Market Cap is ranked 2nd, which '
            'reflects investor confidence in the sector’s potential.')
col2.markdown('\n **Financial Services** shows a wide range '
            'of revenue growth. It indicates some underperformance, likely from traditional '
            'financial institutions, and outperformance from fintech or other high-growth '
            'financial sectors. Companies in this sector can generate strong margins even in tough '
            'times, explaining the high EBITDA despite the narrower revenue growth range.\n')

st.plotly_chart(fig_revenue_ebitda_cap)

