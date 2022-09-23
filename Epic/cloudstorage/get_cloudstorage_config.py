import requests
import json
import colorama
from colorama import Fore
import time

#Affiliate = input(Fore.LIGHTBLUE_EX+"Sac: ")
#time.sleep(0.2)

API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"



headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer 290ef4eeeb764f1a9df4fab92a08c992'
}

r = requests.get(API+'https://fortnite-public-service-prod11.ol.epicgames.com/cloudstorage/Live/system/', headers=headers)
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))

