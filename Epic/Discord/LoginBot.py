from ast import Mod
from cProfile import label
from dataclasses import MISSING
from decimal import Underflow
from email import header
from email.mime import image
from http import client
from os import remove
from pickle import OBJ
from sys import prefix
from textwrap import indent
import time
from turtle import back, title
from xml.etree.ElementInclude import include
from click import style
import discord

from discord import Integration, user
from discord.ext.commands.core import is_owner
from numpy import place
import requests
import json
import random
from discord.ext import commands
from discord.ext import tasks
from discord.file import File
from discord.ui import Button, View
from PIL import Image,ImageDraw,ImageFont
import urllib.request
import psutil
import sys
import socket


from keep_aliveweb import keep_alive
#from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option

_intents = discord.Intents.all()
#bot = commands.Bot(command_prefix='!', intents=_intents, sync_commands = True)
#slash = SlashCommand(bot, sync_commands = True)
#aclint = client()
#bot = app_commands.CommandTree(aclint)
bot = discord.Bot()

Basic = 'MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='

@bot.slash_command(name="botinfo", description="Shows Info Of Bot")
async def info(ctx):
    await ctx.defer()
    embed = discord.Embed(title="Bren's Bot", color=discord.Color.random())
    embed.add_field(name="Version", value="v1.0", )
    embed.add_field(name="Latency", value=str(round(bot.latency * 1000)) + "ms")
    embed.add_field(name="Guilds", value=str(len(bot.guilds)))
    embed.add_field(name="Memory Usage", value=f"{psutil.virtual_memory().percent}% free")
    embed.add_field(name="CPU Usage", value=f"{psutil.cpu_percent()}%")
    channelCount = 0
    memberCount = 0
    for guild in bot.guilds:
        memberCount = memberCount + guild.member_count
        channelCount = channelCount + len(guild.channels)
    embed.add_field(name="Channels", value=channelCount)
    embed.add_field(name="Members", value=memberCount)
    embed.add_field(name="Developer", value="<@364585552105963525>")
    embed.add_field(name="Support Server", value="https://discord.gg/FYvgycEbjf")
    embed.add_field(name="Discord.py Version", value=discord.__version__)
    embed.add_field(name="Python Version", value=f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1005930794772086866/e57dbe22d00c2c0e229b2cb08b8e8e76.png?size=1024')

    button = Button(label="Invite Bot", url="https://discord.com")
    button2 = Button(label="Discord Server", url="https://discord.gg/FYvgycEbjf")

    print("Success")
        
    view=View()
    view.add_item(button)
    view.add_item(button2)

    await ctx.respond(embed=embed, view=view)



@bot.slash_command(name="logout", description="logout your Epic Games Account")
async def logout(ctx):
    await ctx.defer()
    accounts = json.loads(open('./Epic/Discord/auths.json').read()) # better opening
    accounts = accounts['auths'] 

    QuestionMark = "https://cdn.discordapp.com/attachments/907764422968229922/1006692921812197438/unknown.png"
    CheckMark = "https://cdn.discordapp.com/attachments/907764422968229922/1006701273296416879/CheckMark.png"

    all_accounts = [i for i in accounts if i['DiscordauthorID'] == str(ctx.author.id)]

    if len(all_accounts) > 0:
        accounts.remove(all_accounts[0])
        new_list = [_ for _ in accounts] # remove user account
        embed = discord.Embed(title="You Have Been Successfully Logged Out!", color=discord.Color.green())
        embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=CheckMark)
        await ctx.respond(embed=embed)

        with open('./Epic/Discord/auths.json', 'w') as file:
            json.dump({"auths": new_list}, file, indent=2)

    else:
        embed = discord.Embed(title="You Are Not Logged Into A Epic Games Account", color=discord.Color.red())
        embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=QuestionMark)
        await ctx.respond(embed=embed)


    # for table in json_object['auths']:       ## old code
    #     try:
    #         if table['DiscordauthorID'] == str(ctx.author.id):
    #             del table['DiscordauthorID']
    #             del table['token']
    #             del table['accountID']
    #             del table['loadoutUUID']
    #             del table['accountName']
    #             embed = discord.Embed(title="You Have Been Successfully Logged Out!", color=discord.Color.green())
    #             embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
    #             embed.set_thumbnail(url=CheckMark)
    #             await ctx.respond(embed=embed)
    #     except:
    #             embed = discord.Embed(title="You Are Not Logged Into A Epic Games Account", color=discord.Color.red())
    #             embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
    #             embed.set_thumbnail(url=QuestionMark)
    #             await ctx.respond(embed=embed)

    # a_file = open(f"./Epic/Discord/auths.json", "w")
    # empty_auth = {"auths": [_ for _ in json_object['auths']]}
    # json.dump(empty_auth, a_file, indent = 2)
    





@bot.command()
async def account(ctx:str = None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)
    
    
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    payload = json.dumps({})
    response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    #print(response.json())
    #out_file = open("accinfo.json", "w")
    #json.dump(response.json(), out_file, indent = 4)
    if response.status_code == 200:
        BASE = response.json()['profileChanges'][0]['profile']['stats']['attributes']


        bp_stars = BASE['battlestars']
        if bp_stars == None:
            has_bp = "No"
        else:
            has_bp = "Yes"
        wins = BASE["season"]["numWins"]
        totalwins = BASE["lifetime_wins"]
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

        
        embed = discord.Embed(title="Account Info For "+accountName, color=discord.Color.random())
        #embed.add_field(name='Hello!', value=clientUsername, inline=False)
        embed.add_field(name='Account ID', value=accountID, inline=False)
        embed.add_field(name='Current Level', value=level, inline=False)
        embed.add_field(name='Current Skin', value=skin, inline=False)
        embed.add_field(name='Current Pickaxe', value=pickaxe, inline=False)
        embed.add_field(name='Current Backbling', value=backbling, inline=False)
        embed.add_field(name='Battle Stars', value=bp_stars, inline=False)
        embed.add_field(name='Has Battle Pass', value=has_bp, inline=False)
        embed.add_field(name='Season Wins', value=wins, inline=False)
        embed.add_field(name='Total Wins', value=totalwins, inline=False)
        embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url=url)
    else:
        embed = discord.Embed(title="Error 401", color=discord.Color.random())
    await ctx.send(embed=embed)
    print(response.status_code)


