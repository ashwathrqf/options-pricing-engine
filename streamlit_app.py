# import streamlit as st
# import pandas as pd

# # ==========================================================
# # Pricing Models
# # ==========================================================

# from pricing.black_scholes import price_option_bs
# from pricing.binomial import price_option_binomial

# from pricing.monte_carlo import (
#     price_option_mc,
#     price_option_mc_antithetic,
#     price_option_mc_statistics,
#     convergence_curve,
# )

# from pricing.greeks import calculate_greeks
# from pricing.historical_volatility import _historical_volatility

# # ==========================================================
# # Market Data
# # ==========================================================

# from market_data.yahoo_finance import (
#     _get_current_price,
#     _get_company_name,
# )

# from market_data.option_chain import (
#     _get_expiries,
#     _get_option_chain,
#     _get_option_data,
#     _get_available_strikes,
# )

# # ==========================================================
# # Visualizations
# # ==========================================================

# from visualization.payoff import payoff_diagram
# from visualization.convergence import convergence_plot
# from visualization.volatility_smile import volatility_smile

# # ==========================================================
# # Page Configuration
# # ==========================================================

# st.set_page_config(
#     page_title="QuantLab",
#     page_icon="📈",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# st.title("📈 QuantLab")

# st.caption(
#     "Professional Options Analytics Platform"
# )

# st.divider()

# # ==========================================================
# # Sidebar
# # ==========================================================

# st.sidebar.link_button(
#     "⭐ View Source Code",
#     "https://github.com/ashwathrqf/options-pricing-engine",
# )

# st.sidebar.title("⚙️ Controls")

# # ----------------------------------------------------------
# # Market Data
# # ----------------------------------------------------------


# st.sidebar.subheader("Market")

# ticker = st.sidebar.text_input(
#     "Ticker",
#     value="AAPL",
# ).strip().upper()

# if "ticker" not in st.session_state:
#     st.session_state.ticker = ticker

# if "company" not in st.session_state:
#     st.session_state.company = "Manual Mode"

# if "stock_price" not in st.session_state:
#     st.session_state.stock_price = 100.0

# if "historical_sigma" not in st.session_state:
#     st.session_state.historical_sigma = 0.20

# load_market = st.sidebar.button(
#     "Load Market Data",
#     use_container_width=True,
# )

# if load_market:

#     with st.spinner("Downloading market data..."):

#         st.session_state.ticker = ticker

#         st.session_state.company = _get_company_name(
#             ticker
#         )

#         st.session_state.stock_price = _get_current_price(
#             ticker
#         )

#         st.session_state.historical_sigma = _historical_volatility(
#             ticker,
#             "1y",
#         )

# company = st.session_state.company
# S = st.session_state.stock_price
# historical_sigma = st.session_state.historical_sigma

# st.sidebar.success(
#     f"""
# **Company**

# {company}

# **Current Price**

# ${S:.2f}

# **Historical Volatility**

# {historical_sigma*100:.2f}%
# """
# )

# st.sidebar.divider()

# # ----------------------------------------------------------
# # Option Parameters
# # ----------------------------------------------------------

# st.sidebar.subheader("Option Parameters")

# option_type = st.sidebar.selectbox(
#     "Option Type",
#     [
#         "call",
#         "put",
#     ],
# )

# # ----------------------------------------------------------
# # Option Parameters
# # ----------------------------------------------------------

# K = st.sidebar.slider(
#     "Strike Price",
#     min_value=1,
#     max_value=500,
#     value=int(round(S)),
#     step=1,
# )

# T = st.sidebar.slider(
#     "Time to Expiry (Years)",
#     min_value=0.05,
#     max_value=5.0,
#     value=1.0,
# )

# r = (
#     st.sidebar.slider(
#         "Risk-Free Rate (%)",
#         min_value=0,
#         max_value=20,
#         value=5,
#     )
#     / 100
# )

# st.sidebar.divider()

# # ----------------------------------------------------------
# # Volatility
# # ----------------------------------------------------------

# st.sidebar.subheader("Volatility")

# volatility_source = st.sidebar.radio(
#     "Volatility Source",
#     [
#         "Manual",
#         "Historical",
#     ],
# )

# if volatility_source == "Manual":

#     sigma = (
#         st.sidebar.slider(
#             "Volatility (%)",
#             min_value=1,
#             max_value=100,
#             value=20,
#         )
#         / 100
#     )

# else:

#     sigma = historical_sigma

#     st.sidebar.info(
#         f"Using Historical Volatility\n\n{sigma*100:.2f}%"
#     )

# st.sidebar.divider()

# # ----------------------------------------------------------
# # Numerical Methods
# # ----------------------------------------------------------

# st.sidebar.subheader("Numerical Methods")

# num_simulations = st.sidebar.slider(
#     "Monte Carlo Simulations",
#     min_value=1000,
#     max_value=500000,
#     value=100000,
#     step=1000,
# )

