# Write your MySQL query statement below
WITH first_login AS (
    -- Get the first login date for each player
    SELECT 
        player_id, 
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
),
next_day_login AS (
    -- Find players who logged in the day after their first login
    SELECT DISTINCT f.player_id
    FROM first_login f
    JOIN Activity a
        ON f.player_id = a.player_id
       AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
)
SELECT 
    ROUND(
        COUNT(DISTINCT n.player_id) * 1.0 / COUNT(DISTINCT a.player_id), 
        2
    ) AS fraction
FROM Activity a
LEFT JOIN next_day_login n
    ON a.player_id = n.player_id;
