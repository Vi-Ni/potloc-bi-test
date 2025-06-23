import duckdb
import sys
import os

# Connect to the database
con = duckdb.connect("potloc.db")

# Get optional table name from command-line arguments
table_to_export = sys.argv[1] if len(sys.argv) > 1 else None

# Fetch all table names
tables = [row[0] for row in con.execute("SHOW TABLES").fetchall()]

if table_to_export:
    if table_to_export in tables:
        print(f"🗂️ Exporting specified table: {table_to_export}")
        con.execute(f"""
            COPY (SELECT * FROM {table_to_export})
            TO './export/{table_to_export}.csv' (HEADER, DELIMITER ',');
        """)
    else:
        print(f"❌ Error: Table '{table_to_export}' does not exist in the database.")
else:
    if not tables:
        print("⚠️ No tables found in the database.")
    for table_name in tables:
        print(f"🗂️ Exporting table: {table_name}")
        con.execute(f"""
            COPY (SELECT * FROM {table_name})
            TO './export/{table_name}.csv' (HEADER, DELIMITER ',');
        """)