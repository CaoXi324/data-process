# Data Preprocessing Pipeline

This project contains a data preprocessing pipeline that performs the following operations:

## Preprocessing Steps

1. **Missing Data Handling**
   - Removes rows with more than 50% missing values
   - Applies linear interpolation for numeric columns
   - Uses forward-fill and backward-fill for non-numeric columns

2. **Duplicate Handling**
   - Removes duplicate rows from the dataset

3. **Missing Value Cleanup**
   - Removes rows with all missing values
   - Removes any remaining rows with missing values

## Usage

1. Activate the virtual environment:   ```bash
   # Windows
   myenv\Scripts\activate
   
   # Unix/MacOS
   source myenv/bin/activate   ```

2. Install dependencies:   ```bash
   pip install -r requirements.txt   ```

3. Run the preprocessing script:   ```bash
   python data_preprocessing.py   ```

## Input/Output

- Input: `data.csv`
- Output: `cleaned_data.csv`

## Requirements

See `requirements.txt` for package dependencies.