SELECT 
    visited_on, 
    amount, 
    average_amount
FROM (
    SELECT 
        visited_on,
        SUM(SUM(amount)) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(SUM(amount)) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount,
        -- Check if there are at least 6 rows before the current one
        LAG(visited_on, 6) OVER (ORDER BY visited_on) AS start_check
    FROM Customer
    GROUP BY visited_on
) t
WHERE start_check IS NOT NULL
ORDER BY visited_on;