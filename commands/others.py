import discord
from discord.ext import commands

import test_servers



class Others(commands.Cog):
    def __init__(self, client):
        self.client = client

    s1 = test_servers.s1

    @commands.slash_command(guild_ids=[s1], description="Shows the version of the bot!")
    async def version(self,  ctx):
        await ctx.respond("Version - `1.0.0-alpha`")

    # @commands.slash_commands(guild_ids=[s1], description="Shows the GitHub Repository of the bot!")
    # async def github(self, ctx):
    #     await ctx.respond("**Github Repository of the bot** - https://github.com/ArinjoyProgrammer/Mathematician-Bot")



def setup(client):
    client.add_cog(Others(client))
