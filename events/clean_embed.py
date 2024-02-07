# discord import
import discord
from discord.ext import commands

# global import
import random
import re
import requests

# local import
from lib import *


def tweet_has_video(tweet):
    data = requests.get(tweet.replace("vxtwitter.com", "api.vxtwitter.com")).json()
    if "error" in data:
        return False
    elif len(data["media_extended"]) > 0:
        if any([x["type"] == "video" for x in data["media_extended"]]):
            return True
    return False


class clean_embed(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
        if "tiktok.com" in msg.content and "vxtiktok.com" not in msg.content:
            url = re.search("(?P<url>https?://[^\s]+)", msg.content).group("url")
            url = url.replace("tiktok.com", "vxtiktok.com")
            await msg.reply(f"le lien avec un embed qui marche : \n{url}")
        if "twitter.com" in msg.content and "vxtwitter.com" not in msg.content:
            url = re.search("(?P<url>https?://[^\s]+)", msg.content).group("url")
            url = url.replace("twitter.com", "vxtwitter.com")
            if tweet_has_video(url):
                await msg.reply(f"le lien avec un embed qui marche : \n{url}")
        if "https://x.com" in msg.content and "vx.com" not in msg.content:
            url = re.search("(?P<url>https?://[^\s]+)", msg.content).group("url")
            url = url.replace("x.com", "vxtwitter.com")
            data = requests.get(url.replace("vxtwitter.com", "api.vxtwitter.com")).json()
            if tweet_has_video(url):
                await msg.reply(f"le lien avec un embed qui marche : \n{url}")