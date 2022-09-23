import requests
import json
import colorama
from colorama import Fore
import time

API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/cloudstorage/system/DefaultGame.ini"

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = DataToken["accessToken"]




headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}





r = requests.get(API, headers=headers)
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))

