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
    'Authorization': f'Bearer 9caf12962dbe44adb7689051739dea9b'
}

r = requests.post(API+'/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/SetAffiliateName?profileId=common_core&rvn=-1', headers=headers, data='{"affiliateName": "BHE"}')
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))

