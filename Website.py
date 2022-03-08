from re import X
from streamlit_lottie import st_lottie
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import requests


# streamlit run Website.py

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Declare function to load in animation (json)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD Animations ----
StonkAnimation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_oAtVDo.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, this is GandalfMoon :wave:")
    st.title("featuring.. 1 SHOT 1 PUTIN")
    st.write("COMMODITY EXPERT")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Strategy 1")
        #st.write("##")
        st.write(
            """
            - BUY THE DIP
            - DOLLAR COST AVERAGE
            """
        )
    with right_column:
        st_lottie(StonkAnimation, height=300, key="coding")


# ---- STONK CHART ----
#tickerSymbol = 'GOOGL'
#tickerData = yf.Ticker(tickerSymbol)
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High, Low Close, Volume, Dividends, Stock Splits
#st.line_chart(tickerDf.Close)

# ---- Declare Values to Extract Live Data for Pie Chart ----
FXPO_TICKR = yf.Ticker('FXPO.L')
KOPY_TICKR = yf.Ticker('KOPY.ST')
MAHA_TICKR = yf.Ticker('MAHA-A.ST')
NWBO_TICKR = yf.Ticker('NWBO')
PYPL_TICKR = yf.Ticker('PYPL')
PGS_TICKR = yf.Ticker('PGS.OL')
REG_TICKR = yf.Ticker('REG.V')
SSVR_TICKR = yf.Ticker('SSVR.V')
TPIC_TICKR = yf.Ticker('TPIC')
X_TICKR = yf.Ticker('X')

# Valuta Conversions
GBXUSD = 76.34 # 1 USD = GBXUSD
SEKUSD = 9.981 # 1 USD = SEKUSD
NOKUSD = 8.986 # 1 USD = NOKUSD
CADUSD = 1.283 # 1 USD = CADUSD

# Extract Bid Prices
FXPO_BID = (1250*FXPO_TICKR.info['bid'])/GBXUSD
KOPY_BID = (5000*KOPY_TICKR.info['bid'])/SEKUSD
MAHA_BID = (1000*MAHA_TICKR.info['bid'])/SEKUSD
NWBO_BID = 1000*NWBO_TICKR.info['regularMarketPrice']
PYPL_BID = 10*PYPL_TICKR.info['bid']
PGS_BID = (5000*PGS_TICKR.info['bid'])/NOKUSD
REG_BID = (2700*REG_TICKR.info['bid'])/CADUSD
SSVR_BID = (1800*SSVR_TICKR.info['bid'])/CADUSD
TPIC_BID = 150*TPIC_TICKR.info['bid']
X_BID = 55*X_TICKR.info['bid']

# ---- PIE CHART BABY ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Stonks')
        # Declare Values:
        stockTicker = ['FXPO','KOPY','MAHA','NWBO','PYPL','PGS','REG','SSVR','TPIC','X']
        stockValue = [FXPO_BID,KOPY_BID,MAHA_BID,NWBO_BID,PYPL_BID,PGS_BID,REG_BID,SSVR_BID,TPIC_BID,X_BID]
        # Setup Pie Chart
        fig = go.Figure(data=[go.Pie(labels=stockTicker, values=stockValue)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20, marker=dict(line=dict(color='#000000', width=2)))
        fig.update_layout(showlegend=True,margin=dict(l=1,r=2,b=1,t=1))
        st.write(fig)

    with right_column:
        st.title('Crypto')
        # Declare Values:
        stockTicker = ['USDT']
        stockValue = [1]
        # Setup Pie Chart
        fig = go.Figure(data=[go.Pie(labels=stockTicker, values=stockValue)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20, marker=dict(line=dict(color='#000000', width=2)))
        fig.update_layout(showlegend=True,margin=dict(l=1,r=2,b=1,t=1))
        st.write(fig)