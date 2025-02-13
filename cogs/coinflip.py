import discord, random
from discord.ext import commands
from discord import app_commands

class coinflip(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name= 'coinflip', description= 'let the bot choose between two options')
    async def coinflip(self, interaction: discord.Interaction, option1:str, option2:str):
     embed = discord.Embed(title= 'Coinflip', color= discord.Color.from_rgb(255, 81, 130))
     value = [option1, option2]
     embed.add_field(name= 'Option 1', value= option1)
     embed.add_field(name= 'Option 2', value= option2)
     embed.add_field(name= 'Chosen Option', value= random.choice(value), inline= False)
     await interaction.response.send_message(embed= embed)

async def setup(client: commands.Bot) -> None:
   await client.add_cog(coinflip(client))