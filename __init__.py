# discord imports
import discord
from discord.ext import commands

# global imports
import time, random, contextlib, io, shutil, os, requests, sys, asyncio
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
                  on_raw_reaction.on_raw_reaction(leChauffeur),
                  on_ready.on_ready(leChauffeur),
                  reactions_listener.reactions_listener(leChauffeur),
                  RoleIncrementor.RoleIncrementor(leChauffeur)]
for event in event_listener:
    leChauffeur.add_cog(event)

# adding commands_listener
command_listener = [add_role_message.add_role_message(leChauffeur),
                    bzzbzz.bzzbzz(leChauffeur),
                    react.react(leChauffeur),
                    sauce.sauce(leChauffeur),
                    rand.rand(leChauffeur)]
for command in command_listener:
    leChauffeur.add_cog(command)

if __name__ == '__main__':
    leChauffeur.run("Token")
