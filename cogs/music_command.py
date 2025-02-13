import discord
from discord import app_commands
from discord.ext import commands

class music_command(commands.Cog):
    def __init__ (self, client):
        self.client = client

    @app_commands.command(name='skip', description='Skip the current audio')
    async def skip(self, interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.stop()
            embed = discord.Embed(title= 'Skip', description= f'Skipping current song.', color= discord.Color.from_rgb(255, 81, 130))
            await interaction.response.send_message(embed= embed)

    @app_commands.command(name= 'stop', description='stops the current song and disconnects')
    async def stop(self, interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing() or interaction.guild.voice_client.is_connected():
            interaction.guild.voice_client.stop()
        await interaction.guild.voice_client.disconnect()
        embed = discord.Embed(title= 'Stop', description= f'Leaving the call.', color= discord.Color.from_rgb(255, 81, 130))
        await interaction.response.send_message(embed= embed)


    @app_commands.command(name= 'pause', description='pauses the current song')
    async def pause(self, interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_playing():
            interaction.guild.voice_client.pause()
            embed = discord.Embed(title= 'Pause', description= f'Paused.', color= discord.Color.from_rgb(255, 81, 130))
            await interaction.response.send_message(embed= embed)


    @app_commands.command(name= 'resume', description='resumes the current song')
    async def resume(self, interaction: discord.Interaction):
        if interaction.guild.voice_client and interaction.guild.voice_client.is_connected():
            interaction.guild.voice_client.resume()
            embed = discord.Embed(title= 'Resume', description= f'Resuming.', color= discord.Color.from_rgb(255, 81, 130))
            await interaction.response.send_message(embed= embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(music_command(client))