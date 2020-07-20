import os
from fractions import Fraction

import json, requests

import discord
from discord.ext import commands

from .resources.shortcuts import *

class VillagerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open(f"{resources_path}villagers.json", encoding="utf8") as villagers_json:
            data = json.load(villagers_json)
            data_keys = data.keys()

            villagers_json.close()

    @commands.command(name="villager")
    @commands.guild_only()
    async def villager(self, ctx, villager: str):

        for key in self.data_keys:
                    villager_name = self.data[key]["name"]["name-USen"]

                    if villager_name.lower() == villager.lower():
                        villager_species = self.data[key]["species"]
                        villager_gender = self.data[key]["gender"]
                        villager_personality = self.data[key]["personality"]
                        villager_birthday = self.data[key]["birthday-string"]
                        villager_catchphrase = self.data[key]["catch-translations"]["catch-USen"]
                        villager_icon = self.data[key]["icon_uri"]
                        villager_image = self.data[key]["image_uri"]

                        break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"**{villager_name}**", description=f"```{villager_catchphrase}```", colour=colour)
        embed_data.set_thumbnail(url=villager_image)
        embed_data.add_field(name="**Species**", value=villager_species, inline=True)
        embed_data.add_field(name="**Gender**", value=villager_gender, inline=True)
        embed_data.add_field(name="**Personality**", value=villager_personality, inline=True)
        embed_data.add_field(name="**Birthday**", value=villager_birthday, inline=False)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)

    @commands.command(name="odds")
    @commands.guild_only()
    async def vodds(self, ctx, villager: str, species_owned: int, nmt=1, species_completed=0):
        species_count = {
            "alligator": 7,
            "anteater": 7,
            "bear": 15,
            "bird": 13,
            "bull": 6,
            "cat": 23,
            "chicken": 9,
            "cow": 4,
            "cub": 16,
            "deer": 10,
            "dog": 16,
            "duck": 17,
            "eagle": 9,
            "elephant": 11,
            "frog": 18,
            "goat": 8,
            "gorilla": 9,
            "hamster": 8,
            "hippo": 7,
            "horse": 15,
            "kangaroo": 8,
            "koala": 9,
            "lion": 7,
            "monkey": 8,
            "mouse": 15,
            "octopus": 3,
            "ostrich": 10,
            "penguin": 13,
            "pig": 15,
            "rabbit": 20,
            "rhino": 6,
            "sheep": 13,
            "squirrel": 18,
            "tiger": 7,
            "wolf": 11
        }

        for key in self.data_keys:
            villager_name = self.data[key]["name"]["name-USen"]

            if villager_name.lower() == villager.lower():
                villager_species = self.data[key]["species"].lower()
                villager_icon = self.data[key]["icon_uri"]

                break

        n_possible_species = 35 - species_completed
        n_villagers_within_species = species_count[villager_species]
        n_villagers_of_species_owned = species_owned
        n_nmt = nmt

        odds_species = round(1 / n_possible_species * 100, 2)

        specific_odds = round(1 / n_possible_species * 1 / (n_villagers_within_species - n_villagers_of_species_owned) * 100, 2)

        bernoulli_odds = round(100 - (((100 - specific_odds) / 100) ** n_nmt) * 100, 2)

        if (bernoulli_odds == 100):
            bernoulli_odds = 99.99

        specific_odds_frac = "1:" + str(round(1 / (specific_odds / 100)))

        bernoulli_odds_frac = "1:" + str(round(1 / (bernoulli_odds / 100)))

        message = f"You have a **{specific_odds}%** chance ({specific_odds_frac}) of finding **{villager_name}** per {emoji_nmt}, and a **{odds_species}%** (1:{n_possible_species}) of finding any **{villager_species}**.\n\nIf you use **{n_nmt}** {emoji_nmt}, you'll have a **{bernoulli_odds}%** chance ({bernoulli_odds_frac})."

        colour = embed_colour()

        embed_data = discord.Embed(description=message, colour=colour)
        embed_data.set_thumbnail(url=villager_icon)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)


def setup(bot):
    bot.add_cog(VillagerCog(bot))