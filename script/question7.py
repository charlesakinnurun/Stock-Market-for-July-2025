import pandas as pd

# Load the cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Average Daily High-Low Price Difference
df["Price Range"] = df["High Price"] - df["Low Price"]
q7_solution = df.groupby("Ticker")["Price Range"].mean().sort_values(ascending=False).head()
print("Average Daily High-Low Price Difference (Top 5 Tickers)")
print(q7_solution)