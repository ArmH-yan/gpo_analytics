# Dashboard Specifications: Mobile Gaming Performance

## Primary Tool: Power BI
This dashboard leverages Power BI for advanced data modeling and interactive storytelling.

## Data Model (Star Schema)
- **Fact Table**: `Fact_Transactions`, `Fact_Sessions`
- **Dimension Tables**: `Dim_Players`, `Dim_Date`, `Dim_Items`
- **Relationships**: One-to-Many from Dimensions to Facts.

## Power BI Key Features
### 1. Measures (DAX)
- `Total Revenue = SUM(transactions[Amount])`
- `DAU = DISTINCTCOUNT(sessions[PlayerID])`
- `Retention Rate D1 = DIVIDE([Retained Players D1], [New Players], 0)`
- `Rolling 7D Revenue = CALCULATE([Total Revenue], DATESINPERIOD('Dim_Date'[Date], LASTDATE('Dim_Date'[Date]), -7, DAY))`

### 2. Visualizations
- **Executive Summary**: KPI Cards for DAU, MAU, ARPU, and Total Revenue.
- **Engagement Trend**: Area Chart showing DAU and MAU over time.
- **Monetization Deep Dive**: Waterfall Chart showing revenue growth by item category.
- **Cohort Analysis**: Matrix visual showing D1, D7, and D30 retention heatmaps.
- **Player Segmentation**: Tree Map showing the distribution of Whales vs. Minnows.

### 3. Interactivity & Filters
- **Slicers**: Date, Country, Device Platform (iOS/Android).
- **Drill-through**: Click on a Country to see detailed player behavior for that region.
- **Tooltips**: Hover over the Engagement chart to see specific event counts.

## Secondary Tool: Google Sheets
For quick ad-hoc analysis and reporting.
- Use **Connected Sheets** to pull data directly from BigQuery.
- **Pivot Tables** for simple metric aggregation.
- **Sparklines** for visualizing 30-day trends in a compact format.

## Implementation Steps
1. Connect Power BI to the **PostgreSQL** or **BigQuery** source.
2. Build the relationship model (Star Schema).
3. Create the DAX measures mentioned above.
4. Design the UI with a consistent color palette (Gaming-themed: Dark mode with neon accents).
