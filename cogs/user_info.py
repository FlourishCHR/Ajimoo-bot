import discord, datetime
from discord import app_commands
from discord.ext import commands

class userinfo(commands.Cog):
    def __init__ (self, client: commands.Bot):
        self.client = client

    @app_commands.command(name= 'userinfo', description= 'Outputs information on a user.')
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member):
        memstat = interaction.guild.get_member(member.id).status
        member_color = interaction.guild.get_member(member.id).color
        if memstat == discord.Status.online:
            memstatus = 'Online'
        elif memstat == discord.Status.idle:
            memstatus = 'Idle'
        elif memstat == discord.Status.do_not_disturb:
            memstatus = 'Do not disturb'
        elif memstat == discord.Status.offline:
            memstatus =  'Offline'
        else:
            memstatus = 'Error'
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(title= 'User info', description= f'Here is the user info on the user {member.mention}', color= member_color, timestamp= datetime.datetime.now(datetime.UTC))
        embed.set_thumbnail(url= member.avatar)
        embed.add_field(name= 'Member ID', value= member.id)
        embed.add_field(name= 'Name', value= f'{member.name}')
        embed.add_field(name= 'Nickname', value= member.display_name)
        embed.add_field(name= 'Status', value= str(memstatus))
        embed.add_field(name= 'Created at', value= member.created_at.strftime('%#d %b, %Y, %H:%M'))
        embed.add_field(name= 'Joined at', value= member.joined_at.strftime('%#d %b, %Y, %H:%M'))
        embed.add_field(name= f'Roles({int(len(roles))})', value= ' '.join([role.mention + ' | ' for role in roles]), inline=False)
        await interaction.response.send_message(embed= embed)

async def setup(client: commands.Bot) -> None:
   await client.add_cog(userinfo(client))