# discord import
import discord
from discord.ext import commands

class genshin(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def genshin(self, ctx, code):
        #delete message
        await ctx.message.delete()
        url = f'https://genshin.mihoyo.com/en/gift?code={code}'
        sentence = f"Merci {ctx.author.mention} d'avoir partagé le code {code} !\nVoici le lien pour avoir la récompense : {url}"
        await ctx.send(sentence)
