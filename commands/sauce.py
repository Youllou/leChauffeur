# discord import
import discord
from discord.ext import commands

# global import
import random

MAX_SAUCE = 350680


class sauce(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def sauce(self,ctx, minS=0, maxS=MAX_SAUCE):
        if minS > MAX_SAUCE:
            await ctx.send("There's only " + str(
                MAX_SAUCE) + " at this day...\nTho, if you're sure that there's more you should @ my dumbass creator")
        else:
            await ctx.send("https://nhentai.net/g/" + str(random.randrange(minS, maxS)))
