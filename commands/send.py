# discord import
import discord
from discord.ext import commands

# global import
import asyncio

# local import
from lib import *


class send(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def send(self,ctx,*message):
        if ctx.author.guild_permissions.administrator:
            await ctx.send(" ".join(message))