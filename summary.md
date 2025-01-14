
# Data Process

## 1. Data Preprocessing
- Cleans and prepares the data for analysis to ensure accuracy and usability.

## 2. Forecasting
- Uses the SARIMAX model to predict future house prices for different regions.

## Preprocessing Steps

1. **Missing Data Handling**
   - Rows with more than 50% missing values are removed.
   - Missing numeric values are filled using forward-fill, backward-fill, and linear interpolation for a seamless data series.

2. **Duplicate Handling**
   - Removes duplicate rows to eliminate redundancy.

3. **Output**
   - The processed data is saved to `processed_house_prices.csv`.

## Forecasting Steps

1. **Data Loading**
   - Processed data is loaded from `processed_house_prices.csv`.

2. **Data Transformation**
   - Converts data into a long format suitable for time series analysis.

3. **Modeling**
   - The SARIMAX model is applied to forecast house prices for each region.  
   - **Why SARIMAX?**  
     - **Seasonality & Trends**: SARIMAX (Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors) is specifically designed to model time series data with clear seasonal patterns and long-term trends, which are typical in real estate data.  
     - **Incorporating External Factors**: SARIMAX allows the inclusion of external regressors, which can further enhance the accuracy by considering influential variables.  
     - **Proven Performance**: It has been widely used in economic and financial forecasting due to its robustness in handling real-world, complex datasets.

4. **Output**
   - Forecasted house prices are saved to `house_price_forecast.csv` with values rounded to 4 decimal places.

## Combine Steps

1. **Data Loading**
   - Processed data is loaded from `processed_house_prices.csv`, and forecasted data is loaded from `house_price_forecast.csv`.

2. **Data Transformation**
   - Transposes the forecasted data for integration.

3. **Output**
   - The combined data is saved to `combined_data.csv`.

## Frontend Features

### Selectors
1. **State Selector**: Allows multiple state selection. The default state is NY.  
2. **Region Selector**: Filters regions based on the selected states.  
3. **Date Selector**: Sets the date range for displayed data, defaulting to the full range in `combined_data.csv`.

### Visualizations
1. **Line Chart**: Plots house prices of selected regions within the chosen date range. Clicking a month on the x-axis highlights it, displaying its data as a bar chart.  
2. **Bar Chart**: Shows house prices for the selected month.  

### Additional Features
1. **Download**: Exports the data shown in the line chart to a CSV file.  
2. **Forecast Toggle**: Displays forecasted data on the line chart. The forecasted date range must fall within the selected date range for it to appear.


## Repo and UI link
- Data process: https://github.com/CaoXi324/data-process
- Frontend: https://github.com/CaoXi324/house-price-frontend
- Live UI: https://house-price-frontend.vercel.app/

## Statistical Values
- Overall Mean: 214591.64340522003
- Overall Median: 127562.8008
- Overall Skewness: 3.463289583705034
- Overall Standard Deviation: 1334645.7083605824
- Overall 25th Percentile: 101812.6585
- Overall 50th Percentile (Median): 134758.2446
- Overall 75th Percentile: 188455.843
