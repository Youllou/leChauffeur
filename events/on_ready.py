#discord import
import discord
from discord.ext import commands

#local import
from lib import createarbo

#global import
import os
import sys

class on_ready(commands.Cog):
    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #gw2 = self.leChauffeur.get_guild(818160428294471700)
        #self.leChauffeur.me = gw2.get_member(280464892258025473)
        #quebec = gw2.get_role(1011287598230159410)
        #touriste = gw2.get_role(819875308987351041)
        guilds = self.leChauffeur.guilds
        for i in guilds:
            if str(i.id) not in os.listdir("./assets"):
                createarbo.build(i)
                msg = "Hey, il semblerait que vous m'ayez ajouter alors que j'étais endormi\nBon tout d'abord, merci pour l'invitation ^^\nVoici quelques commandes que l'admin doit faire pour que le bot marche à la perfection.\n- `stp regarde #ici` #ici étant le channel ou je devrais regarder les commandes et répondre a celle-ci, vous pouvez ajouter plusieurs channel que je dois regarder\n- `stp active_react {partout,#ici,nulpart}` choisi une des trois options pour activer les réactions (au début il n'y a aucune réactions il faudra utiliser `stp ajoute {mot,'expression de plusieurs mots'} {réaction, 'réaction de plusieurs mots'}`"
                if i.system_channel :
                    await i.system_channel.send(msg)
                else :
                    for j in i.channels:
                        if type(j) == discord.TextChannel:
                            await j.send(msg)
                            break
        print('Logged on as', self.leChauffeur.user)