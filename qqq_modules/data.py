import yfinance as yf
import pandas as pd


def download_qqq_data(start_date, end_date):
    # Download QQQ historical data
    qqq_data = yf.download(
        "QQQ",
        start=start_date,
        end=end_date,
        auto_adjust=False
    )

    # Display first 5 rows
    print(qqq_data.head())

    # Display dataset information
    print("\nDataset information:")
    print(qqq_data.info())

    return qqq_data


def preprocess_data(qqq_data):
    # Check for missing values
    print("\nMissing values before cleaning:")
    print(qqq_data.isnull().sum())

    # Remove rows with missing values
    qqq_data = qqq_data.dropna()

    # Extract adjusted closing price
    adj_close = qqq_data["Adj Close"]["QQQ"]

    # Convert daily prices to monthly prices
    # Use the last trading day's adjusted closing price of each month
    monthly_data = adj_close.resample("ME").last()

    # Calculate monthly returns
    monthly_returns = monthly_data.pct_change()

    print("\nMonthly QQQ prices:")
    print(monthly_data.head(10))

    print("\nMonthly QQQ returns:")
    print(monthly_returns.head(10))

    print("\nNumber of months:", len(monthly_data))

    return qqq_data, monthly_data, monthly_returns
