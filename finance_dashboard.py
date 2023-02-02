import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt
from PIL import Image

image = Image.open("logoponcho-degrade (1).png")
st.image(image, width=700)

@st.cache
def downloadData(dropdown, start, end):

    """ This function is used to download and load stock data from the 'Yahoo Finance' API using the 'yfinance' library.
    The data is retrieved for a specified stock symbol (represented by the 'dropdown' argument) and for a specified date range
    (represented by the 'start' and 'end' arguments). The resulting data frame will only include the 'Adj Close' column and is
    returned as the result of the function. The 'st.cache' decorator is used to cache the results of the function so that it
    doesn't have to be run repeatedly."""

    df = yf.download(dropdown, start=start, end=end)
    df = df['Adj Close']
    return df

@st.experimental_memo
def convert_df(df):
    """
    This function is used to convert a given pandas data frame (represented by the 'df' argument)
    into a CSV-formatted string, encoded in UTF-8 format. The 'to_csv' method is used to convert
    the data frame into a CSV string and the 'encode' method is used to encode it as UTF-8. The 'index'
    argument of the 'to_csv' method is set to 'False' to exclude the index column from the output.
    The 'st.experimental_memo' decorator is used to memoize the function so that it doesn't have to run repeatedly.
    """
    return df.to_csv(index=False).encode('utf-8')

st.sidebar.title("What do you want to analyze?")
section = st.sidebar.selectbox("", ["Argentinian Stocks", "CEDEARs", "ETFs"])

tickers_cedears = ['MELI', 'BABA', 'KO', 'GOLD', 'TSLA',
                     'AAPL', 'AMD', 'VALE', 'META', 'PBR',
                     'AMZN', 'GOOGL', 'VIST', 'TX', 'MSFT',
                     'NVDA', 'WMT', 'BRK-B', 'DIS', 'JNJ',
                     'XOM', 'PG', 'TS', 'X', 'JD', 'MA', 'MCD',
                     'NFLX', 'NKE', 'NIO', 'PYPL', 'QCOM',
                     'RBLX', 'SHOP', 'SNAP', 'SPOT', 'SQ',
                     'SBUX', 'GS', 'UBER', 'V', 'GLOB', 'DE',
                     'DESP', 'EBAY', 'BIDU', 'BAC', 'ADBE', 'ABNB']

tickers_etf = ['ARKK', 'DIA', 'EEM', 'EWZ',
               'IWM', 'QQQ', 'SPY', 'XLE', 'XLF']

tickers_stocks = ['ALUA.BA', 'BBAR.BA', 'BMA.BA',
                    'BYMA.BA', 'CEPU.BA', 'COME.BA',
                    'CRES.BA', 'CVH.BA', 'EDN.BA',
                    'GGAL.BA', 'HARG.BA', 'LOMA.BA',
                    'MIRG.BA', 'PAMP.BA', 'SUPV.BA',
                    'TECO2.BA', 'TGNO4.BA', 'TGSU2.BA',
                    'TRAN.BA', 'TXAR.BA', 'VALO.BA', 'YPFD.BA']

if section == 'Argentinian Stocks':
#SECCIÓN 1: ACCIONES ARGENTINAS

    st.subheader('Argentinian Stocks')
    st.markdown('Argentinian Stocks. Results in ARS')

    # Multiselect dropdown
    dropdown = st.multiselect('Choose tickers', tickers_stocks, key='stocks')

    # Selección de fechas
    start = st.date_input('Start Date', value = pd.to_datetime('2018-01-01'), key='start')
    end = st.date_input('End Date', value = pd.to_datetime('today'), key='end')


    if len(dropdown) > 0:
        df = downloadData(dropdown, start, end)
        st.subheader('Stock price by date')
        st.dataframe(df)
        title="Stock Price: "
        for ticker in dropdown:
            title+= ticker + " -"
        fig = px.line(df, title=title)
        st.plotly_chart(fig)
        csv = convert_df(df)
        st.download_button(
            "Download csv file",
            csv,
            "fileStocks.csv",
            "text/csv",
            key='download-csv'
        )
elif section == 'CEDEARs':
#SECCIÓN 2: CEDEARS

    st.subheader('CEDEARS')
    st.markdown('CEDEARs. Results in USD')

    # Multiselect dropdown
    dropdown2 = st.multiselect('Choose tickers', tickers_cedears, key='cedears')

    # Selección de fechas
    start2 = st.date_input('Start Date', value = pd.to_datetime('2018-01-01'), key='start2')
    end2 = st.date_input('End Date', value = pd.to_datetime('today'), key='endx2')


    if len(dropdown2) > 0:
        df2 = downloadData(dropdown2, start2, end2)
        st.subheader('Close Price by Date')
        st.dataframe(df2)
        title="CEDEARs Price: "
        for ticker in dropdown2:
            title+= ticker + " -"
        fig2 = px.line(df2, title=title)
        st.plotly_chart(fig2)
        csv2 = convert_df(df2)
        st.download_button(
        "Download csv file",
        csv2,
        "fileCedears.csv",
        "text/csv",
        key='download-csv'
                            )
elif section == 'ETFs':
    #SECCIÓN 3: ETF

    st.subheader('ETFs')
    st.markdown('ETFs. Results in USD')

    # Multiselect dropdown
    dropdown3 = st.multiselect('Choose tickers', tickers_etf, key='etf')

    st.markdown("---")
    # Selección de fechas
    start3 = st.date_input('Start Date', value = pd.to_datetime('2018-01-01'))
    end3 = st.date_input('End Date', value = pd.to_datetime('today'))


    if len(dropdown3) > 0:
        df3 = downloadData(dropdown3, start3, end3)
        st.subheader('Close Price by Date')
        st.dataframe(df3)
        title="CEDEARs Price: "
        for ticker in dropdown3:
            title+= ticker + " -"
        fig3 = px.line(df3, title=title)
        st.plotly_chart(fig3)
        csv3 = convert_df(df3)
        st.download_button(
        "Download csv",
        csv3,
        "fileCedears.csv",
        "text/csv",
        key='download-csv'
                            )