import discord
from discord.ext import commands
from datetime import datetime

import test_servers




class Help(commands.Cog):
    def __init__(self, client):
        self.client = client


    s1 = test_servers.s1


    @commands.slash_command(guild_ids=[s1], description="This command helps you by giving you the description of other commands")
    async def help(self, ctx):
        await ctx.respond("This is a Help Command")


def setup(client):
    client.add_cog(Help(client))
