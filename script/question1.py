import pandas as pd

# Load the data from CSV file
df = pd.read_csv("datasets/stock_cleaned.csv")

# ----------- Average Close price by sector -------------
q1_solution = df.groupby("Sector")["Close Price"].mean().sort_values(ascending=False).to_frame(name="Average Close Price")
print("Average Close Price by Sector")
print(q1_solution)