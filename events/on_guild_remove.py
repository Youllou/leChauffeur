#discord import
import shutil

import discord
from discord.ext import commands

# local import
from lib import *

# global import
import os


class on_guild_remove(commands.Cog):

    def __init__(self,bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        shutil.rmtree(f"/assets/{str(guild.id)}/")