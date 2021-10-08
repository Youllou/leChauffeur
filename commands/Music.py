# discord import
import asyncio
import os
import shutil

import discord
from discord.ext import commands

# local import
from lib import *

# global import
import youtube_dl


class music(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot
        self.players = {}
        self.queue = []
        self.url_queue = []

    @commands.command()
    async def play(self, ctx, url):
        await ctx.message.delete()
        len_queue = len(list(mp3_files for mp3_files in os.listdir(f"./assets/{str(ctx.guild.id)}/music") if mp3_files.endswith(".mp3")))
        self.url_queue.append(url)
        self.queue.append(len_queue)
        if len_queue == 0:
            try:
                ctx.voice_client.is_connected()
            except AttributeError :
                await self.join(ctx)
            async with ctx.typing():
                self.dl(ctx, url,"0")
                await self.start_playing(ctx, url)
        else:
            async with ctx.typing():
                self.dl(ctx, url, self.queue[-1]+1)
                await ctx.send(f"Et hop, {url} ajouté à la suite")

    @commands.command()
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        self.queue = []
        shutil.rmtree(f"./assets/{str(ctx.guild.id)}/music/")

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        self.queue = []
        shutil.rmtree(f"./assets/{str(ctx.guild.id)}/music/")

    async def start_playing(self, ctx, url):
        voice = ctx.voice_client
        await ctx.send(f"Et c'est partie pour {url}")
        voice.play(discord.FFmpegPCMAudio(f"./assets/{str(ctx.guild.id)}/{str(self.queue[0])}.mp3"),after = self.next_after_end(ctx,voice.loop))

    def dl(self, ctx, url, name) -> None:
        ydl_opts = {
            'format': 'betsaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.replace(file, f"./assets/{str(ctx.guild.id)}/{str(name)}.mp3")

    def next_after_end(self,ctx,loop):
        asyncio.run_coroutine_threadsafe(self.next_song(ctx),loop)

    @commands.command(aliases=['next'])
    async def next_song(self,ctx):
        os.remove(f"./assets/{str(ctx.guild.id)}/music/{str(self.queue[0])}.mp3")
        self.queue.pop(0)
        self.url_queue.pop(0)
        if len(self.queue) == 0:
            return
        else :
            await self.start_playing(ctx,self.url_queue[0])