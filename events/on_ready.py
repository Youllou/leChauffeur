#discord import
import discord
from discord.ext import commands

#global import
import os

class on_ready(commands.Cog):
    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.leChauffeur.me = self.leChauffeur.get_guild(779434463834275841).get_member(280464892258025473)

        guilds = self.leChauffeur.guilds
        for i in guilds:
            if str(i.id) not in os.listdir("./assets"):
                f = open("./assets/Id2Name.csv", 'a', encoding='UTF-8')
                f.write(f"{str(i.id)} : {i.name}\n")
                os.mkdir(f"./assets/{str(i.id)}")
                f = open(f"./assets/{str(i.id)}/role_react.csv",'w',encoding='UTF-8')
                f = open(f"./assets/{str(i.id)}/emote_only_channel.csv",'w',encoding='UTF-8')
                f = open(f"./assets/{str(i.id)}/reactions.csv",'w',encoding='UTF-8')
                f = open(f"./assets/{str(i.id)}/commandChan.csv",'w',encoding='UTF-8')
                f = open(f"./assets/{str(i.id)}/active_react.csv",'w',encoding='UTF-8')
                msg = "Hey, il semblerait que vous m'ayez ajouter alors que j'étais endormi\nBon tout d'abord, merci pour l'invitation ^^\nVoici quelques commandes que l'admin doit faire pour que le bot marche à la perfection.\n- `stp regarde #ici` #ici étant le channel ou je devrais regarder les commandes et répondre a celle-ci, vous pouvez ajouter plusieurs channel que je dois regarder\n- `stp active_react {partout,#ici,nulpart}` choisi une des trois options pour activer les réactions (au début il n'y a aucune réactions il faudra utiliser `stp ajoute {mot,'expression de plusieurs mots'} {réaction, 'réaction de plusieurs mots'}`"
                if i.system_channel :
                    await i.system_channel.send(msg)
                else :
                    for j in i.channels:
                        if type(j) == discord.TextChannel:
                            await j.send(msg)
                            break
