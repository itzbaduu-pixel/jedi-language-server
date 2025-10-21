import os
import json
import time
import requests
from datetime import datetime

# -------- Top 12 endpoints from your APK --------
ENDPOINTS = [
    "https://api.fastpay97.com",
    "https://api.whatsapp.com/send?phone=",
    "http://55lottery.com/#/register?r_code=5284741404",
    "http://www.w3.org/ns/widgets",
    "https://web.incasher.net/download/btwwin",
    "http://www.w3.org/html/wg/drafts/html/master/browsers.html#named-access-on-the-window-object",
    "http://social.msdn.microsoft.com/Forums/windowsapps/en-US/a327cf3c-f033-4a54-8b7f-03c56ba3203f/windows-foundation-uri-security-problem",
    "https://drawImage.app",
    "https://lotteryList.in",
    "https://DrawerArrowToggle.Com",
    "https://55lottery.com",
    "https://V25.App"
]

# -------- Setup folders --------
os.makedirs("responses", exist_ok=True)
log_file = open("log.txt", "a", encoding="utf-8")

def log(message):
    print(message)
    log_file.write(f"[{datetime.now().isoformat()}] {message}\n")
    log_file.flush()

# -------- Poll each endpoint --------
headers = {"User-Agent": "APK-Endpoint-Tester/1.0"}

for url in ENDPOINTS:
    log(f"\n🔍 Checking: {url}")
    try:
        start = time.time()
        resp = requests.get(url, headers=headers, timeout=10)
        elapsed = round(time.time() - start, 2)
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_").replace("?", "_")[:80]
        ext = "json" if "application/json" in resp.headers.get("Content-Type", "") else "txt"
        filepath = f"responses/{filename}.{ext}"

        with open(filepath, "w", encoding="utf-8") as f:
            try:
                content = resp.json()
                json.dump(content, f, indent=2, ensure_ascii=False)
            except Exception:
                f.write(resp.text)

        log(f"✅ SUCCESS ({resp.status_code}) [{elapsed}s] → saved to {filepath}")

    except Exception as e:
        log(f"❌ ERROR: {type(e).__name__}: {e}")

log("\n--- Test complete ---")
log_file.close()
