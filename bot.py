import os
import discord
from discord.ext import commands
import asyncio
import utils.default
import datetime

TOKEN = 'NTMyNTUzMzk3MTk1NTA1Njg4.DxfSPg._oPnvpyIHAGE_h8_6NPiNjd5Dac'
ICON_URL = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"
global_time = datetime.datetime.now()
TIME_DATE = global_time.strftime("%H:%M %d.%m.%Y")
config = utils.default.get("config.json")
FOOTER = "Bot created by bezel 🔷 {}".format(TIME_DATE)
client = commands.Bot(command_prefix=config.prefix)

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

@client.command(pass_context = True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    author_message = ctx.message.author

    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    em = discord.Embed(title='', description='', colour=discord.Colour.blue())
    em.set_author(name='{} usunął {} wiadomości'.format(author_message, amount), icon_url=ICON_URL)
    em.set_footer(text=FOOTER)
    await client.send_message(channel, embed=em)




#@client.event
#async def on_message(message):
#    if message.content.startswith(".react"):
#        msg = await client.send_message(message.channel, "Głosowanie")
 #       res = await client.wait_for_reaction(['👍', '👎'], message = msg)
  #      await client.send_message(message.channel, '{0.user}, zareagował emotikoną {0.reaction.emoji}!'.format(res))

#@client.event
#async def on_message(message):
 #   if message.content.startswith(".embed"):
  #      em = discord.Embed(title="Tytul", description="Opis", colour=0x00ffe)
   #     em.add_field(name="imie", value="wartość")
    #    await client.send_message(message.channel, embed=em)

#@client.event
#async def on_message(message):
    #if message.content.startswith("kurwa"):
        #await client.delete_message(message)
        #await client.send_message(message.channel, '``Wiadomość **"{}"** została usunięta z powodu naruszeń regulaminu``'.format(message.content))
for file in os.listdir("modules"):
    if file.endswith(".py"):
        name = file[:-2]
        client.load_extension(f"modules.{name}")

client.run(TOKEN)
