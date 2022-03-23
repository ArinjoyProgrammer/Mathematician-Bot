import discord
from discord.ext import commands
from datetime import datetime

import test_servers



class Percentage(commands.Cog):
    def __init__(self, client):
        self.client = client



    s1 = test_servers.s1

    @commands.slash_command(guild_ids=[s1], description="This calculates the Number/Marks into a Percentage!")
    async def percentage(self, ctx, gained_marks: int, total_marks: int):
        percentage = gained_marks / total_marks * 100

        embed = discord.Embed(title="Percentage Calculator", description=f"The **Percentage** of your **Marks/Number** is `{percentage}%`", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by  {ctx.author}")

        await ctx.respond(embed=embed)


    @commands.slash_command(guild_ids=[s1], description="This command takes out the average of two numbers!")
    async def average(self, ctx, num1: int, num2: int):
        sum = num1 + num2
        avg = sum / 2

        embed = discord.Embed(title="Average Sum Calculation", description=f"The Average of `{num1}` and `{num2}` is `{avg}`", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.respond(embed=embed)



def setup(client):
    client.add_cog(Percentage(client))
