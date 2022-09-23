import requests
import json

API = "https://account-public-service-prod03.ol.epicgames.com/account/"

payload='prompt=login'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer e1adddfa1608447c81304924d9e2753e'
}

r = requests.post('https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization?prompt%3D=login', headers=headers, data=payload)

print(r.text)

