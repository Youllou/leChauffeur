# discord import
import discord
from discord.ext import commands

# global import
import re

# local import
from ..lib import *


class add_role_message(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def ajoute_reaction(self, ctx, toReact, *reaction):

        exist = 0
        i = 6
        path = f"./assets/{str(ctx.guild.id)}/reactions.csv"

        # get data
        reactions = get_info.get(path, '\a')

        # verifying if the first expression already exists or not
        for i in range(len(reactions)):
            if toReact.lower() == str(reactions[i][0]).lower():
                exist = 1
                nline = i
                break

        # if the first expression doesn't exits we just write all the message
        if exist == 0:
            get_info.append(path, '\a', [toReact] + reaction)

        # else, we take only the reactions part and add it to the already existing line
        else:
            tmp = ""
            for cols in range(len(reactions[nline]) - 1):
                tmp += reactions[nline][cols]
            reactions[nline] = tmp
            for elmnt in reaction:
                reactions[nline] += "\a" + elmnt
            reactions[nline] += "\n"
            get_info.write(path,'\a',reactions)

        await ctx.message.delete()

    @commands.command()
    async def rm(self, ctx, toReact):

        reactions = []
        exists = 0

        f = open("assets/reactions.csv", "r", encoding="UTF-8")
        while 1:
            line = f.readline()
            if line == "":
                break
            else:
                reactions += [line.split(",")]
        f.close()

        for i in range(len(reactions)):
            if toReact == reactions[i][0]:
                nLine = i
                exists = 1
                break

        if exists == 1:
            f = open("assets/reactions.csv", "r", encoding="UTF-8")
            text = f.readlines()
            f.close()
            text.pop(nLine)
            f = open("assets/reactions.csv", "w", encoding="UTF-8")
            f.writelines(text)
            await ctx.message.delete()
        else:
            await ctx.send("Cette expression n'a pas été trouvé")
