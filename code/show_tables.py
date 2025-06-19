import duckdb

con = duckdb.connect("potloc.db")
tables = con.execute("SHOW TABLES").fetchall()
print(tables)