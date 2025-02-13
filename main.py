import os, discord, time, platform
from dotenv import load_dotenv
from discord.ext import commands
from colorama import Back, Fore, Style

# LOAD TOKEN AND OTHER VARIABLE FROM ENVIRONMENT
load_dotenv(override= True)
TOKEN = os.getenv('DISCORD_TOKEN')

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('./'), intents= discord.Intents().all())

    async def on_ready(self):
        color_prefix = (Back.BLACK + Fore.LIGHTCYAN_EX + time.strftime('%H:%M:%S LOCAL', time.localtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        print(Fore.WHITE + ''.rjust(45, '-'))
        print(color_prefix + ' Logged in as: ' + Fore.LIGHTMAGENTA_EX + str(self.user.name))
        print(color_prefix + ' Bot ID: ' + Fore.LIGHTMAGENTA_EX + str(self.user.id))
        print(color_prefix + ' Discord Version: ' + Fore.LIGHTYELLOW_EX + discord.__version__)
        print(color_prefix + ' Python Version: ' + Fore.LIGHTYELLOW_EX + platform.python_version())
        print(Fore.WHITE + ''.rjust(45, '-'))

    # LOADS THE COGS INTO MAIN
    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

    # ERROR HANDLING
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        embed = discord.Embed(title='Error')
        if isinstance(error, commands.MissingRequiredArgument):
            embed.description = 'Error, missing required argument.'
        elif isinstance(error, commands.BadArgument):
            embed.description = 'Error, wrong argument.'
        else:
            embed.description = 'Command not found.'
        await ctx.send(embed=embed)

if __name__ == '__main__':
    client = Client()
    client.run(token= TOKEN)