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
