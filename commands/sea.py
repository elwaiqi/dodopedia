# sea.py
import discord
from discord.ext import commands

import calendar, requests

from .resources.shortcuts import *


class SeaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "sea")
    @commands.guild_only()
    async def sea(self, ctx, *, sea: str):
        url = acnhapi + "sea/" + sea.lower().replace(" ", "_")

        data = dict(requests.get(url).json())

        sea_name = data["name"]["name-USen"].title()
        sea_icon = data["icon_uri"]

        museum_phrase = data["museum-phrase"]

        price = "{:,}".format(int(data["price"])) + " " + emoji_bells

        speed = data["speed"]

        time_of_day = ""
        if data["availability"]["isAllDay"] == True:
            time_of_day = "All Day"
        else:
            time_of_day = data["availability"]["time"]

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

        shadow_size = data["shadow"]

        embed_data = discord.Embed(title=f"**{sea_name}**", description=f"```{museum_phrase}```", colour=0x00ff00)
        embed_data.set_thumbnail(url=sea_icon)
        embed_data.add_field(name="**Time**", value=time_of_day, inline=True)
        embed_data.add_field(name="**Shadow**", value=shadow_size, inline=True)
        embed_data.add_field(name="**Speed**", value=speed, inline=True)
        embed_data.add_field(name="**Price**", value=price, inline=False)
        embed_data.add_field(name="**Northern Hemisphere**", value=availability_northern, inline=False)
        embed_data.add_field(name="**Southern Hemisphere**", value=availability_southern, inline=False)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed = embed_data)


def setup(bot):
    bot.add_cog(SeaCog(bot))