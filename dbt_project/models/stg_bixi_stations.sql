
WITH base AS (
    SELECT *
    FROM {{ source('raw', 'bixi_stations') }}
)

SELECT
    code,
    name,
    latitude,
    longitude
FROM base
