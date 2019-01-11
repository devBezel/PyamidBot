import discord
import datetime

from utils import default

class Events:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.footer = "Bot created by bezel 🔷 {}".format(TIME_DATE)
        self.date_time = global_time.strftime("%H:%M %d.%m.%Y")
    
    @client.event
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, name='Użytkownik')
        await client.add_roles(member, role)
        em = discord.Embed(title='Witamy na serwerze pyamid.pl {}'.format(member.name), description='', colour=discord.Colour.blue())
        em.set_author(name='PyamidRP', icon_url=ICON_URL)
        em.set_thumbnail(url=ICON_URL)
        em.add_field(name='Strona internetowa', value='pyamid.pl', inline=True)
        em.add_field(name='Panel gracza', value='Wkrotce', inline=True)
        em.set_footer(text=self.footer)
        await client.send_message(client.get_channel('532686123508432897'), embed=em)

    @client.event
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await client.send_message(client.get_channel('532671695782150146'), ':shield: ``[SERVER_LOG_ADD_EMOJI |{}|]`` - {} dodał emoji {} do wiadomości: {}'.format(self.date_time, user.name, reaction.emoji, reaction.message.content))
    
    @client.event
    async def on_message_delete(self, message):
        author = message.author
        content = message.content
        channel = message.channel
        await client.send_message(client.get_channel('532671695782150146'), ':shield: ``[SERVER_LOG_DELETE_MESSAGES |{}|]`` - {}: {}'.format(self.date_time,author, content))

