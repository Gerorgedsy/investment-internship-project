'''import pandas as pd
import numpy as np


def fetch_qqq_data():
    """
    Generate simulated daily QQQ price data.
    This is a temporary replacement for real market data.
    """

    np.random.seed(42)

    # Business days from 2015-01-01 to 2025-01-01
    dates = pd.date_range(
        start="2015-01-01",
        end="2025-01-01",
        freq="B"
    )

    # Simulate daily returns
    daily_returns = np.random.normal(
        loc=0.0006,
        scale=0.015,
        size=len(dates)
    )

    # Generate closing prices
    close = 100 * np.cumprod(1 + daily_returns)

    # Generate open/high/low prices
    open_price = close * (1 + np.random.normal(0, 0.002, len(close)))
    high = np.maximum(open_price, close) * (
        1 + np.random.uniform(0, 0.01, len(close))
    )
    low = np.minimum(open_price, close) * (
        1 - np.random.uniform(0, 0.01, len(close))
    )

    volume = np.random.randint(
        5_000_000,
        20_000_000,
        len(close)
    )

    data = pd.DataFrame({
        "Open": open_price,
        "High": high,
        "Low": low,
        "Close": close,
        "Volume": volume
    }, index=dates)

    return data


if __name__ == "__main__":

    qqq_data = fetch_qqq_data()

    print(qqq_data.head())
    print()
    print(qqq_data.tail())'''

import pandas as pd
import yfinance as yf


def fetch_qqq_data(
    start_date="2015-01-01",
    end_date="2025-01-01"
):
    """
    Download real QQQ historical market data
    from Yahoo Finance.
    """

    print("Downloading real QQQ data...")

    data = yf.download(
        "QQQ",
        start=start_date,
        end=end_date,
        auto_adjust=False
    )

    if data.empty:
        raise ValueError("No QQQ data downloaded.")

    # Keep required columns
    data = data[
        [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    ]

    # Remove missing values
    data = data.dropna()

    print("QQQ data downloaded successfully.")
    print(data.head())

    return data


if __name__ == "__main__":

    qqq = fetch_qqq_data()

    print("\nLast five rows:")
    print(qqq.tail())

    print("\nShape:")
    print(qqq.shape)