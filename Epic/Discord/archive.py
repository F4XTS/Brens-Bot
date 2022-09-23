from ast import Mod
from cProfile import label
from dataclasses import MISSING
from decimal import Underflow
from http import client
from os import remove
from pickle import OBJ
from sys import prefix
from textwrap import indent
import time
from turtle import back
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


def test_user_auth(DiscordauthorID, data):
    a_file = open(f"./Epic/Discord/auths.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    for i in json_object['auths']:
        if i['DiscordauthorID'] == str(DiscordauthorID):
            data = i
            return(data)

DiscordauthorID = '842220666321371168'
data = ''
test = test_user_auth(DiscordauthorID, data)

s1 = json.dumps(test)
i = json.loads(s1)

#await ctx.send('Loaded auth token!')
token = i['token']
accountID = i['accountID']
accountName = i['accountName']

print(accountName)
    



payload = json.dumps({})
API = "https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api"

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
payload = json.dumps({
    "itemIds": [f"ad6c71a1-8b06-4f4b-9fea-298085c3ae27"],
    "archived": 'false'
})

response1 = requests.post(f'https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{accountID}/client/SetItemArchivedStatusBatch?profileId=athena&rvn=-1',data=payload,headers=headers)


data = response1.json()

print(json.dumps(data, indent=4))
a_file1 = open(f"./Epic/Discord/archive.json", "w")
json.dump(data, a_file1, indent = 4)