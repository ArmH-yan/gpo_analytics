# Portfolio Project Plan: Mobile Gaming Analytics & ML

## Project Title
**End-to-End Gaming Analytics: Behavioral Prediction and Market Trend Analysis**

## Objective
This project demonstrates a professional-grade data stack focused on the gaming industry. It combines **Video Game Market Trends** (using the Video Game Sales dataset) with **Player-Level Behavioral Analytics** and **Machine Learning** to predict player "no-shows" (churn).

## Business Problem
A mobile game studio wants to:
1. Identify high-risk players who are likely to "no-show" after registration to trigger re-engagement campaigns.
2. Analyze global gaming market trends (genres, platforms) to inform future product development.
3. Automate the flow of data from operational systems to analytical warehouses and alert systems.

## Key Performance Indicators (KPIs)
- **Churn Risk (No-Show)**: Predicted probability of a player not returning after Day 0.
- **DAU/MAU**: Daily and Monthly Active Users.
- **Global Sales by Genre/Platform**: Market penetration analysis based on the Video Game Sales dataset.
- **ARPU**: Average Revenue Per User.

## Tech Stack & Automation
- **Orchestration**: **Docker** & **Docker Compose**.
- **Data Warehousing**: **PostgreSQL** (Operational) & **BigQuery** (Analytical).
- **Languages**: **SQL** & **Python**.
- **Machine Learning**: **Scikit-learn** (Logistic Regression for Churn Prediction).
- **Automation**:
    - **BigQuery Ingestion**: Automated export from Python.
    - **Alerting**: Automated high-risk player exports to **Google Sheets** for the marketing team.
- **Visualization**: **Power BI** & **Google Sheets**.

## Dataset Description
1. `vgsales.csv`: Historical market data on 16,500+ games (Rank, Name, Platform, Year, Genre, Publisher, Global_Sales).
2. `players`, `sessions`, `transactions`: Custom operational tables simulating real-time player activity and monetization.

## Analytical Approach
1. **Data Engineering**: Python-based ETL pipeline containerized with Docker.
2. **Machine Learning**: Predictive modeling to identify churn risk at the point of registration based on demographic and initial session features.
3. **Market Analysis**: Cross-referencing player segments with global genre trends to identify high-value opportunities.
4. **Dashboarding**: Interactive Power BI reports showcasing both internal engagement and external market benchmarks.