# binomial_steps = st.sidebar.slider(
#     "Binomial Steps",
#     min_value=10,
#     max_value=500,
#     value=100,
# )

# st.sidebar.divider()

# # ----------------------------------------------------------
# # Market Option Chain
# # ----------------------------------------------------------

# expiries = _get_expiries(ticker)

# selected_expiry = st.sidebar.selectbox(
#     "Expiry",
#     expiries,
# )

# available_strikes = _get_available_strikes(
#     ticker,
#     selected_expiry,
#     option_type,
# )

# selected_strike = st.sidebar.selectbox(
#     "Market Strike",
#     available_strikes,
# )

# market_option = _get_option_data(
#     ticker=ticker,
#     expiry=selected_expiry,
#     strike=selected_strike,
#     option_type=option_type,
# )

# market_price = market_option["last_price"]
# market_iv = market_option["implied_volatility"]

# # ==========================================================
# # Pricing Calculations
# # ==========================================================

# with st.spinner("Running pricing models..."):

#     bs_price = price_option_bs(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#     )

#     mc_price = price_option_mc(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#         num_simulations=num_simulations,
#         seed=42,
#     )

#     antithetic_price = price_option_mc_antithetic(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#         num_simulations=num_simulations,
#         seed=42,
#     )

#     binomial_price = price_option_binomial(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#         steps=binomial_steps,
#     )
#     greeks = calculate_greeks(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#     )

#     mc_stats = price_option_mc_statistics(
#         S=S,
#         K=K,
#         T=T,
#         r=r,
#         sigma=sigma,
#         option_type=option_type,
#         num_simulations=num_simulations,
#         seed=42,
#     )

# # ==========================================================
# # Errors
# # ==========================================================

# mc_error = abs(bs_price - mc_price)
# antithetic_error = abs(bs_price - antithetic_price)
# binomial_error = abs(bs_price - binomial_price)
# market_error = abs(bs_price - market_price)

# # ==========================================================
# # Generate Figures (ONLY ONCE)
# # ==========================================================

# payoff_fig = payoff_diagram(
#     strike=K,
#     option_type=option_type,
# )

# convergence = convergence_curve(
#     S=S,
#     K=K,
#     T=T,
#     r=r,
#     sigma=sigma,
#     option_type=option_type,
#     num_simulations=num_simulations,
#     seed=42,
# )

# convergence_fig = convergence_plot(
#     convergence,
#     bs_price,
# )

# option_chain = _get_option_chain(
#     ticker,
#     selected_expiry,
#     option_type,
# )

# smile_fig = volatility_smile(
#     option_chain,
# )

# # ==========================================================
# # Tabs
# # ==========================================================

# pricing_tab, market_tab, greeks_tab, montecarlo_tab = st.tabs(
#     [
#         "📈 Pricing",
#         "🌍 Market Data",
#         "📊 Greeks",
#         "🎲 Monte Carlo",
#     ]
# )

# # ==========================================================
# # PRICING TAB
# # ==========================================================

# with pricing_tab:

