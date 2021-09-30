# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class active_react(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def active_react(self,ctx,where):
        if ctx.author.guild_permissions.administrator:
            if where == 'partout' :
                get_info.write(f"./assets/{str(ctx.guild.id)}/active_react.csv",'\a',['partout'])
            elif where == 'nulpart' :
                get_info.write(f"./assets/{str(ctx.guild.id)}/active_react.csv",'\a',['partout'])
            else :
                channel_id = where[2:-1]
                chan = ctx.guild.get_channel(int(channel_id))
                if chan is None:
                    await ctx.send("Woopsie, le channel indiqué n'a pas été trouvé...")
                else :
                    get_info.append(f'./assets/{str(ctx.guild.id)}/active_react.csv', '\a', [channel_id])
