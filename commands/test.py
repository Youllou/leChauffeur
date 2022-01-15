# discord import
import asyncio

import discord
from discord.ext import commands

# local import
from lib import *

# global import
import requests, random, os
from PIL import Image, ImageDraw


class test(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("stp join")
        await asyncio.sleep(2)
        await ctx.send("stp leave")
        await asyncio.sleep(2)
        await ctx.send("stp join")
        await asyncio.sleep(2)
        await ctx.send("stp play https://www.youtube.com/watch?v=eZTQ5L_su8M&ab_channel=funk")
        await asyncio.sleep(2)
        await ctx.send("stp play du propre")
        await asyncio.sleep(2)
        await ctx.send("stp queue")