#     st.subheader("Pricing Dashboard")

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         st.metric(
#             "Company",
#             company,
#         )

#     with c2:
#         st.metric(
#             "Current Price",
#             f"${S:.2f}",
#         )

#     with c3:
#         st.metric(
#             "Historical Volatility",
#             f"{historical_sigma*100:.2f}%",
#         )

#     with c4:
#         st.metric(
#             "Market IV",
#             f"{market_iv*100:.2f}%",
#         )

#     st.divider()

#     pricing_df = pd.DataFrame(
#         {
#             "Model": [
#                 "Black-Scholes",
#                 "Monte Carlo",
#                 "Antithetic MC",
#                 "Binomial Tree",
#                 "Market",
#             ],
#             "Price": [
#                 round(bs_price, 4),
#                 round(mc_price, 4),
#                 round(antithetic_price, 4),
#                 round(binomial_price, 4),
#                 round(market_price, 4),
#             ],
#             "Error vs BS": [
#                 0.0000,
#                 round(mc_error, 4),
#                 round(antithetic_error, 4),
#                 round(binomial_error, 4),
#                 round(market_error, 4),
#             ],
#         }
#     )

#     st.dataframe(
#         pricing_df,
#         hide_index=True,
#         width="stretch",
#     )

#     st.divider()

#     left, right = st.columns(2)

#     with left:

#         st.subheader("Payoff Diagram")

#         st.plotly_chart(
#             payoff_fig,
#             width="stretch",
#             key="pricing_payoff",
#         )

#     with right:

#         st.subheader("Monte Carlo Convergence")

#         st.plotly_chart(
#             convergence_fig,
#             width="stretch",
#             key="pricing_convergence",
#         )

#     st.divider()

#     st.subheader("Selected Market Contract")

#     m1, m2, m3, m4 = st.columns(4)

#     with m1:
#         st.metric(
#             "Strike",
#             f"${selected_strike:.2f}",
#         )

#     with m2:
#         st.metric(
#             "Last Price",
#             f"${market_option['last_price']:.2f}",
#         )

#     with m3:
#         st.metric(
#             "Bid",
#             f"${market_option['bid']:.2f}",
#         )

#     with m4:
#         st.metric(
#             "Ask",
#             f"${market_option['ask']:.2f}",
#         )

#     m5, m6, m7, m8 = st.columns(4)

#     with m5:
#         st.metric(
#             "Volume",
#             market_option["volume"],
#         )

#     with m6:
#         st.metric(
#             "Open Interest",
#             market_option["open_interest"],
#         )

#     with m7:
#         st.metric(
#             "Implied Volatility",
#             f"{market_iv*100:.2f}%",
#         )

#     with m8:
#         st.metric(
#             "ITM",
#             "Yes" if market_option["in_the_money"] else "No",
#         )

# # ==========================================================
# # MARKET DATA TAB
# # ==========================================================

# with market_tab:

#     st.subheader("Market Overview")

#     c1, c2, c3, c4 = st.columns(4)

#     with c1:
#         st.metric(
#             "Ticker",
#             ticker,
#         )

#     with c2:
#         st.metric(
#             "Company",
#             company,
#         )

#     with c3:
#         st.metric(
#             "Current Price",
#             f"${S:.2f}",
#         )

#     with c4:
#         st.metric(
#             "Historical Volatility",
#             f"{historical_sigma*100:.2f}%",
#         )

#     st.divider()
#     st.subheader("Option Chain")

#     display_columns = [
#         "strike",
#         "lastPrice",
#         "bid",
#         "ask",
#         "volume",
#         "openInterest",
#         "impliedVolatility",
#     ]

#     st.dataframe(
#         option_chain[display_columns],
#         hide_index=True,
#         width="stretch",
#     )

#     st.divider()

#     st.subheader("Volatility Smile")

#     st.plotly_chart(
#         smile_fig,
#         width="stretch",
#         key="volatility_smile",
#     )

# # ==========================================================
# # GREEKS TAB
# # ==========================================================

# with greeks_tab:

#     st.subheader("Option Greeks")

#     g1, g2, g3, g4, g5 = st.columns(5)

#     with g1:
#         st.metric(
#             "Delta",
#             f"{greeks['delta']:.6f}",
#         )

#     with g2:
#         st.metric(
#             "Gamma",
#             f"{greeks['gamma']:.6f}",
#         )

#     with g3:
#         st.metric(
#             "Vega",
#             f"{greeks['vega']:.6f}",
#         )

#     with g4:
#         st.metric(
#             "Theta",
#             f"{greeks['theta']:.6f}",
#         )

#     with g5:
#         st.metric(
#             "Rho",
#             f"{greeks['rho']:.6f}",
#         )

#     st.divider()

#     greeks_df = pd.DataFrame(
#         {
#             "Greek": [
#                 "Delta",
#                 "Gamma",
#                 "Vega",
#                 "Theta",
#                 "Rho",
#             ],
#             "Value": [
#                 round(greeks["delta"], 6),
#                 round(greeks["gamma"], 6),
#                 round(greeks["vega"], 6),
#                 round(greeks["theta"], 6),
#                 round(greeks["rho"], 6),
#             ],
#         }
#     )

#     st.dataframe(
#         greeks_df,
#         hide_index=True,
#         width="stretch",
#     )

#     st.divider()

#     summary1, summary2 = st.columns(2)

#     with summary1:

#         st.info(
# f"""
# Current Inputs

# Stock Price : {S:.2f}

# Strike Price : {K:.2f}

# Volatility : {sigma*100:.2f}%

# Risk Free Rate : {r*100:.2f}%

# Time to Expiry : {T:.2f} Years
# """
#         )

#     with summary2:

#         st.success(
# f"""
# Interpretation

# • Delta measures price sensitivity.

# • Gamma measures delta curvature.

# • Vega measures volatility sensitivity.

# • Theta measures time decay.

# • Rho measures interest-rate sensitivity.
# """
#         )

# # ==========================================================
# # MONTE CARLO TAB
# # ==========================================================

# with montecarlo_tab:

#     st.subheader("Monte Carlo Analytics")
#     mc1, mc2, mc3, mc4 = st.columns(4)

#     with mc1:
#         st.metric(
#             "Standard MC",
#             f"{mc_price:.4f}",
#         )

#     with mc2:
#         st.metric(
#             "Antithetic MC",
#             f"{antithetic_price:.4f}",
#         )

#     with mc3:
#         st.metric(
#             "Std Error",
#             f"{mc_stats['std_error']:.6f}",
#         )

#     with mc4:
#         st.metric(
#             "95% Margin",
#             f"{mc_stats['margin']:.6f}",
#         )

#     st.divider()

#     ci1, ci2, ci3 = st.columns(3)

#     with ci1:
#         st.metric(
#             "95% CI Lower",
#             f"{mc_stats['lower']:.4f}",
#         )

#     with ci2:
#         st.metric(
#             "Estimated Price",
#             f"{mc_stats['price']:.4f}",
#         )

#     with ci3:
#         st.metric(
#             "95% CI Upper",
#             f"{mc_stats['upper']:.4f}",
#         )

#     st.divider()

#     comparison_df = pd.DataFrame(
#         {
#             "Method": [
#                 "Black-Scholes",
#                 "Standard MC",
#                 "Antithetic MC",
#                 "Binomial",
#             ],
#             "Price": [
#                 round(bs_price, 6),
#                 round(mc_price, 6),
#                 round(antithetic_price, 6),
#                 round(binomial_price, 6),
#             ],
#             "Absolute Error": [
#                 0.0,
#                 round(mc_error, 6),
#                 round(antithetic_error, 6),
#                 round(binomial_error, 6),
#             ],
#         }
#     )

#     st.dataframe(
#         comparison_df,
#         hide_index=True,
#         width="stretch",
#     )

#     st.divider()

#     st.plotly_chart(
#         convergence_fig,
#         width="stretch",
#         key="mc_convergence",
#     )

#     st.success(
# f"""
# Simulation Summary

# Simulations
# {num_simulations:,}

# Confidence Level
# {int(mc_stats['confidence']*100)}%

# Estimated Price
# {mc_stats['price']:.4f}

# Confidence Interval

# [{mc_stats['lower']:.4f}, {mc_stats['upper']:.4f}]
# """
#     )

# # ==========================================================
# # FOOTER
# # ==========================================================

# st.divider()

# left, center, right = st.columns(3)

# with left:

#     st.caption(
#         "Developed by Ashwath R"
#     )

# with center:

#     st.caption(
#         "Black-Scholes • Monte Carlo • Binomial Tree"
#     )

# with right:

#     st.caption(
#         "IIT Madras"
#     )

import streamlit as st
import pandas as pd

# ==========================================================
# Pricing Models
# ==========================================================

from pricing.black_scholes import price_option_bs
from pricing.binomial import price_option_binomial

from pricing.monte_carlo import (
    price_option_mc,
    price_option_mc_antithetic,
    price_option_mc_statistics,
    convergence_curve,
)

from pricing.greeks import calculate_greeks
from pricing.historical_volatility import _historical_volatility

# ==========================================================
# Market Data
# ==========================================================

from market_data.yahoo_finance import (
    _get_current_price,
    _get_company_name,
)

from market_data.option_chain import (
    _get_expiries,
    _get_option_chain,
    _get_option_data,
    _get_available_strikes,
)

# ==========================================================
# Visualizations
# ==========================================================

from visualization.payoff import payoff_diagram
from visualization.convergence import convergence_plot
from visualization.volatility_smile import volatility_smile

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="QuantLab",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject custom CSS ──────────────────────────────────────

def _load_css(path: str) -> None:
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

_load_css("style.css")   # keep style.css next to this file

# ── Inject extra HTML (scanline header bar) ────────────────

st.markdown(
    """
    <div style="
        display:flex; align-items:center; gap:0.75rem;
        padding: 0.2rem 0 0.6rem;
        border-bottom: 1px solid rgba(0,212,255,0.12);
        margin-bottom: 1.25rem;
    ">
        <div style="
            font-family:'JetBrains Mono',monospace;
            font-size:1.6rem; font-weight:700;
            background:linear-gradient(90deg,#00D4FF 0%,#7EB9FF 50%,#00FF9D 100%);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent;
            background-clip:text;
            letter-spacing:-0.02em;
        ">📈 QuantLab</div>
        <div style="
            margin-left:auto;
            font-family:'JetBrains Mono',monospace;
            font-size:0.62rem; letter-spacing:0.18em;
            color:#4A5568; text-transform:uppercase;
        ">Professional Options Analytics</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# Sidebar
# ==========================================================

sb = st.sidebar

sb.markdown(
    """
    <div style="
        font-family:'JetBrains Mono',monospace;
        font-size:0.62rem; letter-spacing:0.2em; color:#4A5568;
        text-transform:uppercase; padding:0.5rem 0 1rem;
        border-bottom:1px solid rgba(0,212,255,0.1);
    ">⚙️ &nbsp;Controls</div>
    """,
    unsafe_allow_html=True,
)

# ── Market ─────────────────────────────────────────────────

sb.markdown(
    "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
    "letter-spacing:0.16em;text-transform:uppercase;color:#00D4FF;"
    "margin:1rem 0 0.3rem;'>Market</p>",
    unsafe_allow_html=True,
)

ticker = sb.text_input("Ticker", value="AAPL").strip().upper()

if "ticker" not in st.session_state:
    st.session_state.ticker = ticker
if "company" not in st.session_state:
    st.session_state.company = "Manual Mode"
if "stock_price" not in st.session_state:
    st.session_state.stock_price = 100.0
if "historical_sigma" not in st.session_state:
    st.session_state.historical_sigma = 0.20

load_market = sb.button("⬇  Load Market Data", use_container_width=True)

if load_market:
    with st.spinner("Fetching live data…"):
        st.session_state.ticker          = ticker
        st.session_state.company         = _get_company_name(ticker)
        st.session_state.stock_price     = _get_current_price(ticker)
        st.session_state.historical_sigma = _historical_volatility(ticker, "1y")

company          = st.session_state.company
S                = st.session_state.stock_price
historical_sigma = st.session_state.historical_sigma

sb.markdown(
    f"""
    <div style="
        background:rgba(0,255,157,0.04);
        border:1px solid rgba(0,255,157,0.16);
        border-radius:8px; padding:0.85rem 1rem; margin:0.5rem 0 1rem;
        font-family:'JetBrains Mono',monospace; font-size:0.75rem;
        line-height:2;
    ">
        <span style="color:#4A5568;letter-spacing:0.1em;font-size:0.62rem;">
            COMPANY
        </span><br>
        <span style="color:#E8EDF5;">{company}</span><br>
        <span style="color:#4A5568;letter-spacing:0.1em;font-size:0.62rem;">
            SPOT PRICE
        </span><br>
        <span style="color:#00FF9D;font-weight:600;">${S:.2f}</span><br>
        <span style="color:#4A5568;letter-spacing:0.1em;font-size:0.62rem;">
            HIST. VOL (1Y)
        </span><br>
        <span style="color:#FFB547;font-weight:600;">{historical_sigma*100:.2f}%</span>
    </div>
    """,
    unsafe_allow_html=True,
)

sb.divider()

# ── Option Parameters ──────────────────────────────────────

sb.markdown(
    "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
    "letter-spacing:0.16em;text-transform:uppercase;color:#00D4FF;margin:0 0 0.3rem;'>"
    "Option Parameters</p>",
    unsafe_allow_html=True,
)

option_type = sb.selectbox("Type", ["call", "put"])

K = sb.slider("Strike Price",          min_value=1,    max_value=500,    value=int(round(S)), step=1)
T = sb.slider("Time to Expiry (yrs)",  min_value=0.05, max_value=5.0,    value=1.0)
r = sb.slider("Risk-Free Rate (%)",    min_value=0,    max_value=20,     value=5) / 100

sb.divider()

# ── Volatility ─────────────────────────────────────────────

sb.markdown(
    "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
    "letter-spacing:0.16em;text-transform:uppercase;color:#00D4FF;margin:0 0 0.3rem;'>"
    "Volatility</p>",
    unsafe_allow_html=True,
)

volatility_source = sb.radio("Source", ["Manual", "Historical"])

if volatility_source == "Manual":
    sigma = sb.slider("Volatility (%)", min_value=1, max_value=100, value=20) / 100
else:
    sigma = historical_sigma
    sb.info(f"Using Historical Vol\n\n**{sigma*100:.2f}%**")

sb.divider()

# ── Numerical Methods ──────────────────────────────────────

sb.markdown(
    "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
    "letter-spacing:0.16em;text-transform:uppercase;color:#00D4FF;margin:0 0 0.3rem;'>"
    "Numerical Methods</p>",
    unsafe_allow_html=True,
)

num_simulations = sb.slider("MC Simulations",  min_value=1000,  max_value=500000, value=100000, step=1000)
binomial_steps  = sb.slider("Binomial Steps",  min_value=10,    max_value=500,    value=100)

sb.divider()

# ── Option Chain ───────────────────────────────────────────

sb.markdown(
    "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
    "letter-spacing:0.16em;text-transform:uppercase;color:#00D4FF;margin:0 0 0.3rem;'>"
    "Market Chain</p>",
    unsafe_allow_html=True,
)

expiries          = _get_expiries(ticker)
selected_expiry   = sb.selectbox("Expiry", expiries)
available_strikes = _get_available_strikes(ticker, selected_expiry, option_type)
selected_strike   = sb.selectbox("Strike", available_strikes)

market_option = _get_option_data(
    ticker=ticker,
    expiry=selected_expiry,
    strike=selected_strike,
    option_type=option_type,
)

market_price = market_option["last_price"]
market_iv    = market_option["implied_volatility"]

sb.divider()

sb.markdown(
    """
    <div style="text-align:center;padding:0.5rem 0;">
        <a href="https://github.com/ashwathrqf/options-pricing-engine"
           target="_blank"
           style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;
                  letter-spacing:0.1em;color:#4A5568;text-decoration:none;">
            ⭐ &nbsp;Source Code
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================================
# Pricing Calculations
# ==========================================================

with st.spinner("Running pricing models…"):

    bs_price = price_option_bs(S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type)

    mc_price = price_option_mc(
        S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type,
        num_simulations=num_simulations, seed=42,
    )

    antithetic_price = price_option_mc_antithetic(
        S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type,
        num_simulations=num_simulations, seed=42,
    )

    binomial_price = price_option_binomial(
        S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type,
        steps=binomial_steps,
    )

    greeks = calculate_greeks(S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type)

    mc_stats = price_option_mc_statistics(
        S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type,
        num_simulations=num_simulations, seed=42,
    )

# Errors
mc_error         = abs(bs_price - mc_price)
antithetic_error = abs(bs_price - antithetic_price)
binomial_error   = abs(bs_price - binomial_price)
market_error     = abs(bs_price - market_price)

# ==========================================================
# Figures
# ==========================================================

payoff_fig = payoff_diagram(strike=K, option_type=option_type)

convergence = convergence_curve(
    S=S, K=K, T=T, r=r, sigma=sigma,
    option_type=option_type, num_simulations=num_simulations, seed=42,
)
convergence_fig = convergence_plot(convergence, bs_price)

option_chain = _get_option_chain(ticker, selected_expiry, option_type)
smile_fig    = volatility_smile(option_chain)

# apply a shared dark layout to all plotly figures
_plotly_layout = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(12,18,32,0.6)",
    font_family="'JetBrains Mono', monospace",
    font_color="#8892A4",
    title_font_color="#E8EDF5",
    xaxis=dict(gridcolor="rgba(0,212,255,0.06)", linecolor="rgba(0,212,255,0.12)"),
    yaxis=dict(gridcolor="rgba(0,212,255,0.06)", linecolor="rgba(0,212,255,0.12)"),
    margin=dict(l=40, r=20, t=48, b=40),
)
for _fig in (payoff_fig, convergence_fig, smile_fig):
    try:
        _fig.update_layout(**_plotly_layout)
    except Exception:
        pass

# ==========================================================
# HELPER: coloured HTML metric card (used inline)
# ==========================================================

def _stat_card(label: str, value: str, color: str = "#E8EDF5", sub: str = "") -> str:
    sub_html = (
        f"<div style='font-size:0.65rem;color:#4A5568;"
        f"margin-top:2px;'>{sub}</div>"
        if sub else ""
    )
    return (
        f"<div style='"
        f"background:#0C1220;border:1px solid rgba(0,212,255,0.12);"
        f"border-radius:12px;padding:0.9rem 1.1rem;"
        f"font-family:\"JetBrains Mono\",monospace;'>"
        f"<div style='font-size:0.6rem;letter-spacing:0.16em;"
        f"text-transform:uppercase;color:#4A5568;margin-bottom:4px;'>{label}</div>"
        f"<div style='font-size:1.2rem;font-weight:600;color:{color};'>{value}</div>"
        f"{sub_html}"
        f"</div>"
    )

# ==========================================================
# TABS
# ==========================================================

pricing_tab, market_tab, greeks_tab, montecarlo_tab = st.tabs([
    "📈  Pricing",
    "🌍  Market Data",
    "📊  Greeks",
    "🎲  Monte Carlo",
])

# ==========================================================
# ── PRICING TAB ───────────────────────────────────────────
# ==========================================================

with pricing_tab:

    # ── Top headline row ───────────────────────────────────
    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Live Snapshot</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Company",            company)
    with c2: st.metric("Spot Price",         f"${S:.2f}")
    with c3: st.metric("Historical Vol",     f"{historical_sigma*100:.2f}%")
    with c4: st.metric("Market IV",          f"{market_iv*100:.2f}%")

    st.divider()

    # ── Pricing comparison table ───────────────────────────
    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Model Comparison</p>",
        unsafe_allow_html=True,
    )

    pricing_df = pd.DataFrame({
        "Model":       ["Black-Scholes", "Monte Carlo", "Antithetic MC", "Binomial Tree", "Market"],
        "Price ($)":   [round(bs_price,4), round(mc_price,4), round(antithetic_price,4),
                        round(binomial_price,4), round(market_price,4)],
        "Δ vs BS ($)": [0.0000, round(mc_error,4), round(antithetic_error,4),
                        round(binomial_error,4), round(market_error,4)],
    })

    st.dataframe(pricing_df, hide_index=True, use_container_width=True)

    st.divider()

    # ── Charts ─────────────────────────────────────────────
    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Analytics</p>",
        unsafe_allow_html=True,
    )

    left, right = st.columns(2)

    with left:
        st.markdown(
            "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.68rem;"
            "color:#8892A4;letter-spacing:0.08em;margin-bottom:0.4rem;'>"
            "PAYOFF DIAGRAM</p>",
            unsafe_allow_html=True,
        )
        st.plotly_chart(payoff_fig, use_container_width=True, key="pricing_payoff")

    with right:
        st.markdown(
            "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.68rem;"
            "color:#8892A4;letter-spacing:0.08em;margin-bottom:0.4rem;'>"
            "MC CONVERGENCE</p>",
            unsafe_allow_html=True,
        )
        st.plotly_chart(convergence_fig, use_container_width=True, key="pricing_convergence")

    st.divider()

    # ── Selected contract ──────────────────────────────────
    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Selected Market Contract</p>",
        unsafe_allow_html=True,
    )

    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Strike",     f"${selected_strike:.2f}")
    with m2: st.metric("Last Price", f"${market_option['last_price']:.2f}")
    with m3: st.metric("Bid",        f"${market_option['bid']:.2f}")
    with m4: st.metric("Ask",        f"${market_option['ask']:.2f}")

    m5, m6, m7, m8 = st.columns(4)
    with m5: st.metric("Volume",           market_option["volume"])
    with m6: st.metric("Open Interest",    market_option["open_interest"])
    with m7: st.metric("Implied Vol",      f"{market_iv*100:.2f}%")
    with m8: st.metric("In The Money",     "Yes" if market_option["in_the_money"] else "No")


