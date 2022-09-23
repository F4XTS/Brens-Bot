
import requests

accountid = 'eee7f955847e486287cf67f11613fe1d'

rr = requests.get("https://api.nitestats.com/v1/epic/bearer")
DataToken = rr.json()
BearerToken = 'c8798290147e45f7b5941310b3fdfd64'



data1 = {
    'grant_type': 'authorization_code',
    'code': '9cf7664f990f41b6b7501a2a2bbd19d6'
}


headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {BearerToken}'
}

#playlistid = 'Playlist_BattleLab'



r = requests.post(f'https://fn-service-discovery-live-public.ogs.live.on.epicgames.com/api/v1/links/favorites/eee7f955847e486287cf67f11613fe1d', headers=headers, data=data1)
data = r.json()
print(data)