from ast import Mod
from cProfile import label
from dataclasses import MISSING
from http import client
from sys import prefix
import time
from turtle import back
from xml.etree.ElementInclude import include
from click import style
import discord
from discord import Component, Interaction, file
from discord import user
from discord.ext.commands.core import is_owner
from numpy import place
import requests
import json
import random
from discord.ext import commands
from discord.ext import tasks
from discord import File
from discord.ui import Button, View
#from discord_slash import SlashCommand

_intents = discord.Intents.all()
#bot = commands.Bot(command_prefix='!', intents=_intents)
bot = discord.Bot()

#aclint = client()
#bot = app_commands.CommandTree(aclint)


@bot.slash_command(name="login", description="Login to your Epic Games Account")
async def login(ctx, code):

    data1 = {
        'grant_type': 'authorization_code',
        'code': code
    }
    

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
    }
    
    r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
    data = r.json()
    print(data)
    token = data["access_token"]
    #filename = ("./accounts/"+str(ctx.author.id)+".json")



    #file = open(filename, 'a')
    #file = open(filename, 'a')
    #filename = file.read()
    #file.close()
    #print("Here Is Your Account Data! ------------ " + str("\r\r"+str(data())))
    #file = open(f'./accounts/discord.json', 'r')
    #FileData = file.read()
    if r.status_code == 200:
        #FNAPIHeaders = {'Authorization': '822445a7-3270-432b-95de-7d4e7f742566'}
        FNAPIHeaders = {'Authorization': '94aa02a1-deda7712-adc56662-69db0061'}
        payload = json.dumps({})
        accountID = data["account_id"]
       #print(token)
        response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
        clientUsername = response1.json()['name']
        print(f'Found Client ({clientUsername} - {accountID})!')

        #LOCKERINFO

        response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        filename = ("./accounts/"+str(ctx.author.id)+".json")
        file = open(filename, 'a')
        file.write(json.dumps(response.json(), indent=4))
        file.close()


        #print(response.json())
        loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
        level = response.json()['profileChanges'][0]['profile']['stats']['attributes']["level"]
        lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
        lockerskinID = lockerdata['Character']['items'][0]
        lockerpickaxeID = lockerdata['Pickaxe']['items'][0]
        lockerbackpackID = lockerdata['Backpack']['items'][0]
        #print(lockerdata)
        print(str(json.dumps(lockerdata, indent=4)))
        lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
        lockerpickaxeID = lockerpickaxeID.replace('AthenaPickaxe:', '')
        lockerbackpackID = lockerbackpackID.replace('AthenaBackpack:', '')
        
        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
        url = response.json()['data']['images']['icon']

        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
        skin = response.json()['data']['name']

        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerpickaxeID}')
        pickaxe = response.json()['data']['name']

        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerbackpackID}')
        if lockerbackpackID == "":
            backbling = "None"
        else:
            backbling = response.json()['data']['name']

        
        
        embed = discord.Embed(title="Logged In As "+clientUsername, color=discord.Color.random())
        #embed.add_field(name='Hello!', value=clientUsername, inline=False)
        embed.add_field(name='Account ID', value=accountID, inline=False)
        embed.add_field(name='Current Level', value=level, inline=False)
        embed.add_field(name='Current Skin', value=skin, inline=False)
        embed.add_field(name='Current Pickaxe', value=pickaxe, inline=False)
        embed.add_field(name='Current Backbling', value=backbling, inline=False)
        embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        #await ctx.send(
            #str("\r\r"+str(data()))
        #)
    else:
        await ctx.send("There Was A Error With Ur Login. \nError 404.")

@login.error
async def login_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error", color=discord.Color.random())
        await ctx.send(embed=embed)



