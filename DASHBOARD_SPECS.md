# Dashboard Specifications: Mobile Gaming Performance

## Tool
**Google Sheets / Excel** (as highlighted in the Junior Data Analyst JD)

## Dashboard Layout Overview
The dashboard should be divided into three main sections: Engagement, Retention, and Monetization.

### 1. Engagement Section
- **Metric**: Daily Active Users (DAU) & Monthly Active Users (MAU).
- **Visualization**: Line Chart showing the trend of DAU over the last 30 days.
- **Metric**: Sticky Factor (DAU/MAU).
- **Visualization**: Scorecard with a percentage and a trend indicator (up/down compared to previous period).

### 2. Retention Section
- **Metric**: Day 1, Day 7, and Day 30 Retention.
- **Visualization**:
  - **Cohort Heatmap**: Columns representing days since registration (D0 to D30) and rows representing registration cohorts (by week).
  - **Bar Chart**: Comparison of D7 retention across different countries and device types.

### 3. Monetization Section
- **Metric**: Daily Revenue & ARPU.
- **Visualization**: Dual-axis Combo Chart (Bars for Revenue, Line for ARPU).
- **Metric**: Player Segment Distribution.
- **Visualization**: Donut Chart showing the percentage of Whales, Dolphins, Minnows, and Non-Payers.

## Interactivity Requirements
- **Date Range Picker**: Allow users to filter the entire dashboard by specific dates.
- **Platform Filter**: Filter metrics by iOS vs. Android.
- **Country Filter**: Deep dive into specific geographical markets.

## Technical Implementation (Google Sheets)
- Use **Pivot Tables** to aggregate raw data exported from SQL.
- Use **Conditional Formatting** for the Retention Heatmap (Green-to-Red scale).
- Use **Data Validation** for creating dropdown filters.
