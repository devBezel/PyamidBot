import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime
import asyncio

from utils import default

config = default.get("config.json")
global_time = datetime.datetime.now()
date_time = global_time.strftime("%H:%M %d.%m.%Y")
footer = "Bot created by bezel 🔷 {}".format(date_time)
icon_author = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"

class Admin:
    def __init__(self, client):
        self.client = client


    
    @commands.command(pass_context = True)
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
        channel = ctx.message.channel
        author_message = ctx.message.author
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
        await self.client.delete_messages(messages)
        em = discord.Embed(title='', description='', colour=discord.Colour.blue())
        em.set_author(name='{} usunął {} wiadomości'.format(author_message, amount), icon_url=icon_author)
        em.set_footer(text=footer)
        await self.client.send_message(channel, embed=em)

    @commands.command(pass_context=True)
    @has_permissions(manage_messages=True)
    async def news(self, ctx, *, args):
        channel = ctx.message.channel
        author_message = ctx.message.author
        await self.client.delete_message(ctx.message)
        
        em = discord.Embed(title="", description=args, colour=discord.Colour.blue())
        em.set_author(name="Ogłoszenie od {}".format(author_message), icon_url=icon_author)
        em.set_footer(text=footer)
        await self.client.send_message(channel, embed=em)

def setup(client):
    client.add_cog(Admin(client))