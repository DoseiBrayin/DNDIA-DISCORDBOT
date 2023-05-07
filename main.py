from dotenv import load_dotenv 
import json
import urllib.request
from discord.ext import commands
import os
import discord
import random

load_dotenv() #Carga el archivo .env
TOKEN = os.getenv('DISCORD_TOKEN') #Aqui va el token del bot

intents = discord.Intents.default()  # Crea un objeto Intents
intents.all() #Activa todas las intenciones

bot = commands.Bot(command_prefix='-',intents=intents) #Crea el bot

@bot.command(name='Ping',help='Return anything')
async def ping(ctx):
    await ctx.send('I CAST FIREBALL 🔥')

bot.run(TOKEN)