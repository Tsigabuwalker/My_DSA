WITH user_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS prompt_count,
        AVG(tokens) AS avg_tokens
    FROM prompts
    GROUP BY user_id
)
SELECT 
    u.user_id,
    u.prompt_count,
    ROUND(u.avg_tokens, 2) AS avg_tokens
FROM user_stats u
WHERE u.prompt_count >= 3
  AND EXISTS (
        SELECT 1
        FROM prompts p
        WHERE p.user_id = u.user_id
          AND p.tokens > u.avg_tokens
  )
ORDER BY avg_tokens DESC, user_id ASC;