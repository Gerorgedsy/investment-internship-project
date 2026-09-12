import pandas as pd
import numpy as np


def run_dca_strategy(monthly_data, monthly_investment=500):
    # Calculate shares purchased each month
    dca_shares_bought = monthly_investment / monthly_data

    # Calculate cumulative shares owned
    dca_total_shares = dca_shares_bought.cumsum()

    # Calculate cumulative amount invested
    dca_total_invested = pd.Series(
        np.arange(1, len(monthly_data) + 1) * monthly_investment,
        index=monthly_data.index
    )

    # Calculate portfolio value each month
    dca_portfolio_value = dca_total_shares * monthly_data

    # Final results
    dca_final_value = dca_portfolio_value.iloc[-1]
    dca_invested = dca_total_invested.iloc[-1]
    dca_profit = dca_final_value - dca_invested

    print("\n========== DCA Strategy ==========")
    print(f"Total invested: ${dca_invested:,.2f}")
    print(f"Final portfolio value: ${dca_final_value:,.2f}")
    print(f"Total profit: ${dca_profit:,.2f}")
    print(f"Total shares owned: {dca_total_shares.iloc[-1]:.4f}")

    return {
        "shares_bought": dca_shares_bought,
        "total_shares": dca_total_shares,
        "total_invested": dca_total_invested,
        "portfolio_value": dca_portfolio_value,
        "final_value": dca_final_value,
        "invested": dca_invested,
        "profit": dca_profit,
    }


def run_momentum_strategy(monthly_data, monthly_returns, momentum_monthly_investment=500):
    # Calculate 6-month momentum,
    # using the previous 6 completed months
    # and skipping the current month
    momentum = monthly_returns.shift(1).rolling(window=6).sum()

    # Position:
    # 1 = invest in QQQ
    # 0 = stay in cash
    positions = (momentum > 0).astype(int)

    # Starting balances
    momentum_cash = 0
    momentum_shares = 0

    # Store portfolio values
    momentum_portfolio_values = []

    for date in monthly_data.index:
        price = monthly_data.loc[date]
        position = positions.loc[date]

        # Add $500 contribution every month
        momentum_cash += momentum_monthly_investment

        # If signal = 1, invest all cash into QQQ
        if position == 1:
            if momentum_cash > 0:
                shares_to_buy = momentum_cash / price
                momentum_shares += shares_to_buy
                momentum_cash = 0

        # If signal = 0, sell all QQQ and stay in cash
        else:
            if momentum_shares > 0:
                momentum_cash += momentum_shares * price
                momentum_shares = 0

        # Calculate total portfolio value
        portfolio_value = momentum_cash + momentum_shares * price
        momentum_portfolio_values.append(portfolio_value)

    # Convert to pandas Series
    momentum_portfolio_value = pd.Series(
        momentum_portfolio_values,
        index=monthly_data.index
    )

    # Final results
    momentum_total_invested = len(monthly_data) * momentum_monthly_investment
    momentum_final_value = momentum_portfolio_value.iloc[-1]
    momentum_profit = momentum_final_value - momentum_total_invested

    print("\n========== Momentum Strategy ==========")
    print(f"Total invested: ${momentum_total_invested:,.2f}")
    print(f"Final portfolio value: ${momentum_final_value:,.2f}")
    print(f"Total profit: ${momentum_profit:,.2f}")
    print(f"Final shares owned: {momentum_shares:.4f}")
    print(f"Final cash balance: ${momentum_cash:,.2f}")

    return {
        "momentum": momentum,
        "positions": positions,
        "portfolio_value": momentum_portfolio_value,
        "total_invested": momentum_total_invested,
        "final_value": momentum_final_value,
        "profit": momentum_profit,
        "shares": momentum_shares,
        "cash": momentum_cash,
    }
