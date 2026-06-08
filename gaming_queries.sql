-- Portfolio Project: Gaming Analytics, ML, and Market Trends

-- 1. Top Genres by Global Sales (Market Analysis)
SELECT
    Genre,
    ROUND(SUM(Global_Sales)::NUMERIC, 2) AS TotalGlobalSales,
    COUNT(*) AS NumberOfTitles
FROM vgsales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

-- 2. Player Churn Risk by Country
-- Assuming the 'players' table has been updated by the Python ETL script with 'IsChurnRisk'
SELECT
    Country,
    COUNT(*) AS TotalPlayers,
    SUM(IsChurnRisk) AS HighRiskPlayers,
    ROUND(SUM(IsChurnRisk)::NUMERIC / COUNT(*) * 100, 2) AS ChurnRisk_Pct
FROM players
GROUP BY 1
ORDER BY 4 DESC;

-- 3. Correlation between Market Trends and Internal Monetization
-- Comparing our top item categories with the most popular market genres (Simplified)
WITH MarketTopGenres AS (
    SELECT Genre, SUM(Global_Sales) as Sales
    FROM vgsales
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3
),
InternalRevenue AS (
    SELECT ItemCategory, SUM(Amount) as Revenue
    FROM transactions
    GROUP BY 1
)
SELECT
    i.ItemCategory,
    i.Revenue,
    CASE WHEN i.ItemCategory IN (SELECT Genre FROM MarketTopGenres) THEN 'Aligned with Market' ELSE 'Niche Segment' END AS MarketAlignment
FROM InternalRevenue i;

-- 4. DAU Trend with Platform Context
-- Joins internal player activity with market platform data
SELECT
    DATE(s.LoginTime) AS LogDate,
    p.DeviceType,
    COUNT(DISTINCT s.PlayerID) AS DAU
FROM sessions s
JOIN players p ON s.PlayerID = p.PlayerID
GROUP BY 1, 2
ORDER BY 1, 3 DESC;
