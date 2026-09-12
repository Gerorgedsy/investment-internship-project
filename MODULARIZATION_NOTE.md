# Modularization Note

This version only modularizes the original project. The calculation logic, assumptions, strategy rules, output labels, charts, dates, and constants are intentionally kept the same as the uploaded `qqq_strategy.py`.

## File structure

- `qqq_strategy.py` — main workflow / entry point
- `qqq_modules/data.py` — data download and preprocessing
- `qqq_modules/strategies.py` — DCA and momentum strategies
- `qqq_modules/metrics.py` — return and risk calculations
- `qqq_modules/visualization.py` — charts
- `qqq_modules/reporting.py` — final comparison table and CSV export

Run exactly as before:

```powershell
python qqq_strategy.py
```
