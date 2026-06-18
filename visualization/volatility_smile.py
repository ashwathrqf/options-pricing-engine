import plotly.graph_objects as go


def volatility_smile(option_chain):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=option_chain["strike"],
            y=option_chain["impliedVolatility"] * 100,
            mode="lines+markers",
            name="IV",
        )
    )

    fig.update_layout(
        title="Volatility Smile",
        xaxis_title="Strike Price",
        yaxis_title="Implied Volatility (%)",
        template="plotly_dark",
        height=500,
    )

    return fig