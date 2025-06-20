import duckdb

con = duckdb.connect("potloc.db")

con.execute("CREATE TABLE bixi_trips AS SELECT * FROM read_csv_auto('data/OD_2020.csv')")
con.execute("CREATE TABLE bixi_stations AS SELECT * FROM read_csv_auto('data/stations.csv')")
