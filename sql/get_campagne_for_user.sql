SELECT 
    id,
    name,
    start_date,
    end_date
FROM Campaign
WHERE user_id = ?