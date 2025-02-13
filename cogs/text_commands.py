from discord.ext import commands

class text_commands(commands.Cog):
    def __init__ (self, client):
        self.client = client

    #SAMPLE COMMAND
    #@commands.command()
    #async def foo(self, ctx):
    #    await ctx.send('HELLO, WORLD')

async def setup(client: commands.Bot) -> None:
   await client.add_cog(text_commands(client))