def test_user_auth(DiscordauthorID, data):
    a_file = open(f"./Epic/Discord/auths.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    for i in json_object['auths']:
        if i['DiscordauthorID'] == str(DiscordauthorID):
            data = i
            return(data)


@bot.command()
async def sac(ctx, code:str=None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"



    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.post(API+f'/game/v2/profile/{accountID}/client/SetAffiliateName?profileId=common_core&rvn=-1', headers=headers, data='{"affiliateName": "' + code + '"}' +"'")
    Reeee = r.json()
    if r.status_code == 200:
        embed = discord.Embed(title=f"Support A Creator Code Changed To: {code}", color=discord.Color.random())
    else:
        embed = discord.Embed(title="Error 401", color=discord.Color.random())
    await ctx.send(embed=embed)
    print(r.status_code)


@bot.command()
async def equip(ctx, *,item:str = None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)
    
    if item == "SonicProGaming":
        item = "blaze"
    if item == "MrFounderz":
        item = "Sparkle Supreme"
    if item == "LucidEDP":
        item = "Nightlife"
    if item == "Porn Hub":
        item = "Midas"

    responseFN = requests.get(f'https://fortnite-api.tokencom/v2/cosmetics/br/search?name={item}')


    payload = json.dumps({})
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    response1 = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={

        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    print(response1.json())
    loadoutUUID = response1.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
    print(loadoutUUID)
    
    #print(loadoutUUID)
    lockerdata = response1.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
    lockerskinID = lockerdata['Character']['items'][0]
    #print(lockerdata)
    #print(str(json.dumps(lockerdata, indent=4)))
    lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
    category = responseFN.json()['data']['type']['backendValue']
    type = responseFN.json()['data']['type']['displayValue']
    itemid = responseFN.json()['data']['id']
    itemid = itemid.lower()
    item = itemid
    payload = json.dumps({
        "lockerItem": f"{loadoutUUID}",
        "category": f"{category}".replace('Athena',''),
        "itemToSlot": f"{category}:{itemid}",
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
    

    itemdescription = responseFN.json()['data']['description']
    rarity = responseFN.json()['data']['rarity']['displayValue']
    
    embed = discord.Embed(description=itemdescription)
    #title=f"{type} Changed To **{item}**", color=discord.Color.random()
    if item == "Midas":
        itemicon = "https://media.indiatimes.in/media/content/2017/Feb/pornhub_1486037354.jpg"
        embed.set_author(name=f'Porn Hub - {rarity} {type}', icon_url=itemicon)
    else:
        itemicon = responseFN.json()['data']['images']['icon']
        embed.set_author(name=f'{item} - {rarity} {type}', icon_url=itemicon)
    embed.set_thumbnail(url=itemicon)
    #embed.set_author(name=f'{item} - {rarity} {type}', icon_url=itemicon)
    embed.add_field(name = "ID", value=itemid)

    async def button_callback(interaction):
        if interaction.user == ctx.author:   

            itemicon = responseFN.json()['data']['images']['icon']
            Newembed = discord.Embed(title=f"{type} Changed To {item}", color=discord.Color.random())
        
            Newembed.set_thumbnail(url=itemicon)
            r = requests.post(API+f'/game/v2/profile/{accountID}/client/SetCosmeticLockerSlot?profileId=athena&rvn=-1', headers=headers, data=payload)
            Reeee = r.json()
            await interaction.response.edit_message(embed=Newembed, view=None)
            print("Success")
            print(Reeee)
        else:
            print("no")
        #print(json.dumps(Reeee, indent=4))

    async def button1_callback(interaction):
        await interaction.response.edit_message(content="Oki", view=None)
    button.callback = button_callback
    button1.callback = button1_callback

    view = View()
    view.add_item(button)
    view.add_item(button1)
    await ctx.respond(embed=embed, view=view)
    if item == "Sparkle Supreme":
        await ctx.respond('Ik he is very hot ok calm down')


@bot.command()
async def homebasename(ctx, *,code:str=None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

    payload = json.dumps({
        "homebaseName": f"{code}"
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.post(API+f'/game/v2/profile/{accountID}/client/SetHomebaseName?profileId=common_public&rvn=-1', headers=headers, data=payload)
    Reeee = r.json()
    if r.status_code == 200:
        embed = discord.Embed(title=f"Homebase Name Has Been Changed To: {code}", color=discord.Color.random())
    else:
        embed = discord.Embed(title="Error 401", color=discord.Color.random())
    await ctx.send(embed=embed)
    print(r.status_code)


@bot.command()
async def redeem(ctx, *,code:str=None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    payload = json.dumps({})
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.post(f'https://coderedemption-public-service-prod.ol.epicgames.com/coderedemption/api/shared/accounts/{accountID}/redeem/{code}/evaluate', headers=headers, data=payload)
    Reeee = r.json()
    #if r.status_code == 200:
        #embed = discord.Embed(title=f"Homebase Name Has Been Changed To: {code}", color=discord.Color.random())
    #else:
        #embed = discord.Embed(title="Error 401", color=discord.Color.random())
    await ctx.send('test status 200')
    print(Reeee)
    print(r.status_code)



@bot.command()
async def locker(ctx):
    await ctx.defer()
    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    #print(accountName)
    
    
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    payload = json.dumps({})
    response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    #print(response.json())
    if response.status_code == 200:
        loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
        level = response.json()['profileChanges'][0]['profile']['stats']['attributes']["level"]
        lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
        lockerskinID = lockerdata['Character']['items'][0]
        lockerpickaxeID = lockerdata['Pickaxe']['items'][0]
        lockerbackpackID = lockerdata['Backpack']['items'][0]
        lockerGliderID = lockerdata['Glider']['items'][0]
        
        lockerEmoteID_1 = lockerdata['Dance']['items'][0].replace('AthenaDance:', '')
        lockerEmoteID_2 = lockerdata['Dance']['items'][1].replace('AthenaDance:', '')
        lockerEmoteID_3 = lockerdata['Dance']['items'][2].replace('AthenaDance:', '')
        lockerEmoteID_4 = lockerdata['Dance']['items'][3].replace('AthenaDance:', '')
        lockerEmoteID_5 = lockerdata['Dance']['items'][4].replace('AthenaDance:', '')

        #print(lockerdata)
        #print(str(json.dumps(lockerdata, indent=4)))
        lockerskinID = lockerskinID.replace('AthenaCharacter:', '')
        lockerpickaxeID = lockerpickaxeID.replace('AthenaPickaxe:', '')
        lockerbackpackID = lockerbackpackID.replace('AthenaBackpack:', '')
        print(lockerbackpackID)
        print(lockerEmoteID_1,lockerEmoteID_2,lockerEmoteID_3,lockerEmoteID_4,lockerEmoteID_5)
        lockerGliderID = lockerGliderID.replace('AthenaGlider:', '')

        img1 = Image.open(f'./Epic/Discord/images/Background.png')
        ImageDraw.Draw(img1)

        ico1 = "./Epic/Discord/images/skin.png"
        ico2 = "./Epic/Discord/images/back.png"
        ico3 = "./Epic/Discord/images/pick.png"
        ico4 = "./Epic/Discord/images/glider.png"


        ico5 = "./Epic/Discord/images/emotes/emote1.png"
        ico6 = "./Epic/Discord/images/emotes/emote2.png"
        ico7 = "./Epic/Discord/images/emotes/emote3.png"
        ico8 = "./Epic/Discord/images/emotes/emote4.png"
        ico9 = "./Epic/Discord/images/emotes/emote5.png"

        ico50 = "./Epic/Discord/images/LOCKERBackground.png"
        
        itembgRarity = "./Epic/Discord/images/itemRarity.png"


        response1 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
        if lockerskinID == "cid_694_athena_commando_m_catburglar":
            url = "https://media.indiatimes.in/media/content/2017/Feb/pornhub_1486037354.jpg"
        else:

            url = response1.json()['data']['images']['icon']

        response = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerskinID}')
        SkinData = response.json()
        skin = SkinData['data']['name']


        response2 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerpickaxeID}')
        pickaxe = response2.json()['data']['name']
        pickico = response2.json()['data']['images']['icon']
        PickaxeData = response2.json()

        response3 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerbackpackID}')

        backblingData = response3.json()

        response4 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerGliderID}')
        GliderData = response4.json()
        gliderico = response4.json()['data']['images']['icon']

        response5_1 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerEmoteID_1}')
        EmoteData = response5_1.json()
        emotenames1 = EmoteData['data']['name']
        emote1icon = EmoteData['data']['images']['icon']

        response5_2 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerEmoteID_2}')
        EmoteData = response5_2.json()
        emotenames2 = EmoteData['data']['name']
        emote2icon = EmoteData['data']['images']['icon']

        response5_3 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerEmoteID_3}')
        EmoteData = response5_3.json()
        emotenames3 = EmoteData['data']['name']
        emote3icon = EmoteData['data']['images']['icon']

        response5_4 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerEmoteID_4}')
        EmoteData = response5_4.json()
        emotenames4 = EmoteData['data']['name']
        emote4icon = EmoteData['data']['images']['icon']

        response5_5 = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?id={lockerEmoteID_5}')
        EmoteData = response5_5.json()
        emotenames5 = EmoteData['data']['name']
        emote5icon = EmoteData['data']['images']['icon']

        #RARITYCONFIGS
        itembg = "./Epic/Discord/images/itemBG.png"



        urllib.request.urlretrieve(
            url,
            ico1)
        if lockerbackpackID == "":
            backblingico = "https://i.ibb.co/3CTFzJz/None.png"
            urllib.request.urlretrieve(
                backblingico,
                ico2)
            backbling = "None"
        else:
            backblingico = response3.json()['data']['images']['icon']
            backbling = response.json()['data']['name']
            urllib.request.urlretrieve(
                backblingico,
                ico2)
        urllib.request.urlretrieve(
            pickico,
            ico3)
        urllib.request.urlretrieve(
            gliderico,
            ico4)

        urllib.request.urlretrieve(
            emote1icon,
            ico5)
        urllib.request.urlretrieve(
            emote2icon,
            ico6)
        urllib.request.urlretrieve(
            emote3icon,
            ico7)
        urllib.request.urlretrieve(
            emote4icon,
            ico8)
        urllib.request.urlretrieve(
            emote5icon,
            ico9)
        print('gergeyyu547y45y7456')

        centerr = 0, 0
        img72 = Image.open(itembg).convert("RGBA")

        img2 = Image.open(ico1).convert("RGBA").resize((160,158), Image.Resampling.LANCZOS)

        img3 = Image.open(ico2).convert("RGBA").resize((143,143), Image.Resampling.LANCZOS)

        img4 = Image.open(ico3).convert("RGBA").resize((150,152), Image.Resampling.LANCZOS)

        img5 = Image.open(ico4).convert("RGBA").resize((150,152), Image.Resampling.LANCZOS)

        imgemote1 = Image.open(ico5).convert("RGBA").resize((111,111), Image.Resampling.LANCZOS)
        imgemote2 = Image.open(ico6).convert("RGBA").resize((111,111), Image.Resampling.LANCZOS)
        imgemote3 = Image.open(ico7).convert("RGBA").resize((111,111), Image.Resampling.LANCZOS)
        imgemote4 = Image.open(ico8).convert("RGBA").resize((111,111), Image.Resampling.LANCZOS)
        imgemote5 = Image.open(ico9).convert("RGBA").resize((111,111), Image.Resampling.LANCZOS)
        
        img85 = Image.open(itembgRarity).convert("RGBA")

        img57 = Image.open(ico50).convert("RGBA")

        #SKIN

        img1.paste(img72, (68, 272), mask = img72)
        img1.paste(img2, (52, 272), mask = img2)
        img1.paste(img85, (68, 272), mask = img85)

        #BACKBLING

        img1.paste(img72, (206, 272), mask = img72)
        img1.paste(img3, (194, 272), mask = img3)
        img1.paste(img85, (206, 272), mask = img85)

        #PICKAXE

        img1.paste(img72, (340, 272), mask = img72)
        img1.paste(img4, (329, 272), mask = img4)
        img1.paste(img85, (340, 272), mask = img85)

        img1.paste(img72, (476, 272), mask = img72)
        img1.paste(img5, (461, 272), mask = img5)
        img1.paste(img85, (476, 272), mask = img85)

        #EMOTES

        img85 = Image.open(itembgRarity).convert("RGBA").resize((88,110))
        img72 = Image.open(itembg).convert("RGBA").resize((88,110))
        img1.paste(img72, (68, 440), mask = img72)
        img1.paste(imgemote1, (53, 439), mask = imgemote1)
        img1.paste(img85, (68, 440), mask = img85)

        img1.paste(img72, (164, 440), mask = img72)
        img1.paste(imgemote2, (147, 439), mask = imgemote2)
        img1.paste(img85, (164, 440), mask = img85)

        img1.paste(img72, (260, 440), mask = img72)
        img1.paste(imgemote3, (243, 439), mask = imgemote3)
        img1.paste(img85, (260, 440), mask = img85)

        img1.paste(img72, (356, 440), mask = img72)
        img1.paste(imgemote4, (339, 439), mask = imgemote4)
        img1.paste(img85, (356, 440), mask = img85)

        img1.paste(img72, (452, 440), mask = img72)
        img1.paste(imgemote5, (435, 439), mask = imgemote5)
        img1.paste(img85, (452, 440), mask = img85)




        img1.paste(img57, (centerr), mask = img57)
        #189
        #289
        #159
        img1.save("./Epic/Discord/Cock.png")
        file = discord.File(f"./Epic/Discord/Cock.png", filename="image.png")

        EmoteInfoLink1 = f'https://fnbr.co/emote/{emotenames1}'.replace(" ","-")
        EmoteInfoLink2 = f'https://fnbr.co/emote/{emotenames2}'.replace(" ","-")
        EmoteInfoLink3 = f'https://fnbr.co/emote/{emotenames3}'.replace(" ","-")
        EmoteInfoLink4 = f'https://fnbr.co/emote/{emotenames4}'.replace(" ","-")
        EmoteInfoLink5 = f'https://fnbr.co/emote/{emotenames5}'.replace(" ","-")

        EmoteInfoLink1 = f'[{emotenames1}]({EmoteInfoLink1})\n'
        EmoteInfoLink2 = f'[{emotenames2}]({EmoteInfoLink2})\n'
        EmoteInfoLink3 = f'[{emotenames3}]({EmoteInfoLink3})\n'
        EmoteInfoLink4 = f'[{emotenames4}]({EmoteInfoLink4})\n'
        EmoteInfoLink5 = f'[{emotenames5}]({EmoteInfoLink5})'

        embed = discord.Embed(title="Account Info For "+accountName, color=discord.Color.random())
        #embed.add_field(name='Hello!', value=clientUsername, inline=False)
        embed.add_field(name='Account ID', value=accountID, inline=False)
        embed.add_field(name='Current Level', value=level, inline=False)
        embed.add_field(name='Current Skin', value=skin, inline=True)
        embed.add_field(name='Current Pickaxe', value=pickaxe, inline=True)
        embed.add_field(name='Current Backbling', value=backbling, inline=True)
        embed.add_field(name='Current Emotes', value=EmoteInfoLink1+EmoteInfoLink2+EmoteInfoLink3+EmoteInfoLink4+EmoteInfoLink5, inline=True)
        embed.set_author(name="Requested by " + ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_image(url="attachment://image.png")
        await ctx.send(embed=embed, file=file)


@bot.slash_command(name="shop", description="Sends the current shop as a json.")
async def shop(ctx):
    r = requests.get('https://fortnite-api.com/v2/shop/br')
    data = r.json()
    #embed=discord.Embed(title="Json:", description="cock", color=discord.Color.blue())
    out_file = open("shop.json", "w")
   
    json.dump(data, out_file, indent = 4)
   
    out_file.close()
    await ctx.respond(file=discord.File('shop.json'))


@bot.command()
async def favouritelist(ctx):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

    payload = json.dumps({})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.get(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/creative/favorites/{accountID}', headers=headers)
    Reeee = r.json()
    if r.status_code == 200:
        print("worky")
    else:
        print("no worky")
    await ctx.send("E")
    out_file = open("fav.json", "w")
   
    json.dump(Reeee, out_file, indent = 4)
   
    out_file.close()
    await ctx.respond(file=discord.File('fav.json'))
    print(r.json())


@bot.slash_command(name="favourite", description="Favourite A LTM")
async def favourite(ctx, playlistid):
    await ctx.defer()
    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

    payload = json.dumps({})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    playlistidinput = playlistid.lower()

    r = requests.post(f'https://fn-service-discovery-live-public.ogs.live.on.epicgames.com/api/v1/links/favorites/{accountID}/{playlistidinput}', headers=headers)
    print(r.status_code)
    #r = requests.put(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/creative/favorites/{accountID}/{playlistidinput}', headers=headers)
    #print(r.json())
    #Reeee = r.json()
    
    if r.status_code == 204:
        print(f"{accountName} Has Favorited {playlistid}")
        embed = discord.Embed(description=f"Successfully Favourited **{playlistid}**!", color=discord.Color.random())
        button = Button(label="Get Playlist Details", style=discord.ButtonStyle.green, emoji="📈")
        async def button_callback(interaction):
            if interaction.user == ctx.author:   
                r = requests.get(f'https://fortnite-api.com/v1/playlists/{playlistid}')
                data=r.json()
                if r.status_code == 200:
                    Newembed = discord.Embed(title=f"Info For {playlistid}", color=discord.Color.random())
                    Newembed.add_field(name="Name", value=data['data']['name'])
                    Newembed.add_field(name="Description", value=data['data']['description'])

                    #Newembed.add_field(name="Name", value=data['data']['name'])
                    #Newembed.add_field(name="Description", value=data['data']['description'])
                    #Newembed.add_field(name="Name", value=data['data']['name'])
                    #Newembed.add_field(name="Name", value=data['data']['name'])
                    #Newembed.set_image(url=data['data']['images']['showcase'])
                else:
                    Newembed = discord.Embed(title=f"Details Could Not Be Found <:Error:1014163049017520238>", color=discord.Color.random())
      
                await interaction.response.send_message(embed=Newembed, view=None, ephemeral=True)
                print("Success")
                #print(Reeee)
            else:
                print("no")
            #print(json.dumps(Reeee, indent=4))
        button.callback = button_callback
        view = View()
        view.add_item(button)
        await ctx.respond(embed=embed, view=view)
    else:
        embed = discord.Embed(description=f"Error 404", color=discord.Color.random())
        await ctx.respond(embed=embed)
    out_file = open("fav.json", "w")
   
    #json.dump(Reeee, out_file, indent = 4)
   
    out_file.close()
    #await ctx.respond(file=discord.File('fav.json'))
    #print(r.json())


@bot.slash_command(name="testlogin", description="Login to your Epic Games Account")
async def testlogin(ctx):
    await ctx.defer()
    class LoginMyModal(discord.ui.Modal):
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(
            discord.ui.InputText(
                label="Fortnite Auth Login Code",
                placeholder="Auth Code",
            ),
            *args,
            **kwargs,
        )
        async def callback(self, interaction: discord.Interaction):
            code = self.children[0].value
            embed = discord.Embed(
            title="Your Modal Results",
            fields=[
                discord.EmbedField(name="First Input", value=code, inline=False)
            ],
            color=discord.Color.random(),
            )
            await interaction.response.send_message(embeds=[embed])

            class MyView(discord.ui.View):
                @discord.ui.button(label="Modal Test", style=discord.ButtonStyle.primary)
                async def button_callback(self, button, interaction):
                    modal = LoginMyModal(title="Modal Triggered from Button")
                    await interaction.response.send_modal(modal)

                async def select_callback(self, select, interaction):
                    modal = LoginMyModal(title="Temporary Title")
                    modal.title = select.values[0]
                    await interaction.response.send_modal(modal)

            view = MyView()
            await ctx.respond("Click Button, Receive Modal", view=view)
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
            try:
                token = data["access_token"]
                print(f"Generated Token! {token}")
            except:
                print(f"Invalid Access Token.")

            FNAPIHeaders = {'Authorization': '94aa02a1-deda7712-adc56662-69db0061'}
            payload = json.dumps({})
            accountID = data["account_id"]
            a_file = open(f"./Epic/Discord/auths.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            #print("trehrthrth")

            DiscordauthorID = ctx.author.id
            print(f"Discord ID: {DiscordauthorID}")

            # Checks the auths array to see if discord author ID is in it. If it is, the bot will refresh the token and notice it.
            for x in json_object['auths']:
                if x['DiscordauthorID'] == str(DiscordauthorID):
                    #print(accountID)
                    response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
                    R1 = response1.json()
                    clientUsername = response1.json()['name']
                    print(f'Found Client ({clientUsername} - {accountID})!')

                #LOCKERINFO

                    response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json'
                    })

                    try:
                        error = R1['errorCode']
                        print(f'ERROR: {error}')
                    except:
                        pass

                    embed = discord.Embed(title="Logged In As "+clientUsername, color=discord.Color.random())

                    loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
                    for i in json_object['auths']:
                        if i['DiscordauthorID'] == str(DiscordauthorID):
                            #print('a')
                            print('Found Account') # If this happens, the user is already logged in.
                            i['loadoutUUID'] = loadoutUUID


                    #embed.add_field(name='Hello!', value=clientUsername, inline=False)
                    x['loadoutUUID'] = f"{loadoutUUID}"
                    x['token'] = f"{token}"
                    x['accountID'] = f"{accountID}"
                    x['accountName'] = f"{clientUsername}"
                    #print(x['token'])
                    a_file = open(f"./Epic/Discord/auths.json", "w")
                    json.dump(json_object, a_file, indent = 4)
                    embed = discord.Embed(title="Looks like you are already logged in with your discord account! | "+clientUsername, color=discord.Color.random())
                    return await ctx.respond(embed=embed)
        
            print('Thanks for using this bot \:D.')

            response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                })
            #print(response.json())
                # Below dumps all data except loadout UUID and account name. We will dump it later.
            json_object['auths'].append({
                "DiscordauthorID": f"{DiscordauthorID}",
                "token": f"{token}",
                #"authCode": f'{auth}',
                "accountID": f"{accountID}",
                "loadoutUUID": "",
                "accountName": ""
            })
            a_file = open(f"./Epic/Discord/auths.json", "w")


            loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]

            response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
            R1 = response1.json()
            clientUsername = response1.json()['name']
            for i in json_object['auths']:
                if i['DiscordauthorID'] == str(DiscordauthorID):
                    print(f'Found Client ({clientUsername} - {accountID})!')
                    i['loadoutUUID'] = loadoutUUID
                    i['accountName'] = clientUsername
                    json.dump(json_object, a_file, indent = 4)
    
            level = response.json()['profileChanges'][0]['profile']['stats']['attributes']["level"]
            lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
            lockerskinID = lockerdata['Character']['items'][0]
            lockerpickaxeID = lockerdata['Pickaxe']['items'][0]
            lockerbackpackID = lockerdata['Backpack']['items'][0]
            #print(lockerdata)
            #print(str(json.dumps(lockerdata, indent=4)))
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
            await ctx.respond(embed=embed) # Sends embed


