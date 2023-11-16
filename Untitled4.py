# Import necessary libraries
import pandas as pd
import numpy as np
import datetime

# Load the dataset from the 'kz.csv' file
orders = pd.read_csv('kz.csv')

# Display the first 10 rows of the dataset
orders.head(10)

# Display descriptive statistics for the dataset
orders.describe().apply(lambda s: s.apply('{0:.5f}'.format))

# Display data types of each column
orders.dtypes

# Check for missing values and calculate the percentage of missing values for each column
missing_percentage = orders.isna().sum() / orders.shape[0] * 100
print("Percentage of missing values:\n", missing_percentage)

# Identify and handle specific missing value cases
missing_category_id = orders.loc[orders['category_id'].isna(), :]
print("Rows with missing 'category_id':\n", missing_category_id)

# Fill missing values in 'price' and 'user_id' columns
# Use 'category_code' to fill missing 'price' values and 'brand' to fill missing 'user_id' values
orders.price.fillna(orders.category_code, inplace=True)
orders.price.fillna(0, inplace=True)
orders.user_id.fillna(orders.brand, inplace=True)
orders.user_id.fillna(0, inplace=True)

# Fill missing values in 'category_id' column with 0
orders.category_id.fillna(0, inplace=True)

# Define a function to check if a value can be converted to a float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Define a function to reject values that can be converted to float
# This is useful for identifying and handling cases where numeric data is mistakenly stored as strings
def reject_float(value):
    if value is None:
        return np.NaN
    if is_float(value):
        return np.NaN
    else:
        return value

# Apply the 'reject_float' function to the 'category_code' column
# Replace invalid entries with 'unknown' to ensure consistency and facilitate further analysis
orders.category_code = orders.category_code.apply(reject_float)
orders.category_code.fillna('unknown', inplace=True)

# Calculate the rate of invalid entries in the 'category_code' column
invalid_category_rate = orders[orders.category_code == 'unknown'].shape[0] / orders['category_code'].shape[0]
print('Invalid category rate is {:.2%}'.format(invalid_category_rate))

# Apply the 'reject_float' function to the 'brand' column
# Replace invalid entries with 'unknown' to ensure consistency and facilitate further analysis
orders.brand = orders.brand.apply(reject_float)
orders.brand.fillna('unknown', inplace=True)

# Calculate the rate of invalid entries in the 'brand' column
invalid_brand_rate = orders[orders.brand == 'unknown'].shape[0] / orders['brand'].shape[0]
print('Invalid brand rate is {:.2%}'.format(invalid_brand_rate))

# Fill missing values in the 'category_id' column with 0
# This is done to handle missing values in a numeric column, assuming 0 as an appropriate default
orders.category_id = orders.category_id.apply(lambda x: 0 if pd.isna(x) else x)
