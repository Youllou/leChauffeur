#discord import
import discord
from discord.ext import commands

#global import
import random

#local import
from lib import *

class reactions_listener(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        """
              this fonction react to certain message depending on
              what is in the reactions.csv file
              reaction can be added by using ^^add `word/expression to react to`,`word/expression to say`
        """
        # || tiktok dl project, does not work
        # if "https://vm.tiktok.com/" in msg.content:
        #     msglisted = list(msg.content)
        #     i = 0
        #     while i <= len(msglisted):
        #         if "".join(msglisted[i:i+22]) == "https://vm.tiktok.com/":
        #             msglisted = msglisted[i:]
        #             i+=22
        #             while msglisted[i] != '/':
        #                 i+=1
        #             msglisted = msglisted[:i+1]
        #             break
        #         i+=1
        #
        #     tiktokUrl = "".join(msglisted)
        #
        #     await msg.channel.send(ttdl.dl(tiktokUrl))

        active_react = get_info.get(f'./assets/{str(msg.guild.id)}/active_react.csv', '\a')
        if (not msg.author.bot):
            if active_react[0] == 'nulpart':
                await self.leChauffeur.process_commands(msg)
                return
            elif active_react[0] == 'partout' or str(msg.channel.id) in active_react:

                random.seed(a=None)

                if not msg.author.bot and not msg.content.startswith("^^"):
                    reactions = get_info.get(f"./assets/{str(msg.guild.id)}/reactions.csv","\a")

                    for i in range(len(reactions)):
                        answer = []
                        if ((reactions[i][0].lower() in msg.content.lower() and " " in reactions[i][0]) or (
                                (reactions[i][0].lower() in msg.content.lower().split() and " " not in reactions[i][0]))):
                            for j in range(1, len(reactions[i])):
                                answer.append(reactions[i][j].replace("\\n", "\n"))
                            await msg.channel.send(random.choice(answer))
                await self.leChauffeur.process_commands(msg)
