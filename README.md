# Telco Customer Churn Data Pipeline

## Project Description

This project implements a data pipeline for processing and analyzing telco customer churn data. It loads data from a CSV file, performs data cleaning and transformation, and stores the processed data in a SQLite database. The pipeline is designed to prepare the data for further analysis and machine learning tasks related to customer churn prediction.

## Features

- Data loading and cleaning from CSV
- Data transformation and feature engineering
- Encoding of categorical variables
- Creation of a SQLite database
- Insertion of processed data into the database

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn
- sqlite3

## Installation

1. Clone this repository:git clone https://github.com/swapnil12348/telco-customer-churn-pipeline.git

2. Navigate to the project directory

3. Install the required packages:
pip install pandas numpy scikit-learn

## Usage

1. Place your input CSV file in the project directory or update the file path in `main.py`.

2. Run the main script: python main.py

3. The script will process the data and create a SQLite database named `telco_customer_churn.db` in the project directory.

## Project Structure

- `main.py`: The main script that orchestrates the data pipeline
- `telco_customer_churn.db`: SQLite database (generated after running the script)
- `README.md`: Project documentation

## Data Processing Steps

1. Load and clean data from CSV
2. Transform data and create new features
3. Encode categorical variables
4. Create SQLite database and table
5. Insert processed data into the database

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/telco-customer-churn-pipeline/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
