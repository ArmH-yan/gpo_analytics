# Portfolio Project Plan: Mobile Gaming Analytics

## Project Title
**Mobile Gaming Analytics: Player Behavior and Monetization Analysis**

## Objective
The goal of this project is to analyze large-scale operational data from a mobile game to extract actionable insights regarding player engagement, retention, and monetization. This project directly demonstrates the core competencies required for a Junior Data Analyst role, including SQL proficiency, KPI tracking, and data-driven storytelling.

## Business Problem
A mobile game studio wants to understand why their 7-day retention has dropped and identify the characteristics of their most valuable players (Whales). The management needs a dashboard to monitor daily performance and a deep dive into player activity to inform product decisions.

## Key Performance Indicators (KPIs)
- **DAU/MAU**: Daily and Monthly Active Users to measure engagement.
- **Retention Rate (D1, D7, D30)**: Percentage of users returning after their first day.
- **ARPU/ARPPU**: Average Revenue Per User and Average Revenue Per Paying User.
- **Conversion Rate**: Percentage of active users who make a purchase.
- **Churn Rate**: Rate at which players stop playing the game.

## Dataset Description (Mock/Simulated)
The analysis will be based on three primary tables:
1. `players`: Metadata about players (PlayerID, RegistrationDate, Country, DeviceType).
2. `sessions`: Logs of every time a player opens the app (SessionID, PlayerID, LoginTime, Duration).
3. `transactions`: Records of in-app purchases (TransactionID, PlayerID, Amount, Timestamp, ItemCategory).

## Analytical Approach
1. **Data Cleaning & Preparation (SQL)**:
   - Handle missing values and duplicate session logs.
   - Standardize timestamps for time-series analysis.
2. **Exploratory Data Analysis (EDA)**:
   - Analyze player distribution by geography and device.
   - Identify peak playing hours and average session length.
3. **Behavioral Analysis**:
   - Perform Cohort Analysis to track retention over time.
   - Segment players into "Free-to-Play", "Minnows", "Dolphins", and "Whales" based on spending habits.
4. **Insights & Recommendations**:
   - Identify correlations between session length and likelihood of purchase.
   - Propose features to improve D7 retention based on behavioral trends.

## Tools Used
- **SQL**: Data extraction and KPI calculation.
- **Google Sheets / Excel**: Data visualization and dashboard creation.
- **Markdown**: Project documentation and reporting.
