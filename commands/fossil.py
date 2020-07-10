#fossil.py
import discord
from discord.ext import commands

import requests

from .resources.shortcuts import *


class FossilCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fossil")
    @commands.guild_only()
    async def fossil(self, ctx, *, fossil: str):
        url = acnhapi + "fossils/" + fossil.lower().replace(" ", "_").replace("._", "")

        data = dict(requests.get(url).json())

        fossil_name = data["name"]["name-USen"].title()
        fossil_image = data["image_uri"]

        museum_phrase = data["museum-phrase"]

        price = "{:,}".format(int(data["price"])) + " " + emoji_bells

        embed_data = discord.Embed(title=f"{fossil_name}", description=f"```{museum_phrase}```")
        embed_data.set_thumbnail(url=fossil_image)
        embed_data.add_field(name="**Price**", value=price)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)


def setup(bot):
    bot.add_cog(FossilCog(bot))