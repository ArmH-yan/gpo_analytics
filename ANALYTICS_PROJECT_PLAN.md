# Portfolio Project Plan: Mobile Gaming Analytics (Advanced Stack)

## Project Title
**Mobile Gaming Analytics: End-to-End Player Behavior and Monetization Analysis**

## Objective
The goal of this project is to analyze large-scale operational data from a mobile game to extract actionable insights regarding player engagement, retention, and monetization. This project demonstrates proficiency in a modern data stack, including data orchestration with Docker, ETL with Python, data warehousing in BigQuery, and advanced visualization in Power BI.

## Business Problem
A mobile game studio wants to understand why their 7-day retention has dropped and identify the characteristics of their most valuable players (Whales). The management needs a real-time dashboard to monitor daily performance and a scalable data pipeline to handle growing volumes of player event data.

## Key Performance Indicators (KPIs)
- **DAU/MAU**: Daily and Monthly Active Users to measure engagement.
- **Retention Rate (D1, D7, D30)**: Percentage of users returning after their first day.
- **ARPU/ARPPU**: Average Revenue Per User and Average Revenue Per Paying User.
- **Conversion Rate**: Percentage of active users who make a purchase.
- **Churn Rate**: Rate at which players stop playing the game.

## Dataset Description
The analysis is based on three core tables:
1. `players`: Metadata about players (PlayerID, RegistrationDate, Country, DeviceType).
2. `sessions`: Logs of every time a player opens the app (SessionID, PlayerID, LoginTime, Duration).
3. `transactions`: Records of in-app purchases (TransactionID, PlayerID, Amount, Timestamp, ItemCategory).

## Architecture & Tech Stack
- **Database (OLTP)**: **PostgreSQL** for local storage of operational data.
- **Data Warehouse (OLAP)**: **BigQuery** for large-scale analytical queries and long-term storage.
- **Environment**: **Docker** to containerize the PostgreSQL database and Python environment for reproducibility.
- **ETL/ELT**: **Python** (Pandas, SQLAlchemy) to extract data from PostgreSQL, perform transformations, and load into BigQuery.
- **Visualization**: **Power BI** for interactive dashboards and **Google Sheets** for quick reporting.
- **SQL**: Advanced SQL for KPI calculation and cohort analysis.

## Analytical Approach
1. **Data Engineering (Python & Docker)**:
   - Containerize the local environment for consistent development.
   - Build a Python script to automate data ingestion and cleaning.
2. **Data Warehousing (BigQuery)**:
   - Transfer processed data to BigQuery for high-performance analysis.
   - Use partitioned tables for optimized session log queries.
3. **Behavioral Analysis (SQL)**:
   - Perform Cohort Analysis using window functions.
   - Segment players into "Free-to-Play", "Minnows", "Dolphins", and "Whales" based on spending habits.
4. **Insights & Visualization (Power BI)**:
   - Design a star schema for efficient reporting.
   - Implement DAX measures for complex KPIs like Rolling 7-day Retention.

## Tools Used
- **PostgreSQL**
- **Docker**
- **Python (Pandas)**
- **BigQuery**
- **Power BI**
- **SQL**
