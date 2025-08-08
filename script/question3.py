import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Top 5 Stocks by Market Cap
q3_solution = df.groupby("Ticker")["Market Cap"].mean().sort_values(ascending=False).head()
print("Top 5 Stocks by Market Cap")
print(q3_solution)