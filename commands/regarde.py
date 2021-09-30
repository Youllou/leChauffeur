# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class regarde(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def regarde(self, ctx, channel):
        if ctx.author.guild_permissions.administrator:
            channel_id = channel[2:-1]
            chan = ctx.guild.get_channel(int(channel_id))
            if chan is None:
                await ctx.send("Woopsie, le channel indiqué n'a pas été trouvé...")
            else :
                get_info.append(f'./assets/{str(ctx.guild.id)}/commandChan.csv', '\a', [channel_id])
