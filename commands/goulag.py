# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class goulag(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.command()
    async def goulag_config(self,ctx,mention):
        print("test")
        if (not ctx.author.bot) and ctx.author.guild_permissions.administrator:
            mention = int("".join(list(mention)[3:-1]))

            role = ctx.guild.get_role(mention)
            if role == None:
                await ctx.send("Euh... j'ai pas trouvé ton rôle... déso déso")
            else :
                try :
                    data = get_info.get("assets/"+str(ctx.guild.id)+"/goulogs.csv",'\a')
                except FileNotFoundError:
                    data = [role.id]
                if len(data) == 1:
                    data[0] = role.id
                else:
                    data[0][0] = role.id
                get_info.write("assets/"+str(ctx.guild.id)+"/goulogs.csv",'\a',data)
                await ctx.send("Le goulag a été construit camarade ! ")

    @commands.command()
    async def goulag(self,ctx, mention):
        if (not ctx.author.bot)  and ctx.author.guild_permissions.administrator:
            goulag_file = f"assets/{str(ctx.guild.id)}/goulogs.csv"
            try :
                get_info.get(goulag_file,"\a")
            except FileNotFoundError:
                await ctx.send("HopHopHop..., il serait apréciable de me dire dans un premier temps quel est le rôle correspondant au goulag...\nUtilise la commande goulag_config et ajoute la mention du rôle")
                return -1

            if type(get_info.get(goulag_file,"\a")[0]) == list :
                goulag_role = ctx.guild.get_role(int(get_info.get(goulag_file,"\a")[0][0]))
            else :
                goulag_role = ctx.guild.get_role(int(get_info.get(goulag_file,"\a")[0]))

            # formatting mention to get id
            mention = list(mention)
            if "!" in mention:
                mention = mention[3:-1]
            else:
                mention = mention[2:-1]
            mention = int("".join(mention))

            # fetching user
            to_goulag = ctx.guild.get_member(mention)
            # checking if the personn is already in the goulag or not
            found = False
            already_in = get_info.get(goulag_file,"\a")
            for i in range(len(already_in)):
                if to_goulag.id == int(already_in[i][0]):
                    # if found, getting goulag off and old roles back
                    await to_goulag.remove_roles(goulag_role)
                    for j in already_in[i][1:]:
                        role = ctx.guild.get_role(int(j))
                        await to_goulag.add_roles(role)
                    already_in.pop(i)
                    get_info.write(goulag_file,"\a",already_in)
                    found = True

            if not found:
                # saving old roles
                old_roles = [to_goulag.id]
                old_roles += [role.id for role in to_goulag.roles[1:]]
                get_info.append(goulag_file, "\a",[old_roles])

                # take back all his roles
                for i in old_roles[1:]:
                    await to_goulag.remove_roles(ctx.guild.get_role(int(i)))
                # give him goulag role
                await to_goulag.add_roles(goulag_role)

                await ctx.send(to_goulag.mention+"\nhttps://cdn.discordapp.com/attachments/779434464387268630/852373824389644298/haha-youre-funny-now-go-to-gulag.jpg")