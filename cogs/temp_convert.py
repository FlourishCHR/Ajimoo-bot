import discord
from discord import app_commands
from discord.ext import commands

class temp_convert(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name= 'temp_convert', description= 'Converts temperature to Celsius, Fahrenheit or Kelvin')
    @app_commands.choices(current_temperature= [
     discord.app_commands.Choice(name= 'Celsius', value= 0),
     discord.app_commands.Choice(name= 'Fahrenheit', value= 1),
     discord.app_commands.Choice(name= 'Kelvin', value= 2)
])
    @app_commands.choices(converted_temperature= [
     discord.app_commands.Choice(name= 'Celsius', value= 0),
     discord.app_commands.Choice(name= 'Fahrenheit', value= 1),
     discord.app_commands.Choice(name= 'Kelvin', value= 2)
])                                                                                                                                                                                                                            
    async def temp_convert(self, interaction: discord.Interaction, input: float, current_temperature: discord.app_commands.Choice[int], converted_temperature: discord.app_commands.Choice[int]):
     temperature_list = ['°C', '°F', 'K']
     if current_temperature.value == converted_temperature.value:
           total_temperature = input
     elif current_temperature.value == 0 and converted_temperature.value == 1:  # CELSIUS TO FAHRENHEIT
           total_temperature = round((input * 9/5) + 32, 1)
     elif current_temperature.value == 0 and converted_temperature.value == 2:  # CELSIUS TO KELVIN
           total_temperature = round(input + 273.15, 1)
     elif current_temperature.value == 1 and converted_temperature.value == 0:  # FAHRENHEIT TO CELSIUS
           total_temperature = round((input - 32) * 5/9, 1)
     elif current_temperature.value == 1 and converted_temperature.value == 2:  # FAHRENHEIT TO KELVIN
           total_temperature = round(input - 32 * 5/9 + 273.15, 1)
     elif current_temperature.value == 2 and converted_temperature.value == 0:  # KELVIN TO CELSIUS
           total_temperature = round(input - 273.15, 2)
     elif current_temperature.value == 2 and converted_temperature.value == 1:  # KELVIN TO FAHRENHEIT
           total_temperature = round((input - 273.15) * 9/5 + 32, 2)

     embed = discord.Embed(title= 'Temperature Conversion', color= discord.Color.from_rgb(255, 81, 130))
     embed.add_field(name= f'Input in {current_temperature.name}', value= f'{str(input)} {temperature_list[current_temperature.value]}', inline= True)
     embed.add_field(name= 'Converted to', value= f'{converted_temperature.name}', inline= True)
     embed.add_field(name= f'Output in {converted_temperature.name}', value= f'{str(total_temperature)} {temperature_list[converted_temperature.value]}', inline= False)
     await interaction.response.send_message(embed= embed)

async def setup(client: commands.Bot) -> None:
   await client.add_cog(temp_convert(client))