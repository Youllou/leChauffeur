#discord import
import discord
from discord.ext import commands

# local import
from lib import *

# global import
import os


class on_error(commands.Cog):

    def __init__(self,bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_error(self,event, *args, **kwargs):
        if event == 'on_message':
            pass
        else:
            # print the error with the guild name and the channel name
            print(f'Error for {event} with {args[0].guild.name} in {args[0].channel.name} at {args[0].created_at}')
            print(sys.exc_info())



    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        print(f'Error for command { ctx.command if ctx.command else ctx.message.content } with {ctx.guild.name} in {ctx.channel.name} at {ctx.message.created_at}')
        print(error)
