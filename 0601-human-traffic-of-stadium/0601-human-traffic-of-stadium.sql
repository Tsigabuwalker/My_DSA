# Write your MySQL query statement below
WITH cte AS (
    SELECT *,
           LEAD(id,1) OVER (ORDER BY id)  AS next1,
           LEAD(id,2) OVER (ORDER BY id)  AS next2,
           LAG(id,1)  OVER (ORDER BY id)  AS prev1,
           LAG(id,2)  OVER (ORDER BY id)  AS prev2
    FROM Stadium
    WHERE people >= 100
)
SELECT id, visit_date, people
FROM cte
WHERE (next2 = id + 2)          -- I'm the start of 3+ consecutive
   OR (next1 = id + 1 AND prev1 = id - 1)   -- middle of sequence
   OR (prev2 = id - 2)          -- I'm the end of 3+ consecutive
ORDER BY visit_date;