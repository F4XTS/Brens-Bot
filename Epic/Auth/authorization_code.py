import requests
import json

data1 = {
    'grant_type': 'authorization_code',
    'code': '735d5711e8f7499dacc892fa03e58bd9'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
}

r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
data = r.json
print("Here Is Your Account Data! ------------ " + str(r.json()))

with open('Account.json', 'w') as f:
    f.write(str(r.json()))
    print("\n\n\nYour Account JSON Was Created")