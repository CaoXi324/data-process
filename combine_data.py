import pandas as pd

# Step 1: Load data 2
data1 = pd.read_csv("processed_house_prices.csv")
data2 = pd.read_csv("house_price_forecast.csv", index_col=0)

# Ensure the RegionName order in data2 matches data1
region_order = data1["RegionName"].tolist()
data2 = data2[region_order]

# Reset index of data2 and transpose so dates become columns
data2 = data2.transpose()
data2.columns = [str(date) for date in data2.columns]  # Ensure columns are strings
data2.reset_index(inplace=True)
data2.rename(columns={"index": "RegionName"}, inplace=True)

# Merge the dataframes on RegionName
combined_data = pd.merge(data1, data2, on="RegionName", how="left")

combined_data.to_csv("combined_data.csv", index=False)