-- Portfolio Project: Mobile Gaming Analytics (PostgreSQL / BigQuery Compatible)
-- This script contains SQL queries for calculating key gaming KPIs.

-- 1. Daily Active Users (DAU)
-- Measures unique players who logged in on a specific date.
SELECT
    DATE(LoginTime) AS LogDate,
    COUNT(DISTINCT PlayerID) AS DAU
FROM sessions
GROUP BY 1
ORDER BY 1;

-- 2. Day 1 Retention Rate (Using Window Functions)
-- Calculates the percentage of users who returned exactly one day after their registration.
WITH PlayerActivity AS (
    SELECT
        p.PlayerID,
        p.RegistrationDate::DATE AS RegDate,
        s.LoginTime::DATE AS ActivityDate
    FROM players p
    JOIN sessions s ON p.PlayerID = s.PlayerID
),
RetentionFlags AS (
    SELECT
        RegDate,
        PlayerID,
        MAX(CASE WHEN ActivityDate = RegDate + INTERVAL '1 day' THEN 1 ELSE 0 END) AS D1_Retained
    FROM PlayerActivity
    GROUP BY 1, 2
)
SELECT
    RegDate,
    COUNT(PlayerID) AS NewUsers,
    SUM(D1_Retained) AS RetainedUsers,
    ROUND(SUM(D1_Retained)::NUMERIC / COUNT(PlayerID) * 100, 2) AS D1_Retention_Pct
FROM RetentionFlags
GROUP BY 1
ORDER BY 1;

-- Note for BigQuery: Use DATE_ADD(RegDate, INTERVAL 1 DAY) instead of RegDate + INTERVAL '1 day'.

-- 3. Average Revenue Per User (ARPU) - Last 30 Days
-- Calculates total revenue divided by the total number of unique players in the last 30 days.
WITH ActivePlayers AS (
    SELECT COUNT(DISTINCT PlayerID) AS TotalPlayers
    FROM sessions
    WHERE LoginTime >= CURRENT_DATE - INTERVAL '30 days'
),
Revenue AS (
    SELECT SUM(Amount) AS TotalRevenue
    FROM transactions
    WHERE Timestamp >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT
    TotalRevenue,
    TotalPlayers,
    ROUND(TotalRevenue::NUMERIC / NULLIF(TotalPlayers, 0), 2) AS ARPU
FROM Revenue, ActivePlayers;

-- 4. Player Segmentation by Spending (LTV Ranking)
-- Categorizes players based on their lifetime spending using NTILE or CASE.
SELECT
    p.PlayerID,
    COALESCE(SUM(t.Amount), 0) AS LifetimeSpend,
    CASE
        WHEN SUM(t.Amount) >= 500 THEN 'Whale'
        WHEN SUM(t.Amount) >= 100 THEN 'Dolphin'
        WHEN SUM(t.Amount) > 0 THEN 'Minnow'
        ELSE 'Non-Payer'
    END AS PlayerSegment,
    PERCENT_RANK() OVER (ORDER BY SUM(t.Amount) DESC) AS SpendPercentile
FROM players p
LEFT JOIN transactions t ON p.PlayerID = t.PlayerID
GROUP BY p.PlayerID;
