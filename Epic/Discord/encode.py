import base64
import json

f = open('./Epic/Discord/Clients.json')
  

data = json.load(f)

for i in data['fortnitePCGameClient']['ClientID']:
    FNPC_ClientID=i
for i2 in data['fortnitePCGameClient']['Secret']:
    FNPC_Secret=i2
    

fortnitePCGameClient = base64.b64encode(f"{FNPC_ClientID}:{FNPC_Secret}")

print(fortnitePCGameClient)