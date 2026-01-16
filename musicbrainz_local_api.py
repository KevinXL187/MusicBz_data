import requests, time, json

from urllib3 import request

BASE = "http://localhost:5000/ws/2"
HEADERS = {
    "User-Agent": "MyMBClient/1.0 (xinghai@example.com)",
    "Accept": "application/json",
}

def api_lookup():
    pass

def api_browse():
    pass

def  api_search(endpoint, params={}):
    params.setdefault("fmt", "json")
    r = requests.get(f"{BASE}{endpoint}", headers=HEADERS, params=params)
    r.raise_for_status()
    print("REQUEST:", r.url)
    #time.sleep(1,1)
    return r.json()

first_artists = api_search("/artist", 
                            {"query": "", 
                            "limit": 5})
print(json.dumps(first_artists, indent=2))