@bot.slash_command(name="testacc", description="testacc")
async def testacc(ctx):
    await ctx.defer()
    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

    payload = json.dumps({})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.get(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/br-inventory/account/{accountID}', data=payload,headers=headers)
    Reeee = r.json()

    out_file = open("accinfo.json", "w")
   
    json.dump(Reeee, out_file, indent = 4)
   
    out_file.close()
    #await ctx.respond(file=discord.File('fav.json'))
    print(r.json())


@bot.slash_command(name="connections", description="Shows All Connected Accounts To Epic Games")
async def connections(ctx):
    await ctx.defer()
    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)

    API = "https://account-public-service-prod.ol.epicgames.com"

    payload = json.dumps({})

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.get(f'{API}/account/api/public/account?accountId={accountID}', data=payload,headers=headers)
    data = r.json()
    for i in data:

        connections = i["externalAuths"]


    embed = discord.Embed(title=f"{accountName}'s Connections", color=discord.Color.random())



    if 'github' not in connections:
        pass
    else:
        github = connections["github"]["externalDisplayName"]
        embed.add_field(name="GitHub", value=github)
    
    if 'twitch' not in connections:
        pass
    else:
        twitch = connections["twitch"]["externalDisplayName"]
        embed.add_field(name="Twitch", value=twitch)
    
    if 'nintendo' not in connections:
        pass
    else:
        nintendo = connections["nintendo"]
        nintendo = nintendo

        embed.add_field(name="Nintendo", value="N/A")

    if 'steam' not in connections:
        pass
    else:
        steam = connections["steam"]["externalDisplayName"]
        embed.add_field(name="Steam", value=steam)

    if 'psn' not in connections:
        pass
    else:
        psn = connections["psn"]["externalDisplayName"]
        embed.add_field(name="PSN", value=psn)

    if 'google' not in connections:
        pass
    else:
        google = connections["google"]["externalDisplayName"]
        embed.add_field(name="Google", value=google)

    if 'xbox' not in connections:
        print("eeeeeeee")
    else:
        xbox = connections["xbox"]["externalDisplayName"]
        embed.add_field(name="XBOX", value=xbox)



    #await ctx.respond(file=discord.File('fav.json'))
    print(r.json())
    await ctx.respond(embed=embed)