# ==========================================================
# ── MARKET DATA TAB ──────────────────────────────────────
# ==========================================================

with market_tab:

    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Market Overview</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Ticker",           ticker)
    with c2: st.metric("Company",          company)
    with c3: st.metric("Spot Price",       f"${S:.2f}")
    with c4: st.metric("Historical Vol",   f"{historical_sigma*100:.2f}%")

    st.divider()

    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Option Chain</p>",
        unsafe_allow_html=True,
    )

    display_columns = ["strike","lastPrice","bid","ask","volume","openInterest","impliedVolatility"]
    st.dataframe(option_chain[display_columns], hide_index=True, use_container_width=True)

    st.divider()

    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Volatility Smile</p>",
        unsafe_allow_html=True,
    )

    st.plotly_chart(smile_fig, use_container_width=True, key="volatility_smile")


# ==========================================================
# ── GREEKS TAB ───────────────────────────────────────────
# ==========================================================

with greeks_tab:

    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Option Greeks</p>",
        unsafe_allow_html=True,
    )

    # Glowing greek cards via HTML
    greek_colors = {
        "Delta": "#00D4FF",
        "Gamma": "#00FF9D",
        "Vega":  "#7C3AED",
        "Theta": "#FF4D6D",
        "Rho":   "#FFB547",
    }
    greek_desc = {
        "Delta": "Price sensitivity",
        "Gamma": "Delta curvature",
        "Vega":  "Vol sensitivity",
        "Theta": "Time decay",
        "Rho":   "Rate sensitivity",
    }

    cols = st.columns(5)
    greek_keys = ["delta","gamma","vega","theta","rho"]
    greek_names = ["Delta","Gamma","Vega","Theta","Rho"]

    for col, name, key in zip(cols, greek_names, greek_keys):
        color = greek_colors[name]
        with col:
            st.markdown(
                f"""
                <div style="
                    background:#0C1220;
                    border:1px solid {color}22;
                    border-top:2px solid {color};
                    border-radius:12px;
                    padding:1.1rem 1rem 0.9rem;
                    text-align:center;
                    box-shadow: 0 0 20px {color}0D;
                ">
                    <div style="font-family:'JetBrains Mono',monospace;
                                font-size:0.58rem;letter-spacing:0.18em;
                                text-transform:uppercase;color:#4A5568;margin-bottom:6px;">
                        {name}
                    </div>
                    <div style="font-family:'JetBrains Mono',monospace;
                                font-size:1.3rem;font-weight:600;color:{color};">
                        {greeks[key]:.6f}
                    </div>
                    <div style="font-family:'JetBrains Mono',monospace;
                                font-size:0.6rem;color:#4A5568;margin-top:4px;">
                        {greek_desc[name]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    left, right = st.columns([3, 2])

    with left:
        greeks_df = pd.DataFrame({
            "Greek": greek_names,
            "Value": [round(greeks[k], 6) for k in greek_keys],
        })
        st.dataframe(greeks_df, hide_index=True, use_container_width=True)

    with right:
        st.markdown(
            f"""
            <div style="
                background:rgba(0,212,255,0.04);
                border:1px solid rgba(0,212,255,0.15);
                border-radius:12px; padding:1.2rem 1.4rem;
                font-family:'JetBrains Mono',monospace;
                font-size:0.75rem; line-height:2;
            ">
                <div style="font-size:0.58rem;letter-spacing:0.16em;
                            text-transform:uppercase;color:#4A5568;
                            margin-bottom:0.6rem;">Input Summary</div>
                <span style="color:#4A5568;">Spot </span>
                <span style="color:#E8EDF5;">${S:.2f}</span><br>
                <span style="color:#4A5568;">Strike </span>
                <span style="color:#E8EDF5;">${K:.2f}</span><br>
                <span style="color:#4A5568;">Vol </span>
                <span style="color:#FFB547;">{sigma*100:.2f}%</span><br>
                <span style="color:#4A5568;">Rate </span>
                <span style="color:#E8EDF5;">{r*100:.2f}%</span><br>
                <span style="color:#4A5568;">Expiry </span>
                <span style="color:#E8EDF5;">{T:.2f} yrs</span><br>
                <span style="color:#4A5568;">Type </span>
                <span style="color:#00D4FF;text-transform:uppercase;font-weight:600;">{option_type}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==========================================================
# ── MONTE CARLO TAB ──────────────────────────────────────
# ==========================================================

with montecarlo_tab:

    st.markdown(
        "<p style='font-family:\"JetBrains Mono\",monospace;font-size:0.62rem;"
        "letter-spacing:0.2em;text-transform:uppercase;color:#00D4FF;"
        "border-left:2px solid #00D4FF;padding-left:0.6rem;"
        "background:rgba(0,212,255,0.04);border-radius:0 6px 6px 0;"
        "margin-bottom:1rem;'>Monte Carlo Analytics</p>",
        unsafe_allow_html=True,
    )

    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1: st.metric("Standard MC",    f"${mc_price:.4f}")
    with mc2: st.metric("Antithetic MC",  f"${antithetic_price:.4f}")
    with mc3: st.metric("Std Error",      f"{mc_stats['std_error']:.6f}")
    with mc4: st.metric("95% Margin",     f"{mc_stats['margin']:.6f}")

    st.divider()

    # Confidence interval visual
    ci1, ci2, ci3 = st.columns(3)
    with ci1: st.metric("95% CI Lower",   f"${mc_stats['lower']:.4f}")
    with ci2: st.metric("Estimated Price",f"${mc_stats['price']:.4f}")
    with ci3: st.metric("95% CI Upper",   f"${mc_stats['upper']:.4f}")

    st.divider()

    comparison_df = pd.DataFrame({
        "Method": ["Black-Scholes","Standard MC","Antithetic MC","Binomial"],
        "Price ($)": [round(bs_price,6), round(mc_price,6),
                      round(antithetic_price,6), round(binomial_price,6)],
        "Abs Error": [0.0, round(mc_error,6),
                      round(antithetic_error,6), round(binomial_error,6)],
    })
    st.dataframe(comparison_df, hide_index=True, use_container_width=True)

    st.divider()

    st.plotly_chart(convergence_fig, use_container_width=True, key="mc_convergence")

    # Summary card
    st.markdown(
        f"""
        <div style="
            display:grid; grid-template-columns: repeat(4, 1fr); gap: 1rem;
            background:#0C1220; border:1px solid rgba(0,255,157,0.15);
            border-radius:14px; padding:1.4rem 1.6rem;
            font-family:'JetBrains Mono',monospace;
        ">
            <div>
                <div style="font-size:0.58rem;letter-spacing:0.16em;
                            text-transform:uppercase;color:#4A5568;margin-bottom:4px;">
                    Simulations
                </div>
                <div style="font-size:1rem;font-weight:600;color:#00FF9D;">
                    {num_simulations:,}
                </div>
            </div>
            <div>
                <div style="font-size:0.58rem;letter-spacing:0.16em;
                            text-transform:uppercase;color:#4A5568;margin-bottom:4px;">
                    Confidence
                </div>
                <div style="font-size:1rem;font-weight:600;color:#00D4FF;">
                    {int(mc_stats['confidence']*100)}%
                </div>
            </div>
            <div>
                <div style="font-size:0.58rem;letter-spacing:0.16em;
                            text-transform:uppercase;color:#4A5568;margin-bottom:4px;">
                    Est. Price
                </div>
                <div style="font-size:1rem;font-weight:600;color:#E8EDF5;">
                    ${mc_stats['price']:.4f}
                </div>
            </div>
            <div>
                <div style="font-size:0.58rem;letter-spacing:0.16em;
                            text-transform:uppercase;color:#4A5568;margin-bottom:4px;">
                    95% Interval
                </div>
                <div style="font-size:0.85rem;font-weight:600;color:#FFB547;">
                    [{mc_stats['lower']:.4f},&nbsp;{mc_stats['upper']:.4f}]
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<div style='margin-top:3rem;'></div>", unsafe_allow_html=True)
st.divider()

left, center, right = st.columns(3)

with left:
    st.caption("Developed by Ashwath R  ·  IIT Madras")

with center:
    st.caption("Black-Scholes · Monte Carlo · Binomial Tree")

with right:
    st.caption("Data via Yahoo Finance")