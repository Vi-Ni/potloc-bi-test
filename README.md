# Potloc BI Developer Technical Test

## 🏛 Overview

This technical test is designed to evaluate your ability to:

- Transform raw data into usable models using dbt
- Create clear, impactful dashboards with Looker Studio
- Draw and present meaningful business insights

We expect this test to take approximately **2-3 hours**. Please do not over-optimize or stress; the goal is to understand your working style and analytical thinking.

---

## ✅ Deliverables

You don’t need to submit anything in advance, just be ready to share during the interview:

* A link to your **dashboard**
* Your **code or transformations** (optional GitHub repo, SQL file, etc.)
* Any additional support material if you wish (not required)

---

## 🔧 Setup Instructions (Windows/macOS)

### 🌐 System Prerequisites

- Python 3.8+
- Git installed
- [Poetry](https://python-poetry.org/docs/#installation) installed (`pip install poetry` or via install script)

### ⚡ Step-by-Step Setup

1. **Fork the repository**

   - Visit the GitHub repo link
   - Click **"Fork"** in the top-right corner
   - Clone it locally:

     ```bash
     git clone https://github.com/your-username/potloc-bi-test.git
     cd potloc-bi-test
     ```

   NOTE: you will not be able to commit your changes because the data files are above the GitHub limit of 100Mb.
2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```
3. **Download raw Bixi data for 2020**

   - Go to [Bixi Open Data](https://bixi.com/en/open-data) and download the CSV files for the year 2020.
     - Feel free to use other years in addition to 2020,
       but note that the data format may change, which may complexify the loading and transformations later on.
   - Place the downloaded CSV files without renaming in the `data` folder at the root of this repository.
4. **Load data into DuckDB**
   Run the import script:

   ```bash
   poetry run python code/import_data.py
   ```

   This will create a local database (`potloc.db`) with tables from the CSVs.
5. **Show the header of each imported tables**

   Run the script:

   ```bash
   poetry run python code/show_table_headers.py
   ```
6. **Run dbt commands**
   Inside the dbt_project directory:

   ```bash
   cd dbt_project
   poetry run dbt debug --profiles-dir .dbt
   poetry run dbt run --profiles-dir .dbt
   poetry run dbt test --profiles-dir .dbt
   ```

### 🗂️ Export your final model from DuckDB

1. **Export all tables**

   - Make sure you're in the project root (not inside the `dbt_project` folder).If you're in `dbt_project`, go back one level:

     ```bash
     cd ..
     ```
   - Then run the export script:

     ```bash
     poetry run python code/export_duckdb.py
     ```

   This will export all tables from the `potloc.db` database into the `export` folder.
2. **Export a specific table**

   - To export only one table, add its name at the end of the command.
     For example, to export the `stg_bixi_stations` table:

     ```bash
     poetry run python code/export_duckdb.py stg_bixi_stations
     ```

   The selected table will be saved as a `.csv` file in the `export` folder.

### ⚠️ If dbt Does Not Work

If you're unable to run dbt for technical reasons:

- You may use pure SQL files and a short write-up explaining your logic
- Focus on showing: cleaned data, aggregation logic, and field naming decisions
- You can still export a `.csv` and build the dashboard

---

## 📈 Dashboarding (Looker Studio)

1. Upload you final output csv to:

   - Google Sheets (recommended)
   - Or Google BigQuery (if you have access)
2. [Optional] Use other public datasets to cross with the Bixi aggregated data.

   - We recommend joining the other datasets in Google Sheets or Bigquery, since data loading is not part of the job description.
3. Build a dashboard in Looker Studio (preferred, but you can use another tool).
4. Prepare some key insights as if presenting to decision makers at Bixi.

---

## 🙌 Tips

* Keep it simple. You have only 2 to 3 hours.
* Focus on clarity, insights, and story.
* Don’t hesitate to get creative, we’re looking to learn how you think.

We’re excited to see what you’ll come up with!
