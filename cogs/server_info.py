import discord, datetime
from discord import app_commands
from discord.ext import commands

class serverinfo(commands.Cog):
    def __init__ (self, client: commands.Bot):
        self.client = client

    @app_commands.command(name= 'serverinfo', description= 'Outputs information on the server.')
    async def serverinfo(self, interaction: discord.Interaction):
        embed = discord.Embed(title= 'Server Info', description= f'Here is the server information for the server {interaction.guild.name}', color= discord.Color.from_rgb(255, 81, 130), timestamp= datetime.datetime.now(datetime.UTC))
        embed.set_thumbnail(url= interaction.guild.icon)
        embed.add_field(name= "Server ID", value= interaction.guild.id)
        embed.add_field(name= "Server Owner", value= interaction.guild.owner.mention)
        embed.add_field(name= 'Members', value= interaction.guild.member_count)
        embed.add_field(name= 'Channels', value= f'{len(interaction.guild.text_channels)} Text | {len(interaction.guild.voice_channels)} Voice')
        embed.add_field(name= 'Created at', value= interaction.guild.created_at.strftime('%#d %b, %Y, %H:%M'))
        await interaction.response.send_message(embed= embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(serverinfo(client))