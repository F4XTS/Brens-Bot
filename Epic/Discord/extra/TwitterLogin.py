import requests
import json

data = {
        'grant_type': 'client_credentials',
}
headers = {
    'Authorization': ''
}

r = requests.post('https://api.twitter.com/oauth2/token',data=data, headers=headers)
data = r.json()