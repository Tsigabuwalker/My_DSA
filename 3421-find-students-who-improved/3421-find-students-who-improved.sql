# Write your MySQL query statement below
WITH ScoreRanking AS (
    SELECT 
        student_id,
        subject,
        score,
        -- Rank dates to find the first exam
        RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date ASC) as first_rank,
        -- Rank dates to find the latest exam
        RANK() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) as latest_rank,
        -- Count total exams to ensure there are at least two
        COUNT(*) OVER (PARTITION BY student_id, subject) as exam_count
    FROM Scores
)
SELECT 
    s1.student_id, 
    s1.subject, 
    s1.score AS first_score, 
    s2.score AS latest_score
FROM ScoreRanking s1
JOIN ScoreRanking s2 
    ON s1.student_id = s2.student_id 
    AND s1.subject = s2.subject
WHERE 
    s1.first_rank = 1         -- Pick the first score
    AND s2.latest_rank = 1    -- Pick the latest score
    AND s1.exam_count >= 2    -- Must have at least two exams
    AND s2.score > s1.score   -- Latest score must be higher than first score
ORDER BY 
    student_id, 
    subject;