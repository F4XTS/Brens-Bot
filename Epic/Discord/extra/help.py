import requests
import json

cosmeticid = input("ID: ")

r = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/{cosmeticid}')
data = r.json()

name = data["data"]["name"]
icon = data["data"]["images"]["icon"]
datajson = json.dump(data, indent=4)

print(f"NAME: {name}")
print(f"IconURL: {icon}")

print(f"\n\n\nJSON:\n{datajson} ")
