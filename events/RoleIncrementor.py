import discord
from discord.ext import commands

from ..lib import *

class RoleIncrementor(commands.Cog):

    def __init__(self,bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    def on_message(self,msg):

        if("<@&818526552723423262>" in msg.content):
            romx = self.leChauffeur.get_guild(818160428294471700).get_role(818526552723423262)
            x = romx.name[3:]
            x = int(x)
            x+=1
            await romx.edit(name=romx.name[0:3]+str(x))

        if("<@&888338187175493673>" in msg.content):
            anthonx = self.leChauffeur.get_guild(818160428294471700).get_role(888338187175493673)
            x = anthonx.name[6:]
            x = int(x)
            x+=1
            await anthonx.edit(name=anthonx.name[0:6]+str(x))

        await self.leChauffeur.process_commands(msg)