# Write your MySQL query statement below
SELECT
player_id,
MIN(event_date) AS first_login
From Activity
Group By player_id;


