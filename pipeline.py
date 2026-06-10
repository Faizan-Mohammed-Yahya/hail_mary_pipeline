import requests
import pandas as pd
from datetime import datetime

# --- STEP 1: EXTRACT ---
url = "https://api.open-meteo.com/v1/forecast?latitude=24.7136&longitude=46.6753&current_weather=true"

print("📡 Extracting live weather data for Riyadh...")
response = requests.get(url)
weather_data = response.json()
print("✅ Extraction complete.")

# --- STEP 2: TRANSFORM ---
print("🧹 Starting data transformation...")
current = weather_data["current_weather"]

cleaned_record = {
    "City": "Riyadh",
    "Extraction Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Temperature_C": current["temperature"],
    "WindSpeed_kmh": current["windspeed"],
    "WindDirection": f"{current['winddirection']}°",
    "WeatherCode": current["weathercode"]
}

df = pd.DataFrame([cleaned_record])
print("✅ Transformation complete.")

# --- STEP 3: LOAD (SAVE THE DATA) ---
print("💾 Loading data into storage...")

# This single line saves our table into a permanent file named 'riyadh_weather.csv'
# 'mode="a"' means APPEND: if the file already exists, it will just add a new row at the bottom!
# 'header=False' ensures we don't accidentally write the column names over and over again.
import os
file_exists = os.path.isfile("riyadh_weather.csv")

df.to_csv("riyadh_weather.csv", mode="a", index=False, header=not file_exists)

print("🎉 Success! The data has been saved to 'riyadh_weather.csv'.")