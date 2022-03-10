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
import math

###################################################
# Push to GIT & Launch on Heroku using CMD Promp in folder 'Website':
# git add .
# git commit -m "Commit Message"
# git push heroku master 
# heroku ps:scale web=1
###################################################

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ---- Test Website: streamlit run Website.py
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# _______________________________________________________________________________________________________________________________ #

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Declare function to load in animation (json)
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Define & Load Animations ----
StonkAnimation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_oAtVDo.json")
DataLoadAnimation = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_ZVAR7L.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Commodity 4 Life :wave:")
    st.title("featuring.. 1 SHOT 1 PUTIN")
    st.write("NON FINANCIAL ADVICE")

# ---- Start ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Strategy")
        #st.write("##")
        st.write(
            """
            - BUY THE DIP
            - DOLLAR COST AVERAGE
            - NFA
            """
        )
    with right_column:
        st_lottie(StonkAnimation, height=300, key="coding")

st.info('Fetching Real-Time-Data...')
st_lottie(DataLoadAnimation, height=300, key="testing")
st.snow()

###########################################################################################################################################################
#################################################### To add new stonks the following containers must be modified ##########################################
###########################################################################################################################################################

# ---- Declare Values to Extract Live Data for Pie Chart ----
with st.container():
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
with st.container():
    DKKUSDPEG = yf.Ticker('DKKUSD=X')
    GBPUSDPEG = yf.Ticker('GBPUSD=X')
    SEKUSDPEG = yf.Ticker('SEKUSD=X')
    NOKUSDPEG = yf.Ticker('NOKUSD=X')
    CADUSDPEG = yf.Ticker('CADUSD=X')
    
    #GBPUSD = 1/GBPUSDPEG # 1 USD = GBXUSD
    #SEKUSD = 1/SEKUSDPEG # 1 USD = SEKUSD
    #NOKUSD = 1/NOKUSDPEG # 1 USD = NOKUSD
    #CADUSD = 1/CADUSDPEG # 1 USD = CADUSD
    #DKKUSD = 1/DKKUSDPEG # 1 USD = DKKUSD

    GBPUSD = 0.0131
    SEKUSD = 1/0.1019
    NOKUSD = 1/0.1121
    CADUSD = 1/0.7806
    DKKUSD = 1/0.1476

# Extract Bid Prices in USD (Changed BID to RMP)
with st.container():
    FXPO_BID = ((1250*FXPO_TICKR.info['regularMarketPrice']))*GBPUSD
    KOPY_BID = (5000*KOPY_TICKR.info['regularMarketPrice'])/SEKUSD
    MAHA_BID = (1000*MAHA_TICKR.info['regularMarketPrice'])/SEKUSD
    NWBO_BID = 1000*NWBO_TICKR.info['regularMarketPrice']
    PYPL_BID = 10*PYPL_TICKR.info['regularMarketPrice']
    PGS_BID = (5000*PGS_TICKR.info['regularMarketPrice'])/NOKUSD
    REG_BID = (2700*REG_TICKR.info['regularMarketPrice'])/CADUSD
    SSVR_BID = (1800*SSVR_TICKR.info['regularMarketPrice'])/CADUSD
    TPIC_BID = 150*TPIC_TICKR.info['regularMarketPrice']
    X_BID = 55*X_TICKR.info['regularMarketPrice']
    TotalValue_BID = math.trunc(FXPO_BID+KOPY_BID+MAHA_BID+NWBO_BID+PYPL_BID+PGS_BID+REG_BID+SSVR_BID+TPIC_BID+X_BID)

# Declare real-time portefolje values in DKK
with st.container():
    FXPODKK = math.trunc(FXPO_BID*DKKUSD)
    KOPYDKK = math.trunc(KOPY_BID*DKKUSD)
    MAHADKK = math.trunc(MAHA_BID*DKKUSD)
    NWBODKK = math.trunc(NWBO_BID*DKKUSD)
    PYPLDKK = math.trunc(PYPL_BID*DKKUSD)
    PGSDKK = math.trunc(PGS_BID*DKKUSD)
    REGDKK = math.trunc(REG_BID*DKKUSD)
    SSVRDKK = math.trunc(SSVR_BID*DKKUSD)
    TPICDKK = math.trunc(TPIC_BID*DKKUSD)
    XDKK = math.trunc(X_BID*DKKUSD)
    TotalValue = math.trunc(FXPODKK+KOPYDKK+MAHADKK+NWBODKK+PYPLDKK+PGSDKK+REGDKK+SSVRDKK+TPICDKK+XDKK)

