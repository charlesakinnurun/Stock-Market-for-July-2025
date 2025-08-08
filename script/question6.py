import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Maximum EPS per sector
q6_solution = df.groupby("Sector")["EPS"].max().sort_values(ascending=False)
print("Maximum EPS per sector")
print(q6_solution)