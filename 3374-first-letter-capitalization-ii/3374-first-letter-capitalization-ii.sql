WITH RECURSIVE split AS (
    SELECT
        content_id,
        content_text,
        1 AS pos,
        SUBSTRING_INDEX(content_text, ' ', 1) AS word,
        SUBSTRING(content_text, LENGTH(SUBSTRING_INDEX(content_text, ' ', 1)) + 2) AS rest
    FROM user_content
    
    UNION ALL
    
    SELECT
        content_id,
        content_text,
        pos + 1,
        SUBSTRING_INDEX(rest, ' ', 1),
        SUBSTRING(rest, LENGTH(SUBSTRING_INDEX(rest, ' ', 1)) + 2)
    FROM split
    WHERE rest <> ''
),
transformed AS (
    SELECT
        content_id,
        content_text,
        pos,
        CASE
            WHEN LOCATE('-', word) > 0 THEN
                CONCAT(
                    UPPER(LEFT(SUBSTRING_INDEX(word, '-', 1), 1)),
                    LOWER(SUBSTRING(SUBSTRING_INDEX(word, '-', 1), 2)),
                    '-',
                    UPPER(LEFT(SUBSTRING_INDEX(word, '-', -1), 1)),
                    LOWER(SUBSTRING(SUBSTRING_INDEX(word, '-', -1), 2))
                )
            ELSE
                CONCAT(
                    UPPER(LEFT(word, 1)),
                    LOWER(SUBSTRING(word, 2))
                )
        END AS new_word
    FROM split
)
SELECT
    content_id,
    content_text AS original_text,
    GROUP_CONCAT(new_word ORDER BY pos SEPARATOR ' ') AS converted_text
FROM transformed
GROUP BY content_id, content_text;
