import duckdb

# Connect to the database
con = duckdb.connect("potloc.db")

# List all tables
tables = con.execute("SHOW TABLES").fetchall()

print("📊 Tables and Sample Data in potloc.db\n")

for (table_name,) in tables:
    print(f"🗂️ Table: {table_name}")

    # Get column names
    columns = con.execute(f"PRAGMA table_info('{table_name}')").fetchall()
    col_names = [col[1] for col in columns]
    print("   Columns:")
    for col in col_names:
        print(f"     - {col}")

    # Show first 5 rows
    print("   Sample rows:")
    rows = con.execute(f"SELECT * FROM {table_name} LIMIT 5").fetchall()
    for row in rows:
        print(f"     {row}")

    print("")
