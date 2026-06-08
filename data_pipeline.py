import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os
import time
import pickle

def generate_mock_internal_data(n_players=100):
    """Generates mock operational data for the pipeline."""
    print(f"Generating mock data for {n_players} players...")
    countries = ['Armenia', 'USA', 'UK', 'France', 'Germany', 'Japan']
    devices = ['iOS', 'Android', 'PC']

    players = pd.DataFrame({
        'PlayerID': range(1, n_players + 1),
        'RegistrationDate': pd.date_range(start='2026-06-01', periods=n_players, freq='h'),
        'Country': np.random.choice(countries, n_players),
        'DeviceType': np.random.choice(devices, n_players),
        'InitialSessionDuration': np.random.normal(300, 100, n_players)
    })

    sessions = pd.DataFrame({
        'SessionID': range(1001, 1001 + n_players * 2),
        'PlayerID': np.random.choice(players['PlayerID'], n_players * 2),
        'LoginTime': pd.date_range(start='2026-06-01', periods=n_players * 2, freq='30min'),
        'Duration': np.random.randint(60, 3600, n_players * 2)
    })

    transactions = pd.DataFrame({
        'TransactionID': range(5001, 5011),
        'PlayerID': np.random.choice(players['PlayerID'], 10),
        'Amount': np.random.uniform(0.99, 99.99, 10),
        'Timestamp': pd.date_range(start='2026-06-01', periods=10, freq='D'),
        'ItemCategory': np.random.choice(['Skins', 'Currency', 'Boost', 'Pass'], 10)
    })

    return players, sessions, transactions

def load_vgsales():
    """Attempts to load the vgsales.csv dataset provided by the user."""
    try:
        print("Loading vgsales.csv...")
        return pd.read_csv('vgsales.csv')
    except FileNotFoundError:
        print("vgsales.csv not found. Creating a minimal mock version for demonstration.")
        return pd.DataFrame({
            'Rank': [1, 2], 'Name': ['Mock Game A', 'Mock Game B'],
            'Platform': ['Wii', 'NES'], 'Year': [2006, 1985],
            'Genre': ['Sports', 'Platform'], 'Publisher': ['Nintendo', 'Nintendo'],
            'NA_Sales': [41.49, 29.08], 'EU_Sales': [29.02, 3.58],
            'JP_Sales': [3.77, 6.81], 'Other_Sales': [8.46, 0.77], 'Global_Sales': [82.74, 40.24]
        })

def transform_data(players, sessions, transactions, vgsales):
    """Performs data cleaning and transformations."""
    print("Transforming data...")
    players['RegistrationDate'] = pd.to_datetime(players['RegistrationDate'])
    sessions['LoginTime'] = pd.to_datetime(sessions['LoginTime'])
    transactions['Timestamp'] = pd.to_datetime(transactions['Timestamp'])
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

        players['Country_Enc'] = le_country.transform(players['Country'])
        players['Device_Enc'] = le_device.transform(players['DeviceType'])

        X = players[['Country_Enc', 'Device_Enc', 'InitialSessionDuration']]
        probs = model.predict_proba(X)[:, 1]
        players['ChurnProbability'] = 1 - probs
        players['IsChurnRisk'] = (players['ChurnProbability'] > 0.5).astype(int)

        print("Churn prediction completed.")
        return players
    except FileNotFoundError:
        print("Churn model not found. Skipping prediction.")
        return players

def simulate_bigquery_export(players, sessions, transactions):
    """Simulates the process of exporting data to BigQuery."""
    print("Simulating export to Google BigQuery...")
    print(f"Data ready for BigQuery. Rows to export: Players({len(players)}), Sessions({len(sessions)}), Transactions({len(transactions)})")

def simulate_sheets_automation(players):
    """Simulates updating a Google Sheet with high-risk churn players."""
    print("Simulating Google Sheets Automation...")
    high_risk = players[players['IsChurnRisk'] == 1]
    print(f"Alerted {len(high_risk)} high-risk players to Google Sheets.")

if __name__ == "__main__":
    try:
        # 1. Extract
        p, s, t = generate_mock_internal_data()
        vg = load_vgsales()

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
