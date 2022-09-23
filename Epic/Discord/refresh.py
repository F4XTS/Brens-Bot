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

Basic = 'MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='

data = {
    'grant_type': 'refresh_token',
    'refresh_token': 'f043b4fb8f3246aab639ac633528f57c'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'basic {Basic}'
}
            
r = requests.post('https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',data=data, headers=headers)
data = r.json()

print(str(json.dumps(data, indent=4)))