import streamlit as st
from stocks import Stock, NFLX, fig, NFLX_change, NFLX_change_df, geo_mean_NFLX, ma, fig_return, fig_candlestick

st.set_page_config(page_title='Netflix Stocks Analysis with yfinance, seaborn and plotly')
st.header('Netflix Stocks Analysis.')

st.markdown('\n**Key Analyses:**\n'
                '\n'
               '\n**1. Retrieving Data:** Used yfinance to fetch daily OHLC data '
                '(Open, High, Low, Close) and other stock information like Volume for '
                'the selected ticker.\n'
              '\n**2.Closing Price, Volume, and Daily Change:** Visualized the closing '
              'price over time. Analyzed trading volume and calculated daily percentage '
              'changes in stock price.\n')
st.markdown('\n**3.Moving Averages:** Computed 10-day, 20-day and 50-day Moving Averages '
              'to identify short-term and long-term stock trends.\n'
              '\n**4.Daily Return:** Calculated daily returns to assess average '
              'performance and volatility.\n'
              '\n**5.Candlestick Chart:** Created an interactive candlestick chart '
              'to visualize the stock\'s price movements using the Open, High, Low, '
              'and Close data.')

st.subheader('**1. Retrieving Data:**')
st.markdown('\nWe created a class using yfinance and plotly to download and analyze stock data. '
              'The class automatically retrieves OHLC data for a given ticker symbol '
              '(e.g., "NFLX") from Yahoo Finance.\n'
               '\n')

with st.expander("Class"):
    st.write('''class Stock:
    
    def __init__(
        self,
        ticker: str,
        period: str='1y',
        interval: str='1d',
        start: str=None,
        end: str=None
    ) -> None:
        
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.start = start
        self.end = end
        self.df = yf.Ticker(self.ticker).history(
            period=self.period,
            interval=self.interval,
            start=self.start,
            end=self.end,
        ).drop(['Dividends', 'Stock Splits'], axis=1)
    
    ''')

st.subheader('**2. Closing Price, Volume, Daily Change**')
st.markdown('Closing price serves as a key indicator in analyzing the performance '
              'of that stock over time. Investors typically use the closing price as the '
              'benchmark for evaluating the performance of a stock.\n'
              '\nHistorical closing prices will be ised to calculate the moving average, '
              'percentage change, and volatility.\n'
              '\nVolume is a fundamental metric in trading, especially when used in '
              'conjunction with price analysis. For instance, a price increase along with '
              'high volume often signifies strong buying interest, while a price increase '
              'with low volume may signal a lack of conviction and may not be sustainable.')

st.pyplot(fig)

st.subheader('**2. Moving average.**')
st.markdown('The moving average (MA) is a simple technical analysis tool that '
              'smooths out price data by creating a constantly updated average price. '
              'The average is taken over a specific period of time, like 10 days, '
              '20 minutes, 30 weeks, or any time period the trader chooses.')
st.pyplot(ma)

st.subheader('**3. Daily return.**')
st.markdown('Now that we\'ve done some baseline analysis, let\'s go ahead and dive '
              'a little deeper. We\'re now going to analyze the risk of the stock. '
              'In order to do so we\'ll need to take a closer look at the daily changes '
              'of the stock, and not just its absolute value. Let\'s go ahead and use pandas '
              'to retrieve teh daily returns for the Netflix stock.')

st.pyplot(fig_return)

st.subheader('**4. Candlestick Chart.**')
st.markdown('A candlestick chart is a type of financial chart used to represent the '
              'price movement of an asset over a specific time period. It’s widely used '
              'in technical analysis to help visualize the open, high, low, and close prices '
              '(OHLC) for a particular time frame (e.g., daily, hourly).')

st.plotly_chart(fig_candlestick)

st.divider()

st.subheader('**Takeaway:**')
st.markdown('This page provides a comprehensive analysis of stock performance, '
             'combining retrieved data, moving averages, daily returns, and candlestick '
             'charts to assess trends and risk.')







