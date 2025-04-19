import discord
from discord.ext import commands
import os
from datetime import datetime
from utils import set_data_source, load_config, get_data_source
from data_loader import load_users
from timezone_utils import set_timezone, get_timezone

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

@bot.command()
@commands.has_permissions(administrator=True)
async def checkusers(ctx):
    source = get_data_source()
    users = load_users(source)

    if not users:
        await ctx.send("No users found from current source.")
    else:
        msg = "\n".join([f"<@{u['discord_id']}> expires on {u['expiry_date']}" for u in users])
        await ctx.send(f"📋 Pulled from `{source}`:\n{msg}")


@bot.command()
async def settimezone(ctx, timezone: str):
    if not timezone.startswith("UTC"):
        await ctx.send("❌ Please use the format like `UTC+8` or `UTC-5`.")
        return
    set_timezone(ctx.author.id, timezone)
    await ctx.send(f"✅ Timezone set to `{timezone}` for <@{ctx.author.id}>.")

@bot.command()
async def mytimezone(ctx):
    tz = get_timezone(ctx.author.id)
    if tz:
        await ctx.send(f"🌍 Your timezone is set to `{tz}`.")
    else:
        await ctx.send("❗ You have not set a timezone yet. Use `!settimezone UTC+8`.")


bot.run(os.getenv("DISCORD_BOT_TOKEN"))
