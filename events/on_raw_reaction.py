# discord import
import discord
from discord.ext import commands

# local import
from lib import *


class on_raw_reaction(commands.Cog):
    def __init__(self, bot):
        self.leChauffeur = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        test = await self.test(payload)
        if test[0]:
            user = test[1]
            roleid = test[2]
            print(user)
            print(roleid)
            role = self.leChauffeur.get_guild(payload.guild_id).get_role(int(roleid))
            print(role)
            await user.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        test = await self.test(payload)
        if test[0]:
            user = test[1]
            roleid = test[2]
            role = self.leChauffeur.get_guild(payload.guild_id).get_role(int(roleid))
            await user.remove_roles(role)

    async def test(self, payload) -> ():
        try:
            dat = get_info.get(f"./assets/{str(payload.guild_id)}/role_react.csv", '\a')
        except FileNotFoundError:
            await self.leChauffeur.me.send(
                f"erreur on_raw_reaction_add => FileNotFoundError for guild {self.leChauffeur.get_guild(payload.guild_id)}")
        else:
            if type(dat[0]) == list:
                for row in dat:
                    isgood = await self.testline(row, payload)
                    if isgood[0]:
                        return isgood
                return False,
            elif dat is not None:
                return await self.testline(dat, payload)

            else:
                print("nik")
                return False,

    async def testline(self, row, payload) -> ():
        # 3 tests => could write them in if ... and ... and... format but too long

        if int(row[0]) == payload.message_id:
            current_message = await self.leChauffeur.get_channel(payload.channel_id).fetch_message(
                payload.message_id)
            if str(payload.emoji.id) == row[1]:
                user = await self.leChauffeur.get_guild(payload.guild_id).fetch_member(payload.user_id)
                if not user.bot:
                    print(True)
                    return True, user, row[2]
                else:
                    return False,
            else:
                return False,
        else:
            return False,
