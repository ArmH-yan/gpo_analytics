# Dashboard Specifications: Gaming Performance & Predictions

## Tool: Power BI
The dashboard provides a 360-degree view of player behavior and market trends.

## 1. Predictive Insights (ML Model)
- **Churn Risk Scorecard**: Average predicted churn probability.
- **Risk Distribution**: Histogram of players by churn probability buckets.
- **Top Risk Factors**: Bar chart showing the impact of Country and Device on churn risk.
- **Alert List**: Table of high-risk "No-Show" players (Synced with the Google Sheets automation).

## 2. Market Benchmarking (Video Game Sales)
- **Genre Popularity**: Bubble chart showing Global Sales vs. Number of Titles by Genre.
- **Platform Lifecycle**: Stacked Area chart of Sales by Platform over the years.
- **Market Share**: Donut chart of Publisher sales.

## 3. Engagement & Monetization
- **DAU Trends**: Line chart with a forecast for the next 7 days.
- **Revenue Heatmap**: Global revenue by Country.
- **ARPU by Platform**: Comparison of player value vs. market platform trends.

## Technical DAX Measures
- `Churn Rate % = DIVIDE(COUNTROWS(FILTER(players, players[IsChurnRisk] = 1)), COUNTROWS(players))`
- `Market vs. Internal Sales = [Total Internal Revenue] / SUM(vgsales[Global_Sales])`
- `Predicted No-Shows = SUMX(players, players[IsChurnRisk])`

## UI/UX Design
- **Theme**: Dark Mode with "Cyberpunk" accents.
- **Navigation**: Sidebar with tabs for "Operational Overview", "Predictive Analytics", and "Market Trends".
- **Dynamic Filtering**: Slicers for Genre and Year to filter both the market data and internal segments.
