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

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
leChauffeur = commands.Bot(command_prefix='stp ', intents=intents)

leChauffeur.remove_command('help')

# adding events_listener
event_listener = [emote_only_listener.emote_only_listener(leChauffeur),
                  on_guild_join.on_guild_join(leChauffeur),
                  on_guild_remove.on_guild_remove(leChauffeur),
                  on_raw_reaction.on_raw_reaction(leChauffeur),
                  on_ready.on_ready(leChauffeur),
                  reactions_listener.reactions_listener(leChauffeur),
                  RoleIncrementor.RoleIncrementor(leChauffeur)]
for event in event_listener:
    leChauffeur.add_cog(event)

# adding commands_listener
command_listener = [active_react.active_react(leChauffeur),
                    add_role_message.add_role_message(leChauffeur),
                    bzzbzz.bzzbzz(leChauffeur),
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

for command in command_listener:
    leChauffeur.add_cog(command)


if __name__ == '__main__':
    leChauffeur.run(os.environ['token'])
