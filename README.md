# 📈 Options Pricing Engine

An interactive quantitative finance toolkit for pricing European options, analyzing risk sensitivities (Greeks), and comparing analytical and simulation-based pricing models through a modern Streamlit dashboard.

---

## Features

### Black-Scholes Pricing

* Analytical pricing of European Call and Put options
* Input validation
* Fast closed-form solution

### Monte Carlo Pricing

* Geometric Brownian Motion (GBM) stock price simulation
* Configurable number of simulations
* Reproducible simulations using random seeds
* Convergence analysis support

### Greeks

Computes the five primary option Greeks:

* **Delta (Δ)** – Sensitivity to stock price
* **Gamma (Γ)** – Rate of change of Delta
* **Vega (ν)** – Sensitivity to volatility
* **Theta (Θ)** – Time decay
* **Rho (ρ)** – Sensitivity to interest rate

### Interactive Dashboard

Built using **Streamlit**, featuring:

* Adjustable market parameters
* Black-Scholes pricing
* Monte Carlo pricing
* Pricing error comparison
* Greeks display
* Interactive payoff diagram
* Monte Carlo convergence visualization

---

## Project Structure

```
options-pricing-engine/

├── pricing/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   ├── greeks.py
│   └── __init__.py
│
├── visualization/
│   ├── payoff.py
│   ├── convergence.py
│   └── __init__.py
│
├── tests/
│   ├── test_black_scholes.py
│   ├── test_monte_carlo.py
│   └── test_greeks.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Mathematical Models

### Black-Scholes Model

The analytical pricing model assumes:

* Geometric Brownian Motion
* Constant volatility
* Constant risk-free interest rate
* European exercise
* No dividends
* Frictionless markets

---

### Monte Carlo Simulation

The simulation engine:

* Generates normally distributed random variables
* Simulates terminal asset prices using GBM
* Computes discounted expected option payoff
* Supports convergence analysis

---

### Greeks

Risk metrics are calculated directly from the Black-Scholes model using analytical formulas.

---

## Technologies Used

* Python
* NumPy
* SciPy
* Plotly
* Streamlit
* Pandas

---

## Running the Dashboard

Install the dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run streamlit_app.py
```

---

## Current Progress

* ✅ Black-Scholes Pricing
* ✅ Monte Carlo Pricing
* ✅ Greeks Calculation
* ✅ Interactive Streamlit Dashboard
* ✅ Payoff Visualization
* ✅ Monte Carlo Convergence Visualization

---

## Planned Features

* Binomial Tree Pricing
* Implied Volatility Solver
* American Option Pricing
* Asian Options
* Barrier Options
* Variance Reduction Techniques
* Option Price Heatmaps
* Greeks Sensitivity Plots
* Live Market Data Integration
* Portfolio Analytics

---

## Learning Objectives

This project is designed to strengthen understanding of:

* Quantitative Finance
* Option Pricing Theory
* Numerical Methods
* Monte Carlo Simulation
* Financial Risk Analysis
* Scientific Computing in Python
* Interactive Data Visualization

---

## License

This project is released under the MIT License.
