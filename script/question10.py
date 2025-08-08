import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Percentage of Trading Days with the Close > Open Price
q10_solution = (df["Close Price"] > df["Open Price"]).groupby(df["Ticker"]).mean() * 100
q10_solution = q10_solution.sort_values(ascending=False).head()
print("Percentage of Trading Days with Close > Open Price (Top 5 Tickers)")
print(q10_solution)