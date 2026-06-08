import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle

def generate_synthetic_data(n_samples=1000):
    """Generates synthetic player data for model training."""
    print(f"Generating {n_samples} synthetic player records...")
    countries = ['Armenia', 'USA', 'UK', 'France', 'Germany', 'Japan']
    devices = ['iOS', 'Android', 'PC']

    data = {
        'PlayerID': range(1, n_samples + 1),
        'Country': np.random.choice(countries, n_samples),
        'DeviceType': np.random.choice(devices, n_samples),
        'InitialSessionDuration': np.random.normal(300, 100, n_samples), # Avg 5 mins
        'SignupHour': np.random.randint(0, 24, n_samples)
    }
    df = pd.DataFrame(data)

    # Generate Target: Churn (No-Show after Day 0)
    # Assume players with short initial session and signup during night hours are more likely to churn
    churn_prob = (df['InitialSessionDuration'] < 250).astype(int) * 0.4 + \
                 (df['SignupHour'] < 6).astype(int) * 0.3 + \
                 np.random.random(n_samples) * 0.3

    df['IsRetained'] = (churn_prob < 0.5).astype(int)
    return df

def train_churn_model():
    """Trains a Logistic Regression model to predict player churn."""
    print("Training Churn Prediction Model...")

    df = generate_synthetic_data()

    # Encoding categorical variables
    le_country = LabelEncoder()
    le_device = LabelEncoder()

    df['Country_Enc'] = le_country.fit_transform(df['Country'])
    df['Device_Enc'] = le_device.fit_transform(df['DeviceType'])

    # X and y
    X = df[['Country_Enc', 'Device_Enc', 'InitialSessionDuration']]
    y = df['IsRetained']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred)
    }

    print("Model Evaluation Metrics:")
    for k, v in metrics.items():
        print(f" - {k.capitalize()}: {v:.4f}")

    # Save model, encoders, and metrics
    model_data = {
        'model': model,
        'le_country': le_country,
        'le_device': le_device,
        'metrics': metrics
    }

    with open('churn_model.pkl', 'wb') as f:
        pickle.dump(model_data, f)

    print("Churn model trained and saved to churn_model.pkl")

if __name__ == "__main__":
    train_churn_model()
