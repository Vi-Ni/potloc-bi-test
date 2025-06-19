# BIXI Data Splitter Notebook

import pandas as pd

# Load the raw data
raw_data = pd.read_csv("data/Bixi_raw_202501_202505.csv")  # Replace with your actual filename

# Create a DataFrame with all unique stations (start and end)
start_stations = raw_data[[
    'STARTSTATIONNAME', 
    'STARTSTATIONARRONDISSEMENT', 
    'STARTSTATIONLATITUDE', 
    'STARTSTATIONLONGITUDE'
]].rename(columns={
    'STARTSTATIONNAME': 'STATIONNAME',
    'STARTSTATIONARRONDISSEMENT': 'STATIONARRONDISSEMENT',
    'STARTSTATIONLATITUDE': 'LATITUDE',
    'STARTSTATIONLONGITUDE': 'LONGITUDE'
})

end_stations = raw_data[[
    'ENDSTATIONNAME', 
    'ENDSTATIONARRONDISSEMENT', 
    'ENDSTATIONLATITUDE', 
    'ENDSTATIONLONGITUDE'
]].rename(columns={
    'ENDSTATIONNAME': 'STATIONNAME',
    'ENDSTATIONARRONDISSEMENT': 'STATIONARRONDISSEMENT',
    'ENDSTATIONLATITUDE': 'LATITUDE',
    'ENDSTATIONLONGITUDE': 'LONGITUDE'
})

# Concatenate and drop duplicates
stations = pd.concat([start_stations, end_stations], ignore_index=True).drop_duplicates().reset_index(drop=True)
stations['STATION_ID'] = stations.index

# Save to bixi_stations.csv
stations.to_csv("bixi_stations.csv", index=False)

# Merge to get station IDs for start and end
trips = raw_data.copy()

# Merge for START STATION
trips = trips.merge(
    stations,
    how='left',
    left_on=['STARTSTATIONNAME', 'STARTSTATIONARRONDISSEMENT', 'STARTSTATIONLATITUDE', 'STARTSTATIONLONGITUDE'],
    right_on=['STATIONNAME', 'STATIONARRONDISSEMENT', 'LATITUDE', 'LONGITUDE']
).rename(columns={'STATION_ID': 'START_STATION_ID'})

# Drop merged columns
trips = trips.drop(columns=['STATIONNAME', 'STATIONARRONDISSEMENT', 'LATITUDE', 'LONGITUDE'])

# Merge for END STATION
trips = trips.merge(
    stations,
    how='left',
    left_on=['ENDSTATIONNAME', 'ENDSTATIONARRONDISSEMENT', 'ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE'],
    right_on=['STATIONNAME', 'STATIONARRONDISSEMENT', 'LATITUDE', 'LONGITUDE']
).rename(columns={'STATION_ID': 'END_STATION_ID'})

# Drop merged columns
trips = trips.drop(columns=[
    'STATIONNAME', 'STATIONARRONDISSEMENT', 'LATITUDE', 'LONGITUDE',
    'STARTSTATIONNAME', 'STARTSTATIONARRONDISSEMENT', 'STARTSTATIONLATITUDE', 'STARTSTATIONLONGITUDE',
    'ENDSTATIONNAME', 'ENDSTATIONARRONDISSEMENT', 'ENDSTATIONLATITUDE', 'ENDSTATIONLONGITUDE'
])

# Reorder columns if desired
trips = trips[['START_STATION_ID', 'END_STATION_ID', 'STARTTIMEMS', 'ENDTIMEMS']]

# Save to bixi_trips.csv
trips.to_csv("bixi_trips.csv", index=False)

print("Done! 'bixi_stations.csv' and 'bixi_trips.csv' created.")
