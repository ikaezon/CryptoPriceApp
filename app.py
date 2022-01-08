import streamlit as st
import pandas as pd
import yfinance as yf


def spacer():
    st.markdown("##")
    st.markdown("##")


def btc_chart():
    st.header('**Bitcoin**')
    Bitcoin = 'BTC-USD'
    BTC_Data = yf.Ticker(Bitcoin)
    BTCHis = BTC_Data.history(period="max")
    st.line_chart(BTCHis.Close)


def eth_chart():
    st.header('**Ethereum**')
    Ethereum = 'ETH-USD'
    ETH_Data = yf.Ticker(Ethereum)
    ETHHis = ETH_Data.history(period="max")
    st.line_chart(ETHHis.Close)


def bnb_chart():
    st.header('**Binance Coin**')
    Binance_Coin = 'BNB-USD'
    BNB_Data = yf.Ticker(Binance_Coin)
    BNBHis = BNB_Data.history(period="max")
    st.line_chart(BNBHis.Close)


st.title("""Kaevon's Cryptocurrency Tracker
A crypto price tracker using *Binance API*
""")

spacer()

st.header('**Selected Price**')
st.write('Select various cryptocurrencies on the left sidebar')

df = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')


def round_value(input_value):
    if input_value.values > 1:
        a = float(round(input_value, 2))
    else:
        a = float(round(input_value, 8))
    return a


col1, col2, col3 = st.columns(3)

col1_selection = st.sidebar.selectbox('Price 1', df.symbol, list(df.symbol).index('BTCBUSD'))
col2_selection = st.sidebar.selectbox('Price 2', df.symbol, list(df.symbol).index('ETHBUSD'))
col3_selection = st.sidebar.selectbox('Price 3', df.symbol, list(df.symbol).index('BNBBUSD'))
col4_selection = st.sidebar.selectbox('Price 4', df.symbol, list(df.symbol).index('XRPBUSD'))
col5_selection = st.sidebar.selectbox('Price 5', df.symbol, list(df.symbol).index('ADABUSD'))
col6_selection = st.sidebar.selectbox('Price 6', df.symbol, list(df.symbol).index('DOGEBUSD'))
col7_selection = st.sidebar.selectbox('Price 7', df.symbol, list(df.symbol).index('SHIBBUSD'))
col8_selection = st.sidebar.selectbox('Price 8', df.symbol, list(df.symbol).index('DOTBUSD'))
col9_selection = st.sidebar.selectbox('Price 9', df.symbol, list(df.symbol).index('MATICBUSD'))

col1_df = df[df.symbol == col1_selection]
col2_df = df[df.symbol == col2_selection]
col3_df = df[df.symbol == col3_selection]
col4_df = df[df.symbol == col4_selection]
col5_df = df[df.symbol == col5_selection]
col6_df = df[df.symbol == col6_selection]
col7_df = df[df.symbol == col7_selection]
col8_df = df[df.symbol == col8_selection]
col9_df = df[df.symbol == col9_selection]

col1_price = round_value(col1_df.weightedAvgPrice)
col2_price = round_value(col2_df.weightedAvgPrice)
col3_price = round_value(col3_df.weightedAvgPrice)
col4_price = round_value(col4_df.weightedAvgPrice)
col5_price = round_value(col5_df.weightedAvgPrice)
col6_price = round_value(col6_df.weightedAvgPrice)
col7_price = round_value(col7_df.weightedAvgPrice)
col8_price = round_value(col8_df.weightedAvgPrice)
col9_price = round_value(col9_df.weightedAvgPrice)

col1_percent = f'{float(col1_df.priceChangePercent)}%'
col2_percent = f'{float(col2_df.priceChangePercent)}%'
col3_percent = f'{float(col3_df.priceChangePercent)}%'
col4_percent = f'{float(col4_df.priceChangePercent)}%'
col5_percent = f'{float(col5_df.priceChangePercent)}%'
col6_percent = f'{float(col6_df.priceChangePercent)}%'
col7_percent = f'{float(col7_df.priceChangePercent)}%'
col8_percent = f'{float(col8_df.priceChangePercent)}%'
col9_percent = f'{float(col9_df.priceChangePercent)}%'

col1.metric(col1_selection, col1_price, col1_percent)
col2.metric(col2_selection, col2_price, col2_percent)
col3.metric(col3_selection, col3_price, col3_percent)
col1.metric(col4_selection, col4_price, col4_percent)
col2.metric(col5_selection, col5_price, col5_percent)
col3.metric(col6_selection, col6_price, col6_percent)
col1.metric(col7_selection, col7_price, col7_percent)
col2.metric(col8_selection, col8_price, col8_percent)
col3.metric(col9_selection, col9_price, col9_percent)

spacer()

st.header("**All Prices**")
st.write("List of all cryptocurrencies from *Binance API*")
st.dataframe(df)

spacer()

st.header("**Past price action of Cryptocurrency**")
st.write("History of top 3 Cryptocurrencies from *Yahoo Finance*")

btc_chart()

eth_chart()

bnb_chart()
