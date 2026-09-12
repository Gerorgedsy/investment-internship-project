# QQQ Investment Strategy Analysis

## Project Objective

This project analyzes historical QQQ data from January 2015 to January 2025 and compares two investment strategies:

1. Dollar-Cost Averaging (DCA)
2. Momentum Investing

The objective is to compare the return and risk characteristics of the two strategies.

## Data

Historical QQQ data is downloaded using the `yfinance` library.

The analysis uses adjusted closing prices and converts daily market data into monthly observations.

## Dollar-Cost Averaging Strategy

The DCA strategy invests $500 into QQQ every month regardless of market conditions.

The strategy never sells QQQ during the investment period.

## Momentum Strategy

The momentum strategy uses the previous six completed months of QQQ returns to determine the investment signal.

- Positive momentum: invest in QQQ
- Negative momentum: move the portfolio to cash

The current month is excluded from the momentum calculation to avoid look-ahead bias.

## Results

| Metric | DCA | Momentum |
|---|---:|---:|
| Total Invested | $60,000.00 | $60,000.00 |
| Final Portfolio Value | $166,107.98 | $170,109.98 |
| Total Profit | $106,107.98 | $110,109.98 |
| Total Return | 176.85% | 183.52% |
| Annualized Return | 10.72% | 10.98% |
| Annualized Volatility | 18.58% | 14.51% |
| Sharpe Ratio | 1.02 | 1.13 |
| Maximum Drawdown | -32.58% | -16.97% |

## Conclusion

Both strategies generated strong returns during the 2015–2024 period.

The momentum strategy slightly outperformed DCA in total and annualized return while also producing lower volatility and a substantially smaller maximum drawdown.

The results suggest that the momentum strategy provided a better risk-adjusted performance during the tested historical period.