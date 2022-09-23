import requests
import json
import colorama
from colorama import Fore
import time

#Affiliate = input(Fore.LIGHTBLUE_EX+"Sac: ")
#time.sleep(0.2)

PUBLIC_BASE_URL = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = DataToken["accessToken"]

payload={}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}




r = requests.post(f'{PUBLIC_BASE_URL}/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/ClaimLoginReward?profileId=profile0&rvn=-1',data=payload ,headers=headers)
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))

