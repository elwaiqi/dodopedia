import discord
from discord.ext import commands

from .resources.shortcuts import *


class HelpCog(commands.Cog, name="Help"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="help",
        description="~~I need somebody!~~ Shows this message.",
        usage="<category>"
    )
    async def help(self, ctx, cog="all"):

        colour = embed_colour()

        # Preparing the embed
        help_embed = discord.Embed(
            title="You need help!... But that's OK because this is a seaplane.",
            colour=colour
        )
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")

        cogs = [cog_key for cog_key in self.bot.cogs.keys()]

        if cog == "all":
            for cog in cogs:

                # Get a list of all commands under each cog
                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ""

                for command in cog_commands:
                    commands_list += f"**{command.name}** - *{command.description}*\n"

                # Add cog's details to embed
                help_embed.add_field(
                    name=cog,
                    value=commands_list,
                    inline=False
                )

            pass
        else:
            # If cog was specified
            cogs_lower = [cog.lower() for cog in cogs]

            # If the cog exists
            if cog.lower() in cogs_lower:
                # Get a list of all commands under the specified cog
                commands_list = self.bot.get_cog(cogs[cogs_lower.index(cog.lower())]).get_commands()
                help_text = ""

                # Add details to help_text
                for command in commands_list:
                    help_text += f"```{command.name}```\n" \
                        f"*{command.description}*\n"

                    # Add aliases
                    if len(command.aliases) > 0:
                        help_text += f"**Aliases:** `{'`, `'.join(command.aliases)}`\n\n\n"
                    else:
                        # Adding a newline character to keep it pretty 
                        help_text += "\n"

                    # Format
                    help_text += f"Format: `@{self.bot.user.name}#{self.bot.user.discriminator} {command.name} {command.usage if command.usage is not None else ''}`\n\n\n"

                help_embed.description = help_text
            else:
                # Notify the user of invalid cog
                await ctx.send("Invalid category specified.\nUse `help` to list all categories and commands.")
                return
        
        await ctx.send(embed=help_embed)

        return

    @commands.command(
        name="invite",
        description="Get an link to invite Dodo to a server!"
    )
    async def invite(self, ctx):
        invite_embed = discord.Embed(title="Invite me to your island!", url="https://discord.com/api/oauth2/authorize?client_id=730541096769421422&permissions=3533888&scope=bot")

        await ctx.send(embed=invite_embed)


def setup(bot):
    bot.add_cog(HelpCog(bot))
        