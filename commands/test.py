# discord import
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
        print("commande test :")
        print(ctx)
        msg = await ctx.send("réagis pour tester")
        await msg.add_reaction('\N{THUMBS UP SIGN}')
        self.leChauffeur.test = msg.id
