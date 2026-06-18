import yfinance as yf
import pandas as pd
import streamlit as st


def _validate_inputs(
    ticker: str,
    expiry: str = None,
    option_type: str = None,
):
    if not isinstance(ticker, str) or ticker.strip() == "":
        raise ValueError("Ticker must be a non-empty string.")

    ticker = ticker.strip().upper()

    if expiry is not None:
        if not isinstance(expiry, str):
            raise ValueError("Expiry must be a string.")

    if option_type is not None:
        option_type = option_type.lower()

        if option_type not in ("call", "put"):
            raise ValueError("Option type must be 'call' or 'put'.")

    return ticker, expiry, option_type


def _download_option_chain(ticker: str):

    ticker, _, _ = _validate_inputs(ticker)

    stock = yf.Ticker(ticker)

    return stock


def _get_expiries(ticker: str):

    stock = _download_option_chain(ticker)

    return list(stock.options)

@st.cache_data(ttl=300)
def _get_option_chain(
    ticker: str,
    expiry: str,
    option_type: str,
):

    ticker, expiry, option_type = _validate_inputs(
        ticker,
        expiry,
        option_type,
    )

    stock = _download_option_chain(ticker)

    chain = stock.option_chain(expiry)

    if option_type == "call":
        return chain.calls

    return chain.puts

@st.cache_data(ttl=300)
def _get_option_data(
    ticker: str,
    expiry: str,
    strike: float,
    option_type: str,
):

    chain = _get_option_chain(
        ticker,
        expiry,
        option_type,
    )

    row = chain.loc[
        chain["strike"] == strike
    ]

    if row.empty:
        raise ValueError(
            f"No option found for strike {strike}"
        )

    row = row.iloc[0]

    return {
        "contract_symbol": row["contractSymbol"],
        "strike": float(row["strike"]),
        "last_price": float(row["lastPrice"]),
        "bid": float(row["bid"]),
        "ask": float(row["ask"]),
        "change": float(row["change"]),
        "percent_change": float(row["percentChange"]),
        "volume": int(row["volume"]) if pd.notna(row["volume"]) else 0,
        "open_interest": int(row["openInterest"]) if pd.notna(row["openInterest"]) else 0,
        "implied_volatility": float(row["impliedVolatility"]),
        "in_the_money": bool(row["inTheMoney"]),
        "currency": row["currency"],
    }

def _get_available_strikes(
    ticker,
    expiry,
    option_type,
):

    chain = _get_option_chain(
        ticker,
        expiry,
        option_type,
    )

    return sorted(
        chain["strike"].tolist()
    )

def _get_market_option_price(
    ticker,
    expiry,
    strike,
    option_type,
):

    option = _get_option_data(
        ticker,
        expiry,
        strike,
        option_type,
    )

    return option["last_price"]

