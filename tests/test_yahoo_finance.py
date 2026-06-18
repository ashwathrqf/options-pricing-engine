import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from market_data.yahoo_finance import (
    _get_current_price,
    _get_company_name,
)


def main():

    ticker = "AAPL"

    print("=" * 60)
    print("YAHOO FINANCE TEST")
    print("=" * 60)

    company = _get_company_name(ticker)
    price = _get_current_price(ticker)

    print(f"Ticker        : {ticker}")
    print(f"Company       : {company}")
    print(f"Current Price : ${price:.2f}")


if __name__ == "__main__":
    main()