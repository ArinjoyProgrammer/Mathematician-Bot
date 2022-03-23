import discord
from discord.ext import commands
from datetime import datetime

import test_servers



class NormalCalculation(commands.Cog):
    def __init__(self, client):
        self.client =  client



    s1 = test_servers.s1

    @commands.slash_command(guild_ids=[s1], description="This command does the Addition of the numbers")
    async def add(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Addition", description=f"The **Addition** of   `{num1}`   and   `{num2}`   is   `{num1+num2}`  ", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by  {ctx.author}")

        await ctx.respond(embed=embed)


    @commands.slash_command(guild_ids=[s1], description="This command does the Substraction of the numbers")
    async def substraction(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Substraction", description=f"The **Substraction** of   `{num1}`   and   `{num2}`   is   `{num1-num2}`  ", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by  {ctx.author}")

        await ctx.respond(embed=embed)


    @commands.slash_command(guild_ids=[s1], description="This command does the Multiplication of the numbers")
    async def multiplication(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Multiplication", description=f"The **Multiplication** of   `{num1}`   and   `{num2}`   is   `{num1*num2}`  ", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by  {ctx.author}")

        await ctx.respond(embed=embed)


    @commands.slash_command(guild_ids=[s1], description="This command does the Division of the numbers")
    async def division(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Addition", description=f"The **Division** of   `{num1}`   and   `{num2}`   is   `{num1/num2}`  ", timestamp=datetime.utcnow(), color=discord.Color.random())
        embed.set_footer(text=f"Command Requested by  {ctx.author}")

        await ctx.respond(embed=embed)



def setup(client):
    client.add_cog(NormalCalculation(client))
