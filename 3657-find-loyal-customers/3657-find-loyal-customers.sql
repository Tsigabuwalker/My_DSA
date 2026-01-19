# Write your MySQL query statement below
SELECT 
    customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING 
    -- 1. Made at least 3 purchase transactions
    COUNT(CASE WHEN transaction_type = 'purchase' THEN 1 END) >= 3
    
    -- 2. Have been active for at least 30 days
    AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30
    
    -- 3. Refund rate is less than 20%
    AND (COUNT(CASE WHEN transaction_type = 'refund' THEN 1 END) / COUNT(*)) < 0.2
ORDER BY customer_id ASC;