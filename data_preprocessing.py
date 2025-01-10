import pandas as pd

# Load the data
file_path = "data.csv"
data = pd.read_csv(file_path)

# Drop rows or columns with all missing values
data = data.dropna(how='all', axis=1)  # Drop empty columns
data = data.dropna(how='all', axis=0)  # Drop empty rows

# Interpolate missing values
data = data.interpolate(method='linear', axis=0)

# Save the cleaned data
data.to_csv("cleaned_data.csv", index=False)

cleaned_data = pd.read_csv("cleaned_data.csv")

print("Data preprocessing completed. Cleaned data saved to 'cleaned_house_prices.csv'.")
print("Original Data - Missing Values Count")
print(data.isna().sum())

print("Cleaned Data - Missing Values Count")
print(cleaned_data.isna().sum())