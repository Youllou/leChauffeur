# discord import
import discord
from discord.ext import commands

# local import
from lib import *

# global import
import random, os
from PIL import Image, ImageDraw


class bzzbzz(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def bzzbzz(self, ctx, who=None):
        command_chan = get_info.get(f'./assets/{str(ctx.guild.id)}/commandChan.csv', '\a')
        if (not ctx.author.bot) and str(ctx.channel.id) in command_chan:
            usr=None
            if who is None:
                usr = ctx.author

            else:
                for i in ctx.guild.members:
                    if i.mention == who or i.mention == who.replace("!", ""):
                        usr = i

            if usr is None:
                await ctx.send("utilisateur introuvable")
            else:
                random.seed(a=None)

                data = await usr.display_avatar.read()
                with open(f'./assets/{str(ctx.guild.id)}/pfp.png', 'wb') as f:
                    f.write(data)

                bee = random.randrange(1, 4)
                if bee == 1:
                    x = 455
                    y = 300
                    bwidth = int(840 / 5)
                elif bee == 2:
                    x = 124
                    y = 122
                    bwidth = int(900 / 5)
                elif bee == 3:
                    x = 520
                    y = 195
                    bwidth = int(839 / 5)

                imbee = Image.open("./assets/bees/bee" + str(bee) + ".png")
                pp = Image.open(f"./assets/{str(ctx.guild.id)}/pfp.png")
                wpercent = (bwidth / float(pp.size[0]))
                hsize = int((float(pp.size[1]) * float(wpercent)))
                pp = pp.resize((bwidth, hsize), Image.ANTIALIAS)
                xpp, ypp = pp.size

                mask_im = Image.new("L", pp.size, 0)
                draw = ImageDraw.Draw(mask_im)
                draw.ellipse((xpp / 2 - 90, ypp / 2 - 90, 180, 180), fill=255)

                back_im = imbee.copy()
                back_im.paste(pp, (x, y), mask_im)
                back_im.save("./assets/imtosend.png", quality=95)

                with open('./assets/imtosend.png', 'rb') as f:
                    picture = discord.File(f)
                    await ctx.channel.send(content="Bienvenue dans la ruche " + ctx.author.mention, file=picture)

                os.remove('./assets/imtosend.png')
                os.remove(f'./assets/{str(ctx.guild.id)}/pfp.png')
