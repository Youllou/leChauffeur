# discord import
import discord
from discord.ext import commands

# global import
import asyncio

# local import
from ..lib import *


class shifumi(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def shifumi(self, ctx, who):

        global winName
        if ctx.author.mention == who:
            await ctx.send(
                "Mec, si tu te sens seul on peut en parler... Mais je peux pas t'autoriser à jouer contre toi même...")
        else:
            msg = await ctx.send(who + ", " + ctx.author.mention + " vient de te défier au shifumi. Tu accepte ?")
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

            def check(reaction, user):
                return (user.mention == who or user.mention == who.replace("!", "")) and (
                        reaction.emoji == "✅" or reaction.emoji == "❌")

            try:
                reaction, user = await self.leChauffeur.wait_for('reaction_add', timeout=20.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("trop tard... tant pis")
            else:
                if reaction.emoji == "❌":
                    await ctx.send("L'adversaire à refuser le combat...\nPleutre")
                else:
                    j1 = ctx.author

                    if "!" in who:
                        whoId = int(who[3:-1])
                    else:
                        whoId = int(who[2:-1])
                    print(whoId)
                    print(who)
                    j2 = ctx.guild.get_member(whoId)

                    msgJ1 = j2.mention + " a accepté ton challenge. Alors ? Pierre, Feuille ou Ciseaux ?"
                    msgJ2 = j1.mention + " a fait son choix. A ton tours. Alors ? Pierre, Feuille ou Ciseaux ?"
                    choixJ1 = 0
                    choixJ2 = 0

                    while choixJ2 == choixJ1:
                        msg = await j1.send(msgJ1)
                        await msg.add_reaction("🤜")
                        await msg.add_reaction("✋")
                        await msg.add_reaction("✌️")

                        def check(reaction, user):
                            return (user.mention == j1.mention or user.mention == j1.mention.replace("!", "")) and (
                                    reaction.emoji == "🤜" or reaction.emoji == "✋" or reaction.emoji == "✌️")

                        try:
                            reaction, user = await self.leChauffeur.wait_for('reaction_add', timeout=60.0, check=check)
                        except asyncio.TimeoutError:
                            await j1.send("Bon mec t'abuse là")
                            await ctx.send("la partie est annulé...")
                            choixJ2 = -1
                        else:
                            if reaction.emoji == "🤜":
                                choixJ1 = 0
                                await msg.add_reaction("✅")
                            elif reaction.emoji == "✋":
                                choixJ1 = 1
                                await msg.add_reaction("✅")
                            else:
                                choixJ1 = 2
                                await msg.add_reaction("✅")

                            msg = await j2.send(msgJ2)
                            await msg.add_reaction("🤜")
                            await msg.add_reaction("✋")
                            await msg.add_reaction("✌️")

                            def check(reaction, user):
                                return (user.mention == j2.mention or user.mention == j2.mention.replace("!", "")) and (
                                        reaction.emoji == "🤜" or reaction.emoji == "✋" or reaction.emoji == "✌️")

                            try:
                                reaction, user = await self.leChauffeur.wait_for('reaction_add', timeout=60.0, check=check)
                            except asyncio.TimeoutError:
                                await j2.send("Bon mec t'abuse là")
                                await ctx.send("la partie est annulé...")
                                choixJ2 = -1
                            else:
                                if reaction.emoji == "🤜":
                                    choixJ2 = 0
                                    await msg.add_reaction("✅")
                                elif reaction.emoji == "✋":
                                    choixJ2 = 1
                                    await msg.add_reaction("✅")
                                else:
                                    choixJ2 = 2
                                    await msg.add_reaction("✅")

                            if choixJ1 == choixJ2:
                                await j1.send("égalité, on y retourne")
                                await j2.send("égalité, on y retourne")
                                msgJ1 = "Tu sais ce qu'il te reste à faire... Pierre, Feuille ou Ciseaux ?"

                    if choixJ2 == -1:
                        pass
                    elif choixJ1 == 0:
                        if choixJ2 == 1:
                            await ctx.send(j2.mention + " a gagné, +1 point en jouant Feuille")
                            winName = j2.name
                        else:
                            await ctx.send(j1.mention + " a gagné, +1 point en jouant Pierre")
                            winName = j1.name
                    elif choixJ1 == 1:
                        if choixJ2 == 2:
                            await ctx.send(j2.mention + " a gagné, +1 point en jouant Ciseaux")
                            winName = j2.name
                        else:
                            await ctx.send(j1.mention + " a gagné, +1 point en jouant Feuille")
                            winName = j1.name
                    else:
                        if choixJ2 == 0:
                            await ctx.send(j2.mention + " a gagné, +1 point en jouant Pierre")
                            winName = j2.name
                        else:
                            await ctx.send(j1.mention + " a gagné, +1 point en jouant Ciseaux")
                            winName = j1.name

                    score = get_info.get("assets/" + ctx.guild.name + "/score.csv", ",")
                    exist = 0

                    for i in range(len(score)):  # break if found
                        if winName == score[i][0]:
                            exist = 1
                            nLine = i
                            break

                    print(score)

                    if exist == 0:
                        score.append([winName, "1\n"])
                        get_info.write("assets/" + ctx.guild.name + "/score.csv", "\a", score)
                    else:
                        score[nLine][1] = str(int(score[nLine][1]) + 1) + "\n"
                        get_info.write("assets/" + ctx.guild.name + "/score.csv", "\a", score)

        @commands.command()
        async def shifu_class(ctx):
            score = get_info.get("assets/"+ctx.guild.id+"/score.csv","\a")
            print(score)
            sentence = "```\n"
            for i in range(len(score)):
                sentence+= score[i][0]+" : "+score[i][1].replace("\n","")+" pts\n"
            sentence+="```"
            await ctx.send(sentence)
