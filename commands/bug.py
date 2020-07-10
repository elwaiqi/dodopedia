#bug.py
import discord
from discord.ext import commands

import calendar, requests

from .resources.shortcuts import *


class BugCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bug")
    @commands.guild_only()
    async def bug(self, ctx, *, bug: str):
        url = acnhapi + "bugs/" + bug.lower().replace(" ", "_")

        data = dict(requests.get(url).json())

        bug_name = data["name"]["name-USen"].title()
        bug_icon = data["icon_uri"]

        museum_phrase = data["museum-phrase"]

        price = "{:,}".format(int(data["price"])) + " " + emoji_bells

        location = data["availability"]["location"]

        time_of_day = ""
        if data["availability"]["isAllDay"] == True:
            time_of_day = "All Day"
        else:
            time_of_day = data["availability"]["time"]

        rarity = data["availability"]["rarity"]

        availability_northern = []
        for month in data["availability"]["month-array-northern"]:
            month_name = calendar.month_abbr[month]
            availability_northern.append(month_name)

        availability_southern = []
        for month in data["availability"]["month-array-southern"]:
            month_name = calendar.month_abbr[month]
            availability_southern.append(month_name)

        if data["availability"]["isAllYear"] == True:
            availability_northern = "All Year"
            availability_southern = "All Year"
        else:
            availability_northern = availability_northern[0] + " - " + availability_northern[-1]
            availability_southern = availability_southern[0] + " - " + availability_southern[-1]

        embed_data = discord.Embed(title=f"**{bug_name}**", description=f"```{museum_phrase}```", colour=0x00ff00)
        embed_data.set_thumbnail(url=bug_icon)
        embed_data.add_field(name="**Location**", value=location, inline=True)
        embed_data.add_field(name="**Time**", value=time_of_day, inline=True)
        embed_data.add_field(name="**Rarity**", value=rarity, inline=True)
        embed_data.add_field(name="**Price**", value=price, inline=False)
        embed_data.add_field(name="**Northern Hemisphere**", value=availability_northern, inline=False)
        embed_data.add_field(name="**Southern Hemisphere**", value=availability_southern, inline=False)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)


def setup(bot):
    bot.add_cog(BugCog(bot))