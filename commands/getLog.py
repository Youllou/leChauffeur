# discord import
import discord
from discord import app_commands
from discord.ext import commands

# local import
from lib import *


class getLog(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command(aliases=['logs', 'log'])
    async def getLog(self, ctx):
        if ctx.author.id == 280464892258025473:
            with open("./Bot.log", 'r') as log:
                text = log.read()
                # max len of message on discord is 2000 but we add the ``` at beginning and end to format so 2000-6=1994
                if len(text) > 1994:
                    text = text[-1994:-1]
                if len(text) > 0:
                    await ctx.send(f'```{text}```')
                else:
                    await ctx.send("Nothing to report Sir !\nEverything works perfectly !")
            with open("./Bot.log", 'w') as log:
                log.write("")

    @app_commands.command(name="sync")
    async def sync(self, interaction: discord.Interaction):
        """Syncs the application commands to Discord."""
        if 280464892258025473 == interaction.user.id:
            await interaction.response.send_message("Syncing...")
            await self.leChauffeur.tree.sync()
            await interaction.response.edit_message(content="Synced!")
