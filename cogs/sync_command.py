import discord
from discord.ext import commands
from discord import app_commands

class sync_command(commands.Cog):
    def __init__ (self, client: commands.Bot):
        self.client = client

    # SYNCS BOT COMMANDS (Apparently, it's not recommended to sync the bot on_ready)
    @app_commands.command(name= 'sync_command', description= 'Syncs bot commands (Administrator only)')
    async def sync(self, interaction: discord.Interaction):
            if not interaction.user.guild_permissions.administrator:
                 return await interaction.response.send_message("Error. You have no administrator priviledge")
            synced = await self.client.tree.sync()
            await interaction.response.send_message(f'Command tree synced. Total commands synced: {str(len(synced))}')

async def setup(client: commands.Bot) -> None:
   await client.add_cog(sync_command(client))