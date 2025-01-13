import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
# Load processed data
data = pd.read_csv("processed_house_prices.csv")

# Ensure that date columns are properly identified (columns starting from index 4 onwards)
date_columns = data.columns[5:]  # Assuming first 5 columns are metadata

# Convert to long format
data_long = pd.melt(
    data,
    id_vars=["RegionID", "RegionName", "StateName", "SizeRank", "RegionType"],  # Columns to keep
    value_vars=date_columns,  # Columns to unpivot
    var_name="Date",  # Name for the date column
    value_name="HousePrice"  # Name for the house price values
)

# Ensure proper types
data_long["Date"] = pd.to_datetime(data_long["Date"])  # Convert date column to datetime
data_long["HousePrice"] = pd.to_numeric(data_long["HousePrice"], errors="coerce")  # Ensure numeric prices

# Forecast for each region
regions = data_long["RegionName"].unique()
forecast_results = {}

for region in regions:
    region_data = data_long[data_long["RegionName"] == region].sort_values("Date")
    region_data.set_index("Date", inplace=True)

    model = SARIMAX(region_data["HousePrice"], order=(1, 1, 1), seasonal_order=(0, 1, 1, 12))
    results = model.fit()

    forecast = results.get_forecast(steps=5)
    forecast_results[region] = forecast.predicted_mean.round(4)

forecast_df = pd.DataFrame(forecast_results)
forecast_df.index = pd.date_range(start=data_long["Date"].max() + pd.DateOffset(months=1), periods=5, freq='ME')
forecast_df.to_csv("house_price_forecast.csv")