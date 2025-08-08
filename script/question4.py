import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Close Price for AAPL and MSFT on july 15, 2025
q4_solution =df[(df["Date"] == "2025-07-15") & (df["Ticker"].isin(["AAPL","MSFT"]))][["Ticker","Close Price"]]
print("Close Price for AAPL and MSFT on july 15,2025")
print(q4_solution)