@bot.slash_command(name="account_token", description="token")
async def token(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        DiscordauthorID = ctx.author.id
        data = ''
        test = test_user_auth(DiscordauthorID, data)

        s1 = json.dumps(test)
        i = json.loads(s1)

        #await ctx.send('Loaded auth token!')
        token = i['token']
        accountID = i['accountID']
        accountName = i['accountName']

        embed = discord.Embed(title=f"Token: {token}", color=discord.Color.random())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Please use this in dms", color=discord.Color.random())


@bot.command()
async def archive(ctx, *,item:str = None):

    DiscordauthorID = ctx.author.id
    data = ''
    test = test_user_auth(DiscordauthorID, data)

    s1 = json.dumps(test)
    i = json.loads(s1)

    #await ctx.send('Loaded auth token!')
    token = i['token']
    accountID = i['accountID']
    accountName = i['accountName']

    print(accountName)
    

    responseFN = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search?name={item}')


    payload = json.dumps({})
    API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"
    response1 = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/SetItemArchivedStatusBatch?profileId=athena&rvn=-1',data=payload,headers={

        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })
    print(response1.json())
    payload = json.dumps({
        "itemIds": f"{item}",
        "archived": 'true'
    })



    await ctx.respond('worked')


@bot.command()
async def newids(ctx):
    r = requests.get("https://fortnite-api.com/v2/cosmetics/br/new")
    data = r.json()
    embed = discord.Embed(title="New Cosmetic ID'S", color=discord.Color.blue())
    text = "```md\n"
    lastSection = data["data"]["items"][0]["type"]["backendValue"]
    for item in data["data"]["items"]:
        if lastSection != item["type"]["backendValue"]:
            text = text + "```"
            embed.add_field(name=lastSection, value=text, inline=False)
            lastSection = item["type"]["backendValue"]
            newid = item["id"]
            newname = item["name"]
            text = f'``` {newid} - {newname}\n'
        else:
            newid = item["id"]
            newname = item["name"]
            text = text + " " + f'{newid} - {newname}\n'
            print(text)
    await ctx.respond(embed=embed)


