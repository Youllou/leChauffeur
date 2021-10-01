# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class help(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def help(self,ctx):
        command_chan = get_info.get(f'./assets/{str(ctx.guild.id)}/commandChan.csv', '\a')
        if (not ctx.author.bot) and str(ctx.channel.id) in command_chan:

            reactions = """stp add [message/expression auquel réagir] [réactions+] (si un expression contient des espaces il faut la mettre entre guillemets, vous pouvez mettre plusieurs reactions en le séparant par des espaces)

stp rm [message/expression à supprimer]

stp reaction"""
            randShit = """stp rand {nombre de lettres} {nombre de chiffres}

stp sauce {minSauce} {maxSauce}"""
            picMe = """stp bzzbzz ~~{@somoeone}~~

stp titan ~~{@someone}~~

vos photos ne sont stocké que le temps de l'édition de la photo.
Cependant, les photos envoyés restent stockés sur les serveurs de Discord"""

            games = """stp shifumi [@someone]
            
stp shifu_class"""

            admin = """stp active_react [partout,#ici,nulpart]

stp regarde #ici (#ici étant le channel ou je devrais regarder)

stp goulag [@someone]

stp ajoute_roleReaction [emoji] [@role] (la commande doit etre une réponse au message a ajouter en role_réact et l'emoji ne peut etre un emoji personalisé

stp send [message] (pas besoin de guillemets)"""



            sentence = discord.Embed(title="Tu as demandé de l'aide ? en voici en voilà",
                                     description="entre {} : parametres optionnels, entre [] : parametres obligatoires", color=0xecb683)
            sentence.add_field(name="reactions",value=reactions)
            sentence.add_field(name="random bullshit GO",value = randShit)
            sentence.add_field(name="Be a `insert thing`", value=picMe)
            sentence.add_field(name="Let's play a little Game",value=games)
            sentence.add_field(name="admin only",value=admin)
            await ctx.send(embed=sentence)
