import yfinance as yf
import streamlit as st

def _validate_inputs(ticker: str):

    if not isinstance(ticker, str):
        raise ValueError("Ticker must be a string.")

    ticker = ticker.strip().upper()

    if ticker == "":
        raise ValueError("Ticker cannot be empty.")

    return ticker

def _download_stock(ticker):
    ticker=_validate_inputs(ticker)

    stock=yf.Ticker(ticker)

    return stock

@st.cache_data(ttl=300)
def _get_current_price(ticker):

    stock=_download_stock(ticker)

    history=stock.history(period="1d")

    price=history["Close"].iloc[-1]

    return float(price)

def _get_company_name(ticker):
    stock = _download_stock(ticker)

    return stock.info["longName"]