@bot.command()
async def cosmetic(ctx, *, item):
    emoji1= bot.get_emoji(1011091665894780938)
    
    fetch = await ctx.respond(f'Fetching Cosmetic... {emoji1}')
    r = requests.get(url="https://fortnite-api.com/v2/cosmetics/br/search/?name=" + item)
    data = r.json()
    status = data["status"]
    if status == 200:
        rarity = data["data"]["rarity"]["value"]
        embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.random())
        if rarity == "common":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.light_gray())
        if rarity == "uncommon":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.green())
        if rarity == "rare":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.blue())
        if rarity == "epic":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.purple())
        if rarity == "legendary":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.orange())
        if rarity == "icon":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.teal())
        path = data["data"]["path"]
        reqpaths = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
        pathdata = reqpaths.json()
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.add_field(name="ID", value="```" + str(data["data"]["id"]) + "```", inline=False)
        embed.add_field(name="Description", value="```" + str(data["data"]["description"]) + "```", inline=False)
        embed.add_field(name="MetaTags", value="```" + str(data["data"]["metaTags"]) + "```", inline=False)
        embed.add_field(name="DynamicPakID", value="```" + str(data["data"]["dynamicPakId"]) + "```", inline=False)
        embed.add_field(name="DisplayAssetPath", value="```" + str(data["data"]["displayAssetPath"]) + "```", inline=False)
        embed.add_field(name="Paths", value=f"```{path}```", inline=False)
        for i in pathdata["jsonOutput"][0]["Properties"]["BaseCharacterParts"]:
            base = i["AssetPathName"]
            embed.add_field(name="Character Parts", value=f"```{base}```", inline=True)
            print(base)
        embed.add_field(name="GamePlayTags", value="```" + str(data["data"]["gameplayTags"][0]).replace("[","").replace("]","").replace(",","").replace("'","") + "```")
        embed.set_thumbnail(url=data["data"]["images"]["icon"])
        if status == 404:
            embed = discord.Embed(title="Error 404.", color=discord.Color.random())
        await ctx.edit(content="",embed=embed)
        #r2 = requests.get(url="https://benbot.app/api/v1/cosmetics/br/search?lang=en&searchLang=en&matchMethod=full&name=" + item)
        #data2 = r2.json()
        #embed.add_field(name="GamePlayTags", value="```" + str(data2["gameplayTags"]).replace("[","").replace("]","").replace(",","").replace("'","") + "```")
    if item.startswith("CID" or "BID" or "EID" or "LSID") == True:
        r = requests.get(url="https://fortnite-api.com/v2/cosmetics/br/search/?id=" + item)
        data = r.json()
        rarity = data["data"]["rarity"]["value"]
        embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.random())
        if rarity == "common":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.light_gray())
        if rarity == "uncommon":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.green())
        if rarity == "rare":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.blue())
        if rarity == "epic":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.purple())
        if rarity == "legendary":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.orange())
        if rarity == "icon":
            embed = discord.Embed(title="Item Data - "+data["data"]["name"], color=discord.Color.teal())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.add_field(name="ID", value="```" + str(data["data"]["id"]) + "```", inline=False)
        embed.add_field(name="Description", value="```" + str(data["data"]["description"]) + "```", inline=False)
        embed.add_field(name="MetaTags", value="```" + str(data["data"]["metaTags"]) + "```", inline=False)
        embed.add_field(name="DynamicPakID", value="```" + str(data["data"]["dynamicPakId"]) + "```", inline=False)
        embed.add_field(name="DisplayAssetPath", value="```" + str(data["data"]["displayAssetPath"]) + "```", inline=False)
        embed.add_field(name="Path", value="```" + str(data["data"]["path"]) + "```", inline=False)
        #embed.add_field(name="GamePlayTags", value="```" + str(data["data"]["gameplayTags"][0]).replace("[","").replace("]","").replace(",","").replace("'","") + "```")
        embed.set_thumbnail(url=data["data"]["images"]["icon"])
        await fetch.edit(content="",embed=embed)


