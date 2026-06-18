import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from pricing.historical_volatility import _historical_volatility


def main():

    print("=" * 60)
    print("HISTORICAL VOLATILITY TEST")
    print("=" * 60)

    ticker = "AAPL"
    period = "1y"

    hv = _historical_volatility(
        ticker=ticker,
        period=period,
    )

    print(f"\nTicker                 : {ticker}")
    print(f"Period                 : {period}")
    print(f"Historical Volatility  : {hv:.6f}")
    print(f"Historical Volatility  : {hv*100:.2f}%")


if __name__ == "__main__":
    main()