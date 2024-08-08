# Customer Churn Data Pipeline

## Project Overview

The **Customer Churn Data Pipeline** project is designed to predict customer churn for a telecommunications company. Churn refers to the percentage of customers that stop using a service over a given period. This project uses a dataset to train and evaluate a machine learning model that can predict whether a customer is likely to churn.

## Features

- **Data Loading and Cleaning**: The project starts by loading the data from a CSV file, cleaning it by handling missing values, and converting data types as needed.
- **Data Transformation**: New features such as average monthly charges and tenure groups are created to enhance the model's predictive power.
- **Exploratory Data Analysis (EDA)**: Visualizations and statistical analyses are performed to understand the data distribution and correlations between features.
- **Machine Learning Model**: A RandomForestClassifier is used to train the model, and its performance is evaluated using accuracy, classification report, and a confusion matrix.
- **SQLite Database Integration**: The cleaned and transformed data is stored in an SQLite database for efficient querying and analysis.

## Project Structure

```plaintext
.venv/
│
├── src/
│   ├── data_loader.py            # Module to load data from CSV
│   ├── data_preprocessor.py      # Module to preprocess and clean data
│   ├── exploratory_analysis.py   # Module for performing exploratory data analysis
│   ├── model_trainer.py          # Module to train and evaluate the model
│                      # Main script to run the project
│── main.py
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset used in the project
│
├── telco_customer_churn.db       # SQLite database containing the processed data
│
└── README.md                     # Project documentation
