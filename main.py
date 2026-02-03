import requests
from datetime import datetime, date
url = "https://api.waktusolat.app/v2/solat/WLY01"
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()
today_day = date.today().day
today_prayers = next(item for item in data["prayers"] if item["day"] == today_day)
for name in ["fajr", "syuruk", "dhuhr", "asr", "maghrib", "isha"]:
    ts = today_prayers[name]
    readable = datetime.fromtimestamp(ts).strftime("%H:%M")
    print(f"{name.capitalize():8}: {readable}")
