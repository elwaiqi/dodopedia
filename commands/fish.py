# fish.py
import discord
from discord.ext import commands

import calendar, json, requests

from .resources.shortcuts import *


class FishCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open(f"{resources_path}fish.json") as fish_json:
            self.data = json.load(fish_json)
            self.data_keys = self.data.keys()

            fish_json.close()

    @commands.command(name="fish")
    @commands.guild_only()
    async def fish(self, ctx, *, fish: str):
        fish = cleanup_str(fish)

        for key in self.data_keys:
            if key == fish:
                fish_name = self.data[key]["name"]["name-USen"].title()
                fish_icon = self.data[key]["icon_uri"]

                museum_phrase = self.data[key]["museum-phrase"]

                price = "{:,}".format(int(self.data[key]["price"])) + " " + emoji_bells

                location = self.data[key]["availability"]["location"]

                time_of_day = ""
                if self.data[key]["availability"]["isAllDay"] == True:
                    time_of_day = "All Day"
                else:
                    time_of_day = self.data[key]["availability"]["time"]

                rarity = self.data[key]["availability"]["rarity"]

                availability_northern = []
                for month in self.data[key]["availability"]["month-array-northern"]:
                    month_name = calendar.month_abbr[month]
                    availability_northern.append(month_name)

                availability_southern = []
                for month in self.data[key]["availability"]["month-array-southern"]:
                    month_name = calendar.month_abbr[month]
                    availability_southern.append(month_name)

                if self.data[key]["availability"]["isAllYear"] == True:
                    availability_northern = "All Year"
                    availability_southern = "All Year"
                else:
                    availability_northern = availability_northern[0] + " - " + availability_northern[-1]
                    availability_southern = availability_southern[0] + " - " + availability_southern[-1]

                shadow_size = self.data[key]["shadow"]

                break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"**{fish_name}**", description=f"```{museum_phrase}```", colour=colour)
        embed_data.set_thumbnail(url=fish_icon)
        embed_data.add_field(name="**Location**", value=location, inline=True)
        embed_data.add_field(name="**Time**", value=time_of_day, inline=True)
        embed_data.add_field(name="**Shadow**", value=shadow_size, inline=True)
        embed_data.add_field(name="**Rarity**", value=rarity, inline=True)
        embed_data.add_field(name="**Price**", value=price, inline=True)
        embed_data.add_field(name="**Northern Hemisphere**", value=availability_northern, inline=False)
        embed_data.add_field(name="**Southern Hemisphere**", value=availability_southern, inline=False)

        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed = embed_data)


def setup(bot):
    bot.add_cog(FishCog(bot))