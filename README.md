# 📈 QuantLab – Options Pricing & Analytics Platform

A professional quantitative finance platform for pricing European options, analyzing risk, and visualizing market data.

QuantLab implements multiple pricing models, Greeks, implied volatility estimation, Monte Carlo simulation, and live market data integration through an interactive Streamlit dashboard.

---

## Features

### Pricing Models

- Black-Scholes Analytical Model
- Monte Carlo Simulation
- Antithetic Variates Monte Carlo
- Binomial Tree Model

---

### Risk Analytics

- Delta
- Gamma
- Vega
- Theta
- Rho

---

### Volatility Analytics

- Historical Volatility
- Implied Volatility (Newton-Raphson)
- Volatility Smile

---

### Monte Carlo Analytics

- Standard Monte Carlo Pricing
- Antithetic Variance Reduction
- Confidence Intervals
- Standard Error
- Margin of Error
- Convergence Visualization

---

### Live Market Data

- Yahoo Finance Integration
- Live Stock Prices
- Option Chain Explorer
- Expiry Selection
- Strike Selection
- Bid / Ask Prices
- Volume
- Open Interest
- Market Implied Volatility

---

### Interactive Dashboard

- Streamlit UI
- Plotly Visualizations
- Payoff Diagram
- Monte Carlo Convergence Plot
- Volatility Smile
- Pricing Comparison Dashboard
- Greeks Dashboard

---

# Project Structure

```
QuantLab/

│
├── pricing/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   ├── binomial.py
│   ├── greeks.py
│   ├── implied_volatility.py
│   └── historical_volatility.py
│
├── market_data/
│   ├── yahoo_finance.py
│   └── option_chain.py
│
├── visualization/
│   ├── payoff.py
│   ├── convergence.py
│   └── volatility_smile.py
│
├── tests/
│
├── streamlit_app.py
│
├── requirements.txt
│
├── LICENSE
│
└── README.md
```

---

# Models Implemented

## Black-Scholes Model

Analytical pricing model for European call and put options.

Implemented:

- Input Validation
- d₁ / d₂ Computation
- Call Pricing
- Put Pricing

---

## Monte Carlo Simulation

Risk-neutral simulation of stock price paths.

Features:

- Vectorized NumPy Simulation
- Confidence Intervals
- Standard Error
- Running Convergence
- Antithetic Variance Reduction

---

## Binomial Tree Model

Discrete-time pricing model using backward induction.

Features:

- Cox-Ross-Rubinstein Tree
- Risk-Neutral Probabilities
- Backward Induction
- European Calls & Puts

---

## Greeks

Implemented analytically from Black-Scholes.

- Delta
- Gamma
- Vega
- Theta
- Rho

---

## Implied Volatility

Uses Newton-Raphson iteration to recover implied volatility from market option prices.

---

## Historical Volatility

Calculated from historical log returns using Yahoo Finance market data.

---

# Dashboard

The Streamlit dashboard allows users to:

- Select any stock ticker
- Download live market data
- Choose expiry and strike
- Compare pricing models
- View Greeks
- Analyze volatility
- Explore option chains
- Visualize payoff diagrams
- Observe Monte Carlo convergence

---

# Technologies Used

- Python
- NumPy
- SciPy
- Pandas
- Plotly
- Streamlit
- yFinance

---

# Installation

Clone the repository

```bash
git clone https://github.com/ashwathrqf/options-pricing-engine.git

cd options-pricing-engine
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

# Example

Input

```
Stock Price = 100

Strike Price = 100

Time = 1 Year

Risk-Free Rate = 5%

Volatility = 20%
```

Output

```
Black-Scholes Price

Monte Carlo Price

Binomial Tree Price

Greeks

Confidence Interval

Historical Volatility

Market Implied Volatility
```

---

# Future Improvements

- American Option Pricing
- Asian Options
- Barrier Options
- Heston Stochastic Volatility Model
- Local Volatility Model
- GPU-Accelerated Monte Carlo
- Multi-Asset Options
- Portfolio Greeks
- Real-Time Market Streaming
- Volatility Surface
- SABR Calibration

---

# License

This project is licensed under the MIT License.

---

# Author

**Ashwath R**

B.Tech Mechanical Engineering

Indian Institute of Technology Madras

Interested in Quantitative Finance, Machine Learning, and Scientific Computing.

---

## Preview

Professional options analytics platform featuring:

- Analytical Pricing
- Numerical Pricing
- Risk Analytics
- Live Market Data
- Interactive Financial Visualizations