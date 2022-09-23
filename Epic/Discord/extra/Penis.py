@slash.slash(name='login', description='Log into your Epic Games account.', options=[
    create_option(
        name='auth',
        description='32-character Auth Code',
        option_type=3,
        required=False
    )
])
#@commands.cooldown(1, 30, commands.BucketType.user)
async def login(ctx, auth:str = None):
    if auth is None:
        embed = discord.Embed(
            color = discord.Colour.blue(),
            title='Login to your Epic Games account',
            description='[CLICK ME TO GET YOUR AUTH CODE](https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3Dec684b8c687f479fadea3cb2ad83f5c6%26responseType%3Dcode)\n\nHow to login to your Epic Games account:\n\n1. Visit the link above to get your login code.\n2. Copy the 32 character code that looks like **aabbccddeeff11223344556677889900**, located after **authorizationCode=**.\n3. Send /login <32 character code> to complete your login.\n\n**Need to switch accounts?**\n[Use this link instead](https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3f69e56c7649492c8cc29f1af08a8a12%26responseType%3Dcode&prompt=login)'
        )
        embed.set_footer(text='We recommend that you only log into accounts that you have email access to!')
        embed.set_image(url='https://i.giphy.com/media/lgfx857KjNNxpmHhig/giphy.gif')

        await ctx.send(embed=embed)
    else: # The real command

        # Code below generates a epic auth token
        response = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token', headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ=" # Auth provided by M1
        },
        data={
            "grant_type": "authorization_code",
            "code": auth
        }
        )


        try:
            token = response.json()['access_token']
            print('Generated new token for account')
        except:
            embed = discord.Embed(
                color = discord.Colour.red(),
                title='ERROR',
                description='Invalid access token was entered.'
            )
            return await ctx.send(embed=embed)
        accountID = response.json()['account_id']

        #await ctx.send(f"Generated auth token. Expires at {response.json()['expires_at']}")
        await ctx.author.send(f"I have just generated a new token for you.\nThis token Expires at {response.json()['expires_at']}") # Sends a DM to the author (success)

        a_file = open(f"auths.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        DiscordauthorID = ctx.author.id

        # Checks the auths array to see if discord author ID is in it. If it is, the bot will refresh the token and notice it.
        for x in json_object['auths']:
            if x['DiscordauthorID'] == str(DiscordauthorID):
    
                response = requests.get(f'https://fortnite-api.com/v2/stats/br/v2/{accountID}', headers=headerslmao)
                clientUsername = response.json()['data']['account']['name']
            

                response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena',  json={"text": {}}, headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
                )

                try:
                    error = response.json()['errorCode']
                    embed = discord.Embed(
                        color = discord.Colour.red(),
                        title = 'LOGIN FAILED!',
                        description=f'{error}'
                    )
                    return await ctx.send(embed=embed)
                except:
                    pass
                
                #print(response.json())
                created = response.json()['profileChanges'][0]['profile']['created']
                created = created[:10]
                updated = response.json()['profileChanges'][0]['profile']['updated']
                updated = updated[:10]

                embed = discord.Embed(
                    color = discord.Colour.red(),
                    title=f'Welcome back, {clientUsername}!'
                )
                embed.add_field(name='Account ID', value=f'{accountID}')
                embed.add_field(name='Created at', value=created)
                embed.add_field(name='Last updated', value=updated)

                loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
                print(loadoutUUID)
                #for i in profileChanges[0].profile.stats.attributes.loadouts
                for i in json_object['auths']:
                    if i['DiscordauthorID'] == str(DiscordauthorID):
                        #print('a')
                        print('Found client :)') # If this happens, the user is already logged in.
                        i['loadoutUUID'] = loadoutUUID

                lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
                lockerskinID = lockerdata['Character']['items'][0]
                lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
                response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
                url = response.json()['data']['images']['icon']
                embed.set_thumbnail(url=url)
            
                #profileChanges[0].profile.items["b085ba91-2bdb-43c8-9a1a-01949ca040f9"]
                #await ctx.send('test')
                await ctx.send(embed=embed)

                x['loadoutUUID'] = f"{loadoutUUID}"
                x['token'] = f"{token}"
                x['accountID'] = f"{accountID}"
                x['accountName'] = f"{clientUsername}"


                a_file = open(f"auths.json", "w")
                json.dump(json_object, a_file, indent = 4)
                return await ctx.author.send('It looks like you are already logged in, or you are using the bot again after logging out!\nI changed your token anyways, its now updated with a new one.')
        
        # Below is if a user uses the bot for the first time.

        await ctx.author.send('Thank you for using our bot for the first time. You are now added into our system.')

        # Below dumps all data except loadout UUID and account name. We will dump it later.
        json_object['auths'].append({
            "DiscordauthorID": f"{DiscordauthorID}",
            "token": f"{token}",
            #"authCode": f'{auth}',
            "accountID": f"{accountID}",
            "loadoutUUID": "",
            "accountName": ""
        })
        a_file = open(f"auths.json", "w")
        
        # Below grabs the account username with Fortnite-API.
        response = requests.get(f'https://fortnite-api.com/v2/stats/br/v2/{accountID}', headers=headerslmao)
        try:
            clientUsername = response.json()['data']['account']['name']
        except:
            clientUsername = 'error'

        # Accessing Query Profile to get locker data...
        response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena',  json={"text": {}}, headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        )
        
        # Created/Updated
        created = response.json()['profileChanges'][0]['profile']['created']
        created = created[:10]
        updated = response.json()['profileChanges'][0]['profile']['updated']
        updated = updated[:10]

        # Creates embed
        embed = discord.Embed(
            color = discord.Colour.red(),
            title=f'Welcome, {clientUsername}!'
        )
        embed.add_field(name='Account ID', value=f'{accountID}')
        embed.add_field(name='Created at', value=created)
        embed.add_field(name='Last updated', value=updated)

        # Uses query profile to grab UUID
        loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
        
        # Now, we load back into the token array and dump account name and loadout UUID. We do this by finding the author discord ID, which is already in the array.
        for i in json_object['auths']:
            if i['DiscordauthorID'] == str(DiscordauthorID):
                print('Found client :)') # Used to know we found client
                i['loadoutUUID'] = loadoutUUID
                i['accountName'] = clientUsername
                json.dump(json_object, a_file, indent = 4)
        
        # Now, we are grabbing the author's locker data to retreive the current skin.
        # We use the loadout UUID thats in the array.

        lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
        lockerskinID = lockerdata['Character']['items'][0]
        lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
        url = response.json()['data']['images']['icon']
        embed.set_thumbnail(url=url)

        await ctx.send(embed=embed) # Sends embed