import matplotlib.pyplot as plt
import seaborn as sns


def plot_qqq_historical_price(monthly_data):
    plt.figure(figsize=(12, 6))

    plt.plot(
        monthly_data.index,
        monthly_data.values,
        label="QQQ Adjusted Close"
    )

    plt.title("QQQ Historical Price (2015-2024)")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Closing Price ($)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("qqq_historical_price.png")
    plt.show()


def plot_strategy_comparison(dca_portfolio_value, momentum_portfolio_value, dca_total_invested):
    plt.figure(figsize=(12, 6))

    plt.plot(
        dca_portfolio_value.index,
        dca_portfolio_value.values,
        label="DCA Strategy"
    )

    plt.plot(
        momentum_portfolio_value.index,
        momentum_portfolio_value.values,
        label="Momentum Strategy"
    )

    # Also show cumulative money invested
    plt.plot(
        dca_total_invested.index,
        dca_total_invested.values,
        linestyle="--",
        label="Total Amount Invested"
    )

    plt.title("DCA vs Momentum Strategy Portfolio Value")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("strategy_comparison.png")
    plt.show()
