#discord imports
import discord
from discord.ext import commands

#global imports
import time, random, contextlib, io, shutil, os, requests, sys, asyncio
import importlib as imp
from PIL import Image,ImageDraw

#import listener
from commands import *
from events import *


#local import
from lib import *

intents = discord.Intents.default()
intents.members = True

client = discord.Client()
leChauffeur = commands.Bot(command_prefix='$',intents=intents)

leChauffeur.remove_command('help')



leChauffeur.add_cog(on_ready.on_ready(leChauffeur))












































if __name__ == '__main__':
    leChauffeur.run("Token")
