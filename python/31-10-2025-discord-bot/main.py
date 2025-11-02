import logging
import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

handler = logging.FileHandler(filename="discordbot.log", mode='w', encoding="utf-8")

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# print(token)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Ready! I am {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'test' in message.content.lower():
        await message.delete()
        channel = message.channel
        await channel.send(f'Hey, dieser begriff ist nur fur {message.author} geeignet!')

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)