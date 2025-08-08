# Introduction
![Stock Market](assets/stock.jpg)
***
This dataset contains historical stock market data for a variety of companies during July 2025. It is formatted as a CSV file, with each row representing a daily record for a specific stock.
The data provides a comprehensive overview of daily stock performance and company fundamentals, including:
* Identifiers: The Date of the record and the Ticker symbol of the company.
* Pricing: Open, Close, High, and Low prices for the day.
* Volume & Market Metrics: Volume Traded and Market Cap.
* Financial Ratios: PE Ratio, Dividend Yield, and EPS (Earnings Per Share).
* Performance Metrics: 52 Week High and 52 Week Low.
* Sector Information: The Sector to which the company belongs.
This dataset is ideal for performing various financial analyses, such as tracking stock performance, comparing sectors, and identifying trends
## Cleaning
Based on the analysis of your data, here are the steps for a thorough data cleaning process, from initial inspection to final adjustments.
#### Step 1: Initial Data Inspection
The first and most crucial step is to get a clear overview of your data. This involves checking for missing values, confirming data types, and understanding the range and distribution of your columns.
* Missing Values: The output of the info() command shows that all 14 columns have 4346 non-null entries, which means there are no missing values in your dataset.
* Data Types: The data types for most columns are suitable for analysis (float64 for prices and ratios, int64 for volume).
* Column Names: The column names are descriptive and do not need to be changed.
#### Step 2: Data Type Conversion
The Date column is currently stored as a generic object type, which can be problematic for chronological sorting or time-based analysis.
* Action: Convert the Date column from object to a proper datetime format.
* Reason: This ensures that any operations involving dates are handled correctly.
#### Step 3: Handling Duplicates
You should always check for and remove any duplicate rows. While the info() output doesn't directly show duplicates, it is a recommended step in a robust data cleaning process.
* Action: Check the dataset for any completely duplicated rows and remove them.
* Reason: Duplicates can skew calculations and lead to inaccurate analysis.
#### Step 4: Outlier and Anomaly Detection
Although the data appears to be clean, it's good practice to check for outliers in numerical columns like Open Price or Volume Traded. You can use statistical methods or visualizations (like box plots) to identify and decide how to handle these values.
* Action: Use methods like the Interquartile Range (IQR) to detect and manage outliers, if any are present.
* Reason: Outliers can disproportionately affect statistical analyses and model performance.
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
## Analysis
Here are 10 analytical questions you can solve using pandas on your stock data:
1. Performance Analysis: What was the average 'Close Price' for each 'Sector' during the entire period?
2. Volatility Analysis: Which stock ('Ticker') had the highest average daily trading volume ('Volume Traded')?
3. Stock Comparison: What were the top 5 stocks with the highest average 'Market Cap' in the dataset?
4. Date-Based Filtering: What was the 'Close Price' for 'AAPL' and 'MSFT' on July 15, 2025?
5. Ratio Analysis: List all stocks that had a 'PE Ratio' above 30 and a 'Dividend Yield' greater than 1% on any given day.
6. Growth Metrics: What was the maximum 'EPS' (Earnings Per Share) recorded for each 'Sector'?
7. Price Range: For each 'Ticker', what is the average difference between the 'High Price' and the 'Low Price'?
8. Time-Series Aggregation: What was the total 'Volume Traded' for the 'Technology' sector in June 2025?
9. Sorting and Ranking: Which stock had the largest 'Close Price' on any day in the dataset, and what was that price?
10. Relative Performance: For each 'Ticker', what percentage of its trading days had a 'Close Price' higher than its 'Open Price'?

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
The remaining analysis can be found
[here](/script/)
## Tools I Used
* Python (pandas)
* Git
* Vscode
