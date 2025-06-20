
WITH base AS (
    SELECT *
    FROM {{ source('raw', 'bixi_trips') }}
)

SELECT
    start_date,
    start_station_code,
    end_date,
    end_station_code,
    duration_sec,
    is_member
FROM base
