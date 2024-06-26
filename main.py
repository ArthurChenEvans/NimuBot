import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))