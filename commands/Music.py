# discord import
import asyncio
import os
import re
import shutil

import discord
from discord.ext import commands

# local import
from lib import *

# global import
import pytube


class Music(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot
        self.players = {}
        self.queue = []

    @commands.command()
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()

    @commands.command(aliases=["resume","add"])
    async def play(self, ctx, *query):
        if query == () and len(self.queue) > 0 and ctx.voice_client.is_paused:
            ctx.voice_client.resume()
        else:
            query = " ".join(query)
            await ctx.message.delete()
            if query.startswith("https://www.y"):
                url = query
                yt = pytube.YouTube(url)
            else:
                search = pytube.Search(query)
                yt = search.results[0]
            if len(self.queue) == 0:
                try:
                    ctx.voice_client.is_connected()
                except AttributeError:
                    await self.join(ctx)
                async with ctx.typing():
                    self.dl(ctx, yt)
                    await self.start_playing(ctx, yt.title)
            else:
                async with ctx.typing():
                    self.dl(ctx, yt)
                    await ctx.send(f"Et hop, {yt.title} de {yt.author} ajouté à la suite")

    @commands.command(aliases=['next'])
    async def next_song(self, ctx):
        # os.remove(f"./assets/{str(ctx.guild.id)}/music/{str(self.queue[0])}.webm")
        self.queue.pop(0)
        if len(self.queue) == 0:
            return
        else:
            await self.start_playing(ctx, self.queue[0])

    @commands.command()
    async def again(self,ctx):
        self.queue.insert(0,self.queue[0])
        await ctx.send(f"Et c'est repartit pour {self.queue[0]}")

    @commands.command(aliases=["pause"])
    async def stop(self, ctx):
        ctx.voice_client.pause()

    @commands.command(aliases=["clear"])
    async def clear_queue(self, ctx):
        current = self.queue[0]
        self.queue = [current]

    @commands.command(aliases=['casse toi', 'sors'])
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        self.queue = []
        shutil.rmtree(f"./assets/{str(ctx.guild.id)}/music/")
        os.mkdir(f"./assets/{str(ctx.guild.id)}/music/")

    @commands.command()
    async def queue(self, ctx):
        if len(self.queue) == 0:
            await ctx.send("la file est vide... ajoute des musiques en utilisant play")
        else:
            embed = discord.Embed(title="Et hop voilà ce qu'il y a à suivre",
                                  description=f"En ce moment : {self.queue[0]}")
            will_follow = ""
            if len(self.queue) > 1:
                for i in self.queue[1:-1]:
                    will_follow += i+"\n"
                will_follow += self.queue[-1]
                embed.add_field(name="Ensuite", value=will_follow)
            else:
                embed.add_field(name="c'est tout...", value=":blank:")
            await ctx.send(embed=embed)

    async def start_playing(self, ctx, title):
        voice = ctx.voice_client
        if voice.is_playing:
            voice.pause()
        await ctx.send(f"Et c'est partie pour {title}")
        self.voice = voice
        self.ctx = ctx
        voice.play(discord.FFmpegPCMAudio(f"./assets/{str(ctx.guild.id)}/music/{str(self.queue[0])}.webm"),
                   after= self.next_after_end)

    def dl(self, ctx, yt) -> None:
        stream = yt.streams.get_by_itag(251)
        name = re.sub("<|>|:|\"|/|\\|\||\?|\*|\'", '', yt.title)
        self.queue.append(name)
        stream.download(output_path=f"./assets/{str(ctx.guild.id)}/music/", filename=f"{str(name)}.webm")

    def next_after_end(self, error):
        asyncio.run_coroutine_threadsafe(self.next_song(self.ctx),self.voice.loop)