from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_strategy_comparison(
    dca_result: pd.DataFrame,
    momentum_result: pd.DataFrame
) -> None:
    """
    Plot DCA and momentum portfolio values
    and save the chart in the output folder.
    """

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    plt.figure(figsize=(12, 6))

    plt.plot(
        dca_result.index,
        dca_result["DCA_Portfolio_Value"],
        label="DCA Strategy"
    )

    plt.plot(
        momentum_result.index,
        momentum_result["Momentum_Portfolio_Value"],
        label="Momentum Strategy"
    )

    plt.plot(
        dca_result.index,
        dca_result["DCA_Total_Invested"],
        linestyle="--",
        label="Total Invested"
    )

    plt.title("QQQ Investment Strategy Comparison")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    file_path = output_folder / "strategy_comparison.png"
    plt.savefig(file_path, dpi=300)
    plt.show()

    print(f"Chart saved to: {file_path}")


if __name__ == "__main__":
    from fetch_data import fetch_qqq_data
    from preprocess import preprocess_data
    from strategies import dca_strategy, momentum_strategy

    daily_data = fetch_qqq_data()
    monthly_data = preprocess_data(daily_data)

    dca_result = dca_strategy(monthly_data)
    momentum_result = momentum_strategy(monthly_data)

    plot_strategy_comparison(
        dca_result,
        momentum_result
    )