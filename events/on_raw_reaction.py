#discord import
import discord
from discord.ext import commands

#local import
from lib import *


class on_raw_reaction(commands.Cog):
    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        test = await self.test(payload)
        if test[0]:
            user = test[1]
            dat = test[2]
            await user.add_roles(self.leChauffeur.get_guild(payload.guild_id).get_role(int(dat[2])))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        test = await self.test(payload)
        if test[0]:
            user = test[1]
            dat = test[2]
            await user.remove_roles(self.leChauffeur.get_guild(payload.guild_id).get_role(dat[2]))

    async def test(self, payload):
        try:
            dat = get_info.get(f"./assets/{str(payload.guild_id)}/role_react.csv", '\a')
        except FileNotFoundError:
            await self.leChauffeur.me.send(f"erreur on_raw_reaction_add => FileNotFoundError for guild {self.leChauffeur.get_guild(payload.guild_id)}")
        else:
            if len(dat) >= 1:
                for row in dat:
                    # 3 tests => could write them in if ... and ... and... format but too long

                    if int(row[0]) == payload.message_id:
                        current_message = await self.leChauffeur.get_channel(payload.channel_id).fetch_message(
                            payload.message_id)
                        if str(payload.emoji) == dat[1]:
                            user = await self.leChauffeur.get_guild(payload.guild_id).fetch_member(payload.user_id)
                            if not user.bot:
                                return True, user, dat
                            else:
                                return False,
                        else:
                            return False,
                    else:
                        return False,
            else:
                return False,

