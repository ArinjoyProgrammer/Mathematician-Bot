import discord
from discord.ext import commands
# from dotenv import load_dotenv
import os

import bot_token



intents = discord.Intents.all()

client = commands.Bot(intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")


# Cogs Connections
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f"commands.{filename[:-3]}")



# load_dotenv()
client.run(bot_token.bot_token)
