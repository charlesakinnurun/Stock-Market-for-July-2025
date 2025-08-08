import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Convert date to dataetime type
df["Date"] = pd.to_datetime(df["Date"])

# Total Volume Traded for Technology in June 2025
q8_solution = df[(df["Sector"] == "Technology") & (df["Date"].dt.month == 6) & (df["Date"].dt.year == 2025)]["Volume Traded"].sum()
print("Total Volume Traded for Technology in June 2025")
print(f"Total Volume Traded: {q8_solution}")