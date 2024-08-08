
# Customer Churn Data Pipeline

## Project Description

The Customer Churn Data Pipeline is a Python-based project designed to load, clean, transform customer churn data, and store it into an SQLite database. The pipeline processes data by performing several operations, including filling missing values, creating new features, and encoding categorical variables. The processed data is then inserted into an SQLite database for further analysis or use in machine learning models.

## Project Structure

- `main.py`: The main script that orchestrates the data processing pipeline.
- `load_and_clean_data.py`: Handles the loading and cleaning of the data.
- `transform_data.py`: Contains functions for transforming the data.
- `create_database_and_table.py`: Creates the SQLite database and tables.
- `insert_data.py`: Inserts the processed data into the SQLite database.
- `requirements.txt`: Lists the Python packages required to run the project.
- `README.md`: This document.

## How to Use

### Set up the virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Run the data pipeline:

```bash
python main.py
```

## Requirements

- Python 3.x
- pandas
- numpy
- sqlite3
- scikit-learn

## Future Enhancements

- Implement data visualization for better insights.
- Add support for other database types (e.g., PostgreSQL).
- Integrate machine learning models for churn prediction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

