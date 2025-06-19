import duckdb

con = duckdb.connect("potloc.db")

con.execute("CREATE TABLE bixi_trips AS SELECT * FROM read_csv_auto('data/bixi_trips.csv')")
con.execute("CREATE TABLE bixi_stations AS SELECT * FROM read_csv_auto('data/bixi_stations.csv')")
con.execute("CREATE TABLE montreal_weather AS SELECT * FROM read_csv_auto('data/montreal_weather_2025_Jan_May.csv')")