# Extract Close Prices in USD
with st.container():
    FXPO_CLOSE = ((1250*FXPO_TICKR.info['previousClose']))*GBPUSD
    KOPY_CLOSE = (5000*KOPY_TICKR.info['previousClose'])/SEKUSD
    MAHA_CLOSE = (1000*MAHA_TICKR.info['previousClose'])/SEKUSD
    NWBO_CLOSE = 1000*NWBO_TICKR.info['previousClose']
    PYPL_CLOSE = 10*PYPL_TICKR.info['previousClose']
    PGS_CLOSE = (5000*PGS_TICKR.info['previousClose'])/NOKUSD
    REG_CLOSE = (2700*REG_TICKR.info['previousClose'])/CADUSD
    SSVR_CLOSE = (1800*SSVR_TICKR.info['previousClose'])/CADUSD
    TPIC_CLOSE = 150*TPIC_TICKR.info['previousClose']
    X_CLOSE = 55*X_TICKR.info['previousClose']

# Declare yesterday CLOSE portefolje values (USD)
with st.container():
    FXPOUSD_CLOSE = math.trunc(FXPO_CLOSE)
    KOPYUSD_CLOSE = math.trunc(KOPY_CLOSE)
    MAHAUSD_CLOSE = math.trunc(MAHA_CLOSE)
    NWBOUSD_CLOSE = math.trunc(NWBO_CLOSE)
    PYPLUSD_CLOSE = math.trunc(PYPL_CLOSE)
    PGSUSD_CLOSE = math.trunc(PGS_CLOSE)
    REGUSD_CLOSE = math.trunc(REG_CLOSE)
    SSVRUSD_CLOSE = math.trunc(SSVR_CLOSE)
    TPICUSD_CLOSE = math.trunc(TPIC_CLOSE)
    XUSD_CLOSE = math.trunc(X_CLOSE)
    TotalValue_CLOSE = math.trunc(FXPOUSD_CLOSE+KOPYUSD_CLOSE+MAHAUSD_CLOSE+NWBOUSD_CLOSE+PYPLUSD_CLOSE+PGSUSD_CLOSE+REGUSD_CLOSE+SSVRUSD_CLOSE+TPICUSD_CLOSE+XUSD_CLOSE)

# Declare daily gain in %:
with st.container():
    FXPO_DAILY = round(((FXPO_BID-FXPOUSD_CLOSE)/FXPO_BID)*100,2)
    KOPY_DAILY = round(((KOPY_BID-KOPYUSD_CLOSE)/KOPY_BID)*100,2)
    MAHA_DAILY = round(((MAHA_BID-MAHAUSD_CLOSE)/MAHA_BID)*100,2)
    NWBO_DAILY = round(((NWBO_BID-NWBOUSD_CLOSE)/NWBO_BID)*100,2)
    PYPL_DAILY = round(((PYPL_BID-PYPLUSD_CLOSE)/PYPL_BID)*100,2)
    PGS_DAILY = round(((PGS_BID-PGSUSD_CLOSE)/PGS_BID)*100,2)
    REG_DAILY = round(((REG_BID-REGUSD_CLOSE)/REG_BID)*100,2)
    SSVR_DAILY = round(((SSVR_BID-SSVRUSD_CLOSE)/SSVR_BID)*100,2)
    TPIC_DAILY = round(((TPIC_BID-TPICUSD_CLOSE)/TPIC_BID)*100,2)
    X_DAILY = round(((X_BID-XUSD_CLOSE)/X_BID)*100,2)
    TotalValue_DAILY = round(((TotalValue_BID-TotalValue_CLOSE)/TotalValue_BID)*100,2)

# Declare initial portefolje values
with st.container():
    FXPODKK_INITIAL = 17996.56
    KOPYDKK_INITIAL = 3312.97
    MAHADKK_INITIAL = 9329.61
    NWBODKK_INITIAL = 5955.51
    PYPLDKK_INITIAL = 8553.41
    PGSDKK_INITIAL = 9312.70
    REGDKK_INITIAL = 14538
    SSVRDKK_INITIAL = 11146.04
    TPICDKK_INITIAL = 14514.74
    XDKK_INITIAL = 10450.49
    TotalValue_INITIAL = math.trunc(FXPODKK_INITIAL+KOPYDKK_INITIAL+MAHADKK_INITIAL+NWBODKK_INITIAL+PYPLDKK_INITIAL+PGSDKK_INITIAL+REGDKK_INITIAL+SSVRDKK_INITIAL+TPICDKK_INITIAL+XDKK_INITIAL)

