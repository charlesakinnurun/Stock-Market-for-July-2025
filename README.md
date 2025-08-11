## Introduction
This dataset contains historical stock market data for a variety of companies during July 2025. It is formatted as a CSV file, with each row representing a daily record for a specific stock. The data provides a comprehensive overview of daily stock performance and company fundamentals, including:
* Identifiers: The Date of the record and the Ticker symbol of the company.
* Pricing: Open, Close, High, and Low prices for the day.
* Volume & Market Metrics: Volume Traded and Market Cap.
* Financial Ratios: PE Ratio, Dividend Yield, and EPS (Earnings Per Share).
* Performance Metrics: 52 Week High and 52 Week Low.
* Sector Information: The Sector to which the company belongs. This dataset is ideal for performing various financial analyses, such as tracking stock performance, comparing sectors, and identifying trends
### Data Cleaning
```python
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

```
### Analysis
Here are 10 analytical questions you can solve using pandas on your stock data:
1. **Performance Analysis**: What was the average 'Close Price' for each 'Sector' during the entire period?
2. **Volatility Analysis:** Which stock ('Ticker') had the highest average daily trading volume ('Volume Traded')?
3. **Stock Comparison:** What were the top 5 stocks with the highest average 'Market Cap' in the dataset?
4. **Date-Based Filtering:** What was the 'Close Price' for 'AAPL' and 'MSFT' on July 15, 2025?
5. **Ratio Analysis:** List all stocks that had a 'PE Ratio' above 30 and a 'Dividend Yield' greater than 1% on any given day.
6. **Growth Metrics:** What was the maximum 'EPS' (Earnings Per Share) recorded for each 'Sector'?
7. **Price Range:** For each 'Ticker', what is the average difference between the 'High Price' and the 'Low Price'?
8. **Time-Series Aggregation:** What was the total 'Volume Traded' for the 'Technology' sector in June 2025?
9. **Sorting and Ranking:** Which stock had the largest 'Close Price' on any day in the dataset, and what was that price?
10. **Relative Performance:** For each 'Ticker', what percentage of its trading days had a 'Close Price' higher than its 'Open Price'?
#### What was the average 'Close Price' for each 'Sector' during the entire period?
```python
import pandas as pd

# Load the data from CSV file
df = pd.read_csv("datasets/stock_cleaned.csv")

# ----------- Average Close price by sector -------------
q1_solution = df.groupby("Sector")["Close Price"].mean().sort_values(ascending=False).to_frame(name="Average Close Price")
print("Average Close Price by Sector")
print(q1_solution)
```
#### Which stock ('Ticker') had the highest average daily trading volume ('Volume Traded')?
```python
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("datasets/stock_cleaned.csv")

# Highest Average Daily Trading Volume
q2_solution = df.groupby("Ticker")["Volume Traded"].mean().sort_values(ascending=False).reset_index().head(1)
print("Highest Average Daily Trading Volume")
print(q2_solution)
```
#### What were the top 5 stocks with the highest average 'Market Cap' in the dataset?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Top 5 Stocks by Market Cap
q3_solution = df.groupby("Ticker")["Market Cap"].mean().sort_values(ascending=False).head()
print("Top 5 Stocks by Market Cap")
print(q3_solution)
```
#### What was the 'Close Price' for 'AAPL' and 'MSFT' on July 15, 2025?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Close Price for AAPL and MSFT on july 15, 2025
q4_solution =df[(df["Date"] == "2025-07-15") & (df["Ticker"].isin(["AAPL","MSFT"]))][["Ticker","Close Price"]]
print("Close Price for AAPL and MSFT on july 15,2025")
print(q4_solution)
```
#### List all stocks that had a 'PE Ratio' above 30 and a 'Dividend Yield' greater than 1% on any given day.
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Stocks with PE Ratio > 30 and Dividend Yield > 1%
q5_solution = df[(df["PE Ratio"] > 30) & (df["Dividend Yield"] > 1)]["Ticker"].unique()
print("Stock with PE Ratio > 30 and Dividend Yield > 1%")
print(f"Tickers: {",".join(q5_solution)}")
```
#### What was the maximum 'EPS' (Earnings Per Share) recorded for each 'Sector'?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Maximum EPS per sector
q6_solution = df.groupby("Sector")["EPS"].max().sort_values(ascending=False)
print("Maximum EPS per sector")
print(q6_solution)
```
#### For each 'Ticker', what is the average difference between the 'High Price' and the 'Low Price'?
```python
import pandas as pd

# Load the cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Average Daily High-Low Price Difference
df["Price Range"] = df["High Price"] - df["Low Price"]
q7_solution = df.groupby("Ticker")["Price Range"].mean().sort_values(ascending=False).head()
print("Average Daily High-Low Price Difference (Top 5 Tickers)")
print(q7_solution)
```
#### What was the total 'Volume Traded' for the 'Technology' sector in June 2025?
```python
import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Convert date to dataetime type
df["Date"] = pd.to_datetime(df["Date"])

# Total Volume Traded for Technology in June 2025
q8_solution = df[(df["Sector"] == "Technology") & (df["Date"].dt.month == 6) & (df["Date"].dt.year == 2025)]["Volume Traded"].sum()
print("Total Volume Traded for Technology in June 2025")
print(f"Total Volume Traded: {q8_solution}")
```
#### Which stock had the largest 'Close Price' on any day in the dataset, and what was that price?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Largest Close Price
q9_solution = df.loc[df["Close Price"].idxmax()]
print("Largest Close Price")
print(q9_solution[["Ticker","Date","Close Price"]])
```
#### For each 'Ticker', what percentage of its trading days had a 'Close Price' higher than its 'Open Price'?
```python
import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/stock_cleaned.csv")

# Percentage of Trading Days with the Close > Open Price
q10_solution = (df["Close Price"] > df["Open Price"]).groupby(df["Ticker"]).mean() * 100
q10_solution = q10_solution.sort_values(ascending=False).head()
print("Percentage of Trading Days with Close > Open Price (Top 5 Tickers)")
print(q10_solution)
```
