import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
_ = load_dotenv()
auth_token = os.environ['discord_token']

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
# Testing commit with comments
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

bot.run(auth_token)