@bot.command()
async def wear(ctx, code,*, item):


    responseFN = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={item}')

    
    data1 = {
        'grant_type': 'authorization_code',
        'code': code
    }
    

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
    }
    
    r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
    data = r.json()
    print(data)
    file = open('./accounts/discord.json', 'r')
    FileData = file.read()
    obj = json.loads(FileData)
    accountID = 'eee7f955847e486287cf67f11613fe1d'
    payload = json.dumps({})
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    token = data["access_token"]
    response1 = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={

        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    r = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=campaign&rvn=-1',data=payload,headers={

        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    #filename = ("./accounts/"+str(ctx.author.id)+".json")

    loadoutUUID = response1.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
    print(loadoutUUID)
    lockerdata = response1.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
    lockerskinID = lockerdata['Character']['items'][0]
    #print(lockerdata)
    print(str(json.dumps(lockerdata, indent=4)))
    lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
    category = responseFN.json()['data']['type']['backendValue']
    type = responseFN.json()['data']['type']['displayValue']

    payload = json.dumps({
        "lockerItem": f"{loadoutUUID}",
        "category": f"{category}".replace('Athena',''),
        "itemToSlot": f"{category}:{item}",
        "slotIndex": 0,
        "variantUpdates": [],
        "optLockerUseCountOverride": -1
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    button = Button(label="Equip", style=discord.ButtonStyle.green, emoji="✅")
    button1 = Button(label="Close", style=discord.ButtonStyle.red, emoji="✖️")

    item = responseFN.json()['data']['name']
    itemid = responseFN.json()['data']['id']

    itemdescription = responseFN.json()['data']['description']
    itemicon = responseFN.json()['data']['images']['icon']
    rarity = responseFN.json()['data']['rarity']['displayValue']
    
    embed = discord.Embed(description=itemdescription)
    #title=f"{type} Changed To **{item}**", color=discord.Color.random()
    embed.set_thumbnail(url=itemicon)
    embed.set_author(name=f'{item} - {rarity} {type}', icon_url=itemicon)
    embed.add_field(name = "ID", value=itemid)

    async def button_callback(interaction):
        Newembed = discord.Embed(title=f"{type} Changed To {item}", color=discord.Color.random())
        
        Newembed.set_thumbnail(url=itemicon)
        r = requests.post(API+'/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/SetCosmeticLockerSlot?profileId=athena&rvn=-1', headers=headers, data=payload)
        Reeee = r.json()
        await interaction.response.edit_message(embed=Newembed, view=None)
        print("Success")
        print(Reeee)
        #print(json.dumps(Reeee, indent=4))

    async def button1_callback(interaction):
        await interaction.response.edit_message(content="Oki", view=None)
    button.callback = button_callback
    button1.callback = button1_callback

    view = View()
    view.add_item(button)
    view.add_item(button1)
    await ctx.send(embed=embed, view=view)
    print(r.status_code)


@bot.command()
async def sac(ctx, code):
    file = open('./accounts/discord.json', 'r')
    FileData = file.read()
    obj = json.loads(FileData)
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"



    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer 133dad034b784cd985a6c4a0d8875588'
    }

    r = requests.post(API+'/game/v2/profile/eee7f955847e486287cf67f11613fe1d/client/SetAffiliateName?profileId=common_core&rvn=-1', headers=headers, data='{"affiliateName": "' + code + '"}' +"'")
    Reeee = r.json()
    if r.status_code == 200:
        embed = discord.Embed(title="Sac Changed!", color=discord.Color.random())
    else:
        embed = discord.Embed(title="Error 401", color=discord.Color.random())
    await ctx.send(embed=embed)
    print(r.status_code)



@bot.command()
async def claim(ctx, code):
    
    data1 = {
        'grant_type': 'authorization_code',
        'code': code
    }
    

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
    }
    
    r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
    data = r.json()
    print(data)
    file = open('./accounts/discord.json', 'r')
    FileData = file.read()
    obj = json.loads(FileData)
    accountID = 'eee7f955847e486287cf67f11613fe1d'
    payload = json.dumps({})
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    token = data["access_token"]

    payload = json.dumps({})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.post(API+'/g+', headers=headers, data=payload)
    print(r.json())
    ctx.send(r.json())
    filename = ("./accounts/"+str(ctx.author.id)+".json")
    file = open(filename, 'a')
    file.write(json.dumps(r.json(), indent=4))
    filename = file.read()
    file.close()



@bot.command()
async def vbuck(ctx, code):

    data1 = {
        'grant_type': 'authorization_code',
        'code': code
    }
    

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ='
    }
    
    r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data1, headers=headers)
    data = r.json()
    print(data)
    token = data["access_token"]
    #filename = ("./accounts/"+str(ctx.author.id)+".json")



    #file = open(filename, 'a')
    #file = open(filename, 'a')
    #filename = file.read()
    #file.close()
    #print("Here Is Your Account Data! ------------ " + str("\r\r"+str(data())))
    #file = open(f'./accounts/discord.json', 'r')
    #FileData = file.read()
    if r.status_code == 200:
        #FNAPIHeaders = {'Authorization': '822445a7-3270-432b-95de-7d4e7f742566'}
        FNAPIHeaders = {'Authorization': '94aa02a1-deda7712-adc56662-69db0061'}
        payload = json.dumps({})
        accountID = data["account_id"]
       #print(token)
        response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
        clientUsername = response1.json()['name']
        print(f'Found Client ({clientUsername} - {accountID})!')

        #LOCKERINFO

        response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })
        bruh = response.json()
        filename = ("./accounts/"+str(ctx.author.id)+".json")
        file = open(filename, 'a')
        file.write(json.dumps(bruh, indent=4))
        file.close()

        await ctx.send('e')


bot.run("OTYyOTAzMzY0NTM3MDQ5MTI4.YlOTow.ADHGEQLyqGdyNCYWvxeIY2JHRCE")