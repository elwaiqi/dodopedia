import discord
from discord.ext import commands

from dotenv import load_dotenv

import os, sys, traceback

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

def get_prefix(bot, message):
    prefixes = ["?"]
    
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = [
    "commands.art",
    "commands.bug",
    "commands.fish",
    "commands.fossil",
    "commands.sea"
]

bot = commands.Bot(command_prefix=get_prefix, description="ACNH Waiqi Bot")
bot.remove_command("help")

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("Failed to load extension {extension}.", file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f"\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n")

    # Game Status
    await bot.change_presence(activity=discord.Game(name="#yosoywaiqi"))

    print(f"Successfully logged in and booted...!")

bot.run(TOKEN)