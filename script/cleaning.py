import pandas as pd

# Load the data from CSV file
df = pd.read_csv("datasets/stock_data_july_2025.csv")

# ----------- Step 1: Data Type Conversion --------------
# Convert the "Date" column to a datetime object for proper time-series analysis
df["Date"] = pd.to_datetime(df["Date"])

# --------------- Step 2: Handle Duplicates ------------
# Remove any fully duplicated rows from the DataFrame
df.drop_duplicates(inplace=True)

# Display the Cleaned DataFrame information to verify changes
print("DataFrame after cleaning")
df.info()

# Display the first 5 rows of the cleaned DataFrame
print("First 5 rows of the cleaned DataFrame")
print(df.head())

# Save the cleaned dataset
df.to_csv("datasets/stock_cleaned.csv")
print("Saved Successfully")