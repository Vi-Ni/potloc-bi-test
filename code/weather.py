# 📦 Install if needed:
# !pip install pandas requests

import pandas as pd
import requests
from datetime import datetime, timedelta

# === Configuration ===
API_KEY = "WA6QESSBKVT85DM55MPUB342N"
LOCATION = "Montreal,QC,Canada"
START_DATE = "2025-01-01"
END_DATE = "2025-05-31"
OUTPUT_CSV = "montreal_weather_2025_Jan_May.csv"

# === Fetch data ===
url = (
    f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    f"{LOCATION}/{START_DATE}/{END_DATE}"
    f"?unitGroup=metric&elements=datetime,tempmax,tempmin,precip,humidity,windspeed"
    f"&include=days&key={API_KEY}&contentType=json"
)

resp = requests.get(url)
resp.raise_for_status()
data = resp.json()

# === Parse into DataFrame ===
records = []
for day in data.get("days", []):
    records.append({
        "date": day["datetime"],
        "tempmax_C": day.get("tempmax"),
        "tempmin_C": day.get("tempmin"),
        "precip_mm": day.get("precip"),
        "humidity_pct": day.get("humidity"),
        "windspeed_kmh": day.get("windspeed"),
    })

df = pd.DataFrame(records)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df.to_csv(OUTPUT_CSV, index=False)

print(f"✅ Saved {len(df)} rows to {OUTPUT_CSV}")
