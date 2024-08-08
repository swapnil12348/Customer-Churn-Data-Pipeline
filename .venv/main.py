import pandas as pd
import sqlite3
import numpy as np
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

def load_and_clean_data(file_path):
 # read file
    df = pd.read_csv(file_path)

    # Check the column names
    print("Column names:", df.columns)

    # Clean the 'TotalCharges' column (assuming this is the correct column name)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Fill NaN values in 'TotalCharges' with the mean
    mean_total_charges = df['TotalCharges'].mean()
    df['TotalCharges'].fillna(mean_total_charges, inplace=True)

    # Convert 'SeniorCitizen' to string 'Yes' or 'No'
    df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})

    return df

def transform_data(df):
    # Creating a new feature: Average Monthly Charges
    df['AvgMonthlyCharges'] = df['TotalCharges'] / df['tenure']
    df['AvgMonthlyCharges'].replace([np.inf, -np.inf], np.nan, inplace=True)
    df['AvgMonthlyCharges'].fillna(df['MonthlyCharges'], inplace=True)

    # Creating a categorical feature for tenure
    df['TenureGroup'] = pd.cut(df['tenure'], bins=[0, 12, 24, 36, 48, 60, np.inf],
                               labels=['0-1 year', '1-2 years', '2-3 years', '3-4 years', '4-5 years', '5+ years'])

    # Encoding categorical variables
    le = LabelEncoder()
    categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'Churn', 'TenureGroup']

    for col in categorical_cols:
        df[col + '_Encoded'] = le.fit_transform(df[col])

    return df

def create_database_and_table(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers1 (
        customer_id TEXT PRIMARY KEY,
        gender TEXT,
        senior_citizen TEXT,
        partner TEXT,
        dependents TEXT,
        tenure INTEGER,
        phone_service TEXT,
        multiple_lines TEXT,
        internet_service TEXT,
        online_security TEXT,
        online_backup TEXT,
        device_protection TEXT,
        tech_support TEXT,
        streaming_tv TEXT,
        streaming_movies TEXT,
        contract TEXT,
        paperless_billing TEXT,
        payment_method TEXT,
        monthly_charges REAL,
        total_charges REAL,
        churn TEXT,
        avg_monthly_charges REAL,
        tenure_group TEXT,
        gender_encoded INTEGER,
        senior_citizen_encoded INTEGER,
        partner_encoded INTEGER,
        dependents_encoded INTEGER,
        phone_service_encoded INTEGER,
        multiple_lines_encoded INTEGER,
        internet_service_encoded INTEGER,
        online_security_encoded INTEGER,
        online_backup_encoded INTEGER,
        device_protection_encoded INTEGER,
        tech_support_encoded INTEGER,
        streaming_tv_encoded INTEGER,
        streaming_movies_encoded INTEGER,
        contract_encoded INTEGER,
        paperless_billing_encoded INTEGER,
        payment_method_encoded INTEGER,
        churn_encoded INTEGER,
        tenure_group_encoded INTEGER
    )
    ''')

    conn.commit()
    conn.close()

def insert_data(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql('customers1', conn, if_exists='replace', index=False)
    conn.close()

def main():
    file_path = "C:/Users/swapn/Downloads/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    db_path = 'telco_customer_churn.db'

    print("Starting data processing at", datetime.now())

    # Loading and cleaning data
    df = load_and_clean_data(file_path)
    print("Data loaded and cleaned at", datetime.now())

    # Transforming data
    df_transformed = transform_data(df)
    print("Data transformed at", datetime.now())

    # Creating database and table
    create_database_and_table(db_path)
    print("Database and table created at", datetime.now())

    # Inserting data into database
    insert_data(df_transformed, db_path)
    print("Data inserted into database at", datetime.now())

    print("Data processing completed at", datetime.now())

if __name__ == "__main__":
    main()