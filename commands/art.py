#art.py
import discord
from discord.ext import commands

import json, requests

from .resources.shortcuts import *


class ArtCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        with open(f"{resources_path}art.json", encoding="utf8") as art_json:
            self.data = json.load(art_json)
            self.data_keys = self.data.keys()

            art_json.close()
    
    @commands.command(name="artwork", aliases=["art"])
    @commands.guild_only()
    async def art(self, ctx, *, artwork: str):
        artwork = cleanup_str(artwork)

        for key in self.data_keys:
            if key == artwork:
                artwork_name = self.data[key]["name"]["name-USen"].title()
                artwork_image = self.data[key]["image_uri"]
                
                artwork_can_be_fake = ""
                if self.data[key]["hasFake"] == True:
                    artwork_can_be_fake = "Yes"
                else:
                    artwork_can_be_fake = "No"

                museum_phrase = self.data[key]["museum-desc"]

                price_buy = "{:,}".format(int(self.data[key]["buy-price"])) + " " + emoji_bells
                price_sell = "{:,}".format(int(self.data[key]["sell-price"])) + " " + emoji_bells

                break

        colour = embed_colour()

        embed_data = discord.Embed(title=f"{artwork_name}", description=f"```{museum_phrase}```", colour=colour)
        embed_data.set_thumbnail(url="https://vignette.wikia.nocookie.net/animalcrossing/images/6/6b/ReddNL.png/revision/latest?cb=20200425083709")
        embed_data.add_field(name="**Redd's Price**", value=price_buy, inline=True)
        embed_data.add_field(name="**Sell Price** (if genuine)", value=price_sell, inline=True)
        embed_data.add_field(name="**Has Fake?**", value=artwork_can_be_fake, inline=False)
        embed_data.set_image(url=artwork_image)
        embed_data.set_footer(text=embed_footer_text)

        await ctx.channel.send(embed=embed_data)


def setup(bot):
    bot.add_cog(ArtCog(bot))