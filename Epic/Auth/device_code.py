import requests
import json



headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE5MjA5ZDRhNWUyNWE0NTdmYjliMDc0ODlkMzEzYjQxYQ=='
}
data1 = {
    'grant_type': 'authorization_code',
    'code': '12bda1c1d9a243a7aca545109f7737c5'
}

r = requests.post('https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization', headers=headers, data='{"prompt": "login"}')
data = r.json()
print("Here Is Your Account Data! ------------ " + str(r.json()))

with open('Account.json', 'w') as f:
    f.write(str(r.json()))
    print("\n\n\nYour Account JSON Was Created")
    