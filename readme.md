# House Price Forecasting

This project aims to forecast house prices using a time series analysis approach. It includes data preprocessing and forecasting steps using the SARIMAX model.

## Project Structure

1. **Data Preprocessing Pipeline**
   - Cleans and prepares the data for analysis.

2. **Forecasting**
   - Uses the SARIMAX model to predict future house prices for different regions.

## Preprocessing Steps

1. **Missing Data Handling**
   - Removes rows with more than 50% missing values.
   - Uses forward-fill, backward-fill and linear interpolation for numeric columns.

2. **Duplicate Handling**
   - Removes duplicate rows from the dataset.

3. **Output**
   - Saves the processed data to `processed_house_prices.csv`.
   

## Forecasting Steps

1. **Data Loading**
   - Loads processed data from `processed_house_prices.csv`.

2. **Data Transformation**
   - Converts data to a long format suitable for time series analysis.

3. **Modeling**
   - Fits a SARIMAX model for each region to forecast house prices.

4. **Output**
   - Saves the forecasted house prices to `house_price_forecast.csv` with values rounded to 4 decimal places.

## Combine Steps

1. **Data Loading**
   - Loads processed data from `processed_house_prices.csv` and forecasted data from `house_price_forecast.csv`

2. **Data Transformation**
   - Transpose the forecasted data.

3. **Output**
   - Saves the combined data to `combined_data.csv`.

## Usage

1. Activate the virtual environment:   
```bash
   # Windows
   myenv\Scripts\activate
   
   # Unix/MacOS
   source myenv/bin/activate   
```

2. Install dependencies:   
```bash
   pip install -r requirements.txt   
```

3. Run the preprocessing script:   
```bash
   python data_preprocessing.py   
   ```

4. Run the forecasting script:   
```bash
   python forecast_house_price.py   
```

5. Run the combine script:   
```bash
   python combine_data.py   
```

## Input/Output

- **Input:** `data.csv`
- **Output:** `processed_house_prices.csv`
- **Output:** `house_price_forecast.csv`
- **Output:** `combined_data.csv`

## Requirements

See `requirements.txt` for package dependencies.

## Notes

- Ensure that the input data is properly formatted and preprocessed before running the forecasting script.
- The forecasting model is set to predict the next 5 months of house prices for each region.