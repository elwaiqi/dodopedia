#bug.py
import discord
from discord.ext import commands

import calendar, json, requests, string

from .resources.shortcuts import *


class CritterCog(commands.Cog, name="Critterpedia"):
    def __init__(self, bot):
        self.bot = bot

        with open(f"{resources_path}bugs.json", encoding="utf8") as bugs, open(f"{resources_path}fish.json", encoding="utf8") as fish, open(f"{resources_path}sea.json", encoding="utf8") as sea:
            # Load the data
            self.data_bugs = json.load(bugs)
            self.data_fish = json.load(fish)
            self.data_sea = json.load(sea)

            # Get the keys
            self.data_bugs_keys = self.data_bugs.keys()
            self.data_fish_keys = self.data_fish.keys()
            self.data_sea_keys = self.data_sea.keys()

            bugs.close()
            fish.close()
            sea.close()

    @commands.command(
        name="bug",
        description="Lookup info about a specific bug.",
        usage="<bug name>"
    )
    @commands.guild_only()
    async def bug(self, ctx, *, bug: str):
        bug = cleanup_str(bug)

        for key in self.data_bugs_keys:
            if key == bug:
                bug_name = string.capwords(self.data_bugs[key]["name"]["name-USen"])
                bug_icon = self.data_bugs[key]["icon_uri"]

                museum_phrase = self.data_bugs[key]["museum-phrase"]

                price = "{:,}".format(int(self.data_bugs[key]["price"])) + " " + emoji_bells

                location = self.data_bugs[key]["availability"]["location"]

                time_of_day = ""
                if self.data_bugs[key]["availability"]["isAllDay"] == True:
                    time_of_day = "All Day"
                else:
                    time_of_day = self.data_bugs[key]["availability"]["time"]

                rarity = self.data_bugs[key]["availability"]["rarity"]

                availability_northern = []
                for month in self.data_bugs[key]["availability"]["month-array-northern"]:
                    month_name = calendar.month_abbr[month]
                    availability_northern.append(month_name)

                availability_southern = []
                for month in self.data_bugs[key]["availability"]["month-array-southern"]:
                    month_name = calendar.month_abbr[month]
                    availability_southern.append(month_name)

                if self.data_bugs[key]["availability"]["isAllYear"] == True:
                    availability_northern = "All Year"
                    availability_southern = "All Year"
                else:
                    availability_northern = availability_northern[0] + " - " + availability_northern[-1]
                    availability_southern = availability_southern[0] + " - " + availability_southern[-1]

                break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"**{bug_name}**", description=f"```{museum_phrase}```", colour=colour)
        embed_data.set_thumbnail(url=bug_icon)
        embed_data.add_field(name="**Location**", value=location, inline=True)
        embed_data.add_field(name="**Time**", value=time_of_day, inline=True)
        embed_data.add_field(name="**Rarity**", value=rarity, inline=True)
        embed_data.add_field(name="**Price**", value=price, inline=False)
        embed_data.add_field(name="**Northern Hemisphere**", value=availability_northern, inline=False)
        embed_data.add_field(name="**Southern Hemisphere**", value=availability_southern, inline=False)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)

    @commands.command(
        name="fish",
        description="Lookup info about a specific fish.",
        usage="<fish name>"
    )
    @commands.guild_only()
    async def fish(self, ctx, *, fish: str):
        fish = cleanup_str(fish)

        for key in self.data_fish_keys:
            if key == fish:
                fish_name = string.capwords(self.data_fish[key]["name"]["name-USen"])
                fish_icon = self.data_fish[key]["icon_uri"]

                museum_phrase = self.data_fish[key]["museum-phrase"]

                price = "{:,}".format(int(self.data_fish[key]["price"])) + " " + emoji_bells

                location = self.data_fish[key]["availability"]["location"]

                time_of_day = ""
                if self.data_fish[key]["availability"]["isAllDay"] == True:
                    time_of_day = "All Day"
                else:
                    time_of_day = self.data_fish[key]["availability"]["time"]

                rarity = self.data_fish[key]["availability"]["rarity"]

                availability_northern = []
                for month in self.data_fish[key]["availability"]["month-array-northern"]:
                    month_name = calendar.month_abbr[month]
                    availability_northern.append(month_name)

                availability_southern = []
                for month in self.data_fish[key]["availability"]["month-array-southern"]:
                    month_name = calendar.month_abbr[month]
                    availability_southern.append(month_name)

                if self.data_fish[key]["availability"]["isAllYear"] == True:
                    availability_northern = "All Year"
                    availability_southern = "All Year"
                else:
                    availability_northern = availability_northern[0] + " - " + availability_northern[-1]
                    availability_southern = availability_southern[0] + " - " + availability_southern[-1]

                shadow_size = self.data_fish[key]["shadow"]

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
    
    @commands.command(
        name="sea",
        description="Lookup info about a specific sea creature.",
        usage="<sea creature name>"
    )
    @commands.guild_only()
    async def sea(self, ctx, *, sea: str):
        sea = cleanup_str(sea)

        for key in self.data_sea_keys:
            if key == sea:
                sea_name = string.capwords(self.data_sea[key]["name"]["name-USen"])
                sea_icon = self.data_sea[key]["icon_uri"]

                museum_phrase = self.data_sea[key]["museum-phrase"]

                price = "{:,}".format(int(self.data_sea[key]["price"])) + " " + emoji_bells

                speed = self.data_sea[key]["speed"]

                time_of_day = ""
                if self.data_sea[key]["availability"]["isAllDay"] == True:
                    time_of_day = "All Day"
                else:
                    time_of_day = self.data_sea[key]["availability"]["time"]

                availability_northern = []
                for month in self.data_sea[key]["availability"]["month-array-northern"]:
                    month_name = calendar.month_abbr[month]
                    availability_northern.append(month_name)

                availability_southern = []
                for month in self.data_sea[key]["availability"]["month-array-southern"]:
                    month_name = calendar.month_abbr[month]
                    availability_southern.append(month_name)

                if self.data_sea[key]["availability"]["isAllYear"] == True:
                    availability_northern = "All Year"
                    availability_southern = "All Year"
                else:
                    availability_northern = availability_northern[0] + " - " + availability_northern[-1]
                    availability_southern = availability_southern[0] + " - " + availability_southern[-1]

                shadow_size = self.data_sea[key]["shadow"]

                break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"**{sea_name}**", description=f"```{museum_phrase}```", colour=colour)
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
    bot.add_cog(CritterCog(bot))