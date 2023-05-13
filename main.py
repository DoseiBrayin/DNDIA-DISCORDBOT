from dotenv import load_dotenv 
import json
import urllib.request
from discord.ext import commands
import os
import discord
import random
from funtions import roll_dice,spells

load_dotenv() #Carga el archivo .env
TOKEN = os.getenv('DISCORD_TOKEN') #Aqui va el token del bot

intents = discord.Intents.default()  # Crea un objeto Intents
intents.messages = True  # Permite recibir eventos de mensajes
intents.guilds = True  # Permite recibir eventos de servidores (guilds)
intents.members = True  # Permite recibir eventos de miembros (usuarios) en el servidor
intents.reactions = True  # Permite recibir eventos de reacciones a mensajes
intents.typing = True  # Permite recibir eventos de tipo de teclado
intents.message_content = True  # Permite recibir eventos de mensajes
intents.guild_messages = True  # Permite recibir eventos de mensajes en el servidor
intents.all()

bot = commands.Bot(command_prefix='!',intents=intents) #Crea el bot
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="I'M ON ROLL SESSION 🔥")
    await bot.change_presence(activity=activity)
    print(f'Bot is ready. Logged in as {bot.user}')
    
@bot.command(name='ping',help='Return anything')
async def ping(ctx):
    await ctx.send('I CAST FIREBALL 🔥')

@bot.command(name='commands', help='Shows all available commands')
async def commands_list(ctx):
    command_list = []
    for command in bot.commands:
        if not command.hidden:
            command_list.append((command.name, command.help))
    command_list.sort()
    response = "Available commands:\n"
    for command_name, command_help in command_list:
        response += f"- {command_name}: {command_help}\n"
    await ctx.send(response)

@bot.command(name='init', help='Rolls a initiative')
async def initiative(ctx, dice:str='0'):
    rolled_dice = roll_dice.roll(dice)
    await ctx.send(f'Your dice is: {rolled_dice[0]} = initiative: {rolled_dice[1]}')

@bot.command(name='spell_dice', help='Rolls a spell dice')
async def spell_dice(ctx, name:str,level:int=0):
    spell = spells.spell_dice(name,level)
    await ctx.send(f'You casting {name} type damage: {spell[0]} and your dice is {spell[1]}')
    #await ctx.send(f'Your roll {name} on level {level}')
bot.run(TOKEN)