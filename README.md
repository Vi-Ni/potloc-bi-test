# Potloc BI Developer Technical Test

## 🏛 Overview

This technical test is designed to evaluate your ability to:

- Transform raw data into usable models using dbt
- Create clear, impactful dashboards with Looker Studio
- Draw and present meaningful business insights

We expect this test to take approximately **3 hours**. Please do not over-optimize or stress; the goal is to understand your working style and analytical thinking.

---

## ✅ Deliverables

1. A GitHub repo fork with:
   - Completed dbt models
   - At least 1 test (`unique`, `not null`) in `schema.yml`
   - One `.md` file describing your mart model
2. A Looker Studio dashboard link
3. A short written summary or slides (optional)
4. During the interview, a 30-minute walkthrough of your work

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

2. **Install dependencies using Poetry**

   ```bash
   poetry install
   ```

3. **Download raw Bixi data for 2020**
   - Go to [Bixi Open Data](https://bixi.com/en/open-data) and download the CSV files for the year 2020.
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
   poetry run dbt docs generate && dbt docs serve --profiles-dir .dbt
   ```

### Export your final model (`mart_bixi_usage`) from DuckDB

**Prerequisite**: Ensure you have the DuckDB CLI installed and available in your PATH. If not, install it via:

- macOS (Homebrew): `brew install duckdb-cli`
- pip: `pip install duckdb`

```bash
duckdb ../potloc.db \
  -c "COPY (SELECT * FROM main.mart_bixi_usage) TO '../mart_bixi_usage.csv' (HEADER, DELIMITER ',');"
```

### ⚠️ If dbt Does Not Work

If you're unable to run dbt for technical reasons:

- You may use pure SQL files and a short write-up explaining your logic
- Focus on showing: cleaned data, aggregation logic, and field naming decisions
- You can still export a `.csv` and build the dashboard

---

## 📈 Dashboarding (Looker Studio)

1. Upload `final_output.csv` to:

   - Google Sheets (recommended)
   - Or Google BigQuery (if you have access)
2. Build a dashboard in Looker Studio

---

## 🧰 Analysis Prompts (Inspiration)

---

## 🔄 Submission Instructions

When you’re ready, please:

- Push your code to your GitHub fork
- Share the GitHub link and the Looker Studio dashboard link via email
- (Optional) Include any slides or notes you used

During your technical interview, you'll walk us through your work (~30 minutes).

Good luck and have fun — we’re excited to see your approach!
