import pandas as pd

from fetch_data import fetch_qqq_data


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean daily QQQ data and convert it to monthly data.
    """

    # Remove missing values.
    clean_data = data.dropna().copy()

    # Use the final available closing price of each month.
    monthly_data = clean_data["Close"].resample("ME").last().to_frame()

    # Calculate monthly percentage return.
    monthly_data["Monthly_Return"] = monthly_data["Close"].pct_change()

    # Calculate moving averages.
    monthly_data["MA_3"] = monthly_data["Close"].rolling(window=3).mean()
    monthly_data["MA_6"] = monthly_data["Close"].rolling(window=6).mean()

    return monthly_data


if __name__ == "__main__":
    daily_data = fetch_qqq_data()
    monthly_data = preprocess_data(daily_data)

    print("First ten months:")
    print(monthly_data.head(10))

    print("\nLast five months:")
    print(monthly_data.tail())

    print("\nMonthly data shape:")
    print(monthly_data.shape)