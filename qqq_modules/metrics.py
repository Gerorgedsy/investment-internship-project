import numpy as np


def calculate_returns(dca_results, momentum_results, years=10):
    # ----- DCA -----
    dca_total_return = (
        dca_results["final_value"] - dca_results["invested"]
    ) / dca_results["invested"]

    dca_annualized_return = (
        dca_results["final_value"] / dca_results["invested"]
    ) ** (1 / years) - 1

    # ----- Momentum -----
    momentum_total_return = (
        momentum_results["final_value"] - momentum_results["total_invested"]
    ) / momentum_results["total_invested"]

    momentum_annualized_return = (
        momentum_results["final_value"] / momentum_results["total_invested"]
    ) ** (1 / years) - 1

    print("\n========== Return Comparison ==========")

    print("\nDCA Strategy:")
    print(f"Total Return: {dca_total_return:.2%}")
    print(f"Annualized Return: {dca_annualized_return:.2%}")

    print("\nMomentum Strategy:")
    print(f"Total Return: {momentum_total_return:.2%}")
    print(f"Annualized Return: {momentum_annualized_return:.2%}")

    return {
        "dca_total_return": dca_total_return,
        "dca_annualized_return": dca_annualized_return,
        "momentum_total_return": momentum_total_return,
        "momentum_annualized_return": momentum_annualized_return,
    }


def calculate_max_drawdown_from_returns(strategy_returns):
    cumulative_value = (1 + strategy_returns).cumprod()
    running_max = cumulative_value.cummax()
    drawdown = cumulative_value / running_max - 1
    return drawdown.min()


def calculate_risk_assessment(monthly_data, positions, risk_free_rate=0):
    # Calculate QQQ monthly returns
    qqq_monthly_returns = monthly_data.pct_change().dropna()

    # DCA is always fully invested in QQQ,
    # so its strategy return is QQQ's monthly return
    dca_strategy_returns = qqq_monthly_returns.copy()

    # Momentum strategy:
    # position = 1 -> invested in QQQ
    # position = 0 -> cash
    momentum_strategy_returns = (
        qqq_monthly_returns
        * positions.shift(1).reindex(qqq_monthly_returns.index).fillna(0)
    )

    # Annualized volatility
    dca_volatility = dca_strategy_returns.std() * np.sqrt(12)
    momentum_volatility = momentum_strategy_returns.std() * np.sqrt(12)

    # Annualized Sharpe Ratio
    dca_sharpe_ratio = (
        dca_strategy_returns.mean() * 12 - risk_free_rate
    ) / dca_volatility

    momentum_sharpe_ratio = (
        momentum_strategy_returns.mean() * 12 - risk_free_rate
    ) / momentum_volatility

    dca_max_drawdown = calculate_max_drawdown_from_returns(
        dca_strategy_returns
    )

    momentum_max_drawdown = calculate_max_drawdown_from_returns(
        momentum_strategy_returns
    )

    print("\n========== Risk Assessment ==========")

    print("\nDCA Strategy:")
    print(f"Annualized Volatility: {dca_volatility:.2%}")
    print(f"Sharpe Ratio: {dca_sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {dca_max_drawdown:.2%}")

    print("\nMomentum Strategy:")
    print(f"Annualized Volatility: {momentum_volatility:.2%}")
    print(f"Sharpe Ratio: {momentum_sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {momentum_max_drawdown:.2%}")

    return {
        "qqq_monthly_returns": qqq_monthly_returns,
        "dca_strategy_returns": dca_strategy_returns,
        "momentum_strategy_returns": momentum_strategy_returns,
        "dca_volatility": dca_volatility,
        "momentum_volatility": momentum_volatility,
        "dca_sharpe_ratio": dca_sharpe_ratio,
        "momentum_sharpe_ratio": momentum_sharpe_ratio,
        "dca_max_drawdown": dca_max_drawdown,
        "momentum_max_drawdown": momentum_max_drawdown,
    }
