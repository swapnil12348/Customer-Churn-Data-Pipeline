Customer Churn Data Pipeline
Project Description
This project focuses on building a data processing pipeline for a customer churn dataset. The pipeline is designed to load, clean, transform the data, and store it in a SQLite database for further analysis or model training.

Key Features:
Data Loading and Cleaning:

Reads a CSV file containing customer churn data.
Cleans the 'TotalCharges' column by converting it to numeric and filling any missing values with the column's mean.
Converts the 'SeniorCitizen' column into categorical values ('Yes' or 'No').
Data Transformation:

Calculates the average monthly charges based on the total charges and tenure.
Groups customers into tenure categories (e.g., 0-1 year, 1-2 years).
Encodes categorical variables using LabelEncoder to make them suitable for machine learning models.
Database Management:

Creates a SQLite database and a customers1 table to store the processed data.
Inserts the transformed data into the SQLite database.
Folder Structure:
.idea/: Contains project-specific settings for your IDE.
.venv/: Virtual environment for Python dependencies.
main.py: The main script that runs the data pipeline.
How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/CustomerChurnDataPipeline.git
cd CustomerChurnDataPipeline
Set up the virtual environment:

bash
Copy code
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the data pipeline:

bash
Copy code
python main.py
Requirements
Python 3.x
pandas
numpy
sqlite3
scikit-learn
Future Enhancements
Implement data visualization for better insights.
Add support for other database types (e.g., PostgreSQL).
Integrate machine learning models for churn prediction.
License
This project is licensed under the MIT License - see the LICENSE file for details.
