import os
import requests
import discord
from discord.ext import commands


#from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option

_intents = discord.Intents.all()
bot = discord.Bot()


@bot.event
async def on_ready():
    print("Bot Username: " + bot.user.name)
    print("Bot ID: " + str(bot.user.id))
    await bot.change_presence(activity=discord.Game(name="!help"))



@bot.slash_command(name="slash", description="test1")
async def slash(ctx):
    await ctx.send("Slash Command Successful")

bot.run("OTk0MDUxNjk1NTc3NDE5Nzg4.GiRSRs.1RPAQlcwNZq8-Xyb_SkbTGdooWPfbeCF3ynb_8")