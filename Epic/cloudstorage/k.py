import requests
import json


API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/cloudstorage/system/DefaultGame.ini"

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = DataToken["accessToken"]

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}

API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/"



headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer fff90358489a48ea94d3670838c974c1'
}

r = requests.get(API+'api/cloudstorage/storage/DefaultGame.ini/info', headers=headers)
open('DefaultRuntimeOptions.ini', 'wb').write(r.content)
Reeee = r.json()
print(str(json.dumps(Reeee, indent=4)))


