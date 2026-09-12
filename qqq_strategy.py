from qqq_modules.data import download_qqq_data, preprocess_data
from qqq_modules.strategies import run_dca_strategy, run_momentum_strategy
from qqq_modules.metrics import calculate_returns, calculate_risk_assessment
from qqq_modules.visualization import plot_qqq_historical_price, plot_strategy_comparison
from qqq_modules.reporting import build_and_save_comparison


# Define date range
start_date = "2015-01-01"
end_date = "2025-01-01"


# ==========================================
# Step 2: Data Acquisition
# ==========================================
qqq_data = download_qqq_data(start_date, end_date)


# ==========================================
# Step 3: Data Preprocessing
# ==========================================
qqq_data, monthly_data, monthly_returns = preprocess_data(qqq_data)


# ==========================================
# Step 4: DCA Strategy
# ==========================================
monthly_investment = 500
dca_results = run_dca_strategy(monthly_data, monthly_investment)


# ==========================================
# Step 5: Momentum Strategy
# ==========================================
momentum_monthly_investment = 500
momentum_results = run_momentum_strategy(
    monthly_data,
    monthly_returns,
    momentum_monthly_investment
)


# ==========================================
# Step 6: Return Calculation
# ==========================================
years = 10
return_results = calculate_returns(
    dca_results,
    momentum_results,
    years
)


# ==========================================
# Step 7: Risk Assessment
# ==========================================
risk_free_rate = 0
risk_results = calculate_risk_assessment(
    monthly_data,
    momentum_results["positions"],
    risk_free_rate
)


# ==========================================
# Step 8: Data Visualization
# ==========================================
plot_qqq_historical_price(monthly_data)

plot_strategy_comparison(
    dca_results["portfolio_value"],
    momentum_results["portfolio_value"],
    dca_results["total_invested"]
)


# ==========================================
# Step 9: Final Comparison Table
# ==========================================
comparison = build_and_save_comparison(
    dca_results,
    momentum_results,
    return_results,
    risk_results
)
