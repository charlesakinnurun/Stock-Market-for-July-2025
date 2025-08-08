import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Stocks with PE Ratio > 30 and Dividend Yield > 1%
q5_solution = df[(df["PE Ratio"] > 30) & (df["Dividend Yield"] > 1)]["Ticker"].unique()
print("Stock with PE Ratio > 30 and Dividend Yield > 1%")
print(f"Tickers: {",".join(q5_solution)}")