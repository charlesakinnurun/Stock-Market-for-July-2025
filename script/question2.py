import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("datasets/stock_cleaned.csv")

# Highest Average Daily Trading Volume
q2_solution = df.groupby("Ticker")["Volume Traded"].mean().sort_values(ascending=False).reset_index().head(1)
print("Highest Average Daily Trading Volume")
print(q2_solution)