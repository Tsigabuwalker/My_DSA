# Write your MySQL query statement below
SELECT 
    sample_id,
    dna_sequence,
    species,
    -- Pattern 1: Starts with ATG
    CASE WHEN dna_sequence LIKE 'ATG%' THEN 1 ELSE 0 END AS has_start,
    -- Pattern 2: Ends with TAA, TAG, or TGA
    CASE WHEN dna_sequence LIKE '%TAA' 
           OR dna_sequence LIKE '%TAG' 
           OR dna_sequence LIKE '%TGA' THEN 1 ELSE 0 END AS has_stop,
    -- Pattern 3: Contains the motif ATAT
    CASE WHEN dna_sequence LIKE '%ATAT%' THEN 1 ELSE 0 END AS has_atat,
    -- Pattern 4: Contains at least 3 consecutive Gs
    CASE WHEN dna_sequence LIKE '%GGG%' THEN 1 ELSE 0 END AS has_ggg
FROM Samples
ORDER BY sample_id ASC;