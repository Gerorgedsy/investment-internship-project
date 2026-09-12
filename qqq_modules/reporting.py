import pandas as pd


def build_and_save_comparison(dca_results, momentum_results, return_results, risk_results):
    comparison = pd.DataFrame({
        "Metric": [
            "Total Invested ($)",
            "Final Portfolio Value ($)",
            "Total Profit ($)",
            "Total Return (%)",
            "Annualized Return (%)",
            "Annualized Volatility (%)",
            "Sharpe Ratio",
            "Maximum Drawdown (%)"
        ],

        "DCA Strategy": [
            dca_results["invested"],
            dca_results["final_value"],
            dca_results["profit"],
            return_results["dca_total_return"] * 100,
            return_results["dca_annualized_return"] * 100,
            risk_results["dca_volatility"] * 100,
            risk_results["dca_sharpe_ratio"],
            risk_results["dca_max_drawdown"] * 100
        ],

        "Momentum Strategy": [
            momentum_results["total_invested"],
            momentum_results["final_value"],
            momentum_results["profit"],
            return_results["momentum_total_return"] * 100,
            return_results["momentum_annualized_return"] * 100,
            risk_results["momentum_volatility"] * 100,
            risk_results["momentum_sharpe_ratio"],
            risk_results["momentum_max_drawdown"] * 100
        ]
    })

    # Round numbers to 2 decimal places
    comparison = comparison.round(2)

    print("\n========== Final Strategy Comparison ==========")
    print(comparison.to_string(index=False))

    # Save results to CSV
    comparison.to_csv(
        "strategy_comparison_results.csv",
        index=False
    )

    print("\nResults saved to strategy_comparison_results.csv")

    return comparison
