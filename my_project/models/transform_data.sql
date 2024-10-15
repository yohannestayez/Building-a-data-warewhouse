{{ config(materialized='table') }}

WITH raw_data AS (
    SELECT 
        'DoctorsET' AS source,
        content AS message,
        sender_id,
        date AS timestamp,  -- Using 'date' as the timestamp
        NULL AS status  -- Assuming DoctorsET does not have a status column
    
    FROM "warehouse"."public"."DoctorsET_messages"
    
    UNION ALL

    SELECT 
        'EAHCI' AS source,
        content AS message,
        sender_id,
        date AS timestamp,  -- Using 'date' as the timestamp
        NULL AS status  -- Assuming EAHCI does not have a status column

    FROM "warehouse"."public"."EAHCI_messages"
    
    UNION ALL

    SELECT 
        'lobelia4cosmetics' AS source,
        content AS message,
        sender_id,
        date AS timestamp,  -- Using 'date' as the timestamp
        NULL AS status  -- Assuming lobelia4cosmetics does not have a status column

    FROM "warehouse"."public"."lobelia4cosmetics_messages"
    
    UNION ALL

    SELECT 
        'yetenaweg' AS source,
        content AS message,
        sender_id,
        date AS timestamp,  -- Using 'date' as the timestamp
        NULL AS status  -- Assuming yetenaweg does not have a status column

    FROM "warehouse"."public"."yetenaweg_messages"
),

-- Clean and format the data
cleaned_data AS (
    SELECT
        source,
        message,
        sender_id::BIGINT AS sender_id,  -- Change INT to BIGINT
        timestamp,
        status
    FROM raw_data
    WHERE status IS NULL  -- Exclude rows with status, as all are assumed NULL
),

-- Ensure distinct records
final_data AS (
    SELECT DISTINCT 
        source,
        message,
        sender_id,
        timestamp,
        'Unknown' AS status_description  -- Default status description since all are unknown
    FROM cleaned_data
)

-- Final selection of transformed data
SELECT * 
FROM final_data
ORDER BY timestamp DESC
