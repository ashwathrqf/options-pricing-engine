import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from market_data.option_chain import (
    _get_expiries,
    _get_option_chain,
)

from visualization.volatility_smile import (
    volatility_smile,
)


ticker = "AAPL"

expiry = _get_expiries(ticker)[0]

calls = _get_option_chain(
    ticker,
    expiry,
    "call",
)

fig = volatility_smile(calls)

fig.show()