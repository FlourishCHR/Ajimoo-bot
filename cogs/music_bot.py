import discord, yt_dlp
from discord.ext import commands
from discord import app_commands

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': False}

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []

    @app_commands.command(name='play', description='Search and play an audio')
    async def play(self, interaction: discord.Interaction, search: str):
            voice_channel = interaction.user.voice.channel if interaction.user.voice else None
            if not voice_channel:
                return await interaction.response.send_message('You are not in a voice channel!')

            if not interaction.guild.voice_client:
                await voice_channel.connect()

            await interaction.response.defer()

            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f'ytsearch:{search}', download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                    url = info['url']
                    title = info['title']
                    self.queue.append((url, title))
                    embed = discord.Embed(title= 'Queued', description= f'**{title}**', color= interaction.guild.get_member(interaction.user.id).color)
                    embed.add_field(name= 'Queued by: ', value= interaction.user.mention)
                    await interaction.followup.send(embed= embed)

            if not interaction.guild.voice_client.is_playing():
                await self.play_next(interaction)


    async def play_next(self, interaction: discord.Interaction):
        if self.queue:
            url, title = self.queue.pop(0)
            source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
            interaction.guild.voice_client.play(source, after=lambda _: self.client.loop.create_task(self.play_next(interaction)))
            embed = discord.Embed(title= 'Now Playing', description= f'**{title}**', color= interaction.guild.get_member(interaction.user.id).color)
            embed.add_field(name= 'Requested by: ', value= interaction.user.mention)
            await interaction.followup.send(embed= embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Music(client))