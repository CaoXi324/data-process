import pandas as pd


data = pd.read_csv("processed_house_prices.csv")

# Ensure that date columns are properly identified (columns starting from index 4 onwards)
time_series_columns = data.columns[5:]  # Assuming first 5 columns are metadata

# Select only the time series data
time_series_data = data[time_series_columns]

# Convert data to numeric (if not already)
time_series_data = time_series_data.apply(pd.to_numeric, errors='coerce')

overall_mean = time_series_data.mean().mean()
print("Overall Mean:", overall_mean)

overall_median = time_series_data.median().median()
print("Overall Median:", overall_median)

overall_skewness = time_series_data.skew().mean()
print("Overall Skewness:", overall_skewness)

overall_std_dev = time_series_data.std().mean()
print("Overall Standard Deviation:", overall_std_dev)

overall_percentiles = time_series_data.stack().quantile([0.25, 0.5, 0.75])
print("Overall 25th Percentile:", overall_percentiles[0.25])
print("Overall 50th Percentile (Median):", overall_percentiles[0.5])
print("Overall 75th Percentile:", overall_percentiles[0.75])