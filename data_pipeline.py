import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os
import time
import pickle

def load_local_data():
    """Simulates loading raw CSV data into pandas dataframes."""
    print("Loading raw data from CSVs...")
    players = pd.read_csv('players.csv')
    sessions = pd.read_csv('sessions.csv')
    transactions = pd.read_csv('transactions.csv')
    vgsales = pd.read_csv('vgsales.csv')
    return players, sessions, transactions, vgsales

def transform_data(players, sessions, transactions, vgsales):
    """Performs basic data cleaning and transformations."""
    print("Transforming data...")
    # Convert date columns to datetime objects
    players['RegistrationDate'] = pd.to_datetime(players['RegistrationDate'])
    sessions['LoginTime'] = pd.to_datetime(sessions['LoginTime'])
    transactions['Timestamp'] = pd.to_datetime(transactions['Timestamp'])

    # Simple deduplication
    sessions = sessions.drop_duplicates()

    return players, sessions, transactions, vgsales

def load_to_postgres(players, sessions, transactions, vgsales):
    """Loads cleaned data into a local PostgreSQL database with a simple retry loop."""
    db_url = os.getenv('DATABASE_URL', 'postgresql://analyst:password123@localhost:5432/gaming_db')
    engine = create_engine(db_url)

    max_retries = 5
    for attempt in range(max_retries):
        try:
            print(f"Connecting to PostgreSQL (Attempt {attempt + 1}/{max_retries})...")
            # Try to connect
            with engine.connect() as connection:
                pass
            break
        except OperationalError:
            if attempt < max_retries - 1:
                print("Database not ready, waiting 5 seconds...")
                time.sleep(5)
            else:
                print("Could not connect to database.")
                raise

    print("Writing tables to PostgreSQL...")
    players.to_sql('players', engine, if_exists='replace', index=False)
    sessions.to_sql('sessions', engine, if_exists='replace', index=False)
    transactions.to_sql('transactions', engine, if_exists='replace', index=False)
    vgsales.to_sql('vgsales', engine, if_exists='replace', index=False)
    print("Load to PostgreSQL complete.")

def run_churn_prediction(players):
    """Uses the trained ML model to predict churn for current players."""
    print("Running Churn Prediction...")
    try:
        with open('churn_model.pkl', 'rb') as f:
            model_data = pickle.load(f)

        model = model_data['model']
        le_country = model_data['le_country']
        le_device = model_data['le_device']

        # Prepare features
        players['Country_Enc'] = le_country.transform(players['Country'])
        players['Device_Enc'] = le_device.transform(players['DeviceType'])

        X = players[['Country_Enc', 'Device_Enc']]
        # Probability of being retained
        probs = model.predict_proba(X)[:, 1]
        players['ChurnProbability'] = 1 - probs
        players['IsChurnRisk'] = (players['ChurnProbability'] > 0.5).astype(int)

        print("Churn prediction completed.")
        return players
    except FileNotFoundError:
        print("Churn model not found. Skipping prediction.")
        return players

def simulate_bigquery_export(players, sessions, transactions):
    """
    Simulates the process of exporting data to BigQuery.
    In a real scenario, this would use google-cloud-bigquery client.
    """
    print("Simulating export to Google BigQuery...")
    # Example: players.to_gbq('gaming_dataset.players', project_id='my-project-id')
    print(f"Data ready for BigQuery. Rows to export: Players({len(players)}), Sessions({len(sessions)}), Transactions({len(transactions)})")

def simulate_sheets_automation(players):
    """
    Simulates updating a Google Sheet with high-risk churn players.
    """
    print("Simulating Google Sheets Automation...")
    high_risk = players[players['IsChurnRisk'] == 1]
    # Example using gspread:
    # gc = gspread.service_account(filename='credentials.json')
    # sh = gc.open("Churn Risk Alerts").sheet1
    # sh.update([high_risk.columns.values.tolist()] + high_risk.values.tolist())
    print(f"Alerted {len(high_risk)} high-risk players to Google Sheets.")

if __name__ == "__main__":
    try:
        # 1. Extract
        p, s, t, vg = load_local_data()

        # 2. Transform
        p, s, t, vg = transform_data(p, s, t, vg)

        # 3. Load (PostgreSQL)
        load_to_postgres(p, s, t, vg)

        # 4. ML Prediction
        p = run_churn_prediction(p)

        # 5. Export (BigQuery Simulation)
        simulate_bigquery_export(p, s, t)

        # 6. Sheets Automation (Simulated)
        simulate_sheets_automation(p)

        print("ETL Job Completed Successfully!")
    except Exception as e:
        print(f"ETL Job Failed: {e}")
