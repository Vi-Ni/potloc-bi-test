
WITH base AS (
    SELECT *
    FROM {{ source('raw', 'bixi_trips') }}
)

SELECT
    STARTTIMEMS AS start_time,
    ENDTIMEMS AS end_time,
    (end_time-start_time)/1000 as duration_sec,
    START_STATION_ID AS start_station_id,
    END_STATION_ID AS end_station_id,
FROM base