# Declare total gain in %
with st.container():
    FXPO_TOTAL = round(((FXPODKK-FXPODKK_INITIAL)/FXPODKK)*100,2)
    KOPY_TOTAL = round(((KOPYDKK-KOPYDKK_INITIAL)/KOPYDKK)*100,2)
    MAHA_TOTAL = round(((MAHADKK-MAHADKK_INITIAL)/MAHADKK)*100,2)
    NWBO_TOTAL = round(((NWBODKK-NWBODKK_INITIAL)/NWBODKK)*100,2)
    PYPL_TOTAL = round(((PYPLDKK-PYPLDKK_INITIAL)/PYPLDKK)*100,2)
    PGS_TOTAL = round(((PGSDKK-PGSDKK_INITIAL)/PGSDKK)*100,2)
    REG_TOTAL = round(((REGDKK-REGDKK_INITIAL)/REGDKK)*100,2)
    SSVR_TOTAL = round(((SSVRDKK-SSVRDKK_INITIAL)/SSVRDKK)*100,2)
    TPIC_TOTAL = round(((TPICDKK-TPICDKK_INITIAL)/TPICDKK)*100,2)
    X_TOTAL = round(((XDKK-XDKK_INITIAL)/XDKK)*100,2)
    TotalValue_TOTAL = round(((TotalValue_INITIAL-TotalValue)/TotalValue_INITIAL)*100,2)

# ---- PIE CHART BABY ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title('Stonks Chart')
        # Declare Values:
        stockTicker = ['FXPO','KOPY','MAHA','NWBO','PYPL','PGS','REG','SSVR','TPIC','X']
        stockValue = [FXPO_BID,KOPY_BID,MAHA_BID,NWBO_BID,PYPL_BID,PGS_BID,REG_BID,SSVR_BID,TPIC_BID,X_BID]
        # Setup Pie Chart
        fig = go.Figure(data=[go.Pie(labels=stockTicker, values=stockValue)])
        fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20, marker=dict(line=dict(color='#000000', width=2)))
        fig.update_layout(showlegend=True,margin=dict(l=1,r=2,b=1,t=1))
        st.write(fig)

    with right_column:
        st.title('Raw Numbers (Beta)')
        # Setup Pie Chart (gns anskaffelseskurs, daily gain, total gain)
        fig = go.Figure(data=[go.Table(
            #columnwidth = [80,400],
            header=dict(values=['<b>STONK</b>', '<b>Exposure DKK</b>', '<b>Daily Change %</b>', '<b>Total Change %</b>'],
                        line_color='darkslategray',
                        fill_color='lightskyblue',
                        height=40,
                        font_size=20,
                        align='left'),
            cells=dict(values=[['FXPO', 'KOPY', 'MAHA', 'NWBO', 'PYPL', 'PGS', 'REG', 'SSVR', 'TPIC', 'X','<b>Total<br>Portfolio:</b>'], # 1st column
                            [FXPODKK, KOPYDKK, MAHADKK, NWBODKK, PYPLDKK, PGSDKK, REGDKK, SSVRDKK, TPICDKK, XDKK, TotalValue], #2nd column
                            [FXPO_DAILY, KOPY_DAILY, MAHA_DAILY, NWBO_DAILY, PYPL_DAILY, PGS_DAILY, REG_DAILY, SSVR_DAILY, TPIC_DAILY, X_DAILY, TotalValue_DAILY], #3rd column
                            [FXPO_TOTAL, KOPY_TOTAL, MAHA_TOTAL, NWBO_TOTAL, PYPL_TOTAL, PGS_TOTAL, REG_TOTAL, SSVR_TOTAL, TPIC_TOTAL, X_TOTAL, TotalValue_TOTAL] #4th column
                            ],
                        line_color='darkslategray',
                        fill_color='lightcyan',
                        height=30,
                        font_size=16,
                        align='left'))
        ])
        fig.update_layout(showlegend=True,margin=dict(l=2,r=4,b=2,t=2))
        st.write(fig)
