import discord
from discord.ext import commands
from datetime import datetime

import test_servers



class ComplicatedCalculations(commands.Cog):
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


    @commands.slash_command(guild_ids=[s1], description="Shows the Square Root of any number!")
    async def squareroot(self, ctx, num1: int):
        sqrt = num1 ** 0.5

        embed = discord.Embed(title="Square Root", description=f"The **Square Root** of **{num1}** is = `{sqrt}`", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.respond(embed=embed)


    @commands.slash_command(guild_ids=[s1], description="Shows the Factorial of any number!")
    async def factorial(self, ctx, num1: int):
        factorial = 1

        if num1 < 0:
            await ctx.respond("Factorial dows not exists for negative numbers")
        elif num1 == 0:
            await ctx.respond("The factorial of 0 is 1")
        else:
            for i in range(1, num1 + 1):
                factorial = factorial * 1

        embed = discord.Embed(title="Factorial", description=f"The Factorial of **{num1}** is `{factorial}`", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by {ctx.author}")

        await ctx.respond(embed=embed)



def setup(client):
    client.add_cog(ComplicatedCalculations(client))
