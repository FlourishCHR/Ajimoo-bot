# Ajimoo
 Discord bot
 
 Contains: Music Bot, User and Server information, Timezone updates...etc

SETUP A VIRTUAL ENVIRONMENT
python -m venv venv

Things you need to change/add:
in .env:

DISCORD_TOKEN = Your BOT TOKEN

SERVER_GUILD_ID = Your GUILD ID (SET TO DEVELOPER MODE AND RIGHT CLICK YOUR SERVER > "COPY SERVER ID")

SERVER_CHANNEL_LOCATION = Your Channel ID (Same instruction as Guild but with Channel instead)

in timezone_update:

SERVER_CHANNEL_GUILD and SERVER_CHANNEL_ID in load_dotenv if you need to add more.
Lists of Timezone and Timezone name to put in Channel ID (TIMEZONE_ABBREVIATIONS)
In guild_configs - Listed there.


list of dependencies:
- pytz
- discord.py[voice]
- colorama
- yt_dlp
- python-dotenv

Be sure to often update YT_DLP:

pip install yt_dlp --upgrade

Will update this in the future.

TODO:
- update the whole codebase. (especially the timezone ones)

- add database.

- add new features.
