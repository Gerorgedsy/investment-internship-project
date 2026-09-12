from fetch_data import fetch_qqq_data
from preprocess import preprocess_data
from strategies import dca_strategy, momentum_strategy
from metrics import calculate_metrics
from risk_metrics import calculate_risk_metrics
from plot_results import plot_strategy_comparison

import os
import pandas as pd


def main():

    print("Step 1: Fetching data...")
    data = fetch_qqq_data()


    print("Step 2: Preprocessing data...")
    monthly_data = preprocess_data(data)


    print("Step 3: Running strategies...")
    dca_result = dca_strategy(monthly_data)

    momentum_result = momentum_strategy(monthly_data)


    print("Step 4: Calculating performance metrics...")

    dca_metrics = calculate_metrics(
        dca_result,
        invested_column="DCA_Total_Invested",
        value_column="DCA_Portfolio_Value"
    )

    momentum_metrics = calculate_metrics(
        momentum_result,
        invested_column="Momentum_Total_Invested",
        value_column="Momentum_Portfolio_Value"
    )


    print("Step 5: Calculating risk metrics...")

    dca_risk = calculate_risk_metrics(
        dca_result,
        "DCA_Portfolio_Value"
    )

    momentum_risk = calculate_risk_metrics(
        momentum_result,
        "Momentum_Portfolio_Value"
    )


    print("Step 6: Creating plot...")

    plot_strategy_comparison(
        dca_result,
        momentum_result
    )


    print("Step 7: Saving results...")


    os.makedirs("output", exist_ok=True)


    results = pd.DataFrame({

        "Strategy":
        [
            "DCA",
            "Momentum"
        ],

        "Final Value":
        [
            dca_metrics["Final Value"],
            momentum_metrics["Final Value"]
        ],

        "Total Return":
        [
            dca_metrics["Total Return"],
            momentum_metrics["Total Return"]
        ],

        "Annualized Return":
        [
            dca_metrics["Annualized Return"],
            momentum_metrics["Annualized Return"]
        ],

        "Maximum Drawdown":
        [
            dca_risk["Maximum Drawdown"],
            momentum_risk["Maximum Drawdown"]
        ],

        "Volatility":
        [
            dca_risk["Volatility"],
            momentum_risk["Volatility"]
        ],

        "Sharpe Ratio":
        [
            dca_risk["Sharpe Ratio"],
            momentum_risk["Sharpe Ratio"]
        ]

    })


    results.to_csv(
        "output/results.csv",
        index=False
    )


    print("Finished!")
    print(results)



if __name__ == "__main__":
    main()