#discord import
import discord
from discord.ext import commands

#global import
import re

#local import
from lib import *

class add_role_message(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def ajoute_roleReaction(self, ctx, emoji, role):
        command_chan = get_info.get(f'./assets/{str(ctx.guild.id)}/commandChan.csv','\a')
        if (not ctx.author.bot) and str(ctx.channel.id) in command_chan :
            emoji_pattern = re.compile("["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       u"\U00002702-\U000027B0"
                                       u"\U000024C2-\U0001F251"
                                       "]+", flags=re.UNICODE)
            if ctx.author.guild_permissions.administrator:
                try:
                    old = get_info.get(f"./assets/{str(ctx.guild.id)}/role_react.csv",'\a')
                except FileNotFoundError:
                    await self.leChauffeur.me.send(f"erreur ajoute_roleReaction => FileNotFoundError for guild {ctx.guild.id}")
                else:
                    if ctx.message.reference is None:
                        await ctx.send("Veuillez répondre au message que vous voulez ajouter en commande de réaction")
                    elif type(emoji) == discord.Emoji or emoji_pattern.search(emoji) is None:
                        await ctx.send("Désolé, la commande ne prend pas encore en compte les emojis personalisé\nCa arrivera un jour ne vous inquiétez pas")
                    elif ctx.guild.get_role(int(role[3:-1])) is None:
                        await ctx.send("Woopsi, le role que tu as donné n'a pas été trouvé\nN'hésite pas a faire un petit stp aide_moi pour avoir des infos sur les commandes")
                    else :
                        original = await ctx.channel.fetch_message(ctx.message.reference.message_id)
                        newDat = [original.id,emoji,int(role[3:-1])]
                        get_info.append(f"./assets/{str(ctx.guild.id)}/role_react.csv",'\a',newDat)
                        await original.add_reaction(emoji)