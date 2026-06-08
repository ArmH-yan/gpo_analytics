-- Portfolio Project: Mobile Gaming Analytics
-- This script contains SQL queries for calculating key gaming KPIs.

-- 1. Daily Active Users (DAU)
-- Measures unique players who logged in on a specific date.
SELECT
    DATE(LoginTime) AS LogDate,
    COUNT(DISTINCT PlayerID) AS DAU
FROM sessions
GROUP BY 1
ORDER BY 1;

-- 2. Day 1 Retention Rate
-- Calculates the percentage of users who returned exactly one day after their registration.
WITH RegisterDate AS (
    SELECT PlayerID, DATE(RegistrationDate) AS RegDate
    FROM players
),
Activity AS (
    SELECT DISTINCT PlayerID, DATE(LoginTime) AS LoginDate
    FROM sessions
)
SELECT
    r.RegDate,
    COUNT(DISTINCT r.PlayerID) AS NewUsers,
    COUNT(DISTINCT a.PlayerID) AS RetainedUsers,
    ROUND(CAST(COUNT(DISTINCT a.PlayerID) AS FLOAT) / COUNT(DISTINCT r.PlayerID) * 100, 2) AS D1_Retention_Pct
FROM RegisterDate r
LEFT JOIN Activity a ON r.PlayerID = a.PlayerID AND a.LoginDate = DATE(r.RegDate, '+1 day')
GROUP BY 1
ORDER BY 1;

-- 3. Average Revenue Per User (ARPU) - Last 30 Days
-- Calculates total revenue divided by the total number of unique players in the last 30 days.
WITH ActivePlayers AS (
    SELECT COUNT(DISTINCT PlayerID) AS TotalPlayers
    FROM sessions
    WHERE LoginTime >= DATE('now', '-30 days')
),
Revenue AS (
    SELECT SUM(Amount) AS TotalRevenue
    FROM transactions
    WHERE Timestamp >= DATE('now', '-30 days')
)
SELECT
    TotalRevenue,
    TotalPlayers,
    ROUND(TotalRevenue / TotalPlayers, 2) AS ARPU
FROM Revenue, ActivePlayers;

-- 4. Player Segmentation by Spending
-- Categorizes players based on their lifetime spending.
SELECT
    p.PlayerID,
    COALESCE(SUM(t.Amount), 0) AS LifetimeSpend,
    CASE
        WHEN SUM(t.Amount) >= 500 THEN 'Whale'
        WHEN SUM(t.Amount) >= 100 THEN 'Dolphin'
        WHEN SUM(t.Amount) > 0 THEN 'Minnow'
        ELSE 'Non-Payer'
    END AS PlayerSegment
FROM players p
LEFT JOIN transactions t ON p.PlayerID = t.PlayerID
GROUP BY 1;
