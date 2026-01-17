# Write your MySQL query statement below
-- 1. Create the 'Low Salary' row
SELECT 
    'Low Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000

UNION

-- 2. Create the 'Average Salary' row
SELECT 
    'Average Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income >= 20000 AND income <= 50000

UNION

-- 3. Create the 'High Salary' row
SELECT 
    'High Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;