@bot.command()
async def mapping(ctx, version):
    emoji1= bot.get_emoji(1011091665894780938)
    
    fetch = await ctx.respond(f'Fetching Mapping... {emoji1}')
    r = requests.get(url=f"https://fortnitecentral.gmatrixgames.ga/api/v1/mappings?version=" + version)
    data = r.json()
    if r.status_code == 200:

        embed = discord.Embed(title=version, color=discord.Color.random())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        view=View()
        if data[0] in data:
            embed.add_field(name=data[0]["fileName"], value="Hash\n"+data[0]["hash"], inline=False)
            type1 = data[0]["meta"]["platform"]
            if type1 == "Android":
                button = Button(label="Andriod", url=data[0]["url"])
                view.add_item(button)
                data[0]
        else:
            print("")
            
            
        
        if data[1] in data:
            embed.add_field(name=data[1]["fileName"], value="Hash\n"+data[1]["hash"], inline=False)
            type2 = data[1]["meta"]["platform"]
            if type2 == "Windows":
                button2 = Button(label="Windows", url=data[1]["url"])
                view.add_item(button2)
                print("win")
        else:
            print("")

        print("Success")
        
        
        
        #print(json.dumps(Reeee, indent=4))

        if r.status_code == 404:
            embed = discord.Embed(title="Error 404.", color=discord.Color.random())
        await ctx.edit(content="",embed=embed, view=view)
