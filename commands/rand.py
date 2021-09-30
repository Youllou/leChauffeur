# discord import
import discord
from discord.ext import commands

# local import
from lib import *

# global import
import random


class rand(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def rand(self, ctx, lettre=2, chiffre=4):
        command_chan = get_info.get(f'./assets/{str(ctx.guild.id)}/commandChan.csv', '\a')
        if (not ctx.author.bot) and str(ctx.channel.id) in command_chan:
            random.seed(a=None)
            alpha = "abcdefghijklmnopqrstuvwxyz"

            url = "https://prnt.sc/"
            for i in range(lettre):
                url += random.choice(alpha)
            for i in range(chiffre):
                url += str(random.randrange(0, 9))

            await ctx.send(url)
