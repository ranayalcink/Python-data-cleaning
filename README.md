# preliminary_datacleaning

## Overview:

This project involves the cleaning and preprocessing of a dataset ('kz.csv') for further analysis. The dataset presumably contains information related to orders, including columns such as 'category_id,' 'price,' 'user_id,' 'category_code,' and 'brand.' The goal of this project is to handle missing values, convert data types where necessary, and ensure consistency in certain columns.

## Project Structure:

1. **Importing Libraries:**
   - The necessary libraries, including Pandas, NumPy, and Datetime, are imported to facilitate data manipulation and analysis.

2. **Loading and Displaying the Dataset:**
   - The dataset is loaded into a Pandas DataFrame, and the first 10 rows are displayed for an initial overview.

3. **Descriptive Statistics:**
   - Descriptive statistics are calculated and displayed to gain insights into the numerical features of the dataset.

4. **Data Types:**
   - The data types of each column are displayed to understand how the data is currently structured.

5. **Handling Missing Values:**
   - The percentage of missing values for each column is calculated and displayed.
   - Specific cases of missing values in 'category_id' are identified and displayed.

6. **Filling Missing Values:**
   - Missing values in the 'price' column are filled using information from 'category_code.'
   - Missing values in the 'user_id' column are filled using information from 'brand.'
   - Missing values in 'category_id' are filled with 0, assuming it as an appropriate default.

7. **Handling Numeric Data Stored as Strings:**
   - Functions are defined to identify and handle cases where numeric data is mistakenly stored as strings.
   - The 'category_code' and 'brand' columns are processed to ensure consistency and facilitate analysis.

8. **Invalid Entry Rates:**
   - The rates of invalid entries in the 'category_code' and 'brand' columns are calculated and displayed.

9. **Conclusion:**
   - The project concludes by filling missing values in the 'category_id' column with 0, assuming 0 as an appropriate default.

## Usage:

To replicate the data cleaning and preprocessing steps:
   - Ensure the required libraries are installed (Pandas, NumPy).
   - Load the dataset ('kz.csv') into a Pandas DataFrame.
   - Run the provided script in your Python environment.

## Notes:

- The project assumes certain default values (e.g., filling missing 'category_id' with 0) based on the context of the dataset.
- The functions for handling numeric data stored as strings can be adapted for similar scenarios in other projects.

Feel free to reach out for any questions or improvements!

*This project is part of a portfolio for a data analyst job search and showcases skills in data cleaning and preprocessing.*
