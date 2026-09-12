import pandas as pd


def calculate_metrics(
    result: pd.DataFrame,
    invested_column: str,
    value_column: str
) -> dict:
    """
    Calculate total return and annualized return.
    """

    total_invested = result[invested_column].iloc[-1]
    final_value = result[value_column].iloc[-1]

    total_return = (
        final_value - total_invested
    ) / total_invested

    number_of_months = len(result)
    number_of_years = number_of_months / 12

    annualized_return = (
        final_value / total_invested
    ) ** (1 / number_of_years) - 1

    return {
        "Total Invested": total_invested,
        "Final Value": final_value,
        "Total Return": total_return,
        "Annualized Return": annualized_return
    }

if __name__ == "__main__":
    from fetch_data import fetch_qqq_data
    from preprocess import preprocess_data
    from strategies import dca_strategy, momentum_strategy

    daily_data = fetch_qqq_data()
    monthly_data = preprocess_data(daily_data)

    dca_result = dca_strategy(monthly_data)
    momentum_result = momentum_strategy(monthly_data)

    dca_metrics = calculate_metrics(
        dca_result,
        "DCA_Total_Invested",
        "DCA_Portfolio_Value"
    )

    momentum_metrics = calculate_metrics(
        momentum_result,
        "Momentum_Total_Invested",
        "Momentum_Portfolio_Value"
    )

    print("DCA Metrics:")
    for name, value in dca_metrics.items():
        if "Return" in name:
            print(f"{name}: {value:.2%}")
        else:
            print(f"{name}: ${value:,.2f}")

    print("\nMomentum Metrics:")
    for name, value in momentum_metrics.items():
        if "Return" in name:
            print(f"{name}: {value:.2%}")
        else:
            print(f"{name}: ${value:,.2f}")