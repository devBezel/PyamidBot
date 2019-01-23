import discord
from discord.ext import commands
import datetime
import asyncio

from utils import default

config = default.get("config.json")
global_time = datetime.datetime.now()
date_time = global_time.strftime("%H:%M %d.%m.%Y")
footer = "Bot created by bezel 🔷 {}".format(date_time)
icon_author = "https://cdn.discordapp.com/attachments/473218411670011904/532690186791026688/pyamid.png"

class Misc:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True)
    async def infobot(self, ctx):
        channel = ctx.message.channel
        em = discord.Embed(title='', description='', colour=discord.Colour.blue())
        em.set_author(name="Informacje o PyamidBot", icon_url=icon_author)
        em.add_field(name="Autor", value="bezel", inline = True)
        em.add_field(name="Data rozpoczęcia prac", value="09/01/2018", inline = True)
        em.add_field(name="Technologia", value="Python", inline = True)
        em.add_field(name="Wersja", value="0.1", inline = True)
        em.add_field(name="Opis", value="Bot stworzony z myślą o społeczności pyamid, jej moderacji i do wspolnej zabawy. Możesz sprawdzić jego możliwości pod komendą !pomoc", inline = True)
        em.set_image(url="https://cdn.discordapp.com/attachments/473218411670011904/533048524502335517/iPEsF.png")
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/473218411670011904/533049638446432286/Discord_Thonk.png")
        em.set_footer(text=footer)
        await self.client.send_message(channel, embed=em)



    @commands.command(pass_context = True)
    async def info(self, ctx, user: discord.Member):
            channel = ctx.message.channel
            user_avatar = user.avatar_url
            em = discord.Embed(title='', description='', colour=discord.Colour.blue())
            em.set_thumbnail(url=user_avatar)
            em.set_author(name='Informacje użytkownika {}'.format(user.name), icon_url=icon_author)
            em.add_field(name='ID użytkownika', value='{}'.format(user.id), inline = True)
            em.add_field(name='Status', value='{}'.format(user.status), inline = True)
            em.add_field(name='Najwyższa rola', value='{}'.format(user.top_role), inline = True)
            em.add_field(name='Dolączył do społeczności pyamid', value='{}'.format(user.joined_at), inline = True)
            em.set_footer(text=footer)
            await self.client.send_message(channel, embed=em)

    @commands.command(pass_context = True)
    async def propozycja(self, ctx, *, args):
            author_message = ctx.message.author
            await self.client.delete_message(ctx.message)

            em = discord.Embed(title="", description= args, colour=discord.Colour.blue())
            em.set_author(name=f"Propozycja od {author_message}.", icon_url=icon_author)
            em.set_footer(text=footer)
            msg = await self.client.send_message(self.client.get_channel(config.channel_suggestion), embed=em)

            emoji = ["✅", "⛔"]
            for i in emoji:
                await self.client.add_reaction(msg, i)

    @commands.command(pass_context = True)
    async def pomoc(self, ctx):
        desc = "**Komendy dla użytkownika**\n\n!info @Algorytm - *informacje o użytkowniku*\n!infobot - *informacje o bocie*\n!propozycja <twoja_propozycja> - *wrzuca twoją wiadomość na kanał #propozycje i zaczyna głosowanie*\n!tweet <tekst> - *tradycyjny tweet (jest on w charakterze ooc, nie używamy go w charakterze IC)*\n!pies - *wysyła zdjęcie randomowego psa*\n!kot - *wysyła zdjęcie randomowego kota*\n!zapytaj <pytanie> - *magiczna kula odpowiada ci na pytanie*\n!hot @Algorytm - *pokazuje na ile % jest hot dany użytkownik*\n!rozmawiaj <tekst> - *rozmawianie z botem*\n\n**GENERATOR MEMOW INSTRUKCJA:**\n\n *Mozecie tworzyć własne memy natomiast obrazki do nich są aktualnie ograniczone, w przyszłości będzie wiecej. Macie 4 argumenty do wypełnienia, 1 argument to maksymalnie jedno słowo!*\n\n!meme <slowo> <słowo> <słowo> <słowo>\n!meme_chuck <slowo> <slowo> <slowo> <slowo>"

        em = discord.Embed(title="", description=desc, colour=discord.Colour.blue())
        em.set_author(name="Komendy i pomoc w użytkowaniu bota", icon_url=icon_author)
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/473218411670011904/535088913992384542/question_2.png")
        em.set_footer(text=footer)

        await self.client.send_message(ctx.message.channel, embed = em)


def setup(client):
    client.add_cog(Misc(client))