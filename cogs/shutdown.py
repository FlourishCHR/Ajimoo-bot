import discord
from discord.ext import commands
from discord import app_commands

class shutdown(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name= 'shutdown', description= 'Command to shutdown the bot. (Administrator only)')
    async def shutdown(self, interaction: discord.Interaction):
            if not interaction.user.guild_permissions.administrator:
                return await interaction.response.send_message('Error. You have no administrator priviledge.')
            await interaction.response.send_message('Bot shutting down.')
            await self.client.close()

async def setup(client: commands.Bot) -> None:
   await client.add_cog(shutdown(client))