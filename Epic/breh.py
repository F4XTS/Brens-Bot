import requests
code = input()

data1 = {
    'grant_type': 'authorization_code',
    'code': code
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
}

r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
data0 = r.json()
print(data0)
token = data0["access_token"]