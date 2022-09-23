import requests

url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/deviceAuthorization?prompt%3D=login"

payload='prompt=login'
headers = {
  'Authorization': 'Bearer 32794e9d1abf4fd880b288f1b2f9cd39',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)