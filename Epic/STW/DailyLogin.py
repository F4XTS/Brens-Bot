import requests
import json

API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/"

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = DataToken["accessToken"]


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}

r = requests.post(API+'api/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/ClaimLoginReward?profileId=campaign', headers=headers, data="{}").json()

print(r)

