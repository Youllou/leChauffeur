# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class active_react(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def active_react(self, ctx, where):
        """
        admin command to active bot reaction
        if activated, the bot will react to certain keywords/expression
        :param ctx: the context (a Discord Object)
        :param where: the channel where the bot should react
               can be either    'partout' (everywhere in french)
                                'nulpart' (nowhere in french)
                                '<a_discord_channel_id>' (you just have to do the #channelName)
        """
        if ctx.author.guild_permissions.administrator:
            if where == 'partout':
                get_info.write(f"./assets/{str(ctx.guild.id)}/active_react.csv", '\a', ['partout'])
            elif where == 'nulpart':
                get_info.write(f"./assets/{str(ctx.guild.id)}/active_react.csv", '\a', ['nulpart'])
            else:
                # we retrieve the id
                channel_id = where[2:-1]
                # and get the corresponding Channel Object
                chan = ctx.guild.get_channel(int(channel_id))
                if chan is None:
                    await ctx.send("Woopsie, le channel indiqué n'a pas été trouvé...")
                else:
                    get_info.append(f'./assets/{str(ctx.guild.id)}/active_react.csv', '\a', [channel_id])
