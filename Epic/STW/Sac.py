import requests
import json
import colorama
from colorama import Fore
import time

#Affiliate = input(Fore.LIGHTBLUE_EX+"Sac: ")
#time.sleep(0.2)

API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = DataToken["accessToken"]



data1 = {
    'grant_type': 'authorization_code',
    'code': 'e89669b810bf4af0b48cf2fec67e3660'
}


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}





r = requests.post(API+'/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/SetHomebaseName?profileId=common_core&rvn=-1', headers=headers, data='{"homebaseName": "Brens Homebase"}')
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))

