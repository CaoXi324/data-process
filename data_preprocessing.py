import pandas as pd

# Load the data
file_path = "data.csv"
data = pd.read_csv(file_path)

# Check for missing values
print(data.isnull().sum())

# Inspect the column names
print(data.columns)

# Melt the DataFrame to reshape it
# Melt the DataFrame to reshape it
tidy_data = data.melt(
    id_vars=["RegionID", "SizeRank", "RegionName", "RegionType", "StateName"],
    var_name="Date",
    value_name="Price",
)

# Convert the "Date" column to datetime
tidy_data["Date"] = pd.to_datetime(tidy_data["Date"])

# Preview the reshaped data
print(tidy_data.head())


# Check for missing prices
missing_prices = tidy_data[tidy_data["Price"].isnull()]
print(f"Number of missing prices: {len(missing_prices)}")

# Interpolate missing values (group by region)
tidy_data["Price"] = tidy_data.groupby(["RegionName", "StateName"])["Price"].transform(
    lambda x: x.interpolate(method="linear")
)

# Verify if missing values are filled
print(tidy_data.isnull().sum())