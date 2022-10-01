from dotenv import load_dotenv
import os
load_dotenv()

import discord
from discord.ext import commands
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def hola(ctx): #Comando a decir
    await ctx.send('Qué tal estas?') #Mensaje que dira el bot
 
 
#Cuándo Ejecutes el comando en discord !hola, el bot dira Qué tal estas?
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run(os.getenv('tokendiscord')) #OBTEN UN TOKEN EN: https://discord.com/developers/applications