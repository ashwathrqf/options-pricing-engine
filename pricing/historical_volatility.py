import yfinance as yf
import numpy as np
import streamlit as st

def _download_data(ticker, period):
    stock=yf.Ticker(ticker)
    history=stock.history(period=period)

    return history["Close"]

def _compute_log_returns(ticker,period):
    prices=_download_data(ticker,period)
    returns=np.log(prices/prices.shift(1))
    returns=returns.dropna()

    return returns

def _compute_historical_volatility(ticker, period):
    returns=_compute_log_returns(ticker,period)
    daily_std=returns.std()
    annual_volatility=daily_std*np.sqrt(252) #252 stock days in a year

    return float(annual_volatility)

@st.cache_data(ttl=300)
def _historical_volatility(ticker,period):
    return _compute_historical_volatility(ticker, period)
