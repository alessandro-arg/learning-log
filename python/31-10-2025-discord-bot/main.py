import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

print(token)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Ready! I am {bot.user}')

bot.run(token)