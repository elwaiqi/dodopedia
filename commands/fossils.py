#fossil.py
import discord
from discord.ext import commands

import json, requests

from .resources.shortcuts import *


class FossilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open(f"{resources_path}fossils.json", encoding="utf8") as fossils_json:
            self.data = json.load(fossils_json)
            self.data_keys = self.data.keys()

            fossils_json.close()

    @commands.command(name="fossil")
    @commands.guild_only()
    async def fossil(self, ctx, *, fossil: str):
        fossil = cleanstr(fossil)

        for key in self.data_keys:
            if key == fossil:

                fossil_name = self.data[key]["name"]["name-USen"].title()
                fossil_image = self.data[key]["image_uri"]

                museum_phrase = self.data[key]["museum-phrase"]

                price = "{:,}".format(int(self.data[key]["price"])) + " " + emoji_bells

                break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"{fossil_name}", description=f"```{museum_phrase}```", colour=colour)
        embed_data.set_thumbnail(url=fossil_image)
        embed_data.add_field(name="**Price**", value=price)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)


def setup(bot):
    bot.add_cog(FossilCog(bot))