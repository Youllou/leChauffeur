import datetime
from typing import Optional

import discord
import pytz
from discord import app_commands
from discord.ext import commands


class timestamp(commands.Cog):

    def __init__(self, bot):
        self.leChauffeur = bot

    @app_commands.command(name="timestamp")
    @app_commands.describe(timezone='Your timezone', type="The type of timestamp you want", date='format : dd/mm/yyyy',
                           time='format : hh:mm')
    @app_commands.choices(timezone=[
                                       app_commands.Choice(name=f"UTC+{i}", value=f"Etc/GMT-{i}") for i in range(1, 13)
                                   ] + [
                                       app_commands.Choice(name=f"UTC-{i}", value=f"Etc/GMT+{i}") for i in range(1, 13)
                                   ] + [
                                       app_commands.Choice(name="UTC", value="Etc/GMT")
                                   ])
    @app_commands.choices(type=[
        app_commands.Choice(name="Relative", value="R"),
        app_commands.Choice(name="Short time", value="t"),
        app_commands.Choice(name="Long time", value="T"),
        app_commands.Choice(name="Short date", value="d"),
        app_commands.Choice(name="Long date", value="D"),
        app_commands.Choice(name="Short date/time", value="f"),
        app_commands.Choice(name="Long date/time", value="F")
    ])
    async def timestamp(self, interaction: discord.Interaction, timezone: str, type: str, date: Optional[str],
                        time: Optional[str]):
        """Sends a discord timestamp."""
        pytz_timezone = pytz.timezone(timezone)
        # local_timezone = pytz.timezone(os.environ.get('TIMEZONE'))
        local_timezone = pytz.timezone('EST')
        if date is None:
            date = local_timezone.localize(datetime.datetime.now()).astimezone(pytz_timezone).strftime('%d/%m/%Y')
        if time is None:
            time = local_timezone.localize(datetime.datetime.now()).astimezone(pytz_timezone).strftime('%H:%M')
        localized_time = pytz_timezone.localize(datetime.datetime.strptime(f'{date} {time}', '%d/%m/%Y %H:%M'))
        message = f'<t:{int(localized_time.timestamp())}:{type}>'
        await interaction.response.send_message(message)
