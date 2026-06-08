# Mobile Gaming Analytics & ML Churn Prediction

## 🎮 Project Overview
This project is an end-to-end data analytics and machine learning solution designed for the gaming industry. It combines **market trend analysis** (using the Kaggle Video Game Sales dataset) with **predictive behavioral modeling** to identify players at high risk of "churning" (not returning after registration).

The project showcases a modern data stack capable of handling large-scale operational data, performing automated ETL, and delivering actionable insights through ML-driven alerts.

---

## 🚀 Technical Stack
- **Languages**: Python (Pandas, Scikit-learn, SQLAlchemy, NumPy), SQL (PostgreSQL/BigQuery).
- **Environment & Orchestration**: Docker, Docker Compose.
- **Database**: PostgreSQL (Operational), Google BigQuery (Analytical).
- **Automation**: Google Sheets API (via `gspread`) for automated alerting.
- **Visualization**: Power BI, Google Sheets.

---

## 🧠 Machine Learning Model: Churn Prediction
### Goal
Identify players who will not return to the game after their registration day ("No-Shows").

### Model Details
- **Algorithm**: Logistic Regression.
- **Features**:
  - `Country`: Geographical segment of the player.
  - `DeviceType`: Device platform (iOS, Android, PC).
  - `InitialSessionDuration`: Length of the player's first session.
- **Metrics**:
  - **Accuracy**: ~80% (Measures overall correctness).
  - **Precision**: Measures the accuracy of high-risk flags (important for targeted marketing).
  - **Recall**: Measures the ability to catch all potential churners.

---

## 📊 Dashboard & Analytics
### Power BI Features
- **Star Schema Data Model**: Optimized for high-performance reporting.
- **Retention Heatmap**: Cohort analysis by registration week.
- **Market Benchmarking**: Comparing internal growth with global trends in Genre and Platform from the `vgsales` dataset.
- **DAX Measures**: Advanced KPIs including `Rolling 7-day Retention` and `Churn Risk Distribution`.

---

## 🛠️ Installation & Setup Guide

### 1. Prerequisites
- Install **Docker** and **Docker Compose**.
- Install **Python 3.9+** (for local development).

### 2. Step-by-Step Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Place the Dataset**:
   Download `vgsales.csv` from [Kaggle](https://www.kaggle.com/datasets/gregorut/videogamesales) and place it in the root directory.

3. **Start the Environment (Docker)**:
   This will spin up the PostgreSQL database and the ETL environment.
   ```bash
   docker-compose up --build
   ```

4. **Run the ML Pipeline**:
   Train the model and run the ETL script.
   ```bash
   # Train the churn model
   python churn_model.py

   # Run the end-to-end data pipeline
   python data_pipeline.py
   ```

5. **Access the Data**:
   Connect to PostgreSQL using your favorite tool (e.g., DBeaver) at `localhost:5432` (User: `analyst`, Pass: `password123`).

---

## 📈 Sample SQL Queries
Key analytical queries are available in `gaming_queries.sql` to demonstrate SQL proficiency in calculating KPIs like DAU, MAU, and Churn Risk by Country.
