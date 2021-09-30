#discord import
import discord
from discord.ext import commands

# local import
from lib import *

# global import
import os


class on_guild_join(commands.Cog):

    def __init__(self,bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        f = open("./assets/Id2Name.csv", 'a', encoding='UTF-8')
        f.write(f"{str(guild.id)} : {guild.name}\n")
        os.mkdir(f"./assets/{str(guild.id)}")
        f = open(f"./assets/{str(guild.id)}/role_react.csv",'w',encoding='UTF-8')
        f = open(f"./assets/{str(guild.id)}/emote_only_channel.csv",'w',encoding='UTF-8')
        f = open(f"./assets/{str(guild.id)}/reactions.csv",'w',encoding='UTF-8')
        f = open(f"./assets/{str(guild.id)}/commandChan.csv",'w',encoding='UTF-8')
        f = open(f"./assets/{str(guild.id)}/active_react.csv",'w',encoding='UTF-8')

        msg = "Hey, salut à tous\nBon tout d'abord, merci pour l'invitation ^^\nVoici quelques commandes que l'admin doit faire pour que le bot marche à la perfection.\n- `stp regarde #ici` #ici étant le channel ou je devrais regarder les commandes et répondre a celle-ci, vous pouvez ajouter plusieurs channel que je dois regarder\n- `stp active_react {partout,#ici,nulpart}` choisi une des trois options pour activer les réactions (au début il n'y a aucune réactions il faudra utiliser `stp ajoute {mot,'expression de plusieurs mots'} {réaction, 'réaction de plusieurs mots'}`"
        if guild.system_channel :
            await guild.system_channel.send(msg)
        else :
            for j in guild.channels:
                if type(j) == discord.TextChannel:
                    await j.send(msg)
                    break
