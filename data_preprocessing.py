import pandas as pd

# Load the dataset
data = pd.read_csv("data.csv")

# Step 1: Handle missing data
threshold = len(data.columns) * 0.5
data = data.dropna(thresh=threshold)
# Convert relevant columns to numeric
price_columns = data.columns[5:]  # Assuming the first 5 columns are non-numeric metadata
data[price_columns] = data[price_columns].apply(pd.to_numeric, errors="coerce")
data.loc[:, price_columns] = data.loc[:, price_columns].interpolate(method="linear", axis=1, limit_direction="both")
data.loc[:, price_columns] = data.loc[:, price_columns].fillna(method="ffill")  # Forward-fill
data.loc[:, price_columns] = data.loc[:, price_columns].fillna(method="bfill")  # Backward-fill

data.to_csv("processed_house_prices.csv", index=False)






# Convert wide format to long format
# long_data = pd.melt(
#     data,
#     id_vars=["RegionID", "SizeRank", "RegionName", "StateName"],
#     var_name="Date",
#     value_name="AvgPrice",
# )

# # Display the reshaped data
# print(long_data.head())

# # Convert the 'Date' column to datetime format
# long_data["Date"] = pd.to_datetime(long_data["Date"], format="%m/%d/%Y")

# # Display data with the updated 'Date' column
# print(long_data.head())

# # Remove rows with missing values in the 'AvgPrice' column
# long_data = long_data.dropna(subset=["AvgPrice"])

# # Display the cleaned data
# print(long_data.head())

# # Extract Year and Month from the Date column
# long_data["Year"] = long_data["Date"].dt.year
# long_data["Month"] = long_data["Date"].dt.month

# # Display the updated data
# print(long_data.head())


# # Identify potential outliers using price thresholds
# price_lower_limit = 50000
# price_upper_limit = 1000000

# # Filter data within the acceptable range
# long_data = long_data[
#     (long_data["AvgPrice"] >= price_lower_limit) &
#     (long_data["AvgPrice"] <= price_upper_limit)
# ]

# # Display the filtered data
# print(long_data.head())

# # Save the processed data to a new CSV file
# long_data.to_csv("processed_house_prices.csv", index=False)

# # Verify the saved file
# print("Processed data saved to 'processed_house_prices.csv'")