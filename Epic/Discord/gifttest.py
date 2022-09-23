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


r = requests.get('https://fortnite-api.com/v2/shop/br/combined#')
data=r.json()

for i in data["data"]["featured"]["entries"]:
    print(i['offerId'])