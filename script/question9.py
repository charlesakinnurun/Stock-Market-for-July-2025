import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Largest Close Price
q9_solution = df.loc[df["Close Price"].idxmax()]
print("Largest Close Price")
print(q9_solution[["Ticker","Date","Close Price"]])