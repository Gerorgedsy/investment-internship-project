import numpy as np
import pandas as pd


def calculate_risk_metrics(
    result: pd.DataFrame,
    value_column: str,
    annual_risk_free_rate: float = 0.02
) -> dict:
    """
    Calculate maximum drawdown, annualized volatility,
    and annualized Sharpe ratio from monthly portfolio values.
    """

    portfolio_values = result[value_column].dropna()

    if len(portfolio_values) < 2:
        raise ValueError("Not enough portfolio values to calculate risk metrics.")

    # Monthly portfolio returns.
    monthly_returns = portfolio_values.pct_change().dropna()

    # Annualized volatility.
    annualized_volatility = monthly_returns.std() * np.sqrt(12)

    # Convert annual risk-free rate to a monthly rate.
    monthly_risk_free_rate = (
        (1 + annual_risk_free_rate) ** (1 / 12)
        - 1
    )

    # Monthly excess returns.
    excess_returns = monthly_returns - monthly_risk_free_rate

    # Annualized Sharpe ratio.
    if monthly_returns.std() == 0:
        sharpe_ratio = np.nan
    else:
        sharpe_ratio = (
            excess_returns.mean()
            / monthly_returns.std()
            * np.sqrt(12)
        )

    # Maximum drawdown.
    running_peak = portfolio_values.cummax()
    drawdown = (
        portfolio_values - running_peak
    ) / running_peak

    maximum_drawdown = drawdown.min()

    return {
        "Maximum Drawdown": maximum_drawdown,
        "Volatility": annualized_volatility,
        "Sharpe Ratio": sharpe_ratio
    }

if __name__ == "__main__":
    from fetch_data import fetch_qqq_data
    from preprocess import preprocess_data
    from strategies import dca_strategy, momentum_strategy

    daily_data = fetch_qqq_data()
    monthly_data = preprocess_data(daily_data)

    dca_result = dca_strategy(monthly_data)
    momentum_result = momentum_strategy(monthly_data)

    dca_risk = calculate_risk_metrics(
        dca_result,
        "DCA_Portfolio_Value"
    )

    momentum_risk = calculate_risk_metrics(
        momentum_result,
        "Momentum_Portfolio_Value"
    )

    print("DCA Risk Metrics:")
    for name, value in dca_risk.items():
        if name == "Sharpe Ratio":
            print(f"{name}: {value:.2f}")
        else:
            print(f"{name}: {value:.2%}")

    print("\nMomentum Risk Metrics:")
    for name, value in momentum_risk.items():
        if name == "Sharpe Ratio":
            print(f"{name}: {value:.2f}")
        else:
            print(f"{name}: {value:.2%}")