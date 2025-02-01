import streamlit as st
from source import companies, index, companies_sorted

st.set_page_config(page_title='Introduction')
st.title('Analysis of S&P 500 Stocks: How Outliers Drive Index Leadership')

col1, col2 = st.columns(2, gap='large', vertical_alignment='center')
col1.markdown('This project explores the S&P 500, a critical benchmark of U.S. economic performance, '
              'by analyzing key drivers of stock performance, sectoral dynamics, and market trends. '
              'Using historical stock prices, index data, and company fundamentals, the project covers: \n')
col2.image('SP500.png')

st.markdown('\n**1\. Performance Drivers:** Relationships between revenue growth, EBITDA, and market capitalization.\n'
              '\n**2\. Sectoral Insights:** Market capitalization distribution, growth opportunities, and operational efficiency across industries.\n'
              '\n**3\. Market Trends:** Broader trends influenced by dominant sectors and companies.'
              '\n'
              '\nThe methodology includes data preparation, visualization, and statistical analysis to derive '
            'actionable insights for investment decisions.')

st.divider()

st.dataframe(companies,use_container_width=True)
st.dataframe(index, use_container_width=True)