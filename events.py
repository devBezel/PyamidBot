import discord
from discord.ext import commands
import asyncio
import datetime

from utils import default

config = default.get("config.json")
global_time = datetime.datetime.now()
date_time = global_time.strftime("%H:%M %d.%m.%Y")
footer = "Bot created by bezel 🔷 {}".format(date_time)
icon_author = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"

class Events:
    def __init__(self, client):
        self.client = client
    

    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name='Użytkownik')
        await self.client.add_roles(member, role)
        em = discord.Embed(title='Witamy na serwerze pyamid.pl {}'.format(member.name), description='', colour=discord.Colour.blue())
        em.set_author(name='PyamidRP', icon_url=icon_author)
        em.set_thumbnail(url=icon_author)
        em.add_field(name='Strona internetowa', value='pyamid.pl', inline=True)
        em.add_field(name='Panel gracza', value='Wkrotce', inline=True)
        em.set_footer(text=footer)
        await self.client.send_message(self.client.get_channel(config.channel_logs), embed=em)

    #async def on_reaction_add(self, reaction, user):
     #   channel = reaction.message.channel
      #  await self.client.send_message(self.client.get_channel#(config.channel_logs), ':shield: ``[SERVER_LOG_ADD_EMOJI |{}|]`` - {} dodał emoji {} do wiadomości: {}'.format(date_time, user.name, reaction.emoji, reaction.message.content))
    
    async def on_message_delete(self, message):
        author = message.author
        content = message.content
        await self.client.send_message(self.client.get_channel(config.channel_logs), ':shield: ``[SERVER_LOG_DELETE_MESSAGES |{}|]`` - {}: {}'.format(date_time,author, content))


def setup(client):
    client.add_cog(Events(client))
    