#keep_alive()

@bot.slash_command()
async def modal_slash(ctx: discord.ApplicationContext):
    embed = discord.Embed(title="Text", color=discord.Color.random())

    button = Button(label="test", style=discord.ButtonStyle.green, emoji="✅")

    class MyModal(discord.ui.Modal):
        
        
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

            self.add_item(discord.ui.InputText(label="Short Input"))
            self.add_item(discord.ui.InputText(label="Long Input", style=discord.InputTextStyle.long))

        async def callback(self, interaction: discord.Interaction):
            embed = discord.Embed(title="Modal Results")
            embed.add_field(name="Short Input", value=self.children[0].value)
            embed.add_field(name="Long Input", value=self.children[1].value)
            await interaction.response.send_message(embeds=[embed])
    modal = MyModal(title="Modal via Slash Command")
    async def button_callback(interaction):
        await interaction.response.send_modal(modal)

    button.callback = button_callback

    view = View()
    view.add_item(button)
    
    await ctx.send(embed=embed, view=view)



@bot.slash_command(name="login", description="Login to your Epic Games Account")
async def login(ctx: discord.ApplicationContext):
    await ctx.defer()
    embed = discord.Embed(title="Bren's Bot", color=discord.Color.random())
    Eemoji = '<:check:991513136278552586>'
    #await ctx.send(Eemoji)
    embed.add_field(name="How To Login", value=f"**• Step 1**: Login To **Epic Games**\n\n**• Step 2**: Copy The Auth Code Next To 'authorizationCode'\nExample: **aabbccddeeff11223344556677889900**\n\n**• Step 3**: Type Out **'/login (authcode)'**\n\n**Then Your Done!** {Eemoji}")
    embed.set_image(url='https://cdn.discordapp.com/attachments/1006420994833006822/1014490353040097286/Capture2.PNG')
    button = Button(label="Epic Games", url="https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3446cd72694c4a4485d81b77adbb2141%26responseType%3Dcode")

    button1 = Button(label="Login", style=discord.ButtonStyle.green, emoji="🔒")
    class MyModal1(discord.ui.Modal):

        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

            self.add_item(discord.ui.InputText(label="Authorization Code"))

        async def callback(self, interaction: discord.Interaction):
            code = self.children[0].value
            print(code)
            data = {
            'grant_type': 'authorization_code',
            'code': code
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': f'basic {Basic}'
            }
            
            r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data, headers=headers)
            data = r.json()
            #print(data)
            try:
                token = data["access_token"]
                refreshtoken = data["refresh_token"]
                print(f"Generated Token! {token}")
                print(f"Generated Refresh Token! {refreshtoken}")
            except:
                print(f"Invalid Access Token.")

            FNAPIHeaders = {'Authorization': '94aa02a1-deda7712-adc56662-69db0061'}
            payload = json.dumps({})
            accountID = data["account_id"]
            a_file = open(f"./Epic/Discord/auths.json", "r")
            json_object = json.load(a_file)
            a_file.close()
            #print("trehrthrth")

            DiscordauthorID = ctx.author.id
            #print(DiscordauthorID)

                # Checks the auths array to see if discord author ID is in it. If it is, the bot will refresh the token and notice it.
            for x in json_object['auths']:
                if x['DiscordauthorID'] == str(DiscordauthorID):
                    print(accountID)
                    response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
                    R1 = response1.json()
                    clientUsername = response1.json()['name']
                    print(f'Found Client ({clientUsername} - {accountID})!')

                #LOCKERINFO

                    response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json'
                    })

                    try:
                        error = R1['errorCode']
                        print(f'ERROR: {error}')
                    except:
                        pass
                    
                    embed = discord.Embed(title="Logged In As "+clientUsername, color=discord.Color.random())
                    loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]
                    UUID = response.json()['profileChanges']
                    for i in json_object['auths']:
                        if i['DiscordauthorID'] == str(DiscordauthorID):
                            #print('a')
                            print('Found Account') # If this happens, the user is already logged in.
                            i['loadoutUUID'] = loadoutUUID
                            print(f"loadoutUUID: {loadoutUUID}")



                    #embed.add_field(name='Hello!', value=clientUsername, inline=False)
                    x['loadoutUUID'] = f"{loadoutUUID}"
                    x['token'] = f"{token}"
                    x['refreshtoken'] = f"{refreshtoken}",
                    x['accountID'] = f"{accountID}"
                    x['accountName'] = f"{clientUsername}"
                    #print(x['token'])
                    a_file = open(f"./Epic/Discord/auths.json", "w")
                    json.dump(json_object, a_file, indent = 4)
                    embed = discord.Embed(title="Looks like you are already logged in with your discord account! | "+clientUsername, color=discord.Color.random())
                    return await ctx.respond(embed=embed)
                
            print('Thanks for using this bot \:D.')

            response = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/QueryProfile?profileId=athena&rvn=-1',data=payload,headers={
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                })
            #print(response.json())
                # Below dumps all data except loadout UUID and account name. We will dump it later.
            json_object['auths'].append({
                "DiscordauthorID": f"{DiscordauthorID}",
                "token": f"{token}",
                "refreshtoken": f"{refreshtoken}",
                #"authCode": f'{auth}',
                "accountID": f"{accountID}",
                "loadoutUUID": "",
                "accountName": ""
            })
            a_file = open(f"./Epic/Discord/auths.json", "w")


            loadoutUUID = response.json()['profileChanges'][0]['profile']['stats']['attributes']['loadouts'][0]

            response1 = requests.get(f'https://fortniteapi.io/v1/stats?account={accountID}', headers=FNAPIHeaders)
            R1 = response1.json()
            clientUsername = response1.json()['name']
            for i in json_object['auths']:
                if i['DiscordauthorID'] == str(DiscordauthorID):
                    print(f'Found Client ({clientUsername} - {accountID})!')
                    i['loadoutUUID'] = loadoutUUID
                    i['accountName'] = clientUsername
                    json.dump(json_object, a_file, indent = 4)
            
            level = response.json()['profileChanges'][0]['profile']['stats']['attributes']["level"]
            lockerdata = response.json()['profileChanges'][0]['profile']['items'][loadoutUUID]['attributes']['locker_slots_data']['slots']
            lockerskinID = lockerdata['Character']['items'][0]
            lockerpickaxeID = lockerdata['Pickaxe']['items'][0]
            lockerbackpackID = lockerdata['Backpack']['items'][0]
            #print(lockerdata)
            #print(str(json.dumps(lockerdata, indent=4)))
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
            await interaction.response.edit_message(embed=embed, view=None)
    modal = MyModal1(title="Log into Bren's Bot", )
    async def button_callback(interaction):
        await interaction.response.send_modal(modal)

    button1.callback = button_callback

    view = View()
    view.add_item(button)
    view.add_item(button1)
    
    await ctx.respond(embed=embed, view=view)

