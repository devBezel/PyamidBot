import os
import discord
from discord.ext import commands
import asyncio
from utils import default
import datetime

ICON_URL = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"
global_time = datetime.datetime.now()
TIME_DATE = global_time.strftime("%H:%M | %d.%m.%Y")
config = default.get("config.json")
FOOTER = "Bot created by bezel 🔷 {}".format(TIME_DATE)
client = commands.Bot(command_prefix=config.prefix)

extentions = ['admin', 'events', 'fun', 'misc']
@client.event
async def on_ready():
    print('Gotowy: Tak')
    print("Nazwa: " + client.user.name)
    print("ID: " + client.user.id)
    await client.change_presence(game=discord.Game(name='PyamidRP'))
    


@client.command()
async def wlacz(extention):
    try:
        client.load_extension(extention)
        print("Załadowano {} moduł poprawnie".format(extention))
    except Exception as error:
        print("{} nie mogl zostać załadowany [{}]".format(extention, error))

@client.command()
async def wylacz(extention):
    try:
        client.unload_extension(extention)
        print("Wylączono {} moduł poprawnie!".format(extention))
    except Exception as error:
        print("{} nie mogl zostać załadowany [{}]".format(extention, error))

if __name__ == "__main__":
    for extention in extentions:
        try:
            client.load_extension(extention)
        except Exception as error:
            print("{} nie mogł zostać załadowany [{}]".format(extention, error))
            
client.run(config.token)