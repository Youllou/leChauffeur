# discord imports
import discord
from discord.ext import commands

# global imports
import time, random, contextlib, io, shutil, os, requests, sys, asyncio, webbrowser, threading
import importlib as imp
from PIL import Image, ImageDraw

# import listener
from commands import *
from events import *

# local import
from lib import *

intents = discord.Intents.all()

client = discord.Client(intents=intents)
leChauffeur = commands.Bot(command_prefix='stp ', intents=intents)

leChauffeur.remove_command('help')

# adding events_listener
event_listener = [emote_only_listener.emote_only_listener(leChauffeur),
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
                    titan.titan(leChauffeur),
                    voice_admin.voice_admin(leChauffeur)]


if __name__ == '__main__':

    for event in event_listener:
        asyncio.run(leChauffeur.add_cog(event))

    for command in command_listener:
        asyncio.run(leChauffeur.add_cog(command))

    leChauffeur.run(os.environ['token_Chauffeur'])
