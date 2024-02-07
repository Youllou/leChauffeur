# discord imports
import discord
from discord.ext import commands
from discord import app_commands

# global imports
import time, random, contextlib, io, shutil, os, requests, sys, asyncio, webbrowser, threading, datetime, pytz
import importlib as imp
from PIL import Image, ImageDraw
from typing import Optional

# import listener
from commands import *
from events import *

# local import
from lib import *

intents = discord.Intents.all()
MY_GUILD = 779434195784564787


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


client = MyClient(intents=intents)
leChauffeur = commands.Bot(command_prefix='stp ', intents=intents)
leChauffeur.client = client
leChauffeur.remove_command('help')

# adding events_listener
event_listener = [clean_embed.clean_embed(leChauffeur),
                  emote_only_listener.emote_only_listener(leChauffeur),
                  on_error.on_error(leChauffeur),
                  on_guild_join.on_guild_join(leChauffeur),
                  on_guild_remove.on_guild_remove(leChauffeur),
                  on_raw_reaction.on_raw_reaction(leChauffeur),
                  on_ready.on_ready(leChauffeur),
                  reactions_listener.reactions_listener(leChauffeur),
                  RoleIncrementor.RoleIncrementor(leChauffeur)]

# adding commands_listener
command_listener = [active_react.active_react(leChauffeur),
                    add_role_message.add_role_message(leChauffeur),
                    bzzbzz.bzzbzz(leChauffeur),
                    genshin.genshin(leChauffeur),
                    getLog.getLog(leChauffeur),
                    goulag.goulag(leChauffeur),
                    help.help(leChauffeur),
                    Music.Music(leChauffeur),
                    rand.rand(leChauffeur),
                    react.react(leChauffeur),
                    regarde.regarde(leChauffeur),
                    sauce.sauce(leChauffeur),
                    send.send(leChauffeur),
                    shifumi.shifumi(leChauffeur),
                    test.test(leChauffeur),
                    timestamp.timestamp(leChauffeur),
                    titan.titan(leChauffeur),
                    voice_admin.voice_admin(leChauffeur)]

if __name__ == '__main__':
    leChauffeur.me = 280464892258025473
    for event in event_listener:
        asyncio.run(leChauffeur.add_cog(event))

    for command in command_listener:
        asyncio.run(leChauffeur.add_cog(command))

    #leChauffeur.run('this_is_not_my_token')
    leChauffeur.run(os.environ['token_Chauffeur'])