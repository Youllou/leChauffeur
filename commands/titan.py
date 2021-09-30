# discord import
import os

import discord
from discord.ext import commands

# global import
import requests, random
from PIL import Image, ImageDraw


class titan(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def titan(self, ctx, who=None):
        if who is None:
            usr = ctx.author

        else:
            for i in ctx.guild.members:
                if i.mention == who or i.mention == who.replace("!", ""):
                    usr = i

        if usr is None:
            await ctx.send("utilisateur introuvable")
        else:
            with requests.get(usr.avatar_url_as(format='png')) as r:
                img_data = r.content
            with open(f'assets/{str(ctx.guild.id)}/pfp.png', 'wb') as handler:
                handler.write(img_data)

            titan = random.randrange(1, 5)
            if titan == 1:
                x = 360
                y = 50
                twidth = int(840 / 5)
            if titan == 2:
                x = 60
                y = 20
                twidth = int(840 / 5)
            if titan == 3:
                x = 1076
                y = 0
                twidth = int(840 / 5)
            if titan == 4:
                x = 311
                y = 50
                twidth = int(840 / 5)

            imtitan = Image.open("assets/titans/titan" + str(titan) + ".png")
            pp = Image.open(f'assets/{str(ctx.guild.id)}/pfp.png')
            wpercent = (twidth / float(pp.size[0]))
            hsize = int((float(pp.size[1]) * float(wpercent)))
            pp = pp.resize((twidth, hsize), Image.ANTIALIAS)
            xpp, ypp = pp.size

            mask_im = Image.new("L", pp.size, 0)
            draw = ImageDraw.Draw(mask_im)
            draw.ellipse((xpp / 2 - 90, ypp / 2 - 90, 180, 180), fill=255)
            back_im = imtitan.copy()
            back_im.paste(pp, (x, y), mask_im)
            back_im.save(f'assets/{str(ctx.guild.id)}/imtosend.png', quality=95)

            with open(f'assets/{str(ctx.guild.id)}/imtosend.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)

            os.remove(f'assets/{str(ctx.guild.id)}/pfp.png')
            os.remove(f'assets/{str(ctx.guild.id)}/imtosend.png')