@bot.slash_command(name="userinfo", description="info")
async def userinfo(ctx, user:discord.Member):
    ID = user.id
    embed = discord.Embed(title="User Info")
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="User ID:", value=ID)
    embed.add_field(name="Created At:", value=user.created_at.strftime("%A, %d %B %Y %H:%M:%S UTC"))
    if user.bot == True:
        embed.add_field(name="Is User Bot:", value="Yes :white_check_mark:")
    else:
        embed.add_field(name="Is User Bot:", value="No :x:")
    #if user.premium_since is not None:
        #embed.add_field(name="Has Nitro:", value="Yes")
    #else:
        #embed.add_field(name="Has Nitro:", value="No")
    await ctx.respond(embed=embed)


@bot.command()
async def sections(ctx):
    headers = {'Authorization': "94aa02a1-deda7712-adc56662-69db0061"}
    r = requests.get("https://fortniteapi.io/v2/shop?lang=en" , headers=headers)
    data = r.json()
    embed = discord.Embed(title="Shop Sections", color=discord.Color.random())
    embed.add_field(name="Time updated:", value= "**" + str(data["lastUpdate"]["date"]) + "**", inline=False)
    embed.add_field(name="Updated:", value= "```\n• "+"``````\n• ".join(data["nextRotation"])+"```", inline=True)
    embed.add_field(name="Currently Active:", value= "```\n• "+"``````\n• ".join(data["currentRotation"])+"```", inline=True)
    await ctx.respond(embed=embed)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Beta Testing!"))



bot.run('MTAwNTkzMDc5NDc3MjA4Njg2Ng.G8vEOU.M9GFFnTREeZSS2eL-R_YgAg3r4I528pU7hJAto')

#bot.run("OTYyOTAzMzY0NTM3MDQ5MTI4.YlOTow.ADHGEQLyqGdyNCYWvxeIY2JHRCE")