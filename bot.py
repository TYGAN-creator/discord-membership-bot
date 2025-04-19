import discord
from discord.ext import commands
import os
from utils import set_data_source, load_config

intents = discord.Intents.default()
intents.members = True  # Required to track membership

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
@commands.has_permissions(administrator=True)
async def setsource(ctx, source: str):
    valid_sources = ["google_sheets", "stripe", "postgresql"]
    source = source.lower()
    if source not in valid_sources:
        await ctx.send(f"❌ Invalid source. Choose from: {', '.join(valid_sources)}")
        return

    set_data_source(source)
    await ctx.send(f"✅ Data source updated to **{source}**.")

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
