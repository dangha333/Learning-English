import json
import requests
import time

def translate(text, target='vi'):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": target,
        "dt": "t",
        "q": text
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()[0][0][0]
    except Exception as e:
        print("Lỗi dịch:", e)
    return ""

with open("corpus.json", encoding="utf-8") as f:
    data = json.load(f)

for entry in data:
    example = entry.get("h", "")
    if example:
        entry["h_vi"] = translate(example)
        print(f"{example} -> {entry['h_vi']}")
        time.sleep(1)  # tránh bị chặn API

with open("corpus_translated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    