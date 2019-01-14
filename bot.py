import os
import discord
from discord.ext import commands
import asyncio
import utils.default
import datetime

TOKEN = 'NTMyNTUzMzk3MTk1NTA1Njg4.Dx5KCw.EHn9X8mbdhKyisfku8yiY6niLRg'
ICON_URL = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"
global_time = datetime.datetime.now()
TIME_DATE = global_time.strftime("%H:%M | %d.%m.%Y")
config = utils.default.get("config.json")
FOOTER = "Bot created by bezel 🔷 {}".format(TIME_DATE)
client = commands.Bot(command_prefix=config.prefix)

extentions = ['admin', 'events']
@client.event
async def on_ready():
    print('Gotowy: Tak')
    print("Nazwa: " + client.user.name)
    print("ID: " + client.user.id)
    await client.change_presence(game=discord.Game(name='PyamidRP'))
    

@client.command(pass_context = True)
async def infobot(ctx):
    channel = ctx.message.channel
    em = discord.Embed(title='', description='', colour=discord.Colour.blue())
    em.set_author(name="Informacje o PyamidBot", icon_url=ICON_URL)
    em.add_field(name="Autor", value="bezel", inline = True)
    em.add_field(name="Data rozpoczęcia prac", value="09/01/2018", inline = True)
    em.add_field(name="Technologia", value="Python", inline = True)
    em.add_field(name="Wersja", value="0.1", inline = True)
    em.add_field(name="Opis", value="Bot stworzony z myślą o społeczności pyamid, jej moderacji i do wspolnej zabawy. Możesz sprawdzić jego możliwości pod komendą !pomoc", inline = True)
    em.set_image(url="https://cdn.discordapp.com/attachments/473218411670011904/533048524502335517/iPEsF.png")
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/473218411670011904/533049638446432286/Discord_Thonk.png")
    em.set_footer(text=FOOTER)
    await client.send_message(channel, embed=em)



@client.command(pass_context = True)
async def info(ctx, user: discord.Member):
    channel = ctx.message.channel
    user_avatar = user.avatar_url
    em = discord.Embed(title='', description='', colour=discord.Colour.blue())
    em.set_thumbnail(url=user_avatar)
    em.set_author(name='Informacje użytkownika {}'.format(user.name), icon_url=ICON_URL)
    em.add_field(name='ID użytkownika', value='{}'.format(user.id), inline = True)
    em.add_field(name='Status', value='{}'.format(user.status), inline = True)
    em.add_field(name='Najwyższa rola', value='{}'.format(user.top_role), inline = True)
    em.add_field(name='Dolączył do społeczności pyamid', value='{}'.format(user.joined_at), inline = True)
    em.set_footer(text=FOOTER)
    await client.send_message(channel, embed=em)


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
            
client.run(TOKEN)