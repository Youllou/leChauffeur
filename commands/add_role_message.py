# discord import
import discord
from discord.ext import commands

# global import
import re

# local import
from lib import *


class add_role_message(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def ajoute_roleReaction(self, ctx, emoji, role):

        command_chan = get_info.get(f'./assets/{str(ctx.guild.id)}/commandChan.csv', '\a')
        if (not ctx.author.bot):
            num = "0123456789"
            emoji_pattern = re.compile("["
                                       u"\U00002600-\U000027BF"
                                       u"\U0001F000-\U0001FBF9"  # emoticons
                                       "]+", flags=re.UNICODE)
            print(ctx.author.guild_permissions.administrator)
            if ctx.author.guild_permissions.administrator:
                
                try:
                    old = get_info.get(f"./assets/{str(ctx.guild.id)}/role_react.csv", '\a')
                except FileNotFoundError:
                    await self.leChauffeur.me.send(
                        f"erreur ajoute_roleReaction => FileNotFoundError for guild {ctx.guild.id}")
                else:
                    if ctx.message.reference is None:
                        await ctx.send("Veuillez répondre au message que vous voulez ajouter en commande de réaction")


                    elif ctx.guild.get_role(int(role[3:-1])) is None:
                        await ctx.send(
                            "Woopsi, le role que tu as donné n'a pas été trouvé\n"
                            "N'hésite pas a faire un petit stp aide_moi pour avoir des infos sur les commandes")

                    else:
                        if emoji_pattern.search(emoji) is None:
                            emoji = get_emoji_id.get_emoji_id(emoji)
                            emoji_object = self.leChauffeur.get_emoji(int(emoji))
                            if emoji_object is None :
                                await ctx.send("Arf... désolé, j'ai pas accés au serveur qui a cet émoji...")
                                return
                        else :
                            emoji_object = emoji
                        
                        original = await ctx.channel.fetch_message(ctx.message.reference.message_id)
                        newDat = [original.id, emoji, int(role[3:-1])]
                        get_info.append(f"./assets/{str(ctx.guild.id)}/role_react.csv", '\a', newDat)
                        await original.add_reaction(emoji_object)
                        await ctx.message.delete()


