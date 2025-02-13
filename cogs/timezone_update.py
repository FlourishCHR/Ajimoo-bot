import pytz, os
from discord.ext import commands, tasks
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override= True)
SERVER_GUILD = os.getenv('SERVER_GUILD_ID')
SERVER_CHANNEL_ID = os.getenv('SERVER_CHANNEL_ID')

# 'TZ-Name from pytz' : name in channel
TIMEZONE_ABBREVIATIONS = {
    #'America/Argentina/Buenos_Aires': 'Argentina', #UTC-03
    #'US/Central': 'US-Central', #UTC-06
    #'US/Pacific': 'US-Pacific', #UTC-08
    #'Europe/Madrid' : 'Spain', #UTC+02
    #'Asia/Singapore': 'Asia UTC+8', #UTC+08
    #'Asia/Manila': 'Philippines', #UTC+08
    #'Japan': 'Japan', #UTC+09
}

class timezone_update(commands.Cog):
    def __init__(self, client: commands.Bot, guild_id: int, channel_ids: dict, interval_minutes: int = 10):
        self.client = client
        self.guild_id = guild_id
        self.channel_ids = channel_ids
        self.interval_minutes = interval_minutes
        self.timezone_update.start()

    def cog_unload(self):
        self.timezone_update.stop()

    @tasks.loop(minutes=10)
    async def timezone_update(self):
        guild = self.client.get_guild(self.guild_id) or await self.client.fetch_guild(self.guild_id)
        for channel_id, timezone in self.channel_ids.items():
            channel = guild.get_channel(channel_id) or await self.client.fetch_channel(channel_id)
            if channel:
                current_time = datetime.now(pytz.timezone(timezone))
                timezone_abbreviation = TIMEZONE_ABBREVIATIONS.get(timezone, timezone)
                await channel.edit(name=f'🕓 {timezone_abbreviation} {current_time.strftime("%H:%M")}')
            else:
                print(f"Channel with ID {channel_id} not found in guild {guild.name}")

async def setup(client: commands.Bot) -> None:
    # GUILD ID: {Channel ID: Timezone}
    guild_configs = {
         # SERVER Guild ID
        SERVER_GUILD: {
            # SERVER_CHANNEL_ID IN .env: Timezone

        }
    }
    interval_minutes = 10
    # This should most likely load the cog once. If it works, it works
    loaded_cog = False
    for guild_id, channels in guild_configs.items():
        if not loaded_cog:
            await client.add_cog(timezone_update(client, guild_id, channels, interval_minutes))
            loaded_cog = True