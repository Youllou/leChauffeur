# discord import
import re

import discord
from discord.ext import commands

# global import
import random

# local import
from lib import *


class clean_embed(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        url=re.search("(?P<url>https?://[^\s]+)", msg.content).group("url")
        if "tiktok.com" in msg.content and "vxtiktok.com" not in msg.content:
            url = url.replace("tiktok.com", "vxtiktok.com")
        if "twitter.com" in msg.content and "vxtwitter.com" not in msg.content:
            url = url.replace("twitter.com", "vxtwitter.com")
        if msg.author != self.leChauffeur.user:
            await msg.reply(f"le lien avec un embed qui marche : \n{url}")