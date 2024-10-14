{{ config(materialized='table') }}

WITH raw_data AS (
    -- Combine all messages into one dataset
    SELECT 
        'CheMed123' AS source,
        content AS message,
        sender_id,
        timestamp,
        status
    FROM "warehouse"."public"."CheMed123_messages"
    
    UNION ALL

    SELECT 
        'DoctorsET' AS source,
        content AS message,
        sender_id,
        timestamp,
        status
    FROM "warehouse"."public"."DoctorsET_messages"
    
    UNION ALL

    SELECT 
        'EAHCI' AS source,
        content AS message,
        sender_id,
        timestamp,
        status
    FROM "warehouse"."public"."EAHCI_messages"
    
    UNION ALL

    SELECT 
        'lobelia4cosmetics' AS source,
        content AS message,
        sender_id,
        timestamp,
        status
    FROM "warehouse"."public"."lobelia4cosmetics_messages"
    
    UNION ALL

    SELECT 
        'yetenaweg' AS source,
        content AS message,
        sender_id,
        timestamp,
        status
    FROM "warehouse"."public"."yetenaweg_messages"
),

-- Clean and format the data
cleaned_data AS (
    SELECT
        source,
        message,
        sender_id::INT AS sender_id,  -- Ensure sender_id is an integer
        timestamp,
        status
    FROM raw_data
    WHERE status IS NOT NULL  -- Exclude rows with null status
),

-- Ensure distinct records
final_data AS (
    SELECT DISTINCT 
        source,
        message,
        sender_id,
        timestamp,
        CASE 
            WHEN status = 'sent' THEN 'Sent'
            WHEN status = 'received' THEN 'Received'
            ELSE 'Unknown'
        END AS status_description
    FROM cleaned_data
)

-- Final selection of transformed data
SELECT * 
FROM final_data
ORDER BY timestamp DESC