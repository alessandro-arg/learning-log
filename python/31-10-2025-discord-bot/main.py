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

@bot.command()
async def hallo(ctx):
    await ctx.send(f"Grusse dich {ctx.author.mention}")

@bot.command()
async def msg(ctx, arg):
    await ctx.send(f"Deine nachricht war {arg}")

new_role = 'niceGuy'

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"Deine rolle wurde hinzugefuegt.")
        return
    await ctx.send(f"Die rolle wurde nicht gefunden")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Deine rolle wurde entfernt.")
        return
    await ctx.send(f"Die rolle wurde nicht gefunden")

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