import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

def train_churn_model():
    """
    Trains a simple Logistic Regression model to predict player churn.
    Churn (No-Show) is defined as having only one session on the registration date
    and never returning.
    """
    print("Training Churn Prediction Model...")

    # Load sample data
    players = pd.read_csv('players.csv')
    sessions = pd.read_csv('sessions.csv')

    # Merge and create features
    # Feature 1: Country, Feature 2: DeviceType
    # Target: 1 if Player returned after D0, 0 otherwise (Simplified for this mock)

    # For a real model, we'd look at session counts per player
    session_counts = sessions.groupby('PlayerID').size().reset_index(name='SessionCount')
    data = players.merge(session_counts, on='PlayerID', how='left').fillna(0)

    # Label: 1 if SessionCount > 1 (Retained), 0 if SessionCount <= 1 (Churn/No-Show)
    data['IsRetained'] = (data['SessionCount'] > 1).astype(int)

    # Encoding categorical variables
    le_country = LabelEncoder()
    le_device = LabelEncoder()

    data['Country_Enc'] = le_country.fit_transform(data['Country'])
    data['Device_Enc'] = le_device.fit_transform(data['DeviceType'])

    # X and y
    X = data[['Country_Enc', 'Device_Enc']]
    y = data['IsRetained']

    # Train model
    model = LogisticRegression()
    model.fit(X, y)

    # Save model and encoders
    model_data = {
        'model': model,
        'le_country': le_country,
        'le_device': le_device
    }

    with open('churn_model.pkl', 'wb') as f:
        pickle.dump(model_data, f)

    print("Churn model trained and saved to churn_model.pkl")

if __name__ == "__main__":
    train_churn_model()
