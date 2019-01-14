import discord
from discord.ext import commands
import datetime
import asyncio

from utils import default

class Admin:
     def __init__(self, client):
         self.client = client
         #self.config = default.get("config.json")
         #self.global_time = datetime.datetime.now()
         #self.date_time = self.global_time.strftime("%H:%M %d.%m.%Y")
         #self.footer = "Bot created by bezel 🔷 {}".format(self.datetime)
         #self.icon_author = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"


    @commands.command(pass_context = True)
    async def clear(self, ctx, amount=100):
        channel = ctx.message.channel
        author_message = ctx.message.author

        messages = []
        async for message in client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await client.delete_messages(messages)
        em = discord.Embed(title='', description='', colour=discord.Colour.blue())
        em.set_author(name='{} usunął {} wiadomości'.format(author_message, amount), icon_url="self.icon_author")
        em.set_footer(text="self.footer")
        await client.send_message(channel, embed=em)

def setup(client):
    client.add_cog(Admin(client))
