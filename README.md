# Riyadh Live Weather ETL Pipeline

An automated Python data pipeline that extracts live weather variables for Riyadh, Saudi Arabia, transforms the raw metrics, and handles structured storage for analysis. This project serves as a cornerstone of **Project Hail Mary**, a dedicated technical portfolio focused on computational data engineering.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **Version Control:** Git & GitHub
* **Environment:** VS Code (macOS)

---

## 🛰️ Pipeline Architecture

1. **Extraction:** Connects to live weather feeds to capture real-time ambient conditions for Riyadh.
2. **Transformation:** Cleanses, structures, and timestamps the incoming telemetry.
3. **Loading:** Appends the transformed data into a persistent local storage layer (`riyadh_weather.csv`).

---

## 📂 Project Structure
* `pipeline.py` - The core ETL runtime script executing extraction and transformation logic.
* `riyadh_weather.csv` - The local data destination containing stored climate snapshots.
