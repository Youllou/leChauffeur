#discord import
import discord
from discord.ext import commands

#local import
from lib import *


class emote_only_listener(commands.Cog):

    def __init__(self,bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_message(self,msg):
        if not msg.author.bot :
            chanEmoteOnly = get_info.get(f"./assets/{str(msg.guild.id)}/emote_only_channel.csv","\a")
            isEmoteOnly = False
            for i in chanEmoteOnly:
                if str(msg.channel.id)+"\n" == i[0]:
                    isEmoteOnly = True


            if isEmoteOnly and msg.author != self.leChauffeur.user:
                cleaned_message = remove_emoji.main(msg.content)
                i = 0
                has_text = False
                while i < len(cleaned_message):

                    if cleaned_message[i:i + 2] == "<:":
                        print("has custom")
                        while cleaned_message[i] != ">":
                            i += 1
                        i += 1
                        try:
                            if cleaned_message[i] == " ":
                                i += 1
                        except IndexError:
                            pass

                    elif cleaned_message[i] == " " or cleaned_message[i] == "\n":
                        print("has space")
                        i += 1

                    else:
                        print("has text")
                        has_text = True
                        i += 1
                    print("\n")

                    if has_text:
                        await msg.delete()