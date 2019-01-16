import discord
from discord.ext import commands
import datetime
from utils import default, lists
import objectpath
import aiohttp
import asyncio
import random

config = default.get("config.json")
global_time = datetime.datetime.now()
date_time = global_time.strftime("%H:%M %d.%m.%Y")
footer = "Bot created by bezel 🔷 {}".format(date_time)
icon_author = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"

class Fun:
    def __init__(self, client):
        self.client = client

    
    @commands.command(pass_context=True)
    async def tweet(self, ctx, *, args):
        channel = ctx.message.channel
        author_message = ctx.message.author
        await self.client.delete_message(ctx.message)

        em = discord.Embed(title="", description=args, colour=discord.Colour.blue())
        em.set_author(name=f"{author_message} wysłał tweeta!", icon_url="https://cdn.discordapp.com/attachments/473218411670011904/534792044825018427/twitter-logo-7249D46199-seeklogo.png")
        em.set_footer(text=footer)
        await self.client.send_message(channel, embed=em)

    @commands.command(pass_context=True)
    async def pies(self, ctx):
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    res = await r.json()
                    res = res['url']
                    cs.close()
                if res.endswith(".mp4"):
                    pass
                else:
                    isVideo = False
        em = discord.Embed(title="", description="", colour=discord.Colour.blue())
        em.set_author(name="Generator psiakow", icon_url=icon_author)
        em.set_footer(text=footer)
        await self.client.send_message(ctx.message.channel, content=ctx.message.author.mention, embed=em.set_image(url=res))

    @commands.command(pass_context = True)
    async def kot(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat//meow") as r:
                res = await r.json()
                res = res['file']
                cs.close()
        em = discord.Embed(title="", description="", colour=discord.Colour.blue())
        em.set_author(name="Generator kotow", icon_url=icon_author)
        em.set_footer(text=footer)

        await self.client.send_message(ctx.message.channel, content=ctx.message.author.mention, embed=em.set_image(url=res))
    
    @commands.command(pass_context = True)
    async def zapytaj(self, ctx, *, question):
        anwser = random.choice(lists.ball)
        await self.client.send_message(ctx.message.channel, f"🎱 **Pytanie** {question} \n**Odpowiedź** {anwser}")
    
    @commands.command(pass_context = True)
    async def meme(self, ctx, one_text, two_text, three_text, four_text):
        em = discord.Embed(title="", description="", colour=discord.Colour.blue())
        em.set_author(name="Generator memow", icon_url=icon_author)
        em.set_footer(text=footer)

        await self.client.send_message(ctx.message.channel, embed=em.set_image(url=f"http://apimeme.com/meme?meme=Condescending-Wonka&top={one_text}+{two_text}&bottom={three_text}+{four_text}&test=1"))
    
    @commands.command(pass_context = True)
    async def meme_chuck(self, ctx, one_text, two_text, three_text, four_text):
        em = discord.Embed(title="", description="", colour=discord.Colour.blue())
        em.set_author(name="Generator memow", icon_url=icon_author)
        em.set_footer(text=footer)

        await self.client.send_message(ctx.message.channel, embed=em.set_image(url=f"http://apimeme.com/meme?meme=Chuck-Norris-With-Guns&top={one_text}+{two_text}&bottom={three_text}+{four_text}&test=1"))

    @commands.command(pass_context = True)
    async def hot(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.message.author
        
        random.seed(user.id)
        r = random.randint(1, 100)
        person_hot = r / 1.17

        emoji = "💔"
        if person_hot > 25:
            emoji = "❤"
        elif person_hot > 50:
            emoji = "💖"
        else:
            emoji = "💞"
        
        await self.client.send_message(ctx.message.channel, f"{user.name} jest hot na {person_hot:.2f}% {emoji}")


def setup(client):
    client.add_cog(Fun(client))