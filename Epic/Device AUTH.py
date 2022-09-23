import requests


################

code = input("Code: ")

data = {
        'grant_type': 'authorization_code',
        'code': code
       }
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
}
    
r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data, headers=headers)
data = r.json()
print(data)
token = data["access_token"]

headers1 = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded"
},
data1 = {
    "prompt=login"
}

#url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization"


r = requests.post('https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization', headers=headers1, data=data1)

print(r.json())
