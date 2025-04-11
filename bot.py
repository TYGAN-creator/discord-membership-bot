import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True  # Required to track membership

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Add more membership logic here...

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
