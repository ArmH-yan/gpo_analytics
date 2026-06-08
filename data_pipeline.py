import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import os
import time

def load_local_data():
    """Simulates loading raw CSV data into pandas dataframes."""
    print("Loading raw data from CSVs...")
    players = pd.read_csv('players.csv')
    sessions = pd.read_csv('sessions.csv')
    transactions = pd.read_csv('transactions.csv')
    return players, sessions, transactions

def transform_data(players, sessions, transactions):
    """Performs basic data cleaning and transformations."""
    print("Transforming data...")
    # Convert date columns to datetime objects
    players['RegistrationDate'] = pd.to_datetime(players['RegistrationDate'])
    sessions['LoginTime'] = pd.to_datetime(sessions['LoginTime'])
    transactions['Timestamp'] = pd.to_datetime(transactions['Timestamp'])

    # Simple deduplication
    sessions = sessions.drop_duplicates()

    return players, sessions, transactions

def load_to_postgres(players, sessions, transactions):
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
    print("Load to PostgreSQL complete.")

def simulate_bigquery_export(players, sessions, transactions):
    """
    Simulates the process of exporting data to BigQuery.
    In a real scenario, this would use google-cloud-bigquery client.
    """
    print("Simulating export to Google BigQuery...")
    # Example: players.to_gbq('gaming_dataset.players', project_id='my-project-id')
    print(f"Data ready for BigQuery. Rows to export: Players({len(players)}), Sessions({len(sessions)}), Transactions({len(transactions)})")

if __name__ == "__main__":
    try:
        # 1. Extract
        p, s, t = load_local_data()

        # 2. Transform
        p, s, t = transform_data(p, s, t)

        # 3. Load (PostgreSQL)
        load_to_postgres(p, s, t)

        # 4. Export (BigQuery Simulation)
        simulate_bigquery_export(p, s, t)

        print("ETL Job Completed Successfully!")
    except Exception as e:
        print(f"ETL Job Failed: {e}")
