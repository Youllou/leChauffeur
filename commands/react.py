# discord import
import discord
from discord.ext import commands

# local import
from ..lib import *


class react(commands.Cog):

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
                reactions[nline].append(elmnt)
            reactions[nline] += "\n"
            get_info.write(path, '\a', reactions)

        await ctx.message.delete()

    @commands.command()
    async def rm(self, ctx, toReact):

        exists = 0
        path = f"./assets/{str(ctx.guild.id)}/reactions.csv"

        # get data
        reactions = get_info.get(path, '\a')

        # search for element
        for i in range(len(reactions)):
            if toReact == reactions[i][0]:
                nLine = i
                exists = 1
                break

        # del line if exists
        if exists == 1:
            reactions.pop(nLine)
            get_info.write(path, '\a', reactions)
            await ctx.message.delete()
        else:
            await ctx.send("Cette expression n'a pas été trouvé")

    @commands.command()
    async def reaction(self, ctx):

        expression = ""
        path = f"./assets/{str(ctx.guild.id)}/reactions.csv"

        # get data
        reactions = get_info.get(path, '\a')

        for rows in reactions:
            expression += str(rows[0]) + "\n"
            print(rows[0])

        sentence = discord.Embed(title="Voici l'ensemble des mots/expressions aux quels je réagis",
                                 description=expression, color=0xecb683)
        await ctx.send(embed=sentence)
