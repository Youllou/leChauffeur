# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class voice_admin(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command(aliases=['déco'])
    async def deco(self, ctx, mention):
        if (not ctx.author.bot) and ctx.author.guild_permissions.administrator:
            # formatting mention to get id
            mention = list(mention)
            if "!" in mention:
                mention = mention[3:-1]
            else:
                mention = mention[2:-1]
            mention = int("".join(mention))

            # fetching user
            to_deco = ctx.guild.get_member(mention)

            if to_deco.voice is not None:
                await to_deco.edit(voice_channel=None)

    @commands.command(aliases=['demute','démute'])
    async def mute(self, ctx, mention):
        if (not ctx.author.bot) and ctx.author.guild_permissions.administrator:
            # formatting mention to get id
            mention = list(mention)
            if "!" in mention:
                mention = mention[3:-1]
            else:
                mention = mention[2:-1]
            mention = int("".join(mention))

            # fetching user
            to_mute = ctx.guild.get_member(mention)

            if to_mute.voice is not None:
                if to_mute.voice.mute:
                    await to_mute.edit(mute=False)
                else:
                    await to_mute.edit(mute=True)