import pandas as pd


def dca_strategy(
    monthly_data: pd.DataFrame,
    monthly_investment: float = 500
) -> pd.DataFrame:
    """
    Simulate a monthly Dollar-Cost Averaging strategy.
    """

    result = monthly_data.copy()

    result["DCA_Investment"] = monthly_investment
    result["DCA_Shares_Bought"] = (
        result["DCA_Investment"] / result["Close"]
    )

    result["DCA_Total_Shares"] = (
        result["DCA_Shares_Bought"].cumsum()
    )

    result["DCA_Total_Invested"] = (
        result["DCA_Investment"].cumsum()
    )

    result["DCA_Portfolio_Value"] = (
        result["DCA_Total_Shares"] * result["Close"]
    )

    return result

def momentum_strategy(
    monthly_data: pd.DataFrame,
    monthly_investment: float = 500
) -> pd.DataFrame:
    """
    Simulate a monthly momentum strategy.

    Use the previous 6 months of returns while skipping
    the most recent month.

    If momentum is positive, invest $500 in QQQ.
    Otherwise, keep the $500 as cash.
    """

    result = monthly_data.copy()

    # Calculate 6-month momentum while skipping the most recent month.
    result["Momentum"] = (
        result["Monthly_Return"]
        .shift(1)
        .rolling(window=6)
        .sum()
    )

    # Position:
    # 1 = invest in QQQ
    # 0 = keep this month's contribution as cash
    result["Momentum_Position"] = (
        result["Momentum"] > 0
    ).astype(int)

    # Every month, the investor contributes $500.
    result["Momentum_Contribution"] = monthly_investment

    # Amount used to buy QQQ this month.
    result["Momentum_QQQ_Investment"] = (
        result["Momentum_Contribution"]
        * result["Momentum_Position"]
    )

    # Amount kept as cash this month.
    result["Momentum_Cash_Deposit"] = (
        result["Momentum_Contribution"]
        * (1 - result["Momentum_Position"])
    )

    # Shares bought when the signal is positive.
    result["Momentum_Shares_Bought"] = (
        result["Momentum_QQQ_Investment"]
        / result["Close"]
    )

    # Accumulate all QQQ shares.
    result["Momentum_Total_Shares"] = (
        result["Momentum_Shares_Bought"].cumsum()
    )

    # Accumulate all cash that was not invested.
    result["Momentum_Cash"] = (
        result["Momentum_Cash_Deposit"].cumsum()
    )

    # Total contributed capital.
    result["Momentum_Total_Invested"] = (
        result["Momentum_Contribution"].cumsum()
    )

    # Total portfolio value = QQQ holdings + cash.
    result["Momentum_Portfolio_Value"] = (
        result["Momentum_Total_Shares"] * result["Close"]
        + result["Momentum_Cash"]
    )

    return result

if __name__ == "__main__":
    from fetch_data import fetch_qqq_data
    from preprocess import preprocess_data

    daily_data = fetch_qqq_data()
    monthly_data = preprocess_data(daily_data)

    # Test DCA strategy
    dca_result = dca_strategy(monthly_data)

    print("First ten months of DCA:")
    print(
        dca_result[
            [
                "Close",
                "DCA_Investment",
                "DCA_Shares_Bought",
                "DCA_Total_Invested",
                "DCA_Portfolio_Value"
            ]
        ].head(10)
    )

    print("\nFinal DCA result:")
    print(
        dca_result[
            [
                "DCA_Total_Invested",
                "DCA_Portfolio_Value"
            ]
        ].tail(1)
    )

    # Test momentum strategy
    momentum_result = momentum_strategy(monthly_data)

    print("\nFirst twelve months of Momentum Strategy:")
    print(
        momentum_result[
            [
                "Close",
                "Monthly_Return",
                "Momentum",
                "Momentum_Position",
                "Momentum_QQQ_Investment",
                "Momentum_Cash",
                "Momentum_Portfolio_Value"
            ]
        ].head(12)
    )

    print("\nFinal Momentum result:")
    print(
        momentum_result[
            [
                "Momentum_Total_Invested",
                "Momentum_Cash",
                "Momentum_Portfolio_Value"
            ]
        ].tail(1)
    )