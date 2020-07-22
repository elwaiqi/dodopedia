import discord
from discord.ext import commands

from dotenv import load_dotenv

import os, sys, traceback

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

cogs = [
    "commands.critters",
    "commands.fossils",
    "commands.gallery",
    "commands.help",
    "commands.island_life"
]

def get_prefix(bot, message):
    prefixes = ["?"]
    
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(
    command_prefix=get_prefix,
    description="Dodo Bot",
    case_insensitive=True
)

@bot.event
async def on_ready():
    print(f"\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n")

    # Remove default help command
    bot.remove_command("help")

    # Game Status
    await bot.change_presence(activity=discord.Game(name="Animal Crossing: New Horizons"))

    # Load Cogs
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print("Failed to load cog {cog}.", file=sys.stderr)
            traceback.print_exc()

    print(f"Successfully logged in and booted...!")

@bot.command()
async def ping(ctx):
    await  ctx.channel.send("Pong!")

bot.run(TOKEN)