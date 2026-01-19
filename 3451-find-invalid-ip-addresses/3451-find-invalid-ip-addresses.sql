# Write your MySQL query statement below
SELECT 
    ip, 
    COUNT(*) AS invalid_count
FROM logs
WHERE 
    -- 1. Check for octets > 255 OR leading zeros
    -- 2. Check for incorrect number of octets (not exactly 4)
    ip NOT REGEXP '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    OR ip REGEXP '\\.0[0-9]' -- Specifically catch leading zeros like .01
    OR ip REGEXP '^0[0-9]'   -- Specifically catch leading zeros at the start like 01.
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;