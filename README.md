# Preprocessing

# Day 1: Titanic Data Cleaning and Preprocessing

This project demonstrates a complete Day 1 workflow for data cleaning and basic manipulation using the Titanic dataset with pandas.

## Steps Performed

- **Data Loading & Exploration:**  
  - Loaded Titanic dataset with seaborn
  - Inspected data structure: head, shape, columns, info, and statistics

- **Data Selection & Querying:**  
  - Selected specific columns and rows with `.loc`, `.iloc`, and `.query`
  - Demonstrated Boolean indexing for flexible data queries

- **Missing Value Handling:**  
  - Imputed 'age' missing values with median (robust to outliers and skew)
  - Imputed 'embarked' and 'embark_town' with their modes (most frequent, categorical)
  - Dropped 'deck' column due to excessive missingness (>70%)

- **Duplicates:**  
  - Checked for and dropped duplicate rows

## Key Code Highlights

- How to analyze missingness and choose sound filling/dropping strategies
- Effective ways to select, filter, and manipulate data in pandas
- The reasoning behind statistical